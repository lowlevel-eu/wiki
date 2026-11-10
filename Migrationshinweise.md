# Migrationshinweise

Dieses Wiki führt die Artikel des Lowlevel-MediaWikis als bearbeitbare Markdown-Seiten weiter.
Das [Originalarchiv](https://lowlevel-eu.github.io/) bleibt als schreibgeschützte Referenz erhalten.

- Importiert wurden 535 Artikel- und Weiterleitungsseiten mit 6625 öffentlich zugänglichen Versionen.
- Jede Artikelversion ist ein eigener Git-Commit mit ursprünglichem Benutzernamen,
  dem gemeinsamen E-Mail-Platzhalter `wiki@lowlevel.eu`, UTC-Zeitstempel und Bearbeitungskommentar.
- Vorlagen-, Kategorie-, Diskussions-, Benutzer-, Datei- und Konfigurationsseiten wurden nicht importiert.
  Links dorthin führen gegebenenfalls ins Originalarchiv; benötigte Medien liegen im Ordner `assets/`.
- Vorlagen sind im Artikeltext bereits aufgelöst. Wiederkehrende Textbausteine werden hier direkt im jeweiligen Artikel bearbeitet.
- Historische Artikel wurden von MediaWiki unter Verwendung des Vorlagenstands des Snapshots gerendert.
  Frühere Vorlagen- und Mediendateistände werden dadurch nicht historisch rekonstruiert.
- Artikeldateien tragen ihre zuletzt bekannten Titel. Frühere Verschiebungen sind in den
  ursprünglichen Kommentaren dokumentiert, nicht als nachträglich erfundene Git-Umbenennungen.
- Layouttabellen werden in Lesereihenfolge aufgelöst und einfache Tabellen als Markdown geschrieben.
  Codebeispiele in Tabellen werden in beschriftete Abschnitte mit Codeblöcken umgewandelt.
  Sehr breite Registertabellen mit verbundenen Zellen bleiben als HTML erhalten.
- MediaWiki-Anker werden auf native GitHub-Überschriftenanker abgebildet. Anker außerhalb
  von Überschriften führen zum umgebenden Abschnitt; doppelte unsichtbare HTML-Anker entfallen.
- Ein unsichtbarer Versionsmarker erhält auch solche Bearbeitungen in der Seitenhistorie,
  deren Unterschiede bei der Markdown-Konvertierung verschwinden würden.
- Weiterleitungen sind normale Seiten mit einem Link zum Ziel. Gewöhnliche Artikellinks
  wurden nach Möglichkeit direkt auf das Ziel umgeschrieben.

Die verlinkten Ursprungsseiten und ihre Versionsgeschichten bewahren die bisherigen
Autoren- und Lizenzhinweise. Es wird keine neue Inhaltslizenz vergeben.
