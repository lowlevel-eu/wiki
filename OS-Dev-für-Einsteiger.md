# OS-Dev für Einsteiger

|  |  |  |
| ----- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  | **Navigation** | [Teil 1 - Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") » |

Okay, Du hast also beschlossen, dass Du Dein eigenes Betriebssystem schreiben willst? Dann bist du hier genau richtig.

Dieser Artikel versucht, Dir einen Überblick zu geben, welche Fragen Du Dir stellen solltest und wie Du die Sache am geschicktesten angehst. Er soll sozusagen einen Wegweiser durch das Wiki darstellen, der Dir am Anfang hilft, die relevanten Themen auf Anhieb zu finden.

Auf der anderen Seite wird er sicher auch die eine oder andere Frage offen lassen. Zögere nicht, Dich im [Forum](http://lowlevel.brainsware.org/forum) anzumelden und nachzufragen. Der harte Kern der Community ist auch im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") anzutreffen. Falls Du Probleme mit der Anmeldung im Forum haben solltest, kannst Du Dich dort melden.

## Vor dem Start

Frisch ans Werk, Editor und Compiler ausgepackt – aber halt! Bevor es wirklich losgeht, solltest Du Dir einige Fragen beantworten, damit Du weißt, was Du überhaupt entwickeln willst und worüber Du Informationen suchen musst.

### Willst Du wirklich ein OS schreiben?

Die Frage klingt vielleicht seltsam, aber sie ist genau so gemeint, wie sie da steht. Willst Du wirklich ein OS entwickeln? Ist Dir klar, was ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") macht?

Wenn Du in erster Linie an eine grafische Oberfläche denkst, bist Du hier womöglich falsch. Grafische Oberflächen sind ein interessantes Thema – aber eine vollkommen andere Baustelle. Ein OS ist die [Schnittstelle zur Hardware](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"). Das heißt, Du wirst eine [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") bauen, einen [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler"), [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für störrische Hardware. Du wirst alles tun, nur keine bunten Pixel auf den Bildschirm bringen – oder falls doch, wird dir direkt anschließend die saubere Basis fehlen, damit man mit diesen Pixeln auch etwas sinnvolles anfangen kann.

Du wirst dich mit vielen Fehlern herumschlagen müssen, du wirst trockene Spezifikationen etliche Artikel und [Tutorials](https://lowlevel-eu.github.io/wiki/pages/1423/index.html "Kategorie:Tutorials") lesen müssen und manchmal stundenlang über ein Problem hängen und darüber grübeln, wie man es (am besten oder überhaupt) löst. Du wirst eine Menge fremden Code lesen müssen, eventuell nicht in der Sprache, mit der du dein OS programmierst (falls du dich dazu entscheidest, nicht in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") zu programmieren). Du wirst dich selbst beim Kopieren von fremden Code ertappen, was aber der falsche Weg ist, denn beim Kopieren von Code lernt man nichts. Du wirst einige Wochen, wenn nicht gar Monate brauchen bis du alles verstanden hast. Und selbst dann gibt es immer noch Dinge, die dir Kopfschmerzen bereiten. Es wird immer das ein oder andere Problem, den ein oder anderen Bug geben. Das ist aber in der Entwicklung von nativen Anwendungen auch nicht anders.

Du wirst, sofern du nicht Linux nutzt, auch einige Zeit mit dem Setup deiner Build-Umgebung verbringen. Es wird auch nicht alles von Anfang an klappen mit den [Tools](https://lowlevel-eu.github.io/wiki/pages/1924/index.html "Kategorie:Werkzeuge"). Es ist natürlich nicht unmöglich, auf anderen Systemen als Linux ein Betriebssystem zu entwickeln, aber anfangs schwieriger bzw. erfordert eine größere Vorbereitung.

Wer sich nicht mit Hardware herumschlagen möchte, kann sich ein DOS oder ein abgespecktes [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") als Grundlage nehmen und seine Oberfläche darauf aufbauen. Aber selbst dann gibt es viel zu lernen: Du musst das darunter liegende System verstehen, wissen, wie es arbeitet und dementsprechend deine Vorstellung darauf aufbauen oder gegebenenfalls das System darunter an deine Bedürfnisse anpassen. Aber auch hier gilt wieder viele Spezifikationen, Artikel und Tutorials sowie Code zu lesen.

### Voraussetzungen

Obwohl dieses Wiki den Einstieg in Betriebssystementwicklung so einfach wie möglich machen will, ist Betriebssystementwicklung dennoch sehr komplex, und einige Fertigkeiten sind einfach nötig. Ich will nicht sagen, dass man die Fertigkeiten nicht durch "learning-by-doing" erwerben kann, jedoch wird das bei diesem Thema sehr frustrierend. Außerdem wärst Du dann allein, weil die meisten Forenmitglieder bei Erklärungen zu Betriebssystemtheorie nicht bei Adam und Eva anfangen können.

#### Unverzichtbar

- Programmiererfahrung. Wenn Du noch nie ein Programm geschrieben hast, bist Du hier ziemlich sicher falsch. Wenn Du einen Einstieg suchst, dann werden Dir die Lowlevel-Forenmitglieder sicher trotzdem dabei helfen, Tutorials und Ressourcen zum Einstieg zu finden.
- Gute Kenntnis des Systems. Wenn Du regelmäßig mit der Bedienung Deines Betriebssystems kämpfst, dann ist es schwer, dabei Arbeit getan zu kriegen. Ein Windowsnutzer braucht eventuell sogar mehr Erfahrung als ein Linuxer, da sich manche Tools auf Windows zu Beginn recht zickig verhalten können.
- Neugier und Geduld. Vermutlich die heimlichen Kernqualifikationen jedes Programmierers. Ohne Neugier und Geduld wird es schwer, die Frustrationen der Betriebssystementwicklung zu überstehen.

#### Hilfreich, aber nicht unbedingt nötig

- Unix-Kenntnisse.
- Assembler. Zwar braucht man nur einige Zeilen Assembler (wenn man es richtig macht), und das nötige Stück Assembler haben sich viele durch "learning-by-doing" angeeignet, jedoch helfen Kenntnisse von Assembler enorm beim Verständnis. Es lohnt sich eigentlich bei jedem Projekt, eine Abstraktionsschicht tiefer schauen zu können.
- Englisch. Handbücher und andere Dokumentation sind kaum auf Deutsch zu finden, und das, was man findet, ist häufig veraltet. Außerdem ist OSDev.org oft noch besser als das Lowlevel-Wiki. Wir arbeiten dran *\*g\**

### Die Programmiersprache

Ein weit verbreitetes Vorurteil ist, dass man ein Betriebssystem komplett in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") schreiben muss, oder sogar erst einen Compiler entwickeln müsste. Quatsch. Man kann, wenn man es möchte, aber man muss nicht. Wahr ist, dass man um einige wenige Zeilen Assembler nicht herumkommen wird, aber es hält sich in Grenzen.

Ein übliches Vorgehen ist es, nur das nötigste in Assembler zu schreiben und für den Rest eine Hochsprache zu benutzen. Für die Wahl dieser Hochsprache gibt es im großen und ganzen zwei Alternativen:

- Du nimmst [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Fast jeder spricht diese Sprache und Du bekommst Unmengen an Beispielcode in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Dein Betriebssystem ist eins von vielen und im Forum oder im IRC wird dir fast jeder helfen können.
- Du nimmst nicht [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Du wirst Dich vor allem am Anfang wesentlich seltener beim Kopieren von Code erwischen, weil es einfach nicht geht, ohne ihn in deine Sprache zu übersetzen. Ja, das ist durchaus positiv. Auf der anderen Seite bist du ein Außenseiter und erhältst vielleicht nicht ganz so umfangreich Hilfe und musst Dich möglicherweise öfter selbst durchschlagen – gerade wenn es um Besonderheiten deiner Sprache oder Deines Compilers geht.

Von Mitgliedern der Lowlevel-Community benutzte Alternativen zu [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") sind beispielsweise [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") oder [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") (mit FreePascal oder mit Tricks auch Delphi als Compiler). Theoretisch würde auch [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC") funktionieren. Andere Sprachen hat hier meines Wissens noch niemand versucht, könnten natürlich aber trotzdem funktionieren.

### Entwicklungsumgebung und Tools

Um Dein eigenes Betriebssystem zu entwickeln, brauchst Du ein paar Werkzeuge. Du musst dir eine Buildumgebung aufbauen (was je nach Betriebssystem unterschiedlich komplex ist), du brauchst einen Editor und einen Emulator. All das wird im **[ersten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung")** der Tutorial-Reihe "OS-Dev für Einsteiger" erklärt.

## Wo anfangen?

### Der Bootloader

Dein eigenes Betriebssystem möchte am Anfang irgendwie von der Festplatte oder Diskette in den Speicher geladen werden, bevor es irgendwas macht. Daher brauchst Du einen Bootloader.

Hier gibt es die großen zwei Möglichkeiten, etwas fertiges zu nehmen oder selbst einen Bootloader zu schreiben. Ein guter Bootloader ist ein Projekt für sich, daher empfehle ich grundsätzlich, [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") zu benutzen und sich auf das eigentliche Betriebssystem zu konzentrieren. [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") lädt Dir deinen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und möglicherweise weitere Module vom Dateisystem auf der Platte oder Diskette, initialisiert Dir den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), bietet ein Bootmenü und einiges mehr.

Die folgenden beiden Artikel werden Dir bei den ersten Schritten mit [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") helfen:

- [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB")
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen") (Falls Du Windows benutzt, ist es vermutlich einfacher, ein vorhandenes GRUB-Image z.B. von [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") zu nehmen und den Kernel durch den eigenen zu ersetzen)

Wenn Du trotz diesen Vorteilen darauf bestehst, Deinen Bootloader selbst zu schreiben – so sei es. In den ersten Ausgaben des [Magazins](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin") findest Du die dazu nötigen Informationen. In den folgenden Abschnitten gehe ich allerdings davon aus, dass [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") benutzt wird. Du solltest also sicherstellen, dass Du eine vergleichbare Umgebung herstellst – insbesondere, dass Du im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") bist.

#### Äh ja, nochmal auf deutsch bitte

Im **[vierten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World")** der Reihe "OS-Dev für Einsteiger" wird genau erklärt, wie du dir einen einfachen Kernel in C und per GRUB aufbaust. Du wirst auch auf etwas [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") stoßen. Solltest du kein Assembler beherrschen, keine Bange: Du brauchst nur ganz wenig für die Betriebssystementwicklung. Wenn du keinen Plan hast, wie du in Assembler programmierst, dann lies dir den **[zweiten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-2-Assembler-101 "Teil 2 - Assembler 101")** des Reihe "OS-Dev für Einsteiger" durch, dort bekommst du das benötigte Wissen, um den minimalen Asssembler-Teil zu verstehen.

### Hello World und weiter

Die allererste Aufgabe für ein neues Betriebssystem ist es selbstverständlich, ein "Hello world!" auf den Bildschirm auszugeben. Wenn Du nach dem oben genannten Artikel vorgegangen bist, hast Du diesen Schritt schon erreicht. Wenn nicht: Text gibst du aus, indem Du in der Videospeicher schreibst. Er beginnt für den Textmodus an der Adresse 0xB8000 und enthält für jedes Zeichen (insgesamt 80x25) auf dem Bildschirm je zwei Bytes. Das erste enthält den ASCII-Code des Zeichens selbst, das zweite Attribute wie Farbe. Experimentiere am besten ein bisschen damit herum. (Ausführlicher steht es im Artikel [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe"))

Hey, mein Kernel läuft und gibt was aus, vielleicht wäre jetzt der Grafikmodus...? Nein! Ein wesentlicher Grund dafür ist, dass Du in der nächsten Zeit viele kritische Änderungen und dabei auch viele Fehler machen wirst. Du wirst daher um [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") nicht herumkommen. Am einfachsten geht das über Textausgaben, die leider im Grafikmodus nicht mehr ganz so leicht gehen.

Aber mit dieser Erkenntnis hast du auch schon eine schöne Aufgabe für den nächsten Schritt: Du brauchst Ausgaberoutinen, in C wäre das beispielsweise ein printf (die meistens etwas weniger mächtige Variante im Kernel wird übrigens gern printk oder kprintf genannt).

### Protected Mode

Wenn Du GRUB benutzt, bist Du zwar bereits am Anfang im Protected Mode, allerdings mit einem Standardsatz von Deskriptortabellen. Es wäre jetzt an der Zeit, das zu ändern.

Oh, Du hast keine Ahnung, was Du Dir unter Deskriptortabellen vorzustellen hast? Lies Dir am besten den Artikel zum Protected Mode durch – oder wenn Du einen groben Überblick hast, kannst Du auch direkt zum Artikel über die [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") übergehen. Wenn Du Deinen Bootloader selbst schreibst, findest Du dort auch Informationen, wie Du selbst in den Protected Mode umschaltest. Außerdem ist das Protected-Mode-Tutorial auf den Seiten der FH Zwickau zu empfehlen.

- [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")
- [Umschalten in Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode")
- [Global Descriptor Table](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "Global Descriptor Table") (GDT)
- [Protected-Mode-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/start.htm)

Was Du zunächst machen musst, ist, eine GDT im Speicher aufzubauen. Mit der Beschreibung auf den genannten Seiten sollte das kein Problem darstellen (aber gräme Dich nicht, wenn es nicht im ersten Versuch hinhaut – das ist für viele die erste Stelle, wo sie erst einmal eine Weile hängen).

Wenn Du die GDT aufgebaut hast, kannst Du sie anschließend laden. Das ist einer der wenigen Fälle, wo Du tatsächlich Assembler brauchst. Wenn Du C benutzt, könnte dir der Artikel über [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") helfen. Ansonsten schlag in der Dokumentation deines Compilers nach, wie es dort funktioniert.

Anschließend musst du die Segmentregister neu laden, damit die GDT auch benutzt wird. An dieser Stelle zeigt sich dann, ob Du es richtig gemacht hast. Wenn die Einträge in deiner GDT falsch sind, und beispielsweise das Codesegment nicht korrekt ist, wirst du mit höchster Wahrscheinlichkeit einen GPF auslösen. GPF steht übrigens für *General Protection Fault* und ist Dir vielleicht als *Allgemeine Schutzverletzung* besser bekannt. Weil Du noch keine [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") verarbeitest, wird das zu einem *Triple Fault* führen, was auf einem echten PC einen Reset bewirkt, qemu wird sich mit einer Fehlermeldung beenden.

### Interrupts

Hast Du die GDT gemeistert? Glückwunsch. Aber freu Dich nicht zu früh, wir haben noch mehr Tabellen im Angebot. Die zweite Tabelle, die Du unbedingt benötigst, ist die Interrupt Descriptor Table ([IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT")). Wenn irgendein Stück Hardware melden möchte, dass irgendetwas passiert ist (z.B. eine Taste gedrückt wurde), schickt es im Allgemeinen einen [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") mit einer mehr oder weniger eindeutigen Nummer. In der IDT weist du jedem Interrupt eine Funktion in deinem Kernel zu, die aufgerufen wird, wenn der Interrupt ankommt.

Auch zur IDT kannst Du die im vorigen Abschnitt verlinkten Seiten befragen.

Neben den genannten Hardwareinterrupts gibt es noch weitere. Die wichtigsten davon sind [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception"), die aufgerufen werden, wenn etwas schiefgeht (z.B. Division durch Null oder ein Speicherzugriff ohne Berechtigung) und Softwareinterrupts, die von einem Programm ausgelöst werden, z.B. um Funktionen des Kernels aufzurufen.

Wenn Du die IDT fertig eingerichtet hast, kannst du sie am besten testen, indem du entweder eine Exception provozierst oder einen Softwareinterrupt auslöst. Bevor Du die Hardwareinterrupts mit dem Assemblerbefehl sti anschaltest, solltest Du nämlich erst noch den [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") programmieren, so dass die IRQs (das sind genau die Hardwareinterrupts) beispielsweise auf die Interrupts 0x20 bis 0x2f legst (bis 0x1f liegen schon die Exceptions und Du willst IRQs ja von Exceptions unterscheiden können).

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")

Wenn Du auch Hardwareinterrupts am Laufen hast, hast Du die ersten großen Hürden genommen. Für diejenigen unter uns, die gerne etwas sehen und irgendwas zum Spielen brauchen, wäre das ein guter Zeitpunkt, einfach mal einen Tastaturtreiber zu schreiben und ein bisschen was auszuprobieren. Es kommen noch genug schwere Sachen, bis Dein Produkt sich zurecht ein Betriebssystem nennen kann, aber hey, wenn ich zwei Zahlen eingeben kann und die werden addiert – das ist doch schonmal ein Erfolgserlebnis, oder? Mich hat das jedenfalls motiviert.

### Hm, ja, anschauliches Beispiel?

Im **[fünften Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-5-Interrupts "Teil 5 - Interrupts")** der Reihe "OS-Dev für Einsteiger" wird das Einrichten einer GDT sowie das Einrichten einer IDT und das Aktivieren von Interrupts und deren Behandlung noch einmal erklärt. Wenn Du die Artikel zur [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") und [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") gelesen hast, wird dir schnell der zusammenhang klar.

## Der eigentliche Kernel

Wenn Du bis hierhin gekommen bist, hast Du mittlerweile etwas, was sich Kernel nennt. In Wirklichkeit hast Du aber noch nicht besonders viel von den ganzen Funktionen, die ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") bieten muss. Du hast die Initialisierung geschafft, bei der Du noch nicht besonders viel Auswahl hast. Richtig interessant wird es jetzt, denn jetzt kannst Du viele verschiedene Wege wählen, die eigentliche Funktionalität Deines Kernels umzusetzen.

### Architekturen

Unter der *Architektur* Deines Betriebssystem ist die Art und Weise zu verstehen, wie die Komponenten Deines Systems zusammenspielen. Bevor Du anfängst, Code für die eigentliche Funktionalität des Kernels zu schreiben, solltest Du Dir klar sein, in welche Richtung die Reise gehen soll.

- Die allerwichtigste Entscheidung, die das Aussehen Deines Betriebssystems am schwerwiegendsten beeinflussen wird, ist die Entscheidung zwischen [monolithischem Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") (die Hardwaretreiber sind alle im Kernel) und [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") (der Kernel macht nur das notwendigste, Treiber sind eigenständige [Userspace](https://github.com/lowlevel-eu/wiki/wiki/Userspace "Userspace")-Prozesse) – oder natürlich beliebiger Mischformen davon, z.B. ein modularisierter Monolith wie [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux").
- Besonders beim Microkernel ist eine zentrale Frage, wie die [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") aussehen soll. Auch bei einem monolithischen Kernel ist es kein Fehler, sich diese Frage zu stellen, auch wenn sie eher nachrangig ist.
- Wie soll die Schnittstelle der Programme zum Kernel aussehen? (z.B. [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall"))

### Die Aufgaben des Kernels

Bevor Du Dir anschaust, welche Funktionen Dein Kernel bieten soll, versichere Dich, dass Du weißt, was ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") überhaupt ist. Ja, klar, er ist der Kern des Betriebssystems. Und weiter? Seine zentrale Aufgabe ist es, die Ressourcen des Systems zu verwalten – z.B. den laufenden Programmen Speicher zuzuteilen.

Im Allgemeinen wird für Betriebssysteme im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") ein Modell verwendet, in dem der Kernel in [Ring](https://github.com/lowlevel-eu/wiki/wiki/Ring "Ring") 0 (Kernel Mode) und alle Programme in Ring 3 (User Mode) laufen. Als grobe Richtung kannst Du Dir merken, dass der Kernel alles das ist, was in Ring 0 läuft. Wenn ein User-Mode-Programm Betriebssystemfunktionen benötigt (z.B. mehr Speicher), ruft es den Kernel auf.

Was sind nun also die Funktionen, die ein Kernel im Allgemeinen bietet?

- [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung"): Programme und höchstwahrscheinlich auch der Kernel selbst müssen zur Laufzeit dynamisch Speicher reservieren können. Die Speicherverwaltung im Kernel arbeitet üblicherweise nicht mit beliebigen anforderbaren Größen, sondern mit Blöcken von 4 Kilobytes, sogenannten *Speicherseiten* (engl. *Pages*). Man unterscheidet dabei zwischen [physischer](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#physische-speicherverwaltung "Speicherverwaltung") und [virtueller Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#virtuelle-speicherverwaltung "Speicherverwaltung").
  - Ein anschauliches Beispiel zur Implementierung einer physischen Speicherverwaltung wird im **[siebten Artikel](https://github.com/lowlevel-eu/wiki/wiki/Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung")** der Reihe "OS-Dev für Einsteiger" gegeben
- [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung"): Ein Betriebssystem hat diese Bezeichnung nur verdient, wenn es Programme ausführen kann. Zur Prozessverwaltung gehören Funktionen wie das Starten und Beenden von Prozessen, aber im weiteren Sinne auch [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), also das Umschalten zwischen den einzelnen Prozessen. Neben [Prozessen](https://github.com/lowlevel-eu/wiki/wiki/Prozess "Prozess") möchtest Du eventuell auch [Threads](https://github.com/lowlevel-eu/wiki/wiki/Prozess#threads "Thread") unterstützen.
- [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation"): Je nach Architektur des Betriebssystem extrem wichtig bis erstmal völlig nebensächlich. Es geht dabei darum, dass zwei Programme Informationen austauschen können, z.B. durch Senden von Nachrichten oder Aufruf von Funktionen des anderen Programms.
- [Hardwaretreiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"): Jeder Kernel enthält auch Hardwaretreiber. Je nach Architektur gehören dabei alle, manche oder so gut wie keine Treiber zum Kernel.
- Den Bootprozess anstoßen. Nachdem der Kernel sich selbst initialisiert hat, lädt er in irgendeiner Form ein erstes Programm (unter Linux *init*) und startet es.

Im Umkehrschluss gehören eine [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell"), [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") oder sonstige Anwendungsprogramme **nicht** in den Kernel! Eine Shell im Kernel ist vielleicht akzeptabel für eine frühe Testphase, um überhaupt einmal etwas laufen zu sehen, aber es ist auf Dauer kein tragfähiges Konzept. (Einer der Gründe dafür: Erinnerst Du Dich an den Absatz über die Ringe oben? Was im Kernel liegt, hat Kernel-Mode-Privilegien, und ein Grundsatz für sichere Software ist, nie Privilegien zu haben, die man nicht braucht)

### Schnittstelle zum Userspace

Auch der tollste Kernel mit [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking")-Unterstützung bringt Dir natürlich herzlich wenig, wenn die laufenden Programme nicht mit dem Benutzer interagieren können. Um den Programmen, die ja in einem eigenen Adressraum laufen und meist keinen direkten Zugriff auf die Hardware haben, diese Möglichkeit zu bieten, muss der Kernel eine entsprechende Schnittstelle, üblicherweise in Form von [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall"), anbieten. Wie diese Schnittstelle genau aussieht, hängt von Deiner gewählten Architektur ab. Bei einem Monolithen wird die Schnittstelle eher breit ausfallen, und beispielsweise Funktionen für das Arbeiten mit Dateien mitbringen, während bei einem Mikrokernel vor allem die Funktionen für die [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") im Zentrum stehen werden.

#### Da habt ihr doch sicher auch was in eurer Reihe, oder?

Na klar. Im **[sechsten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-6-Multitasking "Teil 6 - Multitasking")** der Reihe "OS-Dev für Einsteiger" wird das Implementieren von Multitasking per [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") anschaulich und mit Codebeispielen erklärt.

### Treiber

Irgendwann wirst Du vermutlich auf die Idee kommen irgendwas von einer [Diskette](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC") oder [Festplatte](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") lesen zu wollen. Dafür werden zwei Treiber benötigt: einer für das [Diskettenlaufwerk](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC")/die [Festplatte](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") und ein [Dateisystemtreiber](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"). Wie sich die Treiber in Dein System einfügen sollen, hast Du bei der Wahl Deiner Architektur ja schon grob entschieden. Jetzt ist es an der Zeit die Details festzulegen. Für die Treiber musst Du auch erstmal eine Schnittstelle definieren und Dir genau überlegen wie die Kommunikation zwischen Clients und den Treibern ablaufen soll. Dabei ist es sicher keine schlechte Idee, ein bisschen in den Schnittstellen von anderen [Betriebssystemen](https://lowlevel-eu.github.io/wiki/pages/1649/index.html "Kategorie:Betriebssystem") zu stöbern. Weiter könntest Du Dir auch überlegen dir [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"), das von der Lowlevel-Community entwickelt wird, genauer anzusehen, denn damit sparst du unter Umständen viel Zeit und Ärger.

|  |  |  |
| ----- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  | **Navigation** | [Teil 1 - Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6226/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1619/index.html)

<!-- MediaWiki page 1619; revision 6226; parent 6225; 2009-11-09T08:54:49Z -->
