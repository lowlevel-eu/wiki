# Am Lowlevel-Wiki mitarbeiten

Ob Tippfehler, bessere Erklärung oder neuer Artikel: Verbesserungen sind willkommen!
Öffne einen Pull Request in diesem Repository. Fragen und Ideen passen auch in
unsere [Diskussionen](https://github.com/lowlevel-eu/wiki/discussions).

## Einen Artikel bearbeiten

1. Suche die Markdown-Datei unter [`pages/`](pages/). Auf GitHub kannst du über
   das Stiftsymbol direkt einen Änderungsvorschlag erstellen; alternativ klonst
   du das Repository und arbeitest auf einem eigenen Branch.
2. Beschreibe im Pull Request kurz, was du verbessert hast und warum.
3. Nach der Prüfung und dem Merge nach `main` veröffentlicht die GitHub Action
   die Änderungen im [Wiki](https://github.com/lowlevel-eu/wiki/wiki).

Bitte bearbeite die Artikel hier im Repository. Das GitHub-Wiki wird aus `pages/`
veröffentlicht; direkte Änderungen dort werden nicht automatisch zurückimportiert.

## Links, Bilder und Beispiele

- Artikel bleiben als einzelne `.md`-Dateien unter `pages/` liegen. Verlinke sie
  relativ mit Dateiendung, zum Beispiel `[Paging](Paging.md)` oder
  `[Abschnitt](Paging.md#funktionsweise)`. GitHub ergänzt beim Einfügen eines
  Links gegebenenfalls die URL-Kodierung für Umlaute und Sonderzeichen.
- Bilder und weitere Dateien liegen unter `pages/assets/`, mit verständlichen
  Dateinamen. Ein Bild bindest du etwa mit `![Beschreibung](assets/Bild.png)` ein.
- Die Veröffentlichung passt Artikellinks an die Wiki-URLs an. Du musst keine
  zweite Fassung des Artikels pflegen.
- Quelltext gehört in eingezäunte Codeblöcke mit passender Sprache. Bestehende
  Autoren-, Quellen- und Lizenzhinweise bitte erhalten; bei fremden Inhalten
  deren Herkunft und Bedingungen angeben. Siehe [LICENSE.md](LICENSE.md).

## Lokal prüfen

Benötigt werden Python ab 3.10, Pandoc ab 3.1 und Git. Weitere Python-Pakete sind
nicht erforderlich.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/publish_wiki.py check
python3 scripts/publish_wiki.py preview --output /tmp/lowlevel-wiki-preview
```

Das Zielverzeichnis für die Vorschau darf noch nicht existieren. Die Vorschau
enthält dieselben Dateien wie die Veröffentlichung und verändert das Wiki nicht.
Der PR-Workflow prüft die Dateien, Links, Überschriftenanker und die Vorschau
auch automatisch.
