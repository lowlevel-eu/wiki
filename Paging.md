# Paging

Paging ist ein Mechanismus, der auf vielen Architekturen zum Einsatz kommt. Dabei wird zwischen physikalischem und virtuellem Speicher unterschieden. Der virtuelle Speicher wird in gleich große Blocke, so genannte Pages, unterteilt. Dann kann jeder Page ein physikalischer Speicherbereich zugeordnet werden.

Durch das Paging lassen sich weitere Features, wie z.B. [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping"), leichter implementieren. Auch ist durch Paging Speicherschutz gewährleistet, da jeder Prozess einen eigenen virtuellen Adressraum bekommt und somit von den anderen Prozessen abgeschirmt ist.

## Einschalten des Paging-Mechanismus

Zum Einschalten des Paging-Mechanismus auf der x86-Architektur muss man Bit-31 im CR0-Register setzen. Davor muss aber ein gültiges Page-Directory angelegt und dessen Physikalische Adresse im CR3-Register abgelegt worden sein.

## Page-Directory

## Page-Tables

## Links

- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#paging "Ausgabe 8")
- <http://osdever.net/tutorials/pdf/basic_paging.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2019/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1496/index.html)

<!-- MediaWiki page 1496; revision 2019; parent 1946; 2007-06-10T06:55:35Z -->
