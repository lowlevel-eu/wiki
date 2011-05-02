# Paloxena

| Paloxena |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/8304ee34a07d9485b310.png" width="158" height="158" alt="Paloxena.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/8304ee34a07d9485b310.png) |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | — |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolith |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | Bis kernel3 POSIX-ähnlich; ab 3.5 nativ mit POSIX-Wrappern |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | — |
| Homepage |  |

[Gitorious](http://gitorious.org/paloxena)  
[Website](http://xanclic.bplaced.net/)

  
Der Name Paloxena stammt von der wissenschaftlichen Bezeichnung für die „Grüne Stinkwanze“ („Palomena“), ein „Bug“ also. Und das wird das OS wohl vermutlich ausmachen.

## paloxena1

paloxena1 ist das „ursprüngliche“ Paloxena, das geschrieben wurde, weil MyXomycota so ziemlich kaputt war. Dummerweise wurde es noch viel kaputter. Deshalb gibt es jetzt paloxena2 (Und paloxena3. Und paloxena3.5. Und paloxena4). Irgendwann muss man ja einen Glückstreffer landen.

### Programme

- [FASM](https://github.com/lowlevel-eu/wiki/wiki/Flat-Assembler "FASM") 1.69.08: Ein Assembler mit Intelsyntax
- µsh 0.002: Die Shell (portiert von MyXomycota)
- Paloxoreutils:
  - ls
  - cat
- Paloxena nettools:
  - dig
  - ping
- mbr: Gibt 512 Bytes einer Datei von einer gegebenen Position an in Hex-Editor-Form aus
- maumau: Der Klassiker von MyXomycota
- brainfuck: Brainfuckcompiler

### Screenshot

Hier passend zum Namen ein Bild von einem Pink Screen Of Death (Dank an [Hartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut") für die Inspiration):

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/39df70b465c2797ed44e.png" width="720" height="400" alt="Paloxena-PSOD.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/39df70b465c2797ed44e.png)

## paloxena2

### Hast du nicht schon genug Betriebssysteme zu unterhalten?

paloxena1 war ein halbes Abkopieren von MyXomycota. In meinem „Wahn“, alles schön zu machen und gut zu designen, habe ich mich wohl übernommen. Es entstand ein hübsches einheitliches Treiberinterface, das sowohl für die Console als auch für Dateisystemtreiber verwendet werden konnte. Leider hatte die Console dann jede Menge Code zu liefern, der total unnötig war. Den gleichen Code habe ich dann auch z. B. für den PCI-Treiber verwendet. Deshalb soll paloxena2 darauf ausgerichtet sein, wieder ein differenzierteres und vor allem einfacheres Treiberinterface zu liefern. Es soll nicht mehr schön sein. Es soll einfach funktionieren. Außerdem soll es eigentlich so tolle Sachen wie SMP und Threading mitbringen, hoffen wir, dass ich irgendwas dazu rausfinde. ;-)

### Syscalls

Erwähnenswert ist das geplante Syscallinterface. Nachdem ich in paloxena1 bereits versucht habe, die POSIX-Calls zu implementieren (ursprünglich, um die Newlib möglichst einfach portieren zu können &#150; welche in meinen Augen aber kaputt ist), habe ich mich nun entschlossen, die Syscalls einfach umzunummerieren, sodass mein open-Syscall die gleiche Nummer wie der open-Syscall von Linux hat, und so weiter. Dadurch sollen für Linux kompilierte Programme nativ unter paloxena2 ausgeführt werden (ganz einfach, weil ich sowieso die gleichen Syscalls habe, da kann man auch die Nummern umlegen). Dies bringt voraussichtlich vor allem den Vorteil, dass ich keine libc wirklich portieren muss, da ich die von Linux nutzen kann. Bis jetzt klappt es mit der glibc noch nicht so richtig, die diet libc spielt aber schon gut mit.

### ppp

Zum „Crosscompilieren“ (das ja dank der Syscalls eigentlich ein natives Compilieren für Linux ist) gibt es auch ein eigenes Repo, genannt „ppp“, kurz für „Paloxena's Patched Packages“ (ja, der Name klingt absichtlich so bescheuert). Es ist lbuilds von [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") nachempfunden. „Portiert“ wurden bisher folgende Programme (wenn auch mehr schlecht als recht):

- *dash* 0.5.5.1 (Version der Almquist Shell)
- *FASM* 1.69.11 (s. o.)
- *maumau* 0.5 (Was sonst)
- *pdksh* 5.2.14 (Public-Domain-Version der Korn Shell)

## paloxena3

### Oh, mein Gott.

Ja. Es ist schon wieder passiert. Auch paloxena2 war zu kaputt, also gibt es nun paloxena3. Im Großen und Ganzen verfolgt es die gleichen Ziele wie paloxena2 (SMP, Threads, einfacheres Treiberinterface). Bei paloxena2 gab es aber erstens das Problem, dass ich anfangs noch keine Ahnung von SMP hatte und ich das OS zweitens zu Beginn nur als Testplattform für meinen CDI-USB-Treiber verwendet habe &#150; das soll bei paloxena3 von Anfang an besser laufen.

### OSOD

Neu bei paloxena3 ist der OSOD, der Orange Screen Of Death. Die einen schwerwiegenden Fehler anzeigende Farbe ist also nicht mehr pink oder violett, sondern orange, meine Lieblingsfarbe (#FF4000, um genau zu sein). Hier ein entsprechender Screenshot:

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/48d49f3eb3ec3b0a95ae.png" width="720" height="400" alt="Paloxenaosod.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/48d49f3eb3ec3b0a95ae.png)

  

## paloxena4

Aus Spaß an der Freude habe ich mir noch einen Rewrite gegönnt, der allerdings das VFS von paloxena3.5 weiterverwendet. Dieser Rewrite ist zum ersten Mal einigermaßen portabel und wurde bisher auf den i586 sowie auf den Game Boy Advance mit einem ARM7TDMI als CPU (ohne MMU) portiert. Details zum VFS, den aktuellen Features und den Besonderheiten auf dem GBA befinden sich auf der [Website](http://xanclic.bplaced.net/).

Damit das nicht alles war, hier noch ein Screenshot von der GBA-Version direkt nach dem Booten (unter einem Emulator, da ich nicht mal einen GBA besitze):

![pal4-gba1.png](http://xanclic.is-a-geek.org/imgs/pal4-gba1.png)

Wie man evtl. erkennen kann, unterstützt paloxena4 wie auch seine Vorgänger [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"), bisher allerdings nur CDI.audio (Man beachte das kleine „cdi.audio“ in Zeile 9). Für den GBA existiert auch ein entsprechender Treiber.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9733/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2045/index.html)

<!-- MediaWiki page 2045; revision 9733; parent 8169; 2011-05-02T22:25:23Z -->
