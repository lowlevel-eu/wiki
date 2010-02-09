# Paloxena

| Paloxena |  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/8304ee34a07d9485b310.png" width="158" height="158" alt="Paloxena.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/8304ee34a07d9485b310.png) |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | 0.001-o |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") |
| OS-Eigenschaften |  |
| Plattform: | [i386](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Monolith |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | POSIX-ähnlich |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

[Gitorious](http://gitorious.org/paloxena)  
[Forum](http://forum.paloxena.bplaced.net/)

  
Der Name Paloxena stammt von der wissenschaftlichen Bezeichnung für die "Grüne Stinkwanze" ("Palomena"), ein "Bug" also. Und das wird das OS wohl vermutlich ausmachen.

## paloxena1

paloxena1 ist das „ursprüngliche“ Paloxena, das geschrieben wurde, weil MyXomycota so ziemlich kaputt war. Dummerweise wurde es noch viel kaputter. Deshalb gibt es jetzt paloxena2. Irgendwann muss man ja einen Glückstreffer landen.

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

### Akt. Release

Die aktuelle Freigabe ist 0.001-o (zur Benennung der Versionen, siehe [hier](http://forum.paloxena.bplaced.net/viewtopic.php?f=2&t=3)).

- Ankündigung: [Paloxenaforum - "0.001-o"](http://forum.paloxena.bplaced.net/viewtopic.php?f=2&t=13)
- Direktlink: [0.001-o.img.bz2](http://www.paloxena.bplaced.net/releases/0.001-o.img.bz2)

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

### Syscalls

Im Gegensatz zu paloxena2 sind die Linuxsyscalls nicht die nativen Syscalls von paloxena3. Native Calls finden (vorerst) über den Interrupt 0xA2 (in Anlehnung an 0x2A, der aber für IRQs reserviert ist) statt. Wird allerdings der Interrupt 0x80 aufgerufen, so wird der entsprechende Linux-Syscall ausgeführt. Per Interrupt 0x7F sind [PrettyOS](https://github.com/lowlevel-eu/wiki/wiki/PrettyOS "PrettyOS")-Syscalls zu erreichen. Auf diese Art und Weise soll es möglich sein, verschiedene Betriebssysteme zu „emulieren“, sollten zwei Betriebssysteme z. B. den gleichen Interrupt verwenden, dann wird beim Programmstart festgestellt, welche Emulationsart verwendet werden soll, dies ist auch z. B. für den Zustand des Stacks bei Programmaufruf wichtig. Bis jetzt geschieht dies folgendermaßen:

- Wenn an der Stelle 0x7FFFFFFC ein DWord mit dem Wert 42 steht, dann handelt es sich um eine native paloxena3-Anwendung (sollte nur per 0xA2 Syscalls ausführen, darf vorraussichtlich aber auch per 0x80).
- Ist der Entry-Point zwischen 0x14000000 und 0x2000000, dann wird PrettyOS emuliert.
- Sonst handelt es sich um eine Linuxanwendung.

PrettyOS wird bereits ziemlich gut emuliert (allerdings fehlen in Ermangelung eines entsprechenden Treibers die Disketten- bzw. FAT-Funktionen, ebenso gibt es nur eine rudimentäre Tastaturunterstützung), hier ein Screenshot der Shell:

Datei:Prettypaloxena.png

### OSOD

Neu bei paloxena3 ist der OSOD, der Orange Screen Of Death. Die einen schwerwiegenden Fehler anzeigende Farbe ist also nicht mehr pink oder violett, sondern orange, meine Lieblingsfarbe (#FF4000, um genau zu sein). Hier ein entsprechender Screenshot:

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/48d49f3eb3ec3b0a95ae.png" width="720" height="400" alt="Paloxenaosod.png" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/48d49f3eb3ec3b0a95ae.png)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7058/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2045/index.html)

<!-- MediaWiki page 2045; revision 7058; parent 6797; 2010-02-09T23:06:06Z -->
