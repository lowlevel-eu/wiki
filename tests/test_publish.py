import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from publish_wiki import export, git, publish


def commit(repo, message='Teständerung'):
    git(repo, 'add', '--all')
    git(repo, '-c', 'user.name=Test', '-c', 'user.email=test@example.org', 'commit', '--quiet', '-m', message)
    return git(repo, 'rev-parse', 'HEAD')


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.seed = self.base / 'seed'
        self.seed.mkdir()
        git(self.seed, 'init', '--quiet', '--initial-branch=master')
        (self.seed / 'Home.md').write_text('# Start\n\n[Ziel](Ziel)\n')
        (self.seed / 'Ziel.md').write_text('# Ziel\n\nOriginal\n')
        self.baseline = commit(self.seed)
        self.remote = self.base / 'wiki.git'
        git(self.base, 'clone', '--quiet', '--bare', str(self.seed), str(self.remote))
        git(self.seed, 'remote', 'add', 'origin', str(self.remote))
        self.source = self.base / 'source'
        self.source.mkdir()
        git(self.source, 'init', '--quiet', '--initial-branch=main')
        (self.source / 'pages/assets').mkdir(parents=True)
        (self.source / 'pages/Home.md').write_text('# Start\n\n[Ziel](Ziel.md#ziel)\n\n![Bild](assets/a.bin)\n')
        (self.source / 'pages/Ziel.md').write_text('# Ziel\n\nOriginal\n')
        (self.source / 'pages/assets/a.bin').write_bytes(b'\x00\xff\n')
        (self.source / '.github').mkdir()
        config = {'repository': 'lowlevel-eu/wiki', 'wiki_branch': 'master', 'baseline_commit': self.baseline}
        (self.source / '.github/wiki-publish.json').write_text(json.dumps(config))
        self.first_source = commit(self.source)

    def remote_head(self):
        return git(self.base, '--git-dir=' + str(self.remote), 'rev-parse', 'master')

    def test_preview_preserves_assets_and_converts_only_link_targets(self):
        output = self.base / 'preview'
        export(self.source, output)
        self.assertIn('[Ziel](Ziel#ziel)', (output / 'Home.md').read_text())
        self.assertEqual((output / 'assets/a.bin').read_bytes(), b'\x00\xff\n')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            export(self.source, output)

    def test_publish_retains_history_is_repeatable_and_accepts_later_merges(self):
        published = publish(self.source, str(self.remote))
        self.assertEqual(self.remote_head(), published)
        git(self.base, '--git-dir=' + str(self.remote), 'merge-base', '--is-ancestor', self.baseline, published)
        html = git(self.base, '--git-dir=' + str(self.remote), 'show', 'master:Home.md')
        self.assertIn('[Ziel](Ziel#ziel)', html)
        self.assertIsNone(publish(self.source, str(self.remote)))
        self.assertEqual(self.remote_head(), published)
        (self.source / 'pages/Ziel.md').write_text('# Ziel\n\nNeue Erklärung\n')
        commit(self.source)
        updated = publish(self.source, str(self.remote))
        self.assertNotEqual(updated, published)
        git(self.base, '--git-dir=' + str(self.remote), 'merge-base', '--is-ancestor', published, updated)

    def test_direct_wiki_edit_is_not_overwritten(self):
        publish(self.source, str(self.remote))
        checkout = self.base / 'manual'
        git(self.base, 'clone', '--quiet', str(self.remote), str(checkout))
        (checkout / 'Ziel.md').write_text('# Ziel\n\nDirekte Änderung\n')
        manual = commit(checkout)
        git(checkout, 'push', '--quiet', 'origin', 'master')
        with self.assertRaisesRegex(ValueError, 'edited directly'):
            publish(self.source, str(self.remote))
        self.assertEqual(self.remote_head(), manual)

    def test_initial_publication_checks_the_pulled_baseline(self):
        (self.seed / 'Ziel.md').write_text('# Ziel\n\nNeue Wiki-Änderung\n')
        changed = commit(self.seed)
        git(self.seed, 'push', '--quiet', 'origin', 'master')
        with self.assertRaisesRegex(ValueError, 'changed after migration'):
            publish(self.source, str(self.remote))
        self.assertEqual(self.remote_head(), changed)

    def test_stale_source_cannot_replace_newer_publication(self):
        publish(self.source, str(self.remote))
        (self.source / 'pages/Ziel.md').write_text('# Ziel\n\nZweiter Stand\n')
        commit(self.source)
        latest = publish(self.source, str(self.remote))
        git(self.source, 'checkout', '--quiet', self.first_source)
        with self.assertRaisesRegex(ValueError, 'Git failed'):
            publish(self.source, str(self.remote))
        self.assertEqual(self.remote_head(), latest)


if __name__ == '__main__': unittest.main()
