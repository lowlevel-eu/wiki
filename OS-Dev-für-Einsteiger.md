# OS-Dev für Einsteiger

|  |  |  |
| ----- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  | **Navigation** | [Teil 1 - Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") » |

Okay, du hast also beschlossen, dass du dein eigenes Betriebssystem schreiben willst? Dann bist du hier genau richtig.

Die Artikelserie OS-Dev für Einsteiger erklärt Schritt für Schritt zunächst einige Grundkonzepte und dann anhand eines Beispielprojekts die Entwicklung eines eigenen Betriebssystems. Oben und unten auf jeder Seite findest du eine Navigationsleiste, die dich zum nächsten Teil führt. Alle Teile auf einen Blick findest du in der [Kategorie OS-Dev für Einsteiger](https://lowlevel-eu.github.io/wiki/pages/1895/index.html "Kategorie:OS-Dev für Einsteiger").

Dieser Artikel dient als Einstieg in die Serie und geht im Schnelldurchlauf über alle Konzepte. Er versucht damit, dir einen Überblick zu geben, welche Fragen du dir stellen solltest und wie du die Sache am geschicktesten angehst.

Auf der anderen Seite wird die Tutorialreihe sicher auch die eine oder andere Frage offen lassen. Zögere nicht, dich im Forum anzumelden und nachzufragen. Der harte Kern der Community ist auch im [IRC](https://github.com/lowlevel-eu/wiki/wiki/IRC "IRC") anzutreffen. Falls du Probleme mit der Anmeldung im Forum haben solltest, kannst du dich dort melden.

## Vor dem Start

Frisch ans Werk, Editor und Compiler ausgepackt – aber halt! Bevor es wirklich losgeht, solltest du dir einige Fragen beantworten, damit du weißt, was du überhaupt entwickeln willst und worüber du Informationen suchen musst.

### Willst du wirklich ein OS schreiben?

Die Frage klingt vielleicht seltsam, aber sie ist genau so gemeint, wie sie da steht. Willst du wirklich ein OS entwickeln? Ist dir klar, was ein [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") macht?

Wenn du in erster Linie an eine grafische Oberfläche denkst, bist du hier womöglich falsch. Grafische Oberflächen sind ein interessantes Thema – aber eine vollkommen andere Baustelle. Ein OS ist die [Schnittstelle zur Hardware](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"). Das heißt, du wirst eine [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") bauen, einen [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler"), [Treiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber") für störrische Hardware. Du wirst alles tun, nur keine bunten Pixel auf den Bildschirm bringen – oder falls doch, wird dir direkt anschließend die saubere Basis fehlen, damit man mit diesen Pixeln auch etwas sinnvolles anfangen kann.

Du wirst dich mit vielen Fehlern herumschlagen müssen, du wirst trockene Spezifikationen, etliche Artikel und [Tutorials](https://lowlevel-eu.github.io/wiki/pages/1423/index.html "Kategorie:Tutorials") lesen müssen und manchmal stundenlang über einem Problem hängen und darüber grübeln, wie man es (am besten oder überhaupt) löst. Du wirst eine Menge fremden Code lesen müssen, eventuell nicht in der Sprache, mit der du dein OS programmierst (falls du dich dazu entscheidest, nicht in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") zu programmieren). Du wirst dich selbst beim Kopieren von fremden Code ertappen, was aber der falsche Weg ist, denn beim Kopieren von Code lernt man nichts. Du wirst einige Wochen, wenn nicht gar Monate brauchen, bis du alles verstanden hast. Und selbst dann gibt es immer noch Dinge, die dir Kopfschmerzen bereiten. Es wird immer das ein oder andere Problem, den ein oder anderen Bug geben. Das ist aber in der Entwicklung von nativen Anwendungen auch nicht anders.

Du wirst, sofern du nicht Linux nutzt, auch einige Zeit mit dem Setup deiner Build-Umgebung verbringen. Es wird auch nicht alles von Anfang an klappen mit den [Tools](https://lowlevel-eu.github.io/wiki/pages/1924/index.html "Kategorie:Werkzeuge"). Es ist natürlich nicht unmöglich, auf anderen Systemen als Linux ein Betriebssystem zu entwickeln, aber anfangs schwieriger bzw. erfordert eine größere Vorbereitung.

Wer sich nicht mit Hardware herumschlagen möchte, kann sich ein DOS oder ein abgespecktes [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") als Grundlage nehmen und seine Oberfläche darauf aufbauen. Aber selbst dann gibt es viel zu lernen: Du musst das darunter liegende System verstehen, wissen, wie es arbeitet und dementsprechend deine Vorstellung darauf aufbauen oder gegebenenfalls das System darunter an deine Bedürfnisse anpassen. Aber auch hier gilt es wieder viele Spezifikationen, Artikel und Tutorials sowie Code zu lesen.

### Voraussetzungen

Obwohl dieses Wiki den Einstieg in Betriebssystementwicklung so einfach wie möglich machen will, ist Betriebssystementwicklung dennoch sehr komplex, und einige Fertigkeiten sind einfach nötig. Ich will nicht sagen, dass man die Fertigkeiten nicht durch "learning-by-doing" erwerben kann, jedoch wird das bei diesem Thema sehr frustrierend. Außerdem wärst du dann allein, weil die meisten Forenmitglieder bei Erklärungen zu Betriebssystemtheorie nicht bei Adam und Eva anfangen können.

#### Unverzichtbar

- Programmiererfahrung! Wenn du noch nie ein Programm geschrieben hast, bist du hier ziemlich sicher falsch. Das Programmieren eines richtigen Betriebssystems ist keine Anfängerübung zum Erlernen des Programmierens, ein gewisser Level an Programmiererfahrungen ist dafür zwingend erforderlich. Wenn du erst einmal einen Einstieg in das Programmieren als solches suchst, dann werden dir die Lowlevel-Forenmitglieder sicher trotzdem dabei helfen, Tutorials und Ressourcen zu finden.
- Gute Kenntnis des Systems und der benutzten Tools, also Compiler, Linker und deren Kollegen. Wenn du regelmäßig mit der Bedienung deines Betriebssystems oder der benötigten Programmierwerkzeuge kämpfst, dann ist es schwer, dabei Arbeit getan zu kriegen. Ein Windowsnutzer braucht eventuell sogar mehr Erfahrung als ein Linuxer, da sich manche Tools auf Windows zu Beginn recht zickig verhalten können. Auch die Zusammenhänge von Compiler - Assembler - Linker und den dazwischen liegenden Dateiformaten (linkbare Objekt-Dateien und ausführbare Programm-Dateien) sollten zumindest in Grundzügen geläufig sein.
- Neugier und Geduld. Vermutlich die heimlichen Kernqualifikationen jedes Programmierers. Ohne Neugier und Geduld wird es schwer, die Frustrationen der Betriebssystementwicklung zu überstehen.
- Kenntnisse über die Funktionsweise eines Computers. Ein Betriebssystem hat die Aufgabe, den Anwendungsprogrammen einen funktionierenden und fairen Zugang zu den Ressourcen eines Computers zu ermöglichen. Dafür ist es natürlich von Vorteil, wenn man weiß, was den Computer in seinem Innersten zusammenhält. Du solltest also schon recht konkret wissen, was die einzelnen Komponenten eines Computers machen und wie diese zusammenspielen.
- Umrechnen zwischen Zahlensystemen. Beim OS-Dev muss man häufig zwischen Dezimal-, Hexadezimal-, Oktal- und Binärsystem umrechnen, um die richtigen Bits zu setzten/löschen. Eine gute und kurze Anleitung dazu gibt es z.B. [hier](http://www.linuxhilfen.org/c/c_aufsteiger_zahl.html). Nachdem du verstanden hast wie es funktioniert und es mehrmals auf Papier geübt hast, kannst du natürlich auch z.B. den Windowstaschenrechner im "wissenschaftlichen Modus" zum Umrechnen benutzen. Ab Windows 7 gibt es einen "Programmierer"-Modus, der das Umrechnen noch einfacher macht, indem man sogar einzelne Bits an- und abschalten kann.
- Bitweise Operatoren. Man sollte wissen, wie man einzelne Bits innerhalb einer Variable löscht und setzt. Der Artikel [Bitweise Operatoren](https://github.com/lowlevel-eu/wiki/wiki/Bitweise-Operatoren "Bitweise Operatoren") bietet hier das nötige Basiswissen.

#### Hilfreich, aber nicht unbedingt nötig

- Unix-Kenntnisse.
- Assembler. Zwar braucht man nur einige Zeilen Assembler (wenn man es richtig macht), und das nötige Stück Assembler haben sich viele durch "learning-by-doing" angeeignet, jedoch helfen Kenntnisse von Assembler enorm beim Verständnis. Es lohnt sich eigentlich bei jedem Projekt, eine Abstraktionsschicht tiefer schauen zu können.
- Englisch. Handbücher, Spezifikationen und andere Dokumentation sind quasi nie auf Deutsch zu finden, und das, was man findet, ist häufig veraltet. Außerdem ist [OSDev.org](http://wiki.osdev.org) oft noch besser als das Lowlevel-Wiki. Wir arbeiten dran *\*g\**

### Die Programmiersprache

Ein weit verbreitetes Vorurteil ist, dass man ein Betriebssystem komplett in [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") schreiben muss, oder sogar erst einen Compiler entwickeln müsste. Quatsch. Man kann, wenn man es möchte, aber man muss nicht. Wahr ist, dass man um einige wenige Zeilen Assembler nicht herumkommen wird, aber es hält sich in Grenzen.

Ein übliches Vorgehen ist es, nur das nötigste in Assembler zu schreiben und für den Rest eine Hochsprache zu benutzen. Für die Wahl dieser Hochsprache gibt es im grossen und ganzen zwei Alternativen:

- Du nimmst [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Fast jeder spricht diese Sprache und du bekommst Unmengen an Beispielcode in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Dein Betriebssystem ist eins von vielen und im Forum oder im IRC wird dir fast jeder helfen können.
- Du nimmst nicht [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"). Du wirst dich vor allem am Anfang wesentlich seltener beim Kopieren von Code erwischen, weil es einfach nicht geht, ohne ihn in deine Sprache zu übersetzen. Ja, das ist durchaus positiv. Auf der anderen Seite bist du ein Aussenseiter und erhältst vielleicht nicht ganz so umfangreich Hilfe und musst dich möglicherweise öfter selbst durchschlagen – gerade, wenn es um Besonderheiten deiner Sprache oder deines Compilers geht.

Von Mitgliedern der Lowlevel-Community benutzte Alternativen zu [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") sind beispielsweise [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") oder [Pascal](https://github.com/lowlevel-eu/wiki/wiki/Pascal "Pascal") (mit FreePascal oder mit Tricks auch Delphi als Compiler). Theoretisch würden auch [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC") und PureBasic funktionieren. Andere Sprachen hat hier meines Wissens noch niemand versucht, könnten natürlich aber trotzdem funktionieren.

### Plattform

Für welche Plattform du dein Betriebssystem schreiben möchtest, musst du auch überlegen, hier gibt es ebenfalls im Großen und Ganzen zwei Alternativen:

- Du nimmst den x86-PC, der mit extrem hoher Wahrscheinlichkeit bereits vor dir steht. Fast jeder programmiert für den x86-PC und du bekommst Unmengen an Beispielcode hier und im Internet. Dein Betriebssystem ist eins von vielen und im Forum oder im IRC wird dir fast jeder helfen können. Auf der anderen Seite ist die PC-Plattform nun schon über 30 Jahre gewachsen, einiges ist wild zusammengewürfelt und die einzelnen Komponenten benutzen teilweise sehr unterschiedliche Programmierparadigmen, je nach deren Alter. Du wirst dich mit seltsamen Dingen auseinander setzen müssen wie dem [Real-Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") bzw. [Protected-Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") samt zugehöriger Segmentierung oder den unterschiedlichen [Privilegstufen](https://github.com/lowlevel-eu/wiki/wiki/Ring "Ring"). Auch gibt es einige Hardwarekomponenten mehrfach (mit unterschiedlichem Alter und Funktionsumfang) wie z. B. [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") vs. [APIC](https://github.com/lowlevel-eu/wiki/wiki/Advanced-Programmable-Interrupt-Controller "APIC") oder [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") vs. HPET, da muss man sich oft überlegen, bis zu welchem Alter der x86-PCs das eigene Betriebssystem kompatibel sein soll, also welcher Umfang an Hardware (optional) unterstützt werden soll bzw. für das Betriebssystem als Voraussetzung gelten soll.
- Du nimmst eine andere Plattform. Das bedeutet mit hoher Wahrscheinlichkeit, dass erst mal Geld ausgegeben werden muss. Auch bist du dann ein Außenseiter und kaum jemand wird dir helfen können, wenn du mal auf (plattformspezifische) Probleme stößt, da bist du dann auf die (oft recht gute) Dokumentation (in Englisch) oder auf viele Versuche angewiesen. Dafür sind die meisten in Frage kommenden Plattformen recht gut "*aus einem Guss*" und auch sehr deutlich weniger komplex als der x86-PC. Es gibt auch deutlich weniger Stolperfallen und andere Merkwürdigkeiten. Ebenfalls sind die Programmierparadigmen für die einzelnen Hardwarekomponenten auf den Plattformen meist in sich stimmig und recht modern, die meisten alternativen Plattformen sind eben sehr viel jünger als der x86-PC. Wenn du ein Betriebssystem für Spielkonsolen oder SmartPhones entwickeln möchtest dann wirst du mehr mit den Sicherungsmechanismen der Hersteller als mit der Plattform als solches kämpfen, die Hersteller mögen es in der Regel gar nicht, wenn der *zahlende* Kunde die Geräte anders benutzen will, als der Hersteller sich das vorstellt.

Die Mitglieder der Lowlevel-Community entwickeln ihre Betriebssysteme in aller Regel für den x86-PC, Ausnahmen gibt es da fast keine. Auch (fast) das gesamte Wiki hier bezieht sich ausschließlich auf den x86-PC.

### Entwicklungsumgebung und Tools

Um dein eigenes Betriebssystem zu entwickeln, brauchst du ein paar Werkzeuge. Du musst dir eine Buildumgebung aufbauen (was je nach Betriebssystem unterschiedlich komplex ist), du brauchst einen Editor und einen Emulator. All das wird im **[ersten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung")** der Tutorial-Reihe "OS-Dev für Einsteiger" erklärt.

## Wo anfangen?

### Der Bootloader

Dein eigenes Betriebssystem möchte am Anfang irgendwie von der Festplatte oder Diskette in den Speicher geladen werden, bevor es irgendwas macht. Daher brauchst du einen Bootloader.

Hier gibt es die großen zwei Möglichkeiten, etwas fertiges zu nehmen oder selbst einen Bootloader zu schreiben. Ein guter Bootloader ist ein Projekt für sich, daher empfehle ich grundsätzlich, [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") zu benutzen und sich auf das eigentliche Betriebssystem zu konzentrieren. [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") lädt dir deinen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und möglicherweise weitere Module vom Dateisystem auf der Platte oder Diskette, initialisiert dir den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), bietet ein Bootmenü und einiges mehr. Eine detailiertere Erklärung warum hier GRUB empfohlen wird findet sich [hier](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader#warum-grub "Grand Unified Bootloader").

Die folgenden beiden Artikel werden dir bei den ersten Schritten mit [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") helfen:

- [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB")
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen") (Falls Du Windows benutzt, ist es vermutlich einfacher, ein vorhandenes GRUB-Image z.B. von [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur") zu nehmen und den Kernel durch den eigenen zu ersetzen)

Wenn du trotz diesen Vorteilen darauf bestehst, deinen Bootloader selbst zu schreiben – so sei es. In den ersten Ausgaben des [Magazins](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin") findest du die dazu nötigen Informationen. In den folgenden Abschnitten gehe ich allerdings davon aus, dass [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") benutzt wird. Du solltest also sicherstellen, dass du eine vergleichbare Umgebung herstellst – insbesondere, dass du im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") bist.

#### Äh ja, nochmal auf Deutsch bitte

Im **[vierten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-4-Hello-World "Teil 4 - Hello World")** der Reihe "OS-Dev für Einsteiger" wird genau erklärt, wie du dir einen einfachen Kernel in C und mit GRUB aufbaust. Du wirst auch auf etwas [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") stoßen. Solltest du kein Assembler beherrschen, keine Bange: Du brauchst nur ganz wenig für die Betriebssystementwicklung. Wenn du keinen Plan hast, wie du in Assembler programmierst, dann lies dir den **[zweiten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-2-Assembler-101 "Teil 2 - Assembler 101")** des Reihe "OS-Dev für Einsteiger" durch, dort bekommst du das benötigte Wissen, um den minimalen Asssembler-Teil zu verstehen.

### Hello World und weiter

Die allererste Aufgabe für ein neues Betriebssystem ist es selbstverständlich, ein "Hello world!" auf den Bildschirm auszugeben. Wenn du nach dem oben genannten Artikel vorgegangen bist, hast du diesen Schritt schon erreicht. Wenn nicht: Text gibst du aus, indem du in den Videospeicher schreibst. Er beginnt für den Textmodus an der Adresse 0xB8000 und enthält für jedes Zeichen (insgesamt 80x25) auf dem Bildschirm je zwei Bytes. Das erste enthält den ASCII-Code des Zeichens selbst, das zweite Attribute wie Farbe. Experimentiere am besten ein bisschen damit herum. (Ausführlicher steht es im Artikel [Textausgabe](https://github.com/lowlevel-eu/wiki/wiki/Textausgabe "Textausgabe"))

Hey, mein Kernel läuft und gibt was aus, vielleicht wäre jetzt der Grafikmodus...? Nein! Ein wesentlicher Grund dafür ist, dass du in der nächsten Zeit viele kritische Änderungen und dabei auch viele Fehler machen wirst. Du wirst daher um [Debugging](https://github.com/lowlevel-eu/wiki/wiki/Debugging "Debugging") nicht herumkommen. Am einfachsten geht das über Textausgaben, die leider im Grafikmodus nicht mehr ganz so leicht gehen.

Aber mit dieser Erkenntnis hast du auch schon eine schöne Aufgabe für den nächsten Schritt: Du brauchst Ausgaberoutinen, in C wäre das beispielsweise ein printf (die meistens etwas weniger mächtige Variante im Kernel wird übrigens gern printk oder kprintf genannt).

### Protected Mode

Wenn du GRUB benutzt, bist du zwar bereits am Anfang im Protected Mode, allerdings mit einem Standardsatz von Deskriptortabellen. Es wäre jetzt an der Zeit, das zu ändern.

Oh, du hast keine Ahnung, was du dir unter Deskriptortabellen vorzustellen hast? Lies dir am besten den Artikel zum Protected Mode durch – oder wenn du einen groben Überblick hast, kannst du auch direkt zum Artikel über die [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") übergehen. Wenn du Deinen Bootloader selbst schreibst, findest du dort auch Informationen, wie du selbst in den Protected Mode umschaltest. Außerdem ist das Protected-Mode-Tutorial auf den Seiten der FH Zwickau zu empfehlen.

- [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")
- [Umschalten in Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode")
- [Global Descriptor Table](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "Global Descriptor Table") (GDT)
- [Protected-Mode-Tutorial der FH Zwickau](http://www.fh-zwickau.de/doc/prmo/start.htm)

Was du zunächst machen musst, ist, eine GDT im Speicher aufzubauen. Mit der Beschreibung auf den genannten Seiten sollte das kein Problem darstellen (aber gräme dich nicht, wenn es nicht im ersten Versuch hinhaut – das ist für viele die erste Stelle, wo sie erst einmal eine Weile hängen).

Wenn du die GDT aufgebaut hast, kannst du sie anschließend laden. Das ist einer der wenigen Fälle, wo du tatsächlich Assembler brauchst. Wenn du C benutzt, könnte dir der Artikel über [Inline-Assembler mit GCC](https://github.com/lowlevel-eu/wiki/wiki/Inline-Assembler-mit-GCC "Inline-Assembler mit GCC") helfen. Ansonsten schlag in der Dokumentation deines Compilers nach, wie es dort funktioniert.

Anschließend musst du die Segmentregister neu laden, damit die GDT auch benutzt wird. An dieser Stelle zeigt sich dann, ob du es richtig gemacht hast. Wenn die Einträge in deiner GDT falsch sind, und beispielsweise das Codesegment nicht korrekt ist, wirst du mit höchster Wahrscheinlichkeit einen GPF auslösen. GPF steht übrigens für *General Protection Fault* und ist dir vielleicht als *Allgemeine Schutzverletzung* besser bekannt. Weil du noch keine [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception") verarbeitest, wird das zu einem *Triple Fault* führen, was auf einem echten PC einen Reset bewirkt.

### Interrupts

Hast du die GDT gemeistert? Glückwunsch. Aber freu dich nicht zu früh, wir haben noch mehr Tabellen im Angebot. Die zweite Tabelle, die du unbedingt benötigst, ist die Interrupt Descriptor Table ([IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT")). Wenn irgendein Stück Hardware melden möchte, dass irgendetwas passiert ist (z.B. eine Taste gedrückt wurde), schickt es im Allgemeinen einen [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") mit einer mehr oder weniger eindeutigen Nummer. In der IDT weist du jedem Interrupt eine Funktion in deinem Kernel zu, die aufgerufen wird, wenn der Interrupt ankommt.

Auch zur IDT kannst du die im vorigen Abschnitt verlinkten Seiten befragen.

Neben den genannten Hardwareinterrupts gibt es noch weitere. Die wichtigsten davon sind [Exceptions](https://github.com/lowlevel-eu/wiki/wiki/Exception "Exception"), die aufgerufen werden, wenn etwas schiefgeht (z.B. Division durch Null oder ein Speicherzugriff ohne Berechtigung) und Softwareinterrupts, die von einem Programm ausgelöst werden, z.B. um Funktionen des Kernels aufzurufen.

Wenn du die IDT fertig eingerichtet hast, kannst du sie am besten testen, indem du entweder eine Exception provozierst oder einen Softwareinterrupt auslöst. Bevor du die Hardwareinterrupts mit dem Assemblerbefehl sti anschaltest, solltest du nämlich erst noch den [PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") programmieren, so dass die IRQs (das sind genau die Hardwareinterrupts) beispielsweise auf die Interrupts 0x20 bis 0x2f legst (bis 0x1f liegen schon die Exceptions und du willst IRQs ja von Exceptions unterscheiden können).

- [Programmable Interrupt Controller](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "Programmable Interrupt Controller")

Wenn du auch Hardwareinterrupts am Laufen hast, hast du die ersten großen Hürden genommen. Für diejenigen unter uns, die gerne etwas sehen und irgendwas zum Spielen brauchen, wäre das ein guter Zeitpunkt, einfach mal einen Tastaturtreiber zu schreiben und ein bisschen was auszuprobieren. Es kommen noch genug schwere Sachen, bis dein Produkt sich zu Recht ein Betriebssystem nennen kann, aber hey, wenn ich zwei Zahlen eingeben kann und die werden addiert – das ist doch schonmal ein Erfolgserlebnis, oder? Mich hat das jedenfalls motiviert.

### Hm, ja, anschauliches Beispiel?

Im **[fünften Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-5-Interrupts "Teil 5 - Interrupts")** der Reihe "OS-Dev für Einsteiger" wird das Einrichten einer GDT sowie das Einrichten einer IDT und das Aktivieren von Interrupts und deren Behandlung noch einmal erklärt. Wenn du die Artikel zur [GDT](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") und [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") gelesen hast, wird dir schnell der Zusammenhang klar.

## Der eigentliche Kernel

Wenn du bis hierhin gekommen bist, hast du mittlerweile etwas, was sich Kernel nennt. In Wirklichkeit hast du aber noch nicht besonders viel von den ganzen Funktionen, die ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") bieten muss. Du hast die Initialisierung geschafft, bei der du noch nicht besonders viel Auswahl hast. Richtig interessant wird es jetzt, denn jetzt kannst Du viele verschiedene Wege wählen, die eigentliche Funktionalität deines Kernels umzusetzen.

### Architekturen

Unter der *Architektur* deines Betriebssystem ist die Art und Weise zu verstehen, wie die Komponenten deines Systems zusammenspielen. Bevor du anfängst, Code für die eigentliche Funktionalität des Kernels zu schreiben, solltest du dir klar sein, in welche Richtung die Reise gehen soll.

- Die allerwichtigste Entscheidung, die das Aussehen deines Betriebssystems am schwerwiegendsten beeinflussen wird, ist die Entscheidung zwischen [monolithischem Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") (die Hardwaretreiber sind alle im Kernel) und [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") (der Kernel macht nur das notwendigste, Treiber sind eigenständige [Userspace](https://github.com/lowlevel-eu/wiki/wiki/Userspace "Userspace")-Prozesse) – oder natürlich beliebiger Mischformen davon, z.B. ein modularisierter Monolith wie [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux").
- Besonders beim Microkernel ist eine zentrale Frage, wie die [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") aussehen soll. Auch bei einem monolithischen Kernel ist es kein Fehler, sich diese Frage zu stellen, auch wenn sie eher nachrangig ist.
- Wie soll die Schnittstelle der Programme zum Kernel aussehen? (z.B. [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall"))

### Die Aufgaben des Kernels

Bevor du dir anschaust, welche Funktionen dein Kernel bieten soll, versichere dich, dass du weißt, was ein [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") überhaupt ist. Ja, klar, er ist der Kern des Betriebssystems. Und weiter? Seine zentrale Aufgabe ist es, die Ressourcen des Systems zu verwalten – z.B. den laufenden Programmen Speicher zuzuteilen.

Im Allgemeinen wird für Betriebssysteme im [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") ein Modell verwendet, in dem der Kernel in [Ring](https://github.com/lowlevel-eu/wiki/wiki/Ring "Ring") 0 (Kernel Mode) und alle Programme in Ring 3 (User Mode) laufen. Als grobe Richtung kannst du dir merken, dass der Kernel alles das ist, was in Ring 0 läuft. Wenn ein User-Mode-Programm Betriebssystemfunktionen benötigt (z.B. mehr Speicher), ruft es den Kernel auf.

Was sind nun also die Funktionen, die ein Kernel im Allgemeinen bietet?

- [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung"): Programme und höchstwahrscheinlich auch der Kernel selbst müssen zur Laufzeit dynamisch Speicher reservieren können. Die Speicherverwaltung im Kernel arbeitet üblicherweise nicht mit beliebigen anforderbaren Größen, sondern mit Blöcken von 4 Kilobytes, sogenannten *Speicherseiten* (engl. *Pages*). Man unterscheidet dabei zwischen [physischer](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#physische-speicherverwaltung "Speicherverwaltung") und [virtueller Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung#virtuelle-speicherverwaltung "Speicherverwaltung").
  - Ein anschauliches Beispiel zur Implementierung einer physischen Speicherverwaltung wird im **[siebten Artikel](https://github.com/lowlevel-eu/wiki/wiki/Teil-7-Physische-Speicherverwaltung "Teil 7 - Physische Speicherverwaltung")** der Reihe "OS-Dev für Einsteiger" gegeben
- [Prozessverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Prozessverwaltung "Prozessverwaltung"): Ein Betriebssystem hat diese Bezeichnung nur verdient, wenn es Programme ausführen kann. Zur Prozessverwaltung gehören Funktionen wie das Starten und Beenden von Prozessen, aber im weiteren Sinne auch [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking"), also das Umschalten zwischen den einzelnen Prozessen. Neben [Prozessen](https://github.com/lowlevel-eu/wiki/wiki/Prozess "Prozess") möchtest du eventuell auch [Threads](https://github.com/lowlevel-eu/wiki/wiki/Prozess#threads "Thread") unterstützen.
- [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation"): Je nach Architektur des Betriebssystem extrem wichtig bis erstmal völlig nebensächlich. Es geht dabei darum, dass zwei Programme Informationen austauschen können, z.B. durch Senden von Nachrichten oder Aufruf von Funktionen des anderen Programms.
- [Hardwaretreiber](https://github.com/lowlevel-eu/wiki/wiki/Treiber "Treiber"): Jeder Kernel enthält auch Hardwaretreiber. Je nach Architektur gehören dabei alle, manche oder so gut wie keine Treiber zum Kernel.
- Den Bootprozess anstoßen. Nachdem der Kernel sich selbst initialisiert hat, lädt er in irgendeiner Form ein erstes Programm (unter Linux *init*) und startet es.

Im Umkehrschluss gehören eine [Shell](https://github.com/lowlevel-eu/wiki/wiki/Shell "Shell"), [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") oder sonstige Anwendungsprogramme **nicht** in den Kernel! Eine Shell im Kernel ist vielleicht akzeptabel für eine frühe Testphase, um überhaupt einmal etwas laufen zu sehen, aber es ist auf Dauer kein tragfähiges Konzept. (Einer der Gründe dafür: Erinnerst du dich an den Absatz über die Ringe oben? Was im Kernel liegt, hat Kernel-Mode-Privilegien, und ein Grundsatz für sichere Software ist, nie Privilegien zu haben, die man nicht braucht)

### Schnittstelle zum Userspace

Auch der tollste Kernel mit [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking")-Unterstützung bringt dir natürlich herzlich wenig, wenn die laufenden Programme nicht mit dem Benutzer interagieren können. Um den Programmen, die ja in einem eigenen Adressraum laufen und meist keinen direkten Zugriff auf die Hardware haben, diese Möglichkeit zu bieten, muss der Kernel eine entsprechende Schnittstelle, üblicherweise in Form von [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall"), anbieten. Wie diese Schnittstelle genau aussieht, hängt von deiner gewählten Architektur ab. Bei einem Monolithen wird die Schnittstelle eher breit ausfallen, und beispielsweise Funktionen für das Arbeiten mit Dateien mitbringen, während bei einem Mikrokernel vor allem die Funktionen für die [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") im Zentrum stehen werden.

#### Da habt ihr doch sicher auch was in eurer Reihe, oder?

Na klar. Im **[sechsten Teil](https://github.com/lowlevel-eu/wiki/wiki/Teil-6-Multitasking "Teil 6 - Multitasking")** der Reihe "OS-Dev für Einsteiger" wird das Implementieren von Multitasking per [TSS](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "TSS") anschaulich und mit Codebeispielen erklärt.

### Treiber

Irgendwann wirst du vermutlich auf die Idee kommen, irgendwas von einer [Diskette](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC") oder [Festplatte](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") lesen zu wollen. Dafür werden zwei Treiber benötigt: einer für das [Diskettenlaufwerk](https://github.com/lowlevel-eu/wiki/wiki/Floppy-Disk-Controller "FDC") bzw. die [Festplatte](https://github.com/lowlevel-eu/wiki/wiki/AT-Attachment "ATA") und ein [Dateisystemtreiber](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem"). Wie sich die Treiber in dein System einfügen sollen, hast du bei der Wahl deiner Architektur ja schon grob entschieden. Jetzt ist es an der Zeit die Details festzulegen. Für die Treiber musst du auch erstmal eine Schnittstelle definieren und dir genau überlegen, wie die Kommunikation zwischen Clients und den Treibern ablaufen soll. Dabei ist es sicher keine schlechte Idee, ein bisschen in den Schnittstellen von anderen [Betriebssystemen](https://lowlevel-eu.github.io/wiki/pages/1649/index.html "Kategorie:Betriebssystem") zu stöbern. Weiter könntest du dir auch überlegen, dir [CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI"), das von der Lowlevel-Community entwickelt wird, genauer anzusehen, denn damit sparst du unter Umständen viel Zeit und Ärger.

|  |  |  |
| ----- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|  | **Navigation** | [Teil 1 - Entwicklungsumgebung](https://github.com/lowlevel-eu/wiki/wiki/Teil-1-Entwicklungsumgebung "Teil 1 - Entwicklungsumgebung") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9965/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1619/index.html)

<!-- MediaWiki page 1619; revision 9965; parent 9756; 2011-07-22T08:45:05Z -->
