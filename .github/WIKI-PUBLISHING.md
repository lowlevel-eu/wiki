# Das Wiki aus Pull Requests veröffentlichen

`main` in `lowlevel-eu/wiki` ist die maßgebliche Quelle. Alle Wiki-Dateien liegen
unter `pages/`; die vorhandenen Seiten und Medien werden nach
`lowlevel-eu/wiki.wiki.git` auf dessen Branch `master` veröffentlicht.
Bestehende Wiki-URLs bleiben dabei erhalten.

## Einmal auf GitHub einrichten

1. Das Wiki aktiviert lassen. Unter **Settings → General → Features → Wikis**
   die öffentliche Bearbeitung deaktivieren: Beiträge erfolgen über Pull Requests.
   Personen mit Schreibrechten am Repository können das Wiki weiterhin direkt
   bearbeiten; für Änderungen bitte ebenfalls den PR-Weg verwenden.
2. GitHub Actions im Repository erlauben. Der Publish-Job verwendet den von
   GitHub automatisch erzeugten **`GITHUB_TOKEN`** mit `contents: write`.
   Dieser Token gehört zur Actions-Installation dieses Repositories und wird
   für jeden Job neu erzeugt. Ein persönlicher Access Token, ein manuell
   angelegter Secret oder eine zusätzliche GitHub App sind nicht erforderlich.
   Die Schreibberechtigung steht nur im Publish-Job; PR-Prüfungen bleiben lesend.
   Siehe [GitHub-Dokumentation zum GITHUB_TOKEN](https://docs.github.com/en/actions/concepts/security/github_token).

3. Für `main` eine Branch-Regel bzw. ein Ruleset mit Pull Requests und dem
   erforderlichen Statuscheck **Wiki prüfen** einrichten. Die Prüfung wird bei
   jedem PR und bei Pushes nach `main` ausgeführt.
4. Nach dem Push dieser Umstellung den Workflow **Wiki prüfen und veröffentlichen**
   ausführen lassen. Er kann über **Actions → Run workflow** auf `main` erneut
   gestartet werden. GitHub Pages ist dafür nicht erforderlich.

Der Check-Job benötigt keine Schreibrechte oder Secrets. Der Publish-Job läuft
nur auf `main` des Originalrepositories, nach erfolgreicher Prüfung; bei Pull
Requests wird er nicht ausgeführt. Veröffentlichungen werden serialisiert.

## Was veröffentlicht wird

Nur der Inhalt von `pages/` gelangt ins Wiki. README, Lizenzhinweise,
Beitragsleitfaden, Tests und Workflows bleiben im Hauptrepository.
Artikellinks mit `.md` werden für die Wiki-Ausgabe in die bestehenden Wiki-Links
umgewandelt. Dabei werden nur Linkziele bearbeitet, nicht ganze Markdown-Dateien
neu formatiert. Codeblöcke und Inline-Code bleiben unverändert.

Die bisherige Wiki-Historie bleibt erhalten. Eine Veröffentlichung hängt einen
normalen Commit mit Verweis auf den maßgeblichen Source-Commit an; sie verwendet
keinen Force-Push. Dadurch bleiben neue Review- und Autorendaten im Hauptrepository
und die bisherigen Seitenstände im Wiki nachvollziehbar.

## Schutz vor direkten Wiki-Änderungen

Die erste Veröffentlichung erwartet den beim Umzug festgehaltenen Wiki-Commit
in `wiki-publish.json`. Danach speichert `.wiki-publication.json` im veröffentlichten
Wiki den Quell-Commit und Prüfsummen aller veröffentlichten Dateien. Direkte
Änderungen, neue oder gelöschte Dateien führen beim nächsten Lauf zum Abbruch,
statt still überschrieben zu werden. Auch ein älterer Workflow-Stand kann einen
neueren veröffentlichten Quellstand nicht ersetzen.

Falls nach dem Umzug noch jemand direkt im Wiki gearbeitet hat: erst das Wiki
pullen, die Änderungen nach `pages/` übernehmen und prüfen. Vor der ersten
Veröffentlichung den `baseline_commit` in `wiki-publish.json` auf den übernommenen
Wiki-Stand aktualisieren. Nach einer späteren manuellen Änderung sind zusätzlich
die Prüfsummen im Wiki-Publikationsmarker auf den **geprüften und übernommenen**
Dateistand zu aktualisieren. Den Schutz nicht durch einen Force-Push umgehen.

## Werkzeuge

```sh
python3 scripts/publish_wiki.py check
python3 scripts/publish_wiki.py preview --output /tmp/lowlevel-wiki-preview
```

`normalize` ist ein Werkzeug für den einmaligen Umzug oder weitere Importe:
Es setzt vorhandene alte Wiki-Links in `pages/` auf explizite Repository-Dateilinks
um. `publish` erhält im Workflow den automatischen Token über die
Umgebungsvariable `WIKI_TOKEN` und verlangt einen sauberen Arbeitsbaum. Eine lokale Vorschau benötigt keinen Token und schreibt
nichts nach GitHub.
