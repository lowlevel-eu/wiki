from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from wiki_content import inspect, rewrite


class ContentTests(unittest.TestCase):
    def test_destinations_change_without_reformatting_code_or_labels(self):
        text = '# Grüße\n\nGrüße\t[**Link**](Home "Titel") und ![Bild](assets/Stern.png).\n\n```md\n[Beispiel](Home)\n```\n\n`[Beispiel](Home)`\n'
        converted, count = rewrite(text, {'Home.md', 'C++.md'}, 'repository')
        self.assertEqual(count, 1)
        self.assertEqual(converted, text.replace('[**Link**](Home "Titel")', '[**Link**](Home.md "Titel")'))
        restored, count = rewrite(converted, {'Home.md', 'C++.md'}, 'wiki')
        self.assertEqual(restored, text)

    def test_images_nested_labels_unicode_and_fragments(self):
        text = 'Ää [C++](C%2B%2B#code) und [![Bild](assets/a.png)](OS-Dev-f%C3%BCr-Einsteiger).\n'
        converted, count = rewrite(text, {'C++.md', 'OS-Dev-für-Einsteiger.md'}, 'repository')
        self.assertIn('(C%2B%2B.md#code)', converted)
        self.assertIn('(OS-Dev-f%C3%BCr-Einsteiger.md)', converted)
        self.assertEqual(count, 2)

    def test_reference_links_and_html(self):
        text = '[Start][home]\n\n[home]: Home "Titel"\n\n<a href="C%2B%2B">C++</a>\n\n```md\n[example]: Home\n```\n'
        converted, count = rewrite(text, {'Home.md', 'C++.md'}, 'repository')
        self.assertIn('[home]: Home.md "Titel"', converted)
        self.assertIn('href="C%2B%2B.md"', converted)
        self.assertIn('[example]: Home\n', converted)
        self.assertEqual(count, 2)

    def test_absolute_wiki_links_assets_and_external_urls(self):
        text = '[Start](https://github.com/lowlevel-eu/wiki/wiki/Home) ![Bild](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/a.png) [Extern](https://example.com/Home)\n'
        converted, count = rewrite(text, {'Home.md'}, 'repository')
        self.assertEqual(count, 2)
        self.assertIn('[Start](Home.md)', converted)
        self.assertIn('![Bild](assets/a.png)', converted)
        self.assertIn('[Extern](https://example.com/Home)', converted)


if __name__ == '__main__': unittest.main()
