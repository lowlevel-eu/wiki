# Paging

Paging ist ein Mechanismus, der auf vielen Architekturen zum Einsatz kommt. Dabei wird zwischen physikalischem und virtuellem Speicher unterschieden. Der virtuelle Speicher wird in gleich große Blocke, so genannte Pages, unterteilt. Dann kann jeder Page ein physikalischer Speicherbereich zugeordnet werden.

Durch das Paging lassen sich weitere Features, wie z.B. [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping"), leichter implementieren. Auch ist durch Paging Speicherschutz gewährleistet, da jeder Prozess einen eigenen virtuellen Adressraum bekommt und somit von den anderen Prozessen abgeschirmt ist.

## Einschalten des Paging-Mechanismus

Zum Einschalten des Paging-Mechanismus auf der x86-Architektur muss man Bit-31 im CR0-Register setzen. Davor muss aber ein gültiges Page-Directory angelegt und dessen Physikalische Adresse im CR3-Register abgelegt worden sein.

## Page-Directory

Ein Pagedirectory enthält 1024 Eintrage a 4 Byte. Ein Pagedirectory-Eintrag kann jeweils auf ein Pagetable zeigen. Pagedirectories (wie auch Pagetables) müssen immer 4k-aligned sein, d.h sie füllen genau eine Page aus.

| 31..10 | 11..9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----------- | ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Pagetable | Verf. | G | S | 0 | A | C | W | U | R | P |

Verf.: Diese Bits sind frei verfügbar. Sie können z.B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswaped werden können, und/oder um Pages zu makieren, die nicht ausgelagert werden dürfen.

G: Wird ignoriert

S: Gibt die Größe der Page an. 0 steht für 4kB, 1 für 4MB.

A: Wird von der CPU gesetzt, wenn das Pagetable benutzt wurde. Diese Bit wird allerdings nicht von der CPU zurückgesetzt.

C: Wenn dieses Bit gesetzt ist, wird die Page nicht gecachet.

W: Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt.

U: Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0

R: Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann nur die Page nur gelesen werden.

P: Gibt an ob die Page im Speicher liegt. Ist das Bit gelöscht(Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z.B. für Swapping genutzt werden.

## Page-Tables

Ein Pagetable enthält 1024 Einträge a 4 Byte. Jeder Eintrag zeigt auf eine physikalische Page. Pagetables müssen 4k-aligned sein und füllen somit eine ganze Page.

| 31..10 | 11..9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| -------------- | ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Page (phys.) | Verf. | G | 0 | D | A | C | W | U | R | P |

Hier werden nur neue Abkürzungen geklärt, andere sind unter [Page-Directory](#page-directory) zu finden.

G: Wenn G gesetzt ist, wird der TLB für diese Page nicht erneuert, nachdem CR3 neu gesetzt wurde. Diese Flag ist also praktisch für Pages, die in jedem Adressraum gleich gemappt sind (z.B Kernel)

D: Dieses Bit wird von der CPU gesetzt, wenn auf die Page geschrieben wurde. Dieses Bit wird nicht von der CPU zurückgesetzt.

## Translation Lookaside Buffer

Zu beachten ist, dass bei einer Änderung des Page-Directory oder einer Page-Table, der TLB (Translation Lookaside Buffer) invalidiert werden muss, sonst können unerwartete Ereignisse auftreten. Man invalidiert den TLB mit "invlpg \<address\>". Wobei \<address\> eine beliebige Adresse im RAM ist, der TLB, der zugehörigen Page, wird dann invalidiert.

## Speicher mappen

Um eine beliebige physikalische Adresse auf eine beliebige virtuelle Adresse zu mappen, muss man erst den richtigen Eintrag im Pagedirectory und den in der Pagetable berechnen um schließlich die physikalische Page(mit den passenden Flags) in der Pagetable eintragen zu können. Es wird immer von virtuell nach physikalisch zugeordnet, d.h wenn man 0xB8000(phys.) auf 0x12345000(virt.) mappen will, muss man erst den Pagedirectory- und Pagetable-Eintrag von 0x12345000 berechnen. Das geht am besten so:

    Pagedirectory_Eintrag =  virtuelle_adresse >> 22           (= 0x48)
    Pagetable_Eintrag     = (virtuelle_adresse >> 12) % 1024   (= 0x345)

Nun suche man erst die Adresse der Pagetable (im eben berechneten *Pagedirectory_Eintrag* schauen). **Achtung:** Es handelt sich hier um die physikalische adresse. Mit der Adresse der Pagetable kann man jetzt in den *Pagetable_Eintrag* die physikalische Adresse eintragen, die passenden Flags setzen und schon ist die Page gemappt.

## In physikalischen Speicher schreiben

Wenn nun Paging eingeschaltet ist, kann man nicht mehr in den physikalischen Speicher schreiben. Wenn man nicht viel physikalischen Speicher hat, oder 64 Bit benutzt und deswegen der virtuelle Adressraum groß genug ist, kann man den gesamten physikalischen Speicher in den virtuellen mappen.

Es besteht aber auch die Möglichkeit Zugriff auf den gesamten physikalischen Speicher zu haben, ohne das man ihn direkt mappt. Erstmal braucht man eine Möglichkeit das Pagedirectory und die Pagetables noch zu ändern, nachdem Paging eingeschaltet wurde. Wenn man dies kann, kann man sich einfach immer die gerade gebrauchte physikalische Page auf eine festgelegte virtuelle Page mappen und voila. Um nun Zugriff auf das Pagedirectory und die Pagetables zu haben, muss man einfach z.B als letztes Pagetable, das Pagedirectory selber eintragen. Das Pagedirectory wird dann als Pagetable interpretiert und alle Pagetables als Pages in den Speicher gemappt. Somit enthalten die letzten 4 MB die Pagetables, wobei die letzten 4kB das Pagedir enthalten.

## Links

- [Paging Tutorial](http://www.homix-online.de/Tutorials/32PMode-Paging.php)
- [Paging im PM-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/p_spez1.htm)
- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#paging "Ausgabe 8")
- <http://osdever.net/tutorials/pdf/basic_paging.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2990/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1496/index.html)

<!-- MediaWiki page 1496; revision 2990; parent 2989; 2008-06-23T10:45:53Z -->
