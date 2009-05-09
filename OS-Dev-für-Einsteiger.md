# OS-Dev für Einsteiger

Okay, Du hast also beschlossen, dass Du Dein eigenes Betriebssystem schreiben willst? Dann bist du hier genau richtig.

Dieser Artikel versucht, Dir einen Überblick zu geben, welche Fragen Du Dir stellen solltest und wie Du die Sache am geschicktesten angehst. Er soll sozusagen einen Wegweiser durch das Wiki darstellen, der Dir am Anfang hilft, die relevanten Themen auf Anhieb zu finden.

Auf der anderen Seite wird er sicher auch die eine oder andere Frage offen lassen. Zögere nicht, Dich im [Forum](http://lowlevel.brainsware.org/forum) anzumelden und nachzufragen. Der harte Kern der Community ist auch im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") anzutreffen. Falls Du Probleme mit der Anmeldung im Forum haben solltest, kannst Du Dich dort melden.

## Vor dem Start

Frisch ans Werk, Editor und Compiler ausgepackt - aber halt! Bevor es wirklich losgeht, solltest Du Dir einige Fragen beantworten, damit Du weißt, was Du überhaupt entwickeln willst und worüber Du Informationen suchen musst.

### Willst Du wirklich ein OS schreiben?

Die Frage klingt vielleicht seltsam, aber sie ist genau so gemeint, wie sie da steht. Willst Du wirklich ein OS entwickeln? Ist Dir klar, was ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") macht?

Wenn Du in erster Linie an eine grafische Oberfläche denkst, bist Du hier womöglich falsch. Grafische Oberflächen sind ein interessantes Thema - aber eine vollkommen andere Baustelle. Ein OS ist die Schnittstelle zur Hardware. Das heißt, Du wirst eine Speicherverwaltung bauen, einen Scheduler, Treiber für störrische Hardware. Du wirst alles tun, nur keine bunten Pixel auf den Bildschirm bringen - oder falls doch, wird dir direkt anschließend die saubere Basis fehlen, damit man mit diesen Pixeln auch etwas sinnvolles anfangen kann.

Wer sich nicht mit Hardware herumschlagen möchte, kann sich ein DOS oder ein abgespecktes Linux als Grundlage nehmen und seine Oberfläche darauf aufbauen.

### Die Programmiersprache

Ein weit verbreitetes Vorurteil ist, dass man ein Betriebssystem komplett in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") schreiben muss. Quatsch. Man kann, wenn man es möchte, aber man muss nicht. Wahr ist, dass man um einige wenige Zeilen Assembler nicht herumkommen wird. Ein grundlegendes Verständnis der Sprache wäre daher hilfreich, jahrelange Erfahrung ist aber nicht nötig.

Ein übliches Vorgehen ist es, nur das nötigste in Assembler zu schreiben und für den Rest eine Hochsprache zu benutzen. Für die Wahl dieser Hochsprache gibt es im großen und ganzen zwei Alternativen:

- Du nimmst [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Fast jeder spricht diese Sprache und Du bekommst Unmengen an Beispielcode in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Dein Betriebssystem ist eins von vielen und im Forum oder im IRC wird dir fast jeder helfen können.
- Du nimmst nicht [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Du wirst Dich vor allem am Anfang wesentlich seltener beim Kopieren von Code erwischen, weil es einfach nicht geht, ohne ihn in deine Sprache zu übersetzen. Ja, das ist durchaus positiv. Auf der anderen Seite bist du ein Außenseiter und erhältst vielleicht nicht ganz so umfangreich Hilfe und musst Dich möglicherweise öfter selbst durchschlagen - gerade wenn es um Besonderheiten deiner Sprache oder Deines Compilers geht.

Von Mitgliedern der Lowlevel-Community benutzte Alternativen zu [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") sind beispielsweise [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") oder [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") (mit FreePascal oder mit Tricks auch Delphi als Compiler). Theoretisch würde auch [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC") funktionieren. Andere Sprachen hat hier meines Wissens noch niemand versucht, könnten natürlich aber trotzdem funktionieren.

### Entwicklungsumgebung und Tools

Um Dein eigenes Betriebssystem zu entwickeln, brauchst Du ein paar Werkzeuge. Auf die wichtigsten davon gehe ich in diesem Abschnitt kurz ein. Wie man sich eine [Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Entwicklungsumgebung "Entwicklungsumgebung") einrichtet, welche Tools man für sein Vorhaben benötigt und auf welchen Plattformen (Linux, Windows, ...) dies möglich ist, wird im Artikel [Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Entwicklungsumgebung "Entwicklungsumgebung") genauer erläutert.

#### Dein Computer

Fangen wir vorne an: Du brauchst einen PC. Ja, Du hast recht, Du brauchst natürlich strenggenommen keinen PC. Aber es wäre geschickt, denn ich nehme an, Du willst ein x86-Betriebssystem schreiben. Wenn Du wider Erwarten für eine andere Plattform entwickeln möchtest, teil Dich im Forum mit, das wird auch andere interessieren - allerdings bist dann Du derjenige, der erklären darf. Aber zurück zum PC: Am besten hat dieser ein Diskettenlaufwerk, denn Disketten sind für den Anfang das handlichste. Und ein 386er oder höher sollte es schon sein - aber das sollte heutzutage machbar sein.

#### Dein Betriebsystem

Eine Stufe weiter kommen wir zum Betriebssystem. Da Dein eigenes Betriebssystem noch nicht fertig ist, wirst Du vorerst mit einem bestehenden vorlieb nehmen müssen. Hast Du ein [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") installiert? Wunderbar, nimm das. Oder eine BSD-Variante. Trotzdem möchte ich hier nicht lügen, deshalb: Ja, man kann auch [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") nehmen. Aber dazu braucht es schon eine gewisse masochistische Veranlagung (jedenfalls wenn man GRUB und daher ELF benutzen möchte - und das ist der von uns dringend empfohlene Weg). Unter Windows wirst Du aller Voraussicht nach eine Weile mit der Umgebung basteln müssen, während es unter Linux einfach läuft. Man könnte jetzt versuchen, einen Kausalzusammenhang herzustellen, warum die Windowsbenutzer häufiger bei Assembler steckenbleiben - aber lassen wir das...

Falls Du kein Linux auf deinem Rechner installieren willst und auch keinen Bock hast, unter Windows eine geignete Umgebung herstellen, nimm einfach Knoppix. Das ist allerdings auf Dauer keine richtige Lösung. Deswegen empfehle ich Dir, Linux richtig zu installieren. Alternativ kannst Du das Linux-System auch auf einer virtuellen Maschine wie [VMware Server](https://github.com/lowlevel-eu/wiki/wiki/VMware "VMware"), [VirtualBox](https://github.com/lowlevel-eu/wiki/wiki/VirtualBox "VirtualBox") oder [Microsoft Virtual PC](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Virtual-PC "Microsoft Virtual PC") Installieren.

#### Deine Tools

Dann brauchst Du Editor und Compiler. Als Editor hast Du sicher schon Deinen eigenen Favoriten (nämlich vim), aber wenn nicht, dann findest Du vielleicht in der folgenden Liste einen für Dich passenden. Häufig benutzt werden:

- Unter Linux: vim, Kate, gedit, KDevelop, Eclipse
- Unter Windows: Notepad++, Eclipse

Auch beim Compiler ist die Sache relativ klar: Wenn Du [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") nimmst, wird der Compiler im Allgemeinen gcc sein und unter [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") ist damit alles geklärt. Wenn Du gcc unter [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") benutzt, solltest du dir überlegen, ob Du nicht einen Crosscompiler benutzt, der ELF-Dateien erzeugt. Bahnhof? Macht nichts, vertrau mir, installier ihn Dir einfach.

- [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

#### Dein Emulator

Schließlich brauchst Du auch noch eine Möglichkeit, dein Werk zu testen. Ja, ich weiß, der PC. Aber du willst nicht nach jeder kleinen Änderungen neu booten müssen, richtig? Besorg dir einen Emulator. VMware ist ganz nett, aber hilft Dir beim Debuggen nicht besonders weiter. Nimm Qemu oder [Bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") - oder am besten beides. Wenn Dein System in beiden Emulatoren funktioniert, ist immer noch genug Zeit, es auf den echten PC loszulassen.

- <http://www.qemu.org>
- <http://bochs.sourceforge.net>

## Wo anfangen?

### Der Bootloader

Dein eigenes Betriebssystem möchte am Anfang irgendwie von der Festplatte oder Diskette in den Speicher geladen werden, bevor es irgendwas macht. Daher brauchst Du einen Bootloader.

Hier gibt es die großen zwei Möglichkeiten, etwas fertiges zu nehmen oder selbst einen Bootloader zu schreiben. Ein guter Bootloader ist ein Projekt für sich, daher empfehle ich grundsätzlich, [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") zu benutzen und sich auf das eigentliche Betriebssystem zu konzentrieren. [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") lädt Dir deinen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und möglicherweise weitere Module vom Dateisystem auf der Platte oder Diskette, initialisiert Dir den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), bietet ein Bootmenü und einiges mehr.

Die folgenden beiden Artikel werden Dir bei den ersten Schritten mit [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") helfen:

- [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB")
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen") (Falls Du Windows benutzt, ist es vermutlich einfacher, ein vorhandenes GRUB-Image z.B. von [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") zu nehmen und den Kernel durch den eigenen zu ersetzen)

Wenn Du trotz diesen Vorteilen darauf bestehst, Deinen Bootloader selbst zu schreiben - so sei es. In den ersten Ausgaben des [Magazins](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin") findest Du die dazu nötigen Informationen. In den folgenden Abschnitten gehe ich allerdings davon aus, dass [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") benutzt wird. Du solltest also sicherstellen, dass Du eine vergleichbare Umgebung herstellst - insbesondere, dass Du im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") bist.

### Hello World und weiter

Die allererste Aufgabe für ein neues Betriebssystem ist es selbstverständlich, ein "Hello world!" auf den Bildschirm auszugeben. Wenn Du nach dem oben genannten Artikel vorgegangen bist, hast Du diesen Schritt schon erreicht. Wenn nicht: Text gibst du aus, indem Du in der Videospeicher schreibst. Er beginnt für den Textmodus an der Adresse 0xB8000 und enthält für jedes Zeichen (insgesamt 80x25) auf dem Bildschirm je zwei Bytes. Ausführlicher steht es hier: [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe") Das erste enthält den ASCII-Code des Zeichens selbst, das zweite Attribute wie Farbe. Experimentiere am besten ein bisschen damit herum.

Hey, mein Kernel läuft und gibt was aus, vielleicht wäre jetzt der Grafikmodus...? Nein! Ein wesentlicher Grund dafür ist, dass Du in der nächsten Zeit viele kritische Änderungen und dabei auch viele Fehler machen wirst. Du wirst daher um [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") nicht herumkommen. Am einfachsten geht das über Textausgaben, die leider im Grafikmodus nicht mehr ganz so leicht gehen.

Aber mit dieser Erkenntnis hast du auch schon eine schöne Aufgabe für den nächsten Schritt: Du brauchst Ausgaberoutinen, in C wäre das beispielsweise ein printf (die meistens etwas weniger mächtige Variante im Kernel wird übrigens gern printk oder kprintf genannt).

### Protected Mode

Wenn Du GRUB benutzt, bist Du zwar bereits am Anfang im Protected Mode, allerdings mit einem Standardsatz von Deskriptortabellen. Es wäre jetzt an der Zeit, das zu ändern.

Oh, Du hast keine Ahnung, was Du Dir unter Deskriptortabellen vorzustellen hast? Lies Dir am besten den Artikel zum Protected Mode durch. Wenn Du Deinen Bootloader selbst schreibst, findest Du dort auch Informationen, wie Du selbst in den Protected Mode umschaltest. Außerdem ist das Protected-Mode-Tutorial auf den Seiten der FH Zwickau zu empfehlen.

- [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")
- [Umschalten in Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode")
- [Protected-Mode-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/start.htm)

Was Du zunächst machen musst, ist, eine [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") im Speicher aufzubauen. Mit der Beschreibung auf den genannten Seiten sollte das kein Problem darstellen (aber gräme Dich nicht, wenn es nicht im ersten Versuch hinhaut - das ist für viele die erste Stelle, wo sie erst einmal eine Weile hängen).

Wenn Du die GDT aufgebaut hast, kannst Du sie anschließend laden. Das ist einer der wenigen Fälle, wo Du tatsächlich Assembler brauchst. Wenn Du C benutzt, könnte dir der Artikel über [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") helfen. Ansonsten schlag in der Dokumentation deines Compilers nach, wie es dort funktioniert.

Anschließend musst du die Segmentregister neu laden, damit die GDT auch benutzt wird. An dieser Stelle zeigt sich dann, ob Du es richtig gemacht hast. Wenn die Einträge in deiner GDT falsch sind, und beispielsweise das Codesegment nicht korrekt ist, wirst du mit höchster Wahrscheinlichkeit einen GPF auslösen. GPF steht übrigens für *General Protection Fault* und ist Dir vielleicht als *Allgemeine Schutzverletzung* besser bekannt. Weil Du noch keine [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") verarbeitest, wird das zu einem *Triple Fault* führen, was auf einem echten PC einen Reset bewirkt, qemu wird sich mit einer Fehlermeldung beenden.

### Interrupts

Hast Du die GDT gemeistert? Glückwunsch. Aber freu Dich nicht zu früh, wir haben noch mehr Tabellen im Angebot. Die zweite Tabelle, die Du unbedingt benötigst, ist die Interrupt Descriptor Table ([IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT")). Wenn irgendein Stück Hardware melden möchte, dass irgendetwas passiert ist (z.B. eine Taste gedrückt wurde), schickt es im Allgemeinen einen [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") mit einer mehr oder weniger eindeutigen Nummer. In der IDT weist du jedem Interrupt eine Funktion in deinem Kernel zu, die aufgerufen wird, wenn der Interrupt ankommt.

Auch zur IDT kannst Du die im vorigen Abschnitt verlinkten Seiten befragen.

Neben den genannten Hardwareinterrupts gibt es noch weitere. Die wichtigsten davon sind [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception"), die aufgerufen werden, wenn etwas schiefgeht (z.B. Division durch Null oder ein Speicherzugriff ohne Berechtigung) und Softwareinterrupts, die von einem Programm ausgelöst werden, z.B. um Funktionen des Kernels aufzurufen.

Wenn Du die IDT fertig eingerichtet hast, kannst du sie am besten testen, indem du entweder eine Exception provozierst oder einen Softwareinterrupt auslöst. Bevor Du die Hardwareinterrupts mit dem Assemblerbefehl sti anschaltest, solltest Du nämlich erst noch den [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") programmieren, so dass die IRQs (das sind genau die Hardwareinterrupts) beispielsweise auf die Interrupts 0x20 bis 0x2f legst (bis 0x1f liegen schon die Exceptions und Du willst IRQs ja von Exceptions unterscheiden können).

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")

Wenn Du auch Hardwareinterrupts am Laufen hast, hast Du die ersten großen Hürden genommen. Für diejenigen unter uns, die gerne etwas sehen und irgendwas zum Spielen brauchen, wäre das ein guter Zeitpunkt, einfach mal einen Tastaturtreiber zu schreiben und ein bisschen was auszuprobieren. Es kommen noch genug schwere Sachen, bis Dein Produkt sich zurecht ein Betriebssystem nennen kann, aber hey, wenn ich zwei Zahlen eingeben kann und die werden addiert - das ist doch schonmal ein Erfolgserlebnis, oder? Mich hat das jedenfalls motiviert.

## Der eigentliche Kernel

Wenn Du bis hierhin gekommen bist, hast Du mittlerweile etwas, was sich Kernel nennt. In Wirklichkeit hast Du aber noch nicht besonders viel von den ganzen Funktionen, die ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") bieten muss. Du hast die Initialisierung geschafft, bei der Du noch nicht besonders viel Auswahl hast. Richtig interessant wird es jetzt, denn jetzt kannst Du viele verschiedene Wege wählen, die eigentliche Funktionalität Deines Kernels umzusetzen.

### Architekturen

Unter der *Architektur* Deines Betriebssystem ist die Art und Weise zu verstehen, wie die Komponenten Deines Systems zusammenspielen. Bevor Du anfängst, Code für die eigentliche Funktionalität des Kernels zu schreiben, solltest Du Dir klar sein, in welche Richtung die Reise gehen soll.

- Die allerwichtigste Entscheidung, die das Aussehen Deines Betriebssystems am schwerwiegendsten beeinflussen wird, ist die Entscheidung zwischen [monolithischem Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") (die Hardwaretreiber sind alle im Kernel) und [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") (der Kernel macht nur das notwendigste, Treiber sind eigenständige [Userspace](https://github.com/lowlevel-eu/wiki/wiki/Userspace "Userspace")-Prozesse) - oder natürlich beliebiger Mischformen davon, z.B. ein modularisierter Monolith wie [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux").
- Besonders beim Microkernel ist eine zentrale Frage, wie die [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") aussehen soll. Auch bei einem monolithischen Kernel ist es kein Fehler, sich diese Frage zu stellen, auch wenn sie eher nachrangig ist.
- Wie soll die Schnittstelle der Programme zum Kernel aussehen? (z.B. [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall"))

### Die Aufgaben des Kernels

Bevor Du Dir anschaust, welche Funktionen Dein Kernel bieten soll, versichere Dich, dass Du weißt, was ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") überhaupt ist. Ja, klar, er ist der Kern des Betriebssystems. Und weiter? Seine zentrale Aufgabe ist es, die Ressourcen des Systems zu verwalten - z.B. den laufenden Programmen Speicher zuzuteilen.

Im Allgemeinen wird für Betriebssysteme im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") ein Modell verwendet, in dem der Kernel in [Ring](https://github.com/lowlevel-eu/wiki/wiki/Ring "Ring") 0 (Kernel Mode) und alle Programme in Ring 3 (User Mode) laufen. Als grobe Richtung kannst Du Dir merken, dass der Kernel alles das ist, was in Ring 0 läuft. Wenn ein User-Mode-Programm Betriebssystemfunktionen benötigt (z.B. mehr Speicher), ruft es den Kernel auf.

Was sind nun also die Funktionen, die ein Kernel im Allgemeinen bietet?

- [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung"): Programme und höchstwahrscheinlich auch der Kernel selbst müssen zur Laufzeit dynamisch Speicher reservieren können. Die Speicherverwaltung im Kernel arbeitet üblicherweise nicht mit beliebigen anforderbaren Größen, sondern mit Blöcken von 4 Kilobytes, sogenannten *Speicherseiten* (engl. *Pages*). Man unterscheidet dabei zwischen physischer und [virtueller](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") Speicherverwaltung.
- [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung"): Ein Betriebssystem hat diese Bezeichnung nur verdient, wenn es Programme ausführen kann. Zur Prozessverwaltung gehören Funktionen wie das Starten und Beenden von Prozessen, aber im weiteren Sinne auch [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), also das Umschalten zwischen den einzelnen Prozessen. Neben [Prozessen](https://github.com/lowlevel-eu/wiki/wiki/Prozess "Prozess") möchtest Du eventuell auch [Threads](https://github.com/lowlevel-eu/wiki/wiki/Prozess#threads "Thread") unterstützen.
- [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation"): Je nach Architektur des Betriebssystem extrem wichtig bis erstmal völlig nebensächlich. Es geht dabei darum, dass zwei Programme Informationen austauschen können, z.B. durch Senden von Nachrichten oder Aufruf von Funktionen des anderen Programms.
- [Hardwaretreiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"): Jeder Kernel enthält auch Hardwaretreiber. Je nach Architektur gehören dabei alle, manche oder so gut wie keine Treiber zum Kernel.
- Den Bootprozess anstoßen. Nachdem der Kernel sich selbst initialisiert hat, lädt er in irgendeiner Form ein erstes Programm (unter Linux *init*) und startet es.

Im Umkehrschluss gehören eine [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell"), [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") oder sonstige Anwendungsprogramme **nicht** in den Kernel! Eine Shell im Kernel ist vielleicht akzeptabel für eine frühe Testphase, um überhaupt einmal etwas laufen zu sehen, aber es ist auf Dauer kein tragfähiges Konzept. (Einer der Gründe dafür: Erinnerst Du Dich an den Absatz über die Ringe oben? Was im Kernel liegt, hat Kernel-Mode-Privilegien, und ein Grundsatz für sichere Software ist, nie Privilegien zu haben, die man nicht braucht)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4362/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1619/index.html)

<!-- MediaWiki page 1619; revision 4362; parent 4268; 2009-05-09T13:31:51Z -->
