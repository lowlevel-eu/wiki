# Paging

Das **Paging** ist ein Mechanismus, der auf vielen Architekturen zum Einsatz kommt, um virtuellen Speicher zur Verfügung zu stellen. Virtueller Speicher bedeutet, dass auf dem Prozessor ausgeführte Programme nicht mehr direkt mit Speicheradressen arbeiten, die sich direkt auf den physisch als Hardware vorhandenen RAM beziehen, sondern eine Abstraktionsschicht eingeführt wird.

Durch den Einsatz von virtuellem Speicher werden Programme unabhängig davon, an welcher physischen Speicheradresse sie laufen. Dadurch kann vor allem das Problem der Speicherfragmentierung gelöst werden, da Speicherbereiche nicht mehr physisch zusammenhängend sein müssen, um Programmen zusammenhängend zu erscheinen.

Durch das Paging lassen sich außerdem weitere Features, wie z. B. [Swapping](https://github.com/lowlevel-eu/wiki/wiki/Swapping "Swapping"), leichter implementieren. Auch ist durch Paging Speicherschutz gewährleistet, da jeder Prozess einen eigenen virtuellen Adressraum (*Speicherkontext*) zugeordnet bekommen kann und somit von den anderen Prozessen abgeschirmt ist.

## Funktionsweise

Der virtuelle Speicher wird zunächst in gleich große Blöcke, so genannte Pages (Seiten), unterteilt. In der x86-Architektur sind dies Blöcke zu je vier Kilobytes. Einen Speicherkontext kann man sich vereinfacht als eine riesige Tabelle vorstellen, die jedem virtuellen Block einen gleich großen Block irgendwo im physischen Speicher zuweist. Diesen physischen Speicherblock nennt man auch *Page Frame* (dt. Seitenrahmen, oder seltener auch Seitenkachel).

Die folgende Tabelle dient als (von den Zahlen her völlig sinnfreie) Veranschaulichung dieser Übersetzung. Wenn das Programm jetzt auf die Speicheradresse 0x1234 zugreift, wird in Wirklichkeit auf die physische Adresse 0x3234 zugegriffen. Es muss nicht jede virtuelle Adresse *gemappt* (d. h. einer physischen Adresse zugewiesen) sein &#150; der virtuelle Adressraum ist im Allgemeinen auch größer als der installierte physische Speicher (auf i386 beispielsweise 4 GB). Wird auf eine nicht gemappte Adresse zugegriffen, z. B. 0x25a2 im Beispiel, wird eine Exception (x86: [Page Fault](https://github.com/lowlevel-eu/wiki/wiki/Exception#page-fault "Exception")) ausgelöst.

| Virtuell | Physisch |
| ------------------- | ---------- |
| 0x0000 bis 0x0fff | 0xa000 |
| 0x1000 bis 0x1fff | 0x3000 |
| 0x2000 bis 0x2fff | -- |
| ... | ... |

In der Praxis handelt es sich dabei nicht um eine einzige riesige Tabelle, die wie erwähnt zu großen Teilen ohnehin leer bleiben und Speicher verschwenden würde. Stattdessen benutzt man ein zwei- oder mehrstufiges System.

Beim i386 bildet ein *Page Directory* einen Speicherkontext ab. Dabei handelt es sich um eine Tabelle, die virtuellen Speicherblöcken von 4 MB Größe die physische Adresse einer *Page Table* zuweist oder den Speicherbereich als frei markiert.

Die Page Table ist anschließend dafür zuständig, innerhalb „ihrer“ 4 MB die Zuordnung der einzelnen 4K-Pages vorzunehmen. Beim Zugriff auf die Adresse 0x456789 wird also zunächst festgestellt, dass die Pagetable für den Bereich 4 bis 8 MB zuständig ist (0x400000 sind 4 MB), und ihre Adresse im Page Directory nachgeschlagen. Anschließend wird innerhalb der Page Table nachgeschlagen, was die physische Adresse für die Bytes 0x56000 bis 0x56fff dieses 4-MB-Blocks ist. Angenommen, die Page Table ordnet diesen die physische Adresse 0xabcde000 zu, dann liegt der gesuchte Speicher an 0xabcde789.

Wie die CPU aus einer virtuellen die zugeordnete physische Adresse berechnet, soll folgende Grafik zeigen: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/075d16ef1fcec98e13b7.jpg" width="774" height="367" alt="Paging funktionsweise.jpg" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/075d16ef1fcec98e13b7.jpg)

Das Berechnen erfolgt folgendermaßen:

1.  Page Directory suchen, anhand der Adresse in CR3
2.  im Page Directory den Eintrag suchen, dessen Index in Bit 22-31 der virtuellen Adresse steht
3.  dieser Eintrag zeigt auf eine Page Table
4.  in dieser Page Table den Eintrag suchen, dessen Index in Bit 12-21 der virtuellen Adresse steht
5.  dieser Eintrag wiederum zeigt auf eine Page
6.  in dieser Page die gesuchten Daten suchen, deren Offset innerhalb dieser Page in den Bits 0-11 in der virtuellen Adresse steht

(*Hinweis:* Bei Schritt 3 kann der Eintrag auch direkt auf einen 4MB Bereich ("Large Page") zeigen, siehe hierzu [Page Size Extension](https://github.com/lowlevel-eu/wiki/wiki/Page-Size-Extension "Page Size Extension"))

## Einschalten des Paging-Mechanismus

Zum Einschalten des Paging-Mechanismus auf der x86-Architektur muss man Bit-31 im CR0-Register setzen. Davor muss aber ein gültiges Page-Directory angelegt und dessen physische Adresse im CR3-Register abgelegt worden sein.

## Page-Directory

Ein Pagedirectory enthält 1024 Eintrage à vier Byte. Ein Pagedirectory-Eintrag kann jeweils auf ein Pagetable zeigen. Pagedirectories (wie auch Pagetables) müssen immer 4k-aligned sein, d. h. sie füllen genau eine Page aus.

| Bit | Beschreibung |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an, ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page Table benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Wird ignoriert, falls 4-kB-Page, andernfalls wird es von der CPU bei einem Schreibzugriff auf die Page gesetzt |
| 7 | Gibt die Größe der Page an. 0 steht für 4 kB, 1 für 4 MB (oder 2 MB bei Verwendung von PAE). Das S-Bit ist wirkungslos, wenn nicht im [Steuerregister](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Steuerregister") CR4 das PSE-Bit (4-MB-Pages) oder PAE-Bit (2-MB-Pages) gesetzt ist. |
| 8 | Wird ignoriert, falls 4-kB-Page, andernfalls hat es die gleiche Bedeutung wie Bit G in Page-Table-Einträgen (s. u.). |
| 9 &#150; 11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12 &#150; 31 | Bits 12 &#150; 31 eines Zeigers zu einer Pagetable |

## Page Tables

Eine Page Table enthält 1024 Einträge à vier Byte. Jeder Eintrag zeigt auf eine physische Page. Page Tables müssen 4k-aligned sein und füllen somit eine ganze Page.

| Bit | Beschreibung |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Dieses Bit wird von der CPU gesetzt, wenn auf die Page geschrieben wurde. Dieses Bit wird nicht von der CPU zurückgesetzt. |
| 7 | Das (höchste) [PAT](https://github.com/lowlevel-eu/wiki/wiki/PAT "PAT")-Bit. |
| 8 | Wenn G gesetzt ist, wird der TLB (s. u.) für diese Page nicht erneuert, nachdem CR3 neu gesetzt wurde. Diese Flag ist also praktisch für Pages, die in jedem Adressraum gleich gemappt sind (z. B. Kernel) |
| 9 &#150; 11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12 &#150; 31 | 12 &#150; 31 der physischen Adresse eines Pageframes |

## Translation Lookaside Buffer

Der Prozessor benutzt für das Auflösen der virtuellen Adressen eine Art Cache für die zuletzt benutzten Pages, den sogenannten *Translation Lookaside Buffer* oder TLB. Für den Programmierer spielt dieser TLB dann eine Rolle, wenn das Mapping einer Page geändert wird, aber der Prozessor möglicherweise noch die alte physische Adresse im TLB behalten hat.

Daher ist zu beachten, dass bei einer Änderung des Page Directory oder einer Page Table der TLB *invalidiert* werden muss (d. h. der entsprechende Eintrag wird aus dem TLB gelöscht). Versäumt man diese Invalidierung, äußert sich das im Allgemeinen erst später durch völlig unerwartete Ereignisse. Diese Fehler sind extrem schwer zu debuggen, da scheinbar auf die richtige Speicheradresse zugegriffen wird, aber in Wirklichkeit mit falschen Werten gearbeitet wird.

Man invalidiert den TLB mit „invlpg \<address\>“. Wobei \<address\> eine virtuelle Adresse innerhalb der von der Änderung betroffenen Page ist. invlpg ist ab dem 486 vorhanden. Beim Neuladen des [Steuerregisters](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Steuerregister") CR3 wird der TLB ebenfalls komplett geleert (Achtung, das geht natürlich auf die Performance).

## Speicher mappen

Um eine beliebige virtuelle Adresse auf eine beliebige physische Adresse zu mappen, muss man erst den richtigen Eintrag im Page Directory und in der Page Table berechnen, um schließlich die physische Page (mit den passenden Flags) in der Page Table eintragen zu können. Es wird immer von virtuell nach physisch zugeordnet, d. h. wenn man 0xB8000 (phys.) auf 0x12345000 (virt.) mappen will, muss man erst den Page-Directory- und Page-Table-Eintrag von 0x12345000 berechnen. Das geht am besten so: \<c\>Pagedirectory_Eintrag = virtuelle_adresse \>\> 22 (= 0x48) Pagetable_Eintrag = (virtuelle_adresse \>\> 12) % 1024 (= 0x345)\</c\> Nun suche man erst die Adresse der Page Table (im eben berechneten *Pagedirectory_Eintrag* schauen). **Achtung:** Es handelt sich hier um die physische Adresse. Mit der Adresse der Page Table kann man jetzt in den *Pagetable_Eintrag* die physische Adresse eintragen, die passenden Flags setzen und schon ist die Page gemappt.

## In physischen Speicher schreiben

Wenn nun Paging eingeschaltet ist, kann man nicht mehr in den physischen Speicher schreiben. Wenn man nicht viel physischen Speicher hat, oder 64 Bit benutzt und deswegen der virtuelle Adressraum groß genug ist, kann man den gesamten physischen Speicher in den virtuellen mappen.

Es besteht aber auch die Möglichkeit, Zugriff auf den gesamten physischen Speicher zu haben, ohne dass man ihn direkt mappt. Erstmal braucht man eine Möglichkeit das Page Directory und die Page Tables noch zu ändern nachdem Paging eingeschaltet wurde. Wenn man dies kann, kann man sich einfach immer die gerade gebrauchte physische Page auf eine festgelegte virtuelle Page mappen und voilà. Um nun Zugriff auf das Page Directory und die Page Tables zu haben, kann man einfach z. B. als letzte Page Table das Page Directory selbst eintragen. Das Page Directory wird dann als Page Table interpretiert und alle Page Tables als Pages in den Speicher gemappt. Somit enthalten die letzten 4 MB des virtuellen Speichers die Page Tables, wobei die letzten 4 kB das Page Directory enthalten.

## Paging im Long Mode

Das Paging im Long Mode gestaltet sich etwas schwieriger als das Paging im Protected Mode. Dies liegt zunächst einmal daran, dass im Long Mode nicht nur zwei Ebenen existieren, sondern bis zu vier.

### Page-Map Level-4 Table

Eine Page-Map Level-4 Table enthält 512 Eintrage à acht Byte. Ein Page-Map Level-4 Table-Eintrag kann jeweils auf eine Page-Directory Pointer Table zeigen.

| Bit | Funktion |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an, ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page-Map Level-4 Table benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Wird ignoriert und sollte 0 sein. |
| 7-8 | Muss 0 sein. |
| 9-11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12-51 | Gibt die physische Adresse der Page-Directory Pointer Table an. |
| 52-62 | Diese Bits sind frei verfügbar. |
| 63 | Wenn EFER.NXE auf 1 gesetzt ist gibt dieses Bit an, ob das Ausführen von Code in der Page erlaubt ist (0) oder nicht (1). Wenn EFER.NXE auf 0 gesetzt ist und das Bit auf 1 gesetzt ist wird ein Pagefault ausgelöst. |

### Page-Directory Pointer Table

Eine Page-Directory Pointer Table enthält 512 Eintrage à acht Byte. Ein Page-Directory Pointer Table-Eintrag kann jeweils auf eine Page-Directory Table zeigen.

| Bit | Funktion |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an, ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page-Directory Pointer Table benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Wird ignoriert und sollte 0 sein. |
| 7 | Muss 0 sein, wenn 2 MiB Pages oder 4 KiB Pages verwendet werden, muss 1 sein, wenn 1 GiB Pages verwendet werden. |
| 8 | Wenn CR4.PGE und Bit 7 auf 1 gesetzt sind, gibt das Bit an, ob die Page global ist (Nicht durch Instruktionen wie mov cr3 geflusht wird). Muss ansonsten 0 sein. |
| 9-11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12-51 | Gibt die physische Adresse der Page-Directory Table an. Gibt die physische Adresse der Page Table an. Besteht alternativ aus der physischen Adresse der Page (Bits 30-51), dem höchstes PAT Bit (Bit 12, sollte 0 sein wenn nicht benötigt) und reservierten Bits (Bit 13-29), wenn 1 GiB Pages verwendet werden. |
| 52-62 | Diese Bits sind frei verfügbar. |
| 63 | Wenn EFER.NXE auf 1 gesetzt ist gibt dieses Bit an, ob das Ausführen von Code in der Page erlaubt ist (0) oder nicht (1). Wenn EFER.NXE auf 0 gesetzt ist und das Bit auf 1 gesetzt ist wird ein Pagefault ausgelöst. |

### Page-Directory Table

Eine Page-Directory Table enthält 512 Eintrage à acht Byte. Ein Page-Directory Table-Eintrag kann jeweils auf eine Page Table zeigen.

| Bit | Funktion |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an, ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page-Directory Table benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Wird ignoriert und sollte 0 sein. |
| 7 | Muss 0 sein, wenn 1 GiB Pages oder 4 KiB Pages verwendet werden, muss 1 sein, wenn 2 MiB Pages verwendet werden. |
| 8 | Wenn CR4.PGE und Bit 7 auf 1 gesetzt sind, gibt das Bit an, ob die Page global ist (Nicht durch Instruktionen wie mov cr3 geflusht wird). Muss ansonsten 0 sein. |
| 9-11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12-51 | Gibt die physische Adresse der Page Table an. Besteht alternativ aus der physischen Adresse der Page (Bits 21-51), dem höchstes PAT Bit (Bit 12, sollte 0 sein wenn nicht benötigt) und reservierten Bits (Bit 13-20), wenn 2 MiB Pages verwendet werden. |
| 52-62 | Diese Bits sind frei verfügbar. |
| 63 | Wenn EFER.NXE auf 1 gesetzt ist gibt dieses Bit an, ob das Ausführen von Code in der Page erlaubt ist (0) oder nicht (1). Wenn EFER.NXE auf 0 gesetzt ist und das Bit auf 1 gesetzt ist wird ein Pagefault ausgelöst. |

### Page Table

Eine Page Table enthält 512 Eintrage à acht Byte. Ein Page Table-Eintrag kann jeweils auf eine Page zeigen

| Bit | Funktion |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Gibt an, ob die Page momentan im Speicher liegt. Ist das Bit gelöscht (Page nicht im Speicher), dann sind alle anderen Bits für das Betriebssystem frei verfügbar und können z. B. für Swapping genutzt werden. |
| 1 | Wenn dieses Bit gesetzt ist, kann die Page beschrieben werden. Ansonsten kann die Page nur gelesen werden. |
| 2 | Wenn dieses Bit gesetzt ist, darf jeder auf die Page zugreifen. Ansonsten nur Ring 0. |
| 3 | Wenn dieses Bit gesetzt ist, wird Write-Through-Caching benutzt. |
| 4 | Wenn dieses Bit gesetzt ist, wird für die Page kein Cache benutzt. |
| 5 | Wird von der CPU gesetzt, wenn die Page Table benutzt wurde. Dieses Bit wird allerdings nicht von der CPU zurückgesetzt. |
| 6 | Wird ignoriert und sollte 0 sein. |
| 7 | Höchstes PAT Bit. Sollte 0 sein wenn nicht benötigt. |
| 8 | Wenn CR4.PGE und Bit 7 auf 1 gesetzt sind, gibt das Bit an, ob die Page global ist (Nicht durch Instruktionen wie mov cr3 geflusht wird). Muss ansonsten 0 sein. |
| 9-11 | Diese Bits sind frei verfügbar. Sie können z. B. genutzt werden um Pages zu markieren, die zwar im Speicher liegen, aber auch schon auf einen Swapmedium existieren, so dass sie ohne weiteres geswappt werden können, und/oder um Pages zu markieren, die nicht ausgelagert werden dürfen. |
| 12-51 | Gibt die physische Adresse der Page an wenn 4 KiB Pages verwendet werden. |
| 52-62 | Diese Bits sind frei verfügbar. |
| 63 | Wenn EFER.NXE auf 1 gesetzt ist gibt dieses Bit an, ob das Ausführen von Code in der Page erlaubt ist (0) oder nicht (1). Wenn EFER.NXE auf 0 gesetzt ist und das Bit auf 1 gesetzt ist wird ein Pagefault ausgelöst. |

## Weiterführende Artikel

- [Paging Tutorial](https://github.com/lowlevel-eu/wiki/wiki/Paging-Tutorial "Paging Tutorial")

## Links

- [Paging-Tutorial](http://www.homix-online.de/Tutorials/32PMode-Paging.php)
- [Paging im PM-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/p_spez1.htm)
- [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8#paging "Ausgabe 8")
- <http://osdever.net/tutorials/pdf/basic_paging.pdf>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11372/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1496/index.html)

<!-- MediaWiki page 1496; revision 11372; parent 11183; 2017-01-23T22:17:11Z -->
