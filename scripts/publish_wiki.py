#!/usr/bin/env python3
"""Validate, preview or publish pages/ to the existing GitHub Wiki without force pushes."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from wiki_content import REPOSITORY, rewrite, validate

ROOT = Path(__file__).resolve().parents[1]
STATE = '.wiki-publication.json'


def git(repo, *args, env=None):
    command = ['git', '-C', str(repo), '-c', 'credential.helper=', '-c', 'commit.gpgsign=false', *args]
    result = subprocess.run(command, env=env, text=True, capture_output=True)
    if result.returncode:
        raise ValueError('Git failed: ' + result.stderr.strip())
    return result.stdout.strip()


def manifest(directory):
    result = {}
    for file in sorted(directory.rglob('*')):
        relative = file.relative_to(directory)
        if '.git' in relative.parts or relative.as_posix() == STATE:
            continue
        if file.is_symlink():
            raise ValueError('Symlinks are not supported: ' + str(relative))
        if file.is_file():
            result[relative.as_posix()] = hashlib.sha256(file.read_bytes()).hexdigest()
    return result


def export(root, output):
    source = root / 'pages'
    if not (source / 'Home.md').is_file():
        raise ValueError('pages/Home.md is missing')
    if output.exists():
        raise ValueError('Preview output already exists: ' + str(output))
    if output.resolve().is_relative_to(source.resolve()) or source.resolve().is_relative_to(output.resolve()):
        raise ValueError('Output and pages/ must be separate directories')
    validate(source)
    files = manifest(source)
    output.mkdir(parents=True)
    pages = {p.name for p in source.glob('*.md')}
    def copy(name):
        file = source / name
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if file.suffix == '.md':
            text, _ = rewrite(file.read_text(), pages, 'wiki')
            target.write_text(text)
        else:
            shutil.copyfile(file, target)
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(copy, files))
    validate(output, published=True)
    return manifest(output)


def normalize(root):
    directory = root / 'pages'
    pages = {file.name for file in directory.glob('*.md')}
    def prepare(file):
        text, count = rewrite(file.read_text(), pages, 'repository')
        return file, text, count
    with ThreadPoolExecutor(max_workers=4) as pool:
        edits = list(pool.map(prepare, directory.glob('*.md')))
    count = 0
    for file, text, changes in edits:
        if changes:
            file.write_text(text)
            count += changes
    print(f'Updated {count} link destinations; formatting and examples retained.')
    return validate(directory)


def publish(root, remote=None):
    config = json.loads((root / '.github/wiki-publish.json').read_text())
    if config['repository'] != REPOSITORY or not re.fullmatch(r'[0-9a-f]{40}', config['baseline_commit']):
        raise ValueError('Invalid publication configuration')
    branch = config['wiki_branch']
    if not re.fullmatch(r'[A-Za-z0-9_-]+', branch):
        raise ValueError('Invalid wiki branch')
    if git(root, 'status', '--porcelain'):
        raise ValueError('Publishing requires a clean source working tree')
    source_commit = git(root, 'rev-parse', 'HEAD')
    token = os.environ.get('WIKI_TOKEN', '')
    if remote is None and not token:
        raise ValueError('Provide WIKI_TOKEN; in Actions use github.token with contents: write')
    remote = remote or f'https://github.com/{REPOSITORY}.wiki.git'
    with tempfile.TemporaryDirectory(prefix='lowlevel-wiki-publish-') as temporary:
        work = Path(temporary)
        env = os.environ.copy()
        askpass = work / 'askpass.py'
        askpass.write_text('#!/usr/bin/env python3\nimport os, sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ.get("WIKI_TOKEN", ""))\n')
        askpass.chmod(0o700)
        env.update({'GIT_ASKPASS': str(askpass), 'GIT_TERMINAL_PROMPT': '0'})
        git(work, 'clone', '--quiet', '--no-hardlinks', '--single-branch', '--branch', branch, remote, str(work / 'wiki'), env=env)
        wiki = work / 'wiki'
        existing = manifest(wiki)
        state_path = wiki / STATE
        if state_path.exists():
            state = json.loads(state_path.read_text())
            if state.get('repository') != REPOSITORY or state.get('files') != existing:
                raise ValueError('The published wiki was edited directly; import those edits into pages/ before publishing again')
            previous = state.get('source_commit', '')
            if not re.fullmatch(r'[0-9a-f]{40}', previous):
                raise ValueError('Invalid previous source commit in publication state')
            git(root, 'merge-base', '--is-ancestor', previous, source_commit)
        elif git(wiki, 'rev-parse', 'HEAD') != config['baseline_commit']:
            raise ValueError('The wiki changed after migration; pull and import the new edits before the first publication')
        preview = work / 'preview'
        files = export(root, preview)
        if state_path.exists() and files == existing:
            print('The published wiki is already up to date.')
            return None
        for file in wiki.iterdir():
            if file.name == '.git':
                continue
            if file.is_dir():
                shutil.rmtree(file)
            else:
                file.unlink()
        shutil.copytree(preview, wiki, dirs_exist_ok=True)
        (wiki / STATE).write_text(json.dumps({'repository': REPOSITORY, 'source_commit': source_commit, 'files': files}, sort_keys=True, indent=2) + '\n')
        git(wiki, 'add', '--all')
        git(wiki, '-c', 'user.name=Lowlevel Wiki', '-c', 'user.email=wiki@lowlevel.eu',
            'commit', '--quiet', '-m', 'Wiki aus main veröffentlichen (' + source_commit[:12] + ')',
            '-m', 'Quelle: https://github.com/' + REPOSITORY + '/commit/' + source_commit)
        # A normal push also rejects an edit made after the clone above.
        git(wiki, 'push', 'origin', 'HEAD:refs/heads/' + branch, env=env)
        print('Published source commit ' + source_commit + ' to the wiki.')
        return git(wiki, 'rev-parse', 'HEAD')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['check', 'normalize', 'preview', 'publish'])
    parser.add_argument('--output', type=Path, help='A new directory for the wiki preview')
    args = parser.parse_args()
    if args.command == 'check':
        print(validate(ROOT / 'pages'))
    elif args.command == 'normalize':
        print(normalize(ROOT))
    elif args.command == 'preview':
        if args.output is None:
            parser.error('preview requires --output')
        files = export(ROOT, args.output)
        print(f'Wiki preview: {len(files)} files written to {args.output}')
    else:
        publish(ROOT)


if __name__ == '__main__':
    main()
