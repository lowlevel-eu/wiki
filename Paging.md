# Paging

Paging ist ein Mechanismus, der auf vielen Architekturen zum Einsatz kommt. Dabei wird zwischen physikalischem und virtuellem Speicher unterschieden. Der virtuelle Speicher wird in gleich große Blocke, so genannte Pages, unterteilt. Dann kann jeder Page ein physikalischer Speicherbereich zugeordnet werden.

Durch das Paging lassen sich weitere Features, wie z.B. [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping"), leichter implementieren. Auch ist durch Paging Speicherschutz gewährleistet, da jeder Prozess einen eigenen virtuellen Adressraum bekommt und somit von den anderen Prozessen abgeschirmt ist.

## Einschalten des Paging-Mechanismus

Zum Einschalten des Paging-Mechanismus auf der x86-Architektur muss man Bit-31 im CR0-Register setzen. Davor muss aber ein gültiges Page-Directory angelegt und dessen Physikalische Adresse im CR3-Register abgelegt worden sein.

## Page-Directory

## Page-Tables

## Translation Lookaside Buffer

Zu beachten ist, dass bei einer Änderung des Page-Directory oder einer Page-Table, der TLB (Translation Lookaside Buffer) invalidiert werden muss, sonst können unerwartete Ereignisse auftreten. Man invalidiert den TLB mit "invlpg \<address\>". Wobei \<address\> eine beliebige Adresse im RAM ist, der TLB, der zugehörigen Page, wird dann invalidiert.

## Links

- [Paging Tutorial](http://www.homix-online.de/Tutorials/32PMode-Paging.php)
- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#paging "Ausgabe 8")
- <http://osdever.net/tutorials/pdf/basic_paging.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2171/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1496/index.html)

<!-- MediaWiki page 1496; revision 2171; parent 2044; 2007-10-13T00:09:40Z -->
