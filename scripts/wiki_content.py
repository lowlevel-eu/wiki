"""Inspect GFM links with Pandoc and edit destinations without reformatting text."""
from dataclasses import dataclass
from functools import lru_cache
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit, urlunsplit

REPOSITORY = 'lowlevel-eu/wiki'


@dataclass(frozen=True)
class Link:
    url: str
    start: int
    end: int
    kind: str = 'markdown'


@lru_cache(maxsize=8)
def line_positions(text):
    lines = text.splitlines(keepends=True)
    if text.endswith('\n'):
        lines.append('')
    offsets = []
    total = 0
    for line in lines:
        offsets.append(total)
        total += len(line)
    return lines, offsets


def source_offset(text, line, column):
    lines, offsets = line_positions(text)
    if line > len(lines):
        return len(text)
    offset = offsets[line - 1]
    if '\t' not in lines[line - 1]:
        return offset + column - 1
    current = 1
    for character in lines[line - 1]:
        if current >= column:
            break
        current += (4 - (current - 1) % 4) if character == '\t' else 1
        offset += 1
    return offset


def span(text, attrs):
    value = dict(attrs[2]).get('data-pos')
    if not value:
        return None
    ranges = [re.fullmatch(r'(\d+):(\d+)-(\d+):(\d+)', part) for part in value.split(';')]
    if not all(ranges):
        raise ValueError('Unsupported Pandoc source position: ' + value)
    a, b = map(int, ranges[0].groups()[:2])
    c, d = map(int, ranges[-1].groups()[2:])
    return source_offset(text, a, b), source_offset(text, c, d)



class Anchors(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('id', 'name'):
            if attrs.get(key):
                self.values.add(attrs[key])


def inspect(text):
    process = subprocess.run(['pandoc', '--from=gfm+sourcepos-autolink_bare_uris', '--to=json'],
                             input=text, text=True, capture_output=True, check=True)
    ast = json.loads(process.stdout)
    links, anchors, protected = [], set(), []
    raw_seen = set()
    def walk(node, location=None):
        if isinstance(node, list):
            for value in node:
                walk(value, location)
        elif isinstance(node, dict):
            kind, data = node.get('t'), node.get('c')
            if kind in ('Div', 'Span', 'Link', 'Image', 'Code', 'CodeBlock'):
                location = span(text, data[0]) or location
            elif kind == 'Header':
                anchors.add(data[1][0])
                location = span(text, data[1]) or location
            if kind in ('Code', 'CodeBlock') and location:
                protected.append(location)
            if kind in ('Link', 'Image'):
                if location is None:
                    raise ValueError('Pandoc returned a link without source positions')
                links.append(Link(data[-1][0], *location))
            if kind in ('RawBlock', 'RawInline') and data[0] == 'html' and location:
                if location not in raw_seen:
                    raw_seen.add(location)
                    start, end = location
                    raw = text[start:end]
                    parser = Anchors(); parser.feed(raw); anchors.update(parser.values)
                    for match in re.finditer(r'\b(?:href|src)\s*=\s*(["\'])(.*?)\1', raw, re.I | re.S):
                        links.append(Link(unescape(match[2]), start + match.start(2), start + match.end(2), 'html'))
            for value in node.values():
                walk(value, location)
    walk(ast)
    return links, anchors, protected


def local_url(url, pages, mode):
    parsed = urlsplit(url)
    path = parsed.path
    if mode == 'repository':
        wiki = '/' + REPOSITORY + '/wiki'
        raw = '/wiki/' + REPOSITORY + '/'
        if parsed.netloc == 'github.com' and (path == wiki or path.startswith(wiki + '/')):
            path = unquote(path[len(wiki):].lstrip('/')) or 'Home'
        elif parsed.netloc == 'raw.githubusercontent.com' and path.startswith(raw):
            path = unquote(path[len(raw):])
        elif parsed.scheme or parsed.netloc:
            return url
        else:
            path = unquote(path)
        clean = path[2:] if path.startswith('./') else path
        if clean in pages or clean + '.md' in pages:
            path = clean if clean.endswith('.md') else clean + '.md'
        elif clean.startswith('assets/'):
            path = clean
        elif parsed.scheme or parsed.netloc:
            return url
        else:
            path = clean
    else:
        if parsed.scheme or parsed.netloc:
            return url
        path = unquote(path)
        clean = path[2:] if path.startswith('./') else path
        if clean in pages and clean.endswith('.md'):
            path = clean[:-3]
    if not path:
        return url
    return urlunsplit(('', '', quote(path, safe='/-._~'), parsed.query, parsed.fragment))


def destination_range(segment):
    # Locate the destination after a closing link label; balance URL parentheses.
    for marker in reversed(list(re.finditer(r'\]\s*\(', segment))):
        start = marker.end()
        while start < len(segment) and segment[start].isspace():
            start += 1
        if start < len(segment) and segment[start] == '<':
            end = segment.find('>', start + 1)
            if end >= 0:
                return start + 1, end
        depth, end = 0, start
        while end < len(segment):
            char = segment[end]
            if char == '\\':
                end += 2
                continue
            if char == '(':
                depth += 1
            elif char == ')':
                if depth == 0:
                    break
                depth -= 1
            elif char.isspace() and depth == 0:
                break
            end += 1
        if end > start:
            return start, end
    return None


def rewrite(text, pages, mode):
    links, _, protected = inspect(text)
    edits = {}
    definitions = list(re.finditer(r'^ {0,3}\[[^\]\n]+\]:[ \t]*(?:<([^>\n]+)>|([^\s]+))', text, re.M))
    for link in links:
        target = local_url(link.url, pages, mode)
        if target == link.url:
            continue
        if link.kind == 'html':
            edits[(link.start, link.end)] = target.replace('&', '&amp;')
            continue
        segment = text[link.start:link.end]
        found = destination_range(segment)
        if found:
            start, end = found
            edits[(link.start + start, link.start + end)] = target
            continue
        matches = []
        for definition in definitions:
            group = 1 if definition[1] is not None else 2
            start, end = definition.span(group)
            if any(a <= start < b for a, b in protected):
                continue
            if unescape(text[start:end]) == link.url:
                matches.append((start, end))
        if matches:
            for location in matches:
                edits[location] = target
        elif segment.startswith('<') and segment.endswith('>'):
            edits[(link.start, link.end)] = '[' + segment[1:-1] + '](' + target + ')'
        else:
            raise ValueError('Cannot safely rewrite link syntax: ' + segment[:100])
    ordered = sorted(edits.items(), reverse=True)
    previous = len(text) + 1
    for (start, end), value in ordered:
        if end > previous:
            raise ValueError('Overlapping link edits')
        text = text[:start] + value + text[end:]
        previous = start
    return text, len(edits)


def validate(pages_dir, published=False):
    pages_dir = pages_dir.resolve()
    files = {file.name: file for file in pages_dir.glob('*.md')}
    parsed = {name: inspect(file.read_text()) for name, file in files.items()}
    errors = []; checked = 0
    for name, (links, anchors, _) in parsed.items():
        for link in links:
            try:
                url = urlsplit(link.url)
            except ValueError as error:
                errors.append(f'{name}: {error}: {link.url}'); continue
            if url.scheme or url.netloc:
                continue
            checked += 1
            if not url.path:
                target = files[name]
            else:
                path = unquote(url.path)
                target = (pages_dir / path).resolve()
                if published and path + '.md' in files:
                    target = pages_dir / (path + '.md')
            if not target.is_relative_to(pages_dir) or not target.is_file():
                errors.append(f'{name}: missing local file: {link.url}'); continue
            if target.suffix == '.md' and url.fragment and unquote(url.fragment) not in parsed[target.name][1]:
                errors.append(f'{name}: missing heading: {link.url}')
    if errors:
        raise ValueError('\n'.join(errors[:50]) + f'\n{len(errors)} broken links')
    return {'pages': len(files), 'local_links': checked}
