# ARM-OS-Dev Teil 9 – Paging

|  |  |  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----- |
| « [ARM-OS-Dev Teil 8 – Ein erstes Programm](https://github.com/lowlevel-eu/wiki/wiki/ARM-OS-Dev-Teil-8-%E2%80%93-Ein-erstes-Programm "ARM-OS-Dev Teil 8 – Ein erstes Programm") | **Navigation** |  |

## Ziel

Zwar können wir nun ELF-Programme laden, doch das wird natürlich nicht mehr so toll funktionieren, wenn wir mehrere verschiedene auf einmal laden wollen und alle die gleiche Ladeadresse verwenden. Um diesem Problem zu begegnen, kann man den Pagingmechanismus verwenden: Jedes Programm erhält seinen eigenen virtuellen Adressraum, sodass es gar nicht mit anderen Programmen ins Gehege kommen kann, weil es auf deren Daten gar nicht zugreifen kann.

## Paging

Zur Einführung ist es sinnvoll, zunächst den [Paging-Artikel](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") zu lesen, da dieser eine solche am Beispiel x86 liefert. Der auf ARM-Prozessoren verwendete Pagingmechanismus ist dem von x86 recht ähnlich, sodass es nach dem Verständnis des Artikels nicht schwerfallen sollte, auch das ARM-Paging nachzuvollziehen.

An dieser Stelle sei erwähnt, dass es zwei sich leicht voneinander unterscheidende Pagingmethoden auf ARM-Prozessoren gibt: Das VMSAv6-Paging, das mit ARMv6 eingeführt wurde, und ein nicht näher benanntes, welches davor in einigen ARMv5-CPUs implementiert war (daneben gibt es noch eine ganz andere Methode des Speicherschutzes, die sogenannte *Memory Protection Unit* (MPU, im Gegensatz zur MMU), welche hier aber nicht weiter betrachtet wird). Vom Prinzip her unterscheiden sich beide Varianten nicht. Unterschiede sind die, dass man vor VMSAv6 einzelne Teile einer Page verschieden schützen konnte und es 1-kB-Pages gab, während es in VMSAv6 globale Pages (s. x86-Paging) und die Möglichkeit gibt, Codeausführung je nach Page zu erlauben oder zu verbieten.

Da auch ARM gewissen Wert auf Abwärtskompatibilität legt, gibt es die vor-VMSAv6-Pagingvariante auch in VMSAv6, dort heißt sie „VMSAv6, subpages enabled“ (aufgrund der erwähnten Möglichkeit, Teile einer Page einzeln schützen zu lassen). Diese Variante sollte auf allen ARM-CPUs funktionieren, welche eine MMU besitzen, sodass diese hier verwendet wird.

### Translation Table

Wenn die MMU der CPU versucht, eine virtuelle Adresse aufzulösen, nimmt sie die oberen zwölf Bit als Index eines Eintrags in der sogenannten *Translation Table*. Diese hat 4096 Einträge zu je vier Byte, ist also insgesamt 16 kB groß. Die unteren zwei Bit des Eintrags geben den Typ an: Bei 0b00 ist der Eintrag frei, beim Adresszugriff wird eine Abort-Exception ausgelöst. 0b01 ist ein Verweis auf eine weitere Tabelle (eine sogenannte *Coarse Page Table*), 0b10 ein Verweis auf eine Section (sozusagen eine 1-MB-Page); 0b11 ist als Typ reserviert (stand vor VMSAv6 für *Fine Page Tables*).

Ein Coarse-Page-Table-Verweis sieht folgendermaßen aus:

| Bit | Beschreibung |
| --------- | ------------------------------------------------------------------------------------ |
| 0 – 1 | Ist 0b01 (Typ des Eintrags). |
| 2 – 4 | Sollte auf 0 gesetzt werden. |
| 5 – 8 | Gibt die Domain an, der diese Page Table angehört (s. u.). |
| 9 | Möglichst 0. |
| 10 – 31 | Bits 10 bis 31 der Basisadresse der Page Table (muss an einer 1-kB-Grenze liegen). |

Da hier im Tutorial keine Sections verwendet werden, ist es hier unnötig, den Aufbau eines Sectioneintrags darzulegen.

### Domains

Zusätzlich zur Möglichkeit, jeder einzelnen Page spezielle Zugriffsrechte zuzuordnen, bietet ARM auch sogenannte Domains. Eine Domain ist eine Gruppe verschiedener Speicherregionen, auf die man dadurch relativ schnell Zugriff verbieten oder erlauben kann, indem man einfach die Domainzugriffsrechte ändert. Wie man gesehen hat, erfolgt die Zuordnung von Speicher zu Domain in der Translation Table und kann nur für Pages (nicht für Sections) durchgeführt werden. Es gibt drei Zugriffsarten: Gar kein Zugriff, sodass bei Zugriff immer ein Abort ausgelöst wird; *Client*, hierbei werden die Zugriffsrechte, die in der Page Table angegeben sind, beachtet; *Server*, bei welcher jeder Zugriff erlaubt wird (wenn an der virtuellen Adresse eine Page vorhanden ist).

In diesem Tutorial werden wir Domains ignorieren, sodass alle 16 Domains, die es gibt, auf *Client* gestellt werden und alle Page Tables in die Domain 0 eingetragen werden (da aber alle *Client* sind, ist es auch egal, in welche Domain sie kommen).

### Page Tables

Vor VMSAv6 gab es zwei Page-Table-Arten: Coarse und Fine Page Tables, erstere mit 256 Einträgen, letztere mit 1024. Mit VMSAv6 wurden letztere abgeschafft.

Hat die MMU also beim Zugriff auf die Translation Table festgestellt, dass auf eine Page Table verwiesen wird, so verwendet sie die Bits 12 bis 20 der virtuellen Adresse als Index in der angegebenen (Coarse) Page Table. Auch hier gibt es wieder 4-Byte-Einträge, deren niederwertigste zwei Bit den Typ des Eintrags angeben: 0b00 zeigt wieder einen unbenutzten Eintrag an, 0b01 steht für eine 64-kB-Page, 0b10 für eine 4-kB-Page mit Subpages und 0b11 für eine ohne.

Da hier nur 4-kB-Pages mit Subpages verwendet werden (ohne Gebrauch von den Subpages zu machen), sei auch hier nur der Aufbau dieses einen Eintragtyps dargestellt:

| Bit | Beschreibung |
| --------- | ------------------------------------------------------------------------------ |
| 0 – 1 | Ist 0b10 (4-kB-Page mit Subpages). |
| 2 | B-Bit: Bufferable |
| 3 | C-Bit: Cachable |
| 4 – 5 | Zugriffsrechte für das erste Kilobyte. |
| 6 – 7 | Zugriffsrechte für das zweite Kilobyte. |
| 8 – 9 | Zugriffsrechte für das dritte Kilobyte. |
| 10 – 11 | Zugriffsrechte für das vierte Kilobyte. |
| 12 – 31 | Bits 12 bis 31 der Basisadresse der Page (muss an einer 4-kB-Grenze liegen). |

Wenn jemand die genaue Bedeutung von B- und C-Bit verstanden hat, möge er sie hier bitte eintragen. Soweit ich verstanden habe, sollte man beide für MMIO auf 0 und für normalen Speicher auf 1 setzen. Um sicher zu gehen, werden sie in diesem Tutorial einfach auf 0 gesetzt.

Für die Zugriffsrechte gilt:

| Wert | Bedeutung |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0b00 | • Bei gelöschtem R- und S-Bit: Kein Zugriff<br>• Bei gesetztem R-Bit (und gelöschtem S): Von allen Modi aus nur lesbar<br>• Bei gesetztem S-Bit (und gelöschtem R): Von privilegierten Modi aus lesbar, vom Usermodus kein Zugriff<br> |
| 0b01 | Vollzugriff für privilegierte Modi, keiner für Usermodus |
| 0b10 | Vollzugriff für privilegierte Modi, vom Usermodus aus lesbar |
| 0b11 | Vollzugriff für alle Modi |

Privilegierte Modi sind alle nicht-Usermodi. Die Bits R und S befinden sich in einem Kontrollregister der MMU (die Namen stehen für *ROM Protection* respektive *System Protection*).

## CP15

Im Gegensatz zu x86-CPUs befindet sich die MMU aus Programmierersicht bei ARMs nicht direkt in der CPU (bei x86 können Kontrollregister wie CR0 oder CR3, die auch das Paging steuern, wie normale Register mit dem MOV-Befehl gesetzt werden), sondern in einem Koprozessor. Dieser Speicherverwaltungskoprozessor trägt den Namen CP15 (CP für Coprocessor), da seine ID, mit der er in den Koprozessorbefehlen angesprochen wird, 15 ist. Er übernimmt die Speicherverwaltung der CPU (und auch andere Aufgaben, er heißt offiziell *System Control Coprocessor*), das heißt, er kann entweder als MPU oder MMU agieren. Um den CP15 zu steuern, werden mit den Befehle MCR und MRC bestimmte Werte in seine Register geschrieben bzw. daraus gelesen.

MCR- und MRC-Befehle haben die folgende Form:

    mcr/mrc <cp>, <op1>, <rd>, <crn>, <crm>, [op2]

Dabei ist *\<cp\>* die ID des Koprozessors (hier immer 15), *\<op1\>* ein koprozessorspezifischer Opcode (hier immer 0), *\<rd\>* das zu verwendende ARM-Register, *\<crn\>* das erste zu verwendende Koprozessorregister, *\<crm\>* das zweite und optional *\[op2\]* ein zweiter Opcode (wenn nicht angegeben, wird 0 verwendet).

Von uns für Interesse sind die CP15-Register 1 (*Control register*), 2 (*Translation table base*), 3 (*Domain access control*) und 8 (*TLB functions*). Wenn man Aborts behandeln möchte, werden auch 5 (*Fault status*) und 6 (*Fault address*) wichtig.

### Initialisierung

Zuerst möchten wir alle Domains in den Client-Modus versetzen. Hierzu schreibt man den Wert 0x55555555 in das CP15-Register 3: \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mcr p15,0,%0,c3,c0" :: "r"(0x55555555));\</c\>

Bevor man die MMU aktiviert, wird im ARM-Manual empfohlen, den Cache (zumindest temporär) zu deaktivieren, also tun wir das auch: \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mrc p15,0,r0,c1,c0;"

                         "bic r0,#0x0004;"
                         "bic r0,#0x1000;"
                         "mcr p15,0,r0,c1,c0" ::: "r0");</c>

Wie man sieht, werden dazu im Control Register Bit 2 und 12 gelöscht (Daten- und Befehlscache deaktivieren).

Dann sollte eine Translation Table im Translation Table Base Register eingetragen werden: \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mcr p15,0,%0,c2,c0,0" :: "r"(translation_table));\</c\> Wobei *translation_table* die physische Adresse einer Translation Table sein müsste. Dabei werden die unteren zwei Bit und die Bits 3 und 4 für Einstellungen zum Caching verwendet, die ich wieder der Einfachheit halber auf 0 gelassen habe (kein Caching) – sollte jemand eine sichere Einstellung mit Caching kennen, ist er frei, diese hier zu ergänzen.

Nachdem dies geschehen ist, kann man Bit 0 im Control Register setzen (MMU aktivieren) und Bit 23 löschen (Subpages aktivieren, quasi-vor-VMSAv6-Paging). Sofort anschließend sollte laut Manual ein sogenannter Prefetch Flush durchgeführt werden (was bei vernünftigem Mapping aber wohl unnötig sein dürfte), welcher erreicht wird, indem 0 ins CP15-Register 7 geschrieben wird, wobei als zweites CP15-Register 5 und als zweiter Opcode 4 angegeben wird. \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mrc p15,0,r0,c1,c0;"

                         "orr r0,#0x00000001;"
                         "bic r0,#0x00800000;"
                         "mcr p15,0,r0,c1,c0;"
                         "mcr p15,0,%0,c7,c5,4" :: "r"(0) : "r0");</c>

Jetzt könnte man den Cache (theoretisch) wieder aktivieren, indem man die Bits 2 und 12 im Control Register wieder setzt.

### TLB

Wie auch bei x86 gibt es einen TLB, der die Zuordnung von virtuellen zu physischen Adressen cachet. Und auch bei ARM muss man natürlich einzelne Einträge invalidieren, wenn die Zuordnung verändert wurde. Hierfür wird das CP15-Register 8 verwendet. Um einen einzelnen Eintrag zu invalidieren, verwendet man (mit *address* == virtuelle Adresse): \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mcr p15,0,%0,c8,c7,1" :: "r"(address));\</c\>

Um den TLB komplett zu leeren (beim Wechsel der Translation Table notwendig), verwendet man im Gegensatz dazu als zweiten Opcode 0: \<c\>\_\_asm\_\_ \_\_volatile\_\_ ("mcr p15,0,%0,c8,c7,0" :: "r"(0));\</c\>

## Aufteilung des Adressraums

Nun ist es an der Zeit, ein paar Designfragen zu klären. Erstens: Soll der komplette Kernel in jeden Adressraum gemappt werden? Einfache Frage, einfache Antwort: Ja. Das ist einfacher und erspart uns jede Menge Kontextwechsel. Zweitens: Wie viel Platz soll der Kernel erhalten? Hier folgen wir der häufig genutzten 3-zu-1-GB-Aufteilung (3 GB für das Programm, 1 GB für den Kernel). Der Einfachheit halber erhält der Kernel das untere GB im Speicher (0x00000000 bis 0x3FFFFFFF) und das Programm die oberen 3 GB.

Damit sind also in jeder Translation Table die ersten 1024 Einträge gleich. Nun ist die Frage, wie man dafür sorgt, dass dies tatsächlich der Fall ist. Die einfachste Möglichkeit ist es, alle Kernel-Page-Tables gleich zu Beginn anzulegen und dann beim Anlegen eines neuen Kontexts in der entsprechenden Translation Table einzutragen – das ist auch genau das, was wir hier tun werden. 1024 Page Tables kosten 1 MB Speicher – das sollte zu verkraften sein. Wiederum der Einfachheit halber legen wir die konstant nach 0x00100000 (also hinter den gemappten Flashspeicher). Infolge dessen müssen wir natürlich die *pmm_init*-Funktion anpassen, da jetzt erst der Speicher ab 0x00200000 benutzbar ist.

Kommen wir zur Frage, wie der virtuelle Adressraum im Kernelbereich aufgeteilt wird. Die ist hier nicht ganz so kompliziert wie auf einem x86-Rechner, da wir fest mit 128 MB Speicher rechnen können. Also mappen wir einfach die ersten 128 MB physischen auf die ersten 128 MB virtuellen Speicher. Den Rest können wir dann für beliebige Dinge nutzen, wobei es sich empfiehlt, noch etwas Platz für MMIO freizuhalten, der physisch über 128 MB liegt (da wir bisher nur den Timer an 0x13000000 und die serielle Schnittstelle an 0x16000000 benutzen, können wir auch einfach die ersten 2 GB direkt mappen (0x00000000 bis 0x1FFFFFFF) und uns weiter keine Gedanken darum machen).

## Anlegen des Kernelcontexts

Um Paging benutzen zu können, muss zunächst ein Kernelcontext angelegt werden. Dafür müssen 16 kB zusammenhängender physischer Speicher an einer 16-kB-Grenze als Translation Table reserviert werden. Die ersten 1024 Einträge erhalten Verweise auf die Kernel-Page-Tables (jede Page Table ist 1 kB groß), der Rest wird mit 0 gefüllt. \<c\>uint32_t \*kernel_translation_table = (uint32_t \*)pmm_alloc_16k(); for (int i = 0; i \< 1024; i++)

       kernel_translation_table[i] = (0x00100000 + i * 1024) | 1;

memset(&kernel_translation_table\[1024\], 0, 3072 \* sizeof(uint32_t));\</c\>

Nun wäre es auch nicht schlecht, die Page Tables zu initialisieren. Das geht zum Beispiel per: \<c\>uint32_t \*kernel_page_tables = (uint32_t \*)0x00100000; for (uintptr_t addr = 0; addr \< 128 \* 1048576; addr += 4096)

       kernel_page_tables[addr >> 12] = addr | (0x55 << 4) | 2;

memset(&kernel_page_tables\[(128 \* 1048576) \>\> 10\], 0, (((1024 - 128) \* 1048576) \>\> 10) \* sizeof(uint32_t));\</c\>

Die Zugriffsrechte 0x55 (0b01010101) führen dazu, dass die Pages aus allen privilegierten Modi heraus gelesen und beschrieben werden können, man im Usermodus jedoch keinen Zugriff hat.

Danach kann man den CP15 wie oben beschrieben initialisieren.

## Weitere Kontexte

Um weitere Kontexte anzulegen, muss man genauso wie beim Anlegen des Kernelcontexts vorgehen, außer dass man jetzt die ersten 1024 Einträge direkt per memcpy aus dem Kernelcontext herauskopieren kann. Um einen Kontext zu wechseln, muss man die neue Translation Table eintragen und dann den TLB komplett leeren.

Um eine virtuelle Adresse auf eine bestimmte physische zu mappen, muss ggf. eine Page Table angelegt werden (deren Adresse OR 1 dann in der Translation Table eingetragen wird), in welcher dann die physische Adresse an der passenden Stelle mit den entsprechenden Zugriffsrechten eingetragen wird. Möchte man z. B. physisch 0x12345000 nach virtuell 0x6A2A1000 mit Vollzugriff aus allen Modi mappen, dann passiert dies folgendermaßen:

- Verwende 0x6A2A1000 \>\> 20 == 0x6A2 als Index in der Translation Table.
- Ist dort bereits eine Page Table eingetragen, verwende diese – ansonsten erstelle eine und trage sie ein.
- Verwende ((0x6A2A1000 \>\> 12) & 0xFF) == 0xA1 als Index in der Page Table.
- Trage an dieser Stelle 0x12345000 \| 0xFF0 \| 2 ein (0xFF0 ist 0b11111111 \<\< 4, also Vollzugriff aus allen Modi für die gesamte Page; 2 zeigt eine 4-kB-Page an).

Um ein Mapping zu entfernen, muss man einfach 0 eintragen. In jedem Falle sollte man anschließend den entsprechenden TLB-Eintrag invalidieren.

## Tasks

Auch das Taskmanagement müssen wir jetzt etwas verändern: Zunächst erhält jeder Task ein zusätzliches Attribut, und zwar seinen Kontext (bei uns reicht die Adresse der Translation Table, wenn wir kein Identity Mapping für den gesamten RAM hätten, müsste man sowohl die physische als auch die virtuelle Adresse speichern). Weiterhin müssen der IRQ- und der SVC-Stack in den Kernelcontext gemappt werden, ebenso wie die Taskstruktur selbst (wobei man sich das ebenfalls sparen kann, wieder wegen des Identity Mappings) – hierfür empfiehlt sich eine Funktion *vmm_alloc*, die ein *pmm_alloc* ausführt und die Adresse sofort mappt. Den Userstack allerdings müssen wir in den Userbereich (also die oberen 3 GB) legen, damit das Programm im Usermodus auch darauf zugreifen kann. Am besten kommt er ganz nach oben, das heißt, von 0xFFFFF000 bis 0xFFFFFFFF. Dazu muss man beim Initialisieren die Page an 0xFFFFF000 auf einen mit *pmm_alloc* reservierten Pageframe mappen und das User-R13 auf 0 setzen (beim ersten *push* wird es um vier verringert, bevor der Wert dann nach 0xFFFFFFFC gespeichert wird).

Beim Taskwechsel muss dann natürlich der Kontext wie beschrieben gewechselt werden.

Desweiteren können wir das Programm jetzt logischerweise nicht mehr nach 0x00200000 laden lassen, weil dort im virtuellen Adressraum der Kernel liegt. Stattdessen bietet sich 0x40000000 an. Weiterhin muss der ELF-Loader angepasst werden, sodass er nicht einfach nur die Daten in den Speicher kopiert, sondern die entsprechenden Adressen zuvor im Kontext des neuen Programms mappt.

## Ergebnis

Wir sollten jetzt beliebig viele Programme laden können (solange sie in den Speicher passen), ohne, dass sie einander beeinflussen. Zudem ist jetzt auch der Kernel vor unberechtigten Zugriffen der Programme geschützt. Das nächste Ziel wäre es wohl, Aborts abzufangen, um darauf dementsprechend reagieren zu können (z. B. entweder das Programm mit einem Segfault beenden oder die entsprechenden Adressen mappen, was nützlich ist, wenn der Userstack dynamisch wachsen soll).

## Weitere Quellen

Das *ARM Architecture Reference Manual* (s. [ARM – Weblinks](https://github.com/lowlevel-eu/wiki/wiki/ARM#weblinks "ARM")) beschreibt das VMSAv6-Paging in den Kapiteln *The System Control Coprocessor* und *Virtual Memory System Architecture* (VMSA).

Eine Beispielimplementierung des Tutorialkernels mit Paging kann man [hier](https://gitorious.org/arm-os-dev/kernel/trees/8756adf6f8a5a97017fa11bab83b0885538ff386) finden.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9818/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2432/index.html)

<!-- MediaWiki page 2432; revision 9818; parent 0; 2011-05-28T16:24:44Z -->
