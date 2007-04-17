# Paging

Paging ist ein Mechanismus, der auf vielen Architekturen zum Einsatz kommt. Dabei wird zwischen physikalischem und virtuellem Speicher unterschieden. Der virtuelle Speicher wird in gleich große Blocke, so genannte Pages, unterteilt. Dann kann jeder Page ein physikalischer Speicherbereich zugeordnet werden.

Durch das Paging lassen sich weitere Features, wie z.B. [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping"), leichter implementieren. Auch ist durch Paging Speicherschutz gewährleistet, da jeder Prozess einen eigenen virtuellen Addressraum bekommt und somit von den anderen Prozessen abgeschirmt ist.

## Einschalten des Paging-Mechanismus

Zum einschalten des Paging-Mechanismus muss man Bit-31 im CR0 register setzen. Dafor muss aber ein gültiges Page-Directory angelegt und desen Physicaliche Adresse im CR3-register Abgelegt werden.

## Page-Directory

## Page-Tables

## Links

- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#paging "Ausgabe 8")
- <http://osdever.net/tutorials/pdf/basic_paging.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1946/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1496/index.html)

<!-- MediaWiki page 1496; revision 1946; parent 1912; 2007-04-17T18:15:22Z -->
