# Klovnix

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Keine Homepage, keine Download-Möglichkeit, keine sichtbare relevanz --[PNoob](https://lowlevel-eu.github.io/wiki/pages/2377/index.html "Benutzer:PNoob") 13:44, 8. Mär. 2011 (CET)

| Klovnix |  |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
|  |  |
| Entwickler: | XUNIX |
| Akt. Version: | --- |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Werbe Klausel |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolithischer Kernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | --- |
| Binärformat: | .bin |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | --- |
| Homepage |  |

---

**Klovnix** ist ein von mir in Assembler hergestelltes Hobby-OS.

## Dateiformat

Jenes soll ein eigenes Dateiformat besitzen, welches recht einfach zu erklären ist. Nehmen wir an, dass die Ausführbaren Dateien am Anfang die Kennungsnummer 0x2000 haben. Darunter wird sich der Dateiname der Datei befinden. Wenn wir jetzt die dir Funktion benutzen, sucht die Funktion im ganzem Diskettenimage erstmal nach Dateien, die am Anfang diese Kennungsnummer haben. Durch einen String-Compare wird dann der Dateiname "identifiziert" und viollá, wird nach einander der Dateiname aufgelistet. So funktioniert es auch bei anderen Dateien, die eine andere Kennungsnummer haben. Das gleiche funktioniert bei der Funktion, wo man die Dateien ausführt. Es sucht nach den Dateien(aber insgeheim) und dann, wenn diese eingetippte Datei genauso heißt, wie eine Datei von den vielen, führt er sie aus. Dieses Dateiformat-Projekt ist im Alpha-Stadium. Also bitte dazu noch keine Kommentare abgeben. Danke.

## Features

Für die Version **0.1.0** ist vorausgesehen:

- Bootloader
- Tastaturtreiber
- Text-Editor
- Dieses da oben genannte Dateisystem
- Ordner-Erstellen Funktion(im Alpha-Stadium, keine Diskussion darüber)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9619/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2406/index.html)

<!-- MediaWiki page 2406; revision 9619; parent 9617; 2011-03-08T12:44:44Z -->
