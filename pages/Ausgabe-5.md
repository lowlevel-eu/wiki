# Ausgabe 5

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 4](Ausgabe-4 "Ausgabe 4") | **Navigation** | [Ausgabe 6](Ausgabe-6 "Ausgabe 6") » |

## Vorwort

Hallo erstmal :-)

Es hat mal wieder viel zu lange gedauert, bis diese Ausgabe erschienen ist, doch ich hoffe, dass die zusätzlichen Stunden, die ich investiert habe, sich lohnen werden, denn die letzte Ausgabe schien ja nicht sehr beliebt zu sein...

Wie auch immer. Ich freue mich, dass an dieser Ausgabe sehr viele Leute (außer mir und Phil) mitgearbeitet haben und ich auch sonst viel Feedback erhalte. Da wäre zum Beispiel Lizer, der drei hervorragende Tutorials geschrieben hat (in dieser Ausgabe sind zwei davon abgedruckt), aber auch Icy Wolf, der jetzt parallel zu Phil seine Kommentare abgibt und Neo3, der nun für die News zuständig ist.

Achja, bevor ich es vergesse: ein riesen Dankeschön an jaboe, der Tim Robinsons Artikel über [Kernel](Kernel "Kernel")-Entwicklung in [C](C "C") übersetzt hat!

## News

### Über mich

Ich bin 19 Jahre alt und habe schon meine erste Anlehre als Elektroausrüster bestanden, neben dem habe ich ein großes Interesse an Elektronik und PC-Programmierung. Ich habe mit 13 Jahren angefangen, HTML-Web-Seiten zu basteln. Nach zwei Jahren suchte ich mir aber schon eine neue Herausforderung und begann mit VB 6. Als MS dann auf VB.net umzog, ging ich natürlich mit, zwischendurch hab ich mich aber auch mit anderen Programmiersprachen beschäftigt, wie [Pascal](Pascal "Pascal") und [C++](C%2B%2B "C++"), blieb dann doch bei VB.net.

Mich hat das OS-Programmieren eigentlich erst so richtig gepackt vor etwa einem Monat und da ich von einem Kollegen (der eine Elektroniker-Lehre macht) etwas von [Assembler](Assembler "Assembler") gehört habe und auch erfahren habe, das man damit CPUs programmiert, hab ich mich auf die suche im Internet gemacht nach OS-Programmierung mit ASM, fand dann auch einige Themen in Foren darüber und erfuhr, dass ich zuerst einen Bootloader in ASM proggen muss, damit ich da drauf aufbauen kann mit dem Kernel. Und bin schlussendlich hier bei Lowlevel gelandet.

### Windows Longhorn

MS mit seinem Windows Longhorn, das angeblich Ende 2005 auf den Markt kommen soll.

[Hier](http://www.microsoft.com/germany/ms/msdnbiblio/pdc2003/longhorn.htm) werden schnell die wichtigsten Neuerungen von Longhorn angekratzt, wie das User Interface (Avalon), die Kommunikation (Indigo) und das revolutionäre Dateisystem WinFS.

### Apple Mac OS X Panther

<http://www.apple.com/de/macosx/>

Informiert euch selbst darüber, ist alles auf Deutsch ;-)

## [Kernel](Kernel "Kernel")-Entwicklung in [C](C "C")

Nun gut - eure einzige Erfahrung mit dem Programmieren von Betriebssystemen dürfte das Schreiben eines [Bootloaders](Bootloader "Bootloader") in [Assembler](Assembler "Assembler") sein. Wenn ihr ihn von Grund auf geschrieben habt, dann dürfte es einige Wochen gedauert haben (mindestens), und ihr wünschtet, es gäbe einen einfacheren Weg. Nun: hier ist er, besonders wenn ihr bereits mit der [C](C "C")-Programmiersprache vertraut seit. Wenn ihr noch nicht mit [C](C "C") vertraut sein solltet (und ihr aber eine andere Highlevel-Sprache beherrscht), lernt es, denn es ist es wert, weil es einfach ist, euren [Kernel](Kernel "Kernel") in [C](C "C") zu programmieren. Wichtig ist vor allem, die richtigen Informationen zu bekommen und die richtigen Tools zu haben.

### Die Programmiersprache [C](C "C")

[C](C "C") wurde eigentlich als Low-Level-HLL konzipiert (Unix-[Kernels](Kernel "Kernel") wurden traditionell in [C](C "C") geschrieben) und seine Hauptvorteile waren seine Portabilität und seine Nähe zur Maschine. Es ist einfach, nicht-portable Programme in [C](C "C") zu schreiben, aber mit etwas Wissen ausgestattet, ist es möglich, mit Portabilität im Hintergedanken zu programmieren. Es gibt nichts, was kompiliertem [C](C "C")-Code von [Assembler](Assembler "Assembler") unterscheidet - in Wahrheit ist euer Assembler nicht mehr als ein Low-Level-Compiler, einer, der die Angaben direkt in maschinenlesbare Opcodes übersetzt. Wie jede andere High-Level-Sprache auch, abstrahiert [C](C "C") den Code mehr und trennt euch von der Maschine; dennoch beschränkt euch [C](C "C") nicht zu sehr bei dem Code, den ihr programmiert.

### Tools

Es gibt zwei Hauptkomponenten, die in die Erzeugung von maschinenlesbarem Code aus [C](C "C")-Quelltext eingebunden sind: ein Compiler und ein Linker. Der Compiler macht die meiste Arbeit und ist verantwortlich für die Verwandlung von [C](C "C")-Quellcode in Objektdateien - das sind die Dateien, die Maschinencode und Daten enthalten, aber für sich selbst kein vollständiges Programm darstellen. Viele [C](C "C")-Compiler besitzen die Möglichkeit, direkt aus dem Quelltext eine ausführbare Datei zu erzeugen, in diesem Fall ruft der Compiler den Linker intern auf. Der Linker bündelt alle Objektdateien, setzt die Referenzen, die sie sich gegenseitig zuweisen, leitet sie um (relocation) und erzeugt eine ausführbare Datei.

Die meisten Linker arbeiten mit den Quelldateien von jedem Compiler, solange dieser kompatible Objektdateien erzeugt. Das erlaubt euch zum Beispiel, das meiste von eurem [Kernel](Kernel "Kernel") in [C](C "C"), aber einige maschinenabhängige Teile in [Assembler](Assembler "Assembler") zu schreiben.

Zum Entwickeln würde ich irgendein Paket empfehlen, welches den GNU GCC-Compiler und den ld-Linker enthält, denn:

- sie sind kostenlos und Open-Source
- ld unterstützt faktisch jedes bekannte Format
- es sind von gcc Versionen für jeden bekannten Prozessortyp erhältlich

GNU-Pakete sind für verschiedene Betriebssysteme erhältlich; der MS-DOS-Port heißt DJGPP und ein guter Windows-Port ist Cygwin. Alle Linux-Distributionen sollten die GNU-Tools enthalten. Denkt daran, dass jeder Port im Allgemeinen nur die Generation von Programmen für die Plattform unterstützt, auf der auch läuft (sofern ihr nicht den Compiler und den Linker rekompiliert), und die angebundenen Laufzeitbibliotheken haben im Allgemeinen nur einen geringen Nutzen für die Betriebssystemprogrammierer. DJGPP-Programme benötigen DOS, um zu funktionieren und Cygwin-Programme sind auf die cygwin1.dll angewiesen, welche wiederum die Win32-API anspricht. Es ist jedoch möglich, die vorgegebene Laufzeitbibliothek zu ignorieren und eure eigene zu schreiben, und das ist es, was wir tun werden. Wenn ihr unter Windows programmiert, ist es ratsam, Cygwin zu benutzen (patcht oder erzeugt ihn neu, um ELF zu unterstützen, wenn es gewünscht wird) denn er ist um einiges schneller als DJGPP und erlaubt es, von Grund auf lange Kommandozeilen und Dateinamen zu verwenden.

**Wichtig!** Denkt daran, dass Cygwins Ausgabe von flachen Binärdateien zur Zeit nicht richtig funktioniert.

Einige andere Tools sind nützlich bei der Betriebssystementwicklung. Das GNU-binutils-Paket (gebündelt mit gcc und ld) schließt das passende objdump-Programm ein, welches euch die Möglichkeit gibt, die interne Struktur eurer ausführbaren Dateien zu betrachten und sie zu deassemblieren - unerlässlich, wenn ihr Loader programmiert und komplizierte Dinge probiert. Ein möglicher Nachteil bei der Nutzung eines generischen Linkers ist, daß er eure selbstentwickelten ausführbaren Formate nicht unterstützen wird. Wie auch immer, es ist selten von Nutzen, ein eigenes ausführbares Format zu entwickeln: es gibt genug von ihnen.

Unix ELF und Windows PE neigen dazu, am populärsten unter den Betriebssystementwicklern zu werden, hauptsächlich wegen der guten Unterstützung der beiden durch die verfügbaren Linker. ELF scheint mehr in Amateur-Kerneln verwendet, hauptsächlich wegen seiner Einfachheit, obwohl PE leistungsfähiger (und infolgedessen komplexer) ist. Beide sind sehr gut dokumentiert. COFF wird ebenfalls in einigen Projekten verwandt, obwohl ihm die grundlegende Unterstützung von Eigenschaften wie dynamisches Linken fehlt. Eine Alternative für einfache Kernels ist das flache Binärformat (das heißt kein wirkliches Format). In diesem Fall schreibt der Linker rohen Code und Daten in die Ausgabedatei, und das Ergebnis ist ähnlich dem Format der COM-Dateien in MS-DOS, obwohl die resultierende Datei größer sein kann als 64kB und 32-Bit Opcodes verwenden kann (vorausgesetzt, der Loader aktiviert vorher den Protected-Mode).

Ein Nachteil sämtlicher etablierter IA-32-Compiler ist, dass sie von einem flachen 32-Bit-Adressraum ausgehen, in dem CS, DS, ES und SS eine gemeinsame Basisadresse haben. Da sie keine far-Pointer (48-Bit seg16:ofs32) benutzen, erschweren sie das Schreiben von Code für ein segmentiertes Betriebssystem. Programme in einem segmentierten Betriebssystem, welches in [C](C "C") geschrieben wurde, sind auf sehr viel Assemblercode angewiesen und wären sehr viel weniger effizient als Programme, die für ein "flaches" Betriebssystem geschrieben worden sind. Nun, während des Schreibens, stellte Watcom in Aussicht, ihren Watcom-Compiler zu veröffentlichen, der angeblich far-Pointer im 32-Bit Protected Mode unterstützen würde.

Hier sind einige weitere Warnungen zum Gebrauch von gcc und ld (obwohl das potentiell für jeden anderen Compiler / Linker zutrifft). Erstens setzt gcc gern die Stringliterale (Konstanten vom Stringtyp), die von Funktionen genutzt werden, einfach vor den Funktionscode. Normalerweise ist das kein Problem, aber ein paar Leute verheddern sich bei dem Versuch ihre Kernel "Hello, world" ausgeben zu lassen. Beachtet dieses Beispiel: \<c\> int main(void)

       {
           char *str = "Hello, world", *ch;
           unsigned short *vidmem = (unsigned short*) 0xb8000;
           unsigned i;
           
           for (ch = str, i = 0; *ch; ch++, i++)
               vidmem[ i ] = (unsigned char) *ch | 0x0700;
           
           for (;;)
               ;
       }</c>

Dieser Quelltext soll die Zeichenkette "Hello, World" in den Videospeicher schreiben, in weißem Text auf schwarzem Hintergrund, in der oberen liken Ecke des Bildschirms. Jedoch wird gcc, wenn es kompiliert ist, den Literalstring "Hello, world!" genau vor dem Code für main ausgeben. Wenn das nun als flaches Bnärformat gelinkt und ausgeführt wird, dann beginnt die Ausführung dort, wo sich der String befindet und die Maschine wird wahrscheinlich abstürzen. Es gibt ein paar Möglichkeiten, das zu umgehen:

- Schreibt eine kurze Funktion, die lediglich main() aufruft und anhält. Auf diesem Weg enthält die erste Funktion des Programmes keine Literalstrings.
- Benutzt die gcc-Option -fwritable-strings. Das wird gcc dazu veranlassen, die Literalstrings in die Datensektion der ausführbaren Datei zu schreiben, weg von jeglichem Code.

Von diesen Möglichkeiten ist wahrscheinlich die Erste vorzuziehen. Ich schreibe meinen Startpunkt vorzugsweise in Assembler, wo ich den Stack einrichten kann und das BSS auf Null setzen kann, bevor ich main() aufrufe. Ihr werdet feststellen, dass normale Usermode-Programme das auch tun: der wahre Startpunkt ist eine kleine Routine in der C-Bibliothek, welche die Umgebung einrichtet, bevor sie main() aufruft. Normalerweise ist sie als crt0-Funktion bekannt.

Die andere Hauptschwierigkeit betrifft Objektdateiformate. Es gibt zwei Varianten des 32-Bit COFF-Formates: eins wird von Microsofts Win32-Tools genutzt, das Andere von Rest der Welt. Sie sind nur geringfügig unterschiedlich und Linker, die das eine Format erwarten werden glücklicherweise auch das Andere linken. Die Unterschiede machen sich bei der Adressenverlagerung bemerkbar: wenn ihr Code in, sagen wir NASM, schreibt und ihn mit dem Microsoft Linker zusammen mit einigen Modulen, die mit Virtual C++ kompiliert wurden, linkt, dann werden die Adressen am Ende falsch ausgegeben. Es gibt keinen echten Workaround dafür, allerdings erlauben es euch glücklicherweise die meisten Tools, die mit dem PE-Format arbeiten, Dateien im Win32-Format auszugeben: NASM hat seine -f wn32 Option, und Cygwin besitzt das pei-i386 Ausgabeformat.

### Die Laufzeitbibliothek

Ein Hauptbestandteil beim Programmieren eines Betriebssystems ist das Neuschreiben der Laufzeitbibliothek, auch bekannt als libc. Das liegt darin begründet, dass die Laufzeitbibliothek der am meisten betriebsystemabhängige Teil des Compilerpaketes ist: die [C](C "C")-Laufzeitbibliothek stellt genug Funktionalität bereit, die es euch ermöglicht, portierbare Programme zu schreiben, die inneren Abläufe jedoch sind abhängig von dem eingesetzten Betriebssystem. Tatsächlich benutzen Compileranbieter oft unterschiedliche Laufzeitbibliotheken für das selbe Betriebssystem: Microsoft Visual C++ stellt verschiedene Bibliotheken für die verschiedenen Kombinationen aus debug/multi-threated/DLL bereit, und die älteren MS-DOS-Compiler boten Laufzeitbibliotheken für bis zu sechs unterschiedliche Speichermodelle an.

Bis auf weiteres sollte es ausreichend sein, nur eine Laufzeitbibliothek zu schreiben (obwohl das Schreiben einer Makefile, die eine Auswahl an dynamischem oder statischem Linken anbietet oft nützlich ist). Ihr solltet euch zum Ziel setzen, die Bibliothek so zu replizieren, wie es nach dem ISO-C-Standart vorgegeben ist, denn es wird die Portierung von Programmen auf euer Betriebssystem einfacher machen.

Es macht es wesentlich einfacher, Code für Bibliotheken zu schreiben, wenn ihr Quelltext von bestehenden Implementierungen in die Hände bekommt, besonders wenn die Umgebung der Bibliothek vergleichbar mit der ist, in der ihr entwickelt. Es gibt viele [C](C "C")-Funktionen, welche betriebssystem- und plattformabhängig sind: zum Beispiel kann das meiste der string.h und wchar.h direkt kopiert werden. Umgekehrt gibt es viele Funktionen, die euer Compiler anbieten kann, die aber keinen Sinn für euer Betriebssystem haben: viele DOS-Compiler bieten eine bios.h-Headerdatei an, die den Zugriff auf das PC-BIOS ermöglicht. Solange ihr keinen VM86-Monitor in euren Kernel implementiert, werdet ihr nicht in der Lage sein, BIOS-Funktionen direkt aufzurufen. Allerdings sind solche Funktionen Erweiterungen und haben als solche Namen mit einem Unterstrich (z.B. \_biosdisk()) am Anfang. Ihr habt nicht die Verpflichtung, diese Erweiterungen zu implementieren, und ihr könnt eure eigenen Erweiterungen festlegen, wenn ihr wollt, solange ihr ihnen einen Namen mit Unterstrich am Anfang gebt.

Andere Funktionen der C-Bibliothek sind abhängig von der Unterstützung durch den Kernel: das meiste der stdio.h ist auf das Vorhandensein mehrer Arten von Dateisystemen angewiesen, selbst wenn printf() eine Zieladresse für die Ausgabe benötigt. Da wir gerade bei printf() sind: die meisten Implementierungen von OpenSource-C-Bibliotheken definieren eine generische printf()-Engine, da die selbe Funktionalität an vielen Stellen benötigt wird (printf(),fprintf(), sprintf() und den v-,w-, und vw-Versionen dieser Funktionen). Ihr solltet in der Lage sein, diese allgemeine Engine zu herauszufiltern und sie für eure Eigene zu verwenden, oder zumindest versuchen, sie zu emulieren: schreibt eine Funktion, die einen Formatstring akzeptiert und eine Liste mit Argumenten, die ihre Ausgabe an ein abstraktes Interface weitergibt (entweder eine Funktion oder eine gepufferten Stream).

Obwohl eine komplette Laufzeitbibliothek am nützlichsten ist, wenn es darum geht, Benutzerapplikationen zu schreiben und zu portieren, ist es ebenfalls dienlich, eine gute Unterstützung der Laufzeitbibliothek durch den Kernel zu haben. Häufig genutzte Routinen einzubinden macht das schreiben von Kernelcode schneller und einfacher und es macht den entstehenden Kernel kleiner, da allgemeine Routinen nur einmal eingebunden sind. Es ist ebenso ein gutes Verfahren, solche Routinen Treiberprogrammierern zugänglich zu machen, um sie vor der Einbindung allgemeiner Routinen in ihren (binären) Treibern zu bewahren.

### OS-spezifische Unterstützung

[C](C "C") ist als Kernelsprache nicht perfekt: offensichtlich gibt es keine standardisierte Möglichkeit, den Zugriff auf die Funktionen einer Maschine zu erlauben. Das bedeutet, dass es oft notwendig ist zu Inline-Assembler zurückzugreifen, oder Teile in Assembler zu programmieren und sie mit der Compilerausgabe zur Linkzeit zu linken. Inline-Assembler ermöglicht es euch, Teile von [C](C "C")-Funktionen in [Assembler](Assembler "Assembler") zu schreiben und wie gewohnt auf die Variablen von C-Funktionen zuzugreifen: der Code, den ihr schreibt, wird in den Code, den der Compiler generiert, eingefügt. Die Unterstützung von Inlineassembler variiert unter verschiedenen Compilern, wenn ihr die AT+T-Syntax durchhaltet, ist gcc der Beste unter den PC-Compilern. Obwohl Visual C++ und Borland C++ beide eine vertrautere Intel-Syntax verwenden, sind ihre Inlineassembler nicht genauso stark integriert mit dem Rest der Compiler. Gcc zwingt euch zu einer esoterischen Syntax, aber erlaubt es euch, jegliche C-Ausdrücke als eine Eingabe an einen Assemblerblock zu verwenden und die Ausgaben überall zu platzieren.

Der resultierende Assembler ist also besser mit dem Optimierer integriert als in den Compilern von Borland und Microsoft: zum Beispiel erlaubt gcc es euch genau anzugeben, welche Register als Resultat eines Assemblerblockes verändert werden. Einiger Assemblercode wird auch im Usermode benötigt, wenn ihr Softwareinterrupts zum Aufrufen von Kernel-Syscall verwendet. Ihr könntet die Interruptaufrufe direkt im Code der C-Bibliothek platzieren (so wie es MS-DOS-Bibliotheken tun),oder eine seperate Bibliothek mit einer Funktion für jeden Aufruf erzeugen und normal darauf verlinken (so wie es Windows NT mit der ntdll.dll macht). Es dürfte auch Sinn machen die betriebssystemabhängige Schnittstelle in eine sprachunabhängige Bibliothek einzufügen, so dass Programme, die in verschiedene Sprachen geschrieben wurden die gleiche Betriebssystembibliothek benutzen können. Das ermöglicht es Leuten, Programme in anderen Sprachen als in C zu schreiben, oder in Sprachen, die keine C-Bindungen erlauben.

### [C++](C%2B%2B "C++") im [Kernel](Kernel "Kernel")

Über die Nutzung von [C++](C%2B%2B "C++") im [Kernel](Kernel "Kernel") variieren die Meinungen: die meisten Linuxkernelprogrammier halten sich davon fern, während einige Leute ganze Betriebssysteme in [C++](C%2B%2B "C++") entwickelt haben. Ich halte mich an [C](C "C"), obwohl ich keinen Grund sehe, warum ihr [C++](C%2B%2B "C++") nicht benutzen solltet, solange ihr wisst, was ihr tut. Eine Sache, über die ihr euch klar sein solltet ist, das ihr zum Schreiben eines [C++](C%2B%2B "C++")-[Kernels](Kernel "Kernel") ein bisschen mehr Code für das Gerüst benötigt, und einige [C++](C%2B%2B "C++")-Funktionen sind tabu für euch (solange ihr nicht den benötigten Code für die Unterstüung schreiben könnt).

Als allererstes werdet ihr die new- und delete-Operatoren programmieren müssen. Das ist einfach, wenn ihr bereits malloc() und free() geschrieben habt: new und delete können Ein-Zeilen-Funktionen sein, die jede von ihnen aufruft. Wenn ihr globale Instanzen von Klassen haben wollt, müsst ihr einigen Code in die Startup-Routine einfügen, um jeden ihrer Konstruktoren aufzurufen. Die Art wie das getan wird, unterscheidet zwischen den Compilern, so dass es das Beste ist, die Laufzeitbibliothek eures Compilers durchzusuchen um zu sehen, wie der Hersteller es gemacht hat; versucht in Dateien mit Namen wie crt0.c zu suchen. Ihr werdet vermutlich atexit() implementieren müssen, da der Compiler wahrscheinlich Code ausgeben wird, der atexit() benutzt, um globale Destruktoren von Objekten aufzurufen, wenn das Programm beendet wird. Wiedereinmal wird es von dem Compiler, den ihr verwendet, abhängen und für welches Betriebssystem auch immer der Compiler ausgelegt ist.

Normalerweise würde ich das Aufräumen von beidem, Exceptionhandling und großen Virtuellen Klassen, im Kernel steuern. Exceptionhandling führt gewöhnlich zu unnötigem Aufblähen, und das Aufrufen von massenhaft virtuellen Funktionen führt zu unnötigen Umleitungen und behindert den Optimierer. Errinert euch, euer Kernel sollte so effizient wie möglich sein, auch zum Nachteil eines schönen Designs, wenn notwendig.

Ein Betriebssystem in einer Sprache wie [C](C "C") zu schreiben, kann wesentlich produktiver sein, als es komplett in [Assembler](Assembler "Assembler") zu programmieren, insbesondere wenn ihr bereit seit auf die geringfügigen Geschwindigkeitsvorteile, die [Assembler](Assembler "Assembler") ermöglicht, zu verzichten. Es sind freie Compiler verfügbar, so wie gcc, die das Schreiben von [Kernelcode](Kernel "Kernel") verhältnismäßig einfach machen, und die Nutzung von C wird sich auf lange Sicht auszahlen.

## Programmierung eines [GRUB](Grand-Unified-Bootloader "GRUB")-kompatiblen [Kernels](Kernel "Kernel")

### Vorwort

Nun gut, erstmal möchte ich den Leser recht herzlich begrüßen. Ich hoffe, dass alle Sonderzeichen (Umlaute, etc.) korrekt dargestellt werden und dieser Text auch ansonsten in Ordnung ist. Nun zum Rechtlichen. Dieser Text darf gerne von jedermann verbreitet werden, so lange damit kein Geld verdient wird. Außerdem werde ich stinksauer, wenn jemand im Text rumpfuscht. Wenn also jemand Fehler entdeckt oder sonst was auszusetzen hat, bitte einfach ein Mail schreiben (lizer@gmx.net). Ansonsten ist noch zu sagen, dass sich dieser Text hauptsächlich an OS-Developer richtet. Ich gehe also davon aus, dass ich hier keine Begriffe erklären muss. Gut, das wars auch schon. Viel Spaß!

Dann mal los. Um einen [Kernel](Kernel "Kernel") zu schreiben, der von [GRUB](Grand-Unified-Bootloader "GRUB") problemlos als solcher erkannt und geladen werden kann, muss man im Grunde nur eins berücksichtigen, nämlich dass der Mutliboot Header vorhanden ist, und zwar an der richtigen Stelle. Zunächst einmal eine Auflistung aller Komponenten des Headers.

1.  **Die "magische Zahl"** Sie leitet den Header ein und teilt so dem Loader mit, was er zu erwarten hat. Die Zahl: 0x1BADB002.
2.  **Die Flags** Sie sagen dem Loader, was von ihm erwartet wird. Die ersten 16 Bits \[0..15\] stellen die "Bedingungen" dar. Wenn also ein Bit gesetzt ist, der Bootloader aber die entsprechende Erwartung des Kernels nicht erfüllen kann, bricht der Loader den Bootvorgang ab. Die hinteren 16 Bits \[16..31\] nenne ich jetzt mal die "Vorlieben" des Kernels. Sie stellen Erwartungen an den Bootloader, wie auch die ersten 16 Bits; wenn der Bootloader diesen hier aber nicht genügen kann, ist das nur halb so schlimm - es wird trotzdem weiter geladen.
3.  **Die Checksumme** Wird benötigt, um den Header zu validieren. Sie wird folgendermaßen berechnet: 0x1BADB002 + FLAGS + CHECKSUM = 0. Sieht zwar blöd aus, nach kurzem Grübeln ist es aber ganz logisch. Da es sich bei allen Komponenten des Headers um vorzeichenlose 32-Bit-Zahlen handelt - in C wohl bekannter unter der Bezeichnung \`unsigned\`- lässt sich die Checksumme ganz leicht berechnen, wenn man den Header limits.h benutzt. Ein schnelles Beispiel: Sind keine Flags gesetzt, die Variable \`flags\` also gleich 0 (Null), wäre die Checksumme gleich 0xE4524FFE.

Gut, das waren auch schon die wichtigsten Komponenten des Headers. Nun noch etwas mehr über die Flags. Die nächsten fünf Komponenten werden nämlich durch das Setzen von Flag 16 aktiviert. Sie enthalten Informationen darüber, wo der Loader den Kernel hinladen soll etc.

1.  Die **Adresse des Headers**, also der Offset von der Variable \`magic\`, welche die magische Zahl enthält.
2.  **Offset des Code Segments** (auch bekannt als Text Segment).
3.  **Offset des Endes des Data Segments** Diese Adresse minus der Adresse des Code Segments ergibt die Anzahl der insgesamt zu ladenden Bytes.
4.  **Offset des Endes des BSS-Segments** Hab ich noch nie benutzt, daher auch keine genauere Erklärung. *(Anmerkung von Blitzmaster: Das BSS Segment gibt einen Bereich an, der von GRUB mit 0 initialisiert wird und nicht für Boot-Module oder Boot-Informationen Strukturen verwendet wird. Das BSS Segment kann dem Kernel für noch nicht initialisierte Daten dienen, also einfach ein Reservierter Bereich nach dem eigentlichen Kernel wo er seine eigenen Daten/Strukturen ablegen darf)*
5.  **Entry Point** Die Adresse, an die der Loader nach dem Laden springen soll. Bei einem C-Kernel (was ja bei uns der Fall ist), wäre das die Adresse von main(). (Anmerkung: Da der Loader zu der gegebenen Adresse springt, egal, ob es die von main() ist, oder nicht, können wir auch eine andere Funktion als Startroutine wählen bzw. main() einen beliebigen Namen geben. Na ja, wollte ich nur mal anmerken.)

Und weiter. Die folgenden Optionen werden nur berücksichtigt, wenn Flag zwei (2) gesetzt wurde. Sie geben dem Loader auskunft darüber, welcher Grafik-Modus erwünscht ist. Leider hat es bei mir noch nie geklappt; ich schreibe die Felder trotzdem dazu, vielleicht hat jemand anders mehr Glück.

1.  **Modus 0 (Null) = lineare Grafik, 1 (Eins) = EGA (Text). Alle weiteren Nummern sind noch nicht definiert.**
2.  **Spalten** Na ja, die Anzahl der Spalten eben bzw. die Anzahl der Pixel pro Zeile, falls wir im Grafik-Modus sind. 0 (Null) bedeutet, dass der Kernel hier keine Vorlieben hat, d.h. der Bootloader darf hier machen, was er will.
3.  Die **Zeilen** im Text-Modus bzw. die Anzahl der Pixel pro Spalte im Grafik-Modus. Für 0 (Null) gilt das selbe wie für die Spalten.
4.  **Farbtiefe** (Bits Per Pixel, BPP) im Grafik-Modus, 0 (Null) im Textmodus. Eine 0 (Null) im Grafik-Modus bedeutet, dass der Kernel auch hier keine Vorlieben hat.

Gut, das waren die Komponenten des Multiboot Headers. Es gibt logischerweise noch mehr Flags, auch wenn längst nicht alle definiertn sind. Diese hier sind aber meiner Meinung nach die wichtigsten, die anderen habe ich noch nicht benutzt.

Hier noch eine kurze Übersicht über die Flags.

       00..15: Anforderungen (siehe oben)
       16..31: Vorlieben (siehe oben)
       
       00: Irgendwas mit Modulen, hab ich nicht kapiert...
       01: Information über den Arbeitsspeicher verlangen.
       02: Video-Einstellungen (siehe oben)
       03..15: nicht definiert
       16: Kernel-Adresse(n) (siehe oben)
       17..31: nicht definiert

Die Information, die vom Loader angefordert wird, wird in einer Struktur gespeichert, welche wiederum irgendwo im Speicher abgelegt wird. Die Adresse wird vom Loader in EBX gespeichert. Das ist allerdings nur für Leute von Interesse, die vorhaben, ihrem C-Kernel noch ein Assembler-Script voranzustellen. Sie könnten dann einfach EBX \`pushen\` und den Pointer in main() übernehmen, etwa mit dem Funktionskopf

\<c\> int main(multiboot_info \*mbi) { ... };\</c\>

Die Struktur \`multiboot_info\` ist in multiboot.h definiert, welche GRUB beiliegen sollte.

Weil ich aber von Assembler die Schnauze voll hab, lass die Information Information sein und gehe einfach davon aus, dass ich alles nötige auch selbst in Erfahrung bringen kann.

Nun zu den wirklich wichtigen Dingen. Damit der Bootloader den Header auch findet, muss dieser in den ersten 8192 Bytes des Kernels zu finden sein, und zwar vollständig. Zunächst mal machen wir es uns ganz einfach und gehen davon aus, dass unser Kernel niemals so groß wird, dass der Header (der ja automatisch ins Data Segment am Ende des Kernels geschoben wird) so weit nach hinten rutschen könnte.

Zunächst einmal brauchen wir einen Prototyp von main(), da wir ja deren Offset in den Header schreiben wollen.

\<c\> void main(void);\</c\>

Wunderbar. Jetzt zum Header.

\<c\> const unsigned MultibootHeader\[12\] = {

         0x1BADB002, // der magische Wert
         0x00000000, // die Flags
         0xE4524FFE, // die Checksumme
         (unsigned) MultibootHeader, // Offset des Headers
         (unsigned) main, // Offset von main() als Beginn des Code Segments
         0x00000000, // Data Segment, da scheißen wir drauf
         0x00000000, // BSS Segment, wer braucht`n sowas?
         (unsigned) main, // nochmal main(), diesmal als Entry Point
         0x00000000, // Grafik? Nein, danke! 
         0x00000050, // 80 Spalten
         0x00000019, // 25 Zeilen
         0x00000000 // 0 BPP, wir sind im Text-Modus
       };</c>

Da hätten wir unseren Multiboot Header. So lange der Kernel nicht zu groß wird, sollte alles funktionieren.

Anmerkung: Ich erstelle den Kernel immer mit folgenden Befehlen:

       gcc -c -ffreestanding -fwritable-strings -nostdinc -O3 -Wall *.c;
       ld -Ttext 0x100000 --oformat elf32-i386 -O 1 -o kernel kernel.o [andere Module.o] 

...und es klappt problemlos. Möglicherweise gibt\`s bei anderen Formaten (also nicht elf32-i386) Schwierigkeiten, aber das ist mir egal.

Ja, und wenn der Kernel doch mal zu groß wird, lässt sich der Header ganz einfach am Anfang halten, indem man ihn folgendermaßen erstellt:

\<c\> const unsigned MultibootHeader\[12\] \_\_attribute\_\_

             ((section(".text"))) = { /* Header Information */ };</c>

Nach der entsprechenden Änderung meldet mbchk (das Multiboot Header Checksum Check Programm, boah!) den Header konstant bei 4096. (Danke an den hilfreichen Mensch vom BuHaBoard, der mir diesen Trick gezeigt hat. Leider fällt mir der Name nicht mehr ein...)

Ok, das war\`s auch schon. Ziemlich simple Sache. Ich wünsche dann noch viel Spaß und beende hiermit das Tutorial. Wiedersehn!

PS: Jetzt hätte ich fast das wichtigste vergessen! Nachdem ihm GRUB als Bootloader installiert habt (egal auf welchem Medium, das müsst ihr auch allein hinkriegen), bootet ihr euren Kernel, indem ihr in der Boot-Shell von GRUB folgendes eingebt.

       kernel /directory/kernel
       boot

Evtl. wollt ihr vorher noch das root-Verzeichnis festlegen, was folgendermaßen funktioniert.

       root (hdX,Y)/directory 

X ist die Nummer der Festplatte, beginnend bei Null (also hd0 ist die erste Platte), Y ist die Nummer der Partition, ebenfalls bei Null beginnend. \`/directory\` kann auch weg gelassen werden, dann ist / das root-Verzeichnis. Wahlweise kann auch eine Floppy als root gewählt werden.

       root (fd0) 

Es sei noch anzumerken, dass der Kernel möglichst nah am root-Verzeichnis gespeichert sein sollte, also vorzugsweise in /kernel oder ähnlich, da GRUB nicht genug Speicher hat, um ewigen Verzweigungen der Verzeichnis-Hierarchie nachzugehen.

Ach ja, der Kernel kann auch direkt so angegeben werden, wenn man das root-Directory nicht ändern will/muss.

       kernel (hdX,Y)/directory/kernel 

Ok, das war\`s jetzt aber wirklich. Man sieht sich im Netz.

**Lizer** - lizer@gmx.net

## Memory Typing - Textausgabe im Protected Mode

Dieses Tutorial richtet sich an OS-Developer, die schon etwas Erfahrung mitbringen. Ich gehe davon aus, dass ein funktionierender Bootloader vorhanden ist, der ein C-Programm in den Speicher lädt und ausführt. Weiterhin gehe ich davon aus, dass wir uns im Protected Mode befinden, was ohnehin der Fall sein müsste, wenn erstere Bedingung erfüllt ist, denn C-Compiler erstellen normalerweise 32Bit-Code, der im Real Mode nicht laufen würde. Ich persönlich verwende GRUB (Grand Unified Bootloader) und kann nicht dafür garantieren, dass mein Beispiel-Code auf allen Rechner-Architekturen und mit allen Bootloadern läuft; besonders dann nicht, wenn der Bootloader Marke Eigenbau ist.

Dann wäre noch zu sagen, dass ich alle Beispiele unter Linux geschrieben und mit GCC kompiliert habe und es evtl. möglich wäre, dass der Code unter anderen Systemen bzw. von anderen Compilern nicht (korrekt) übersetzt werden kann. Ich empfehle daher allen Windows-Usern, sich DJGPP zu besorgen, eine (kostenlose) Portation von GCC auf Windows.

Zunächst wäre zu klären, wie der Code kompiliert werden soll. Hier meine Kommando-Zeile.

       gcc -c -ffreestanding -nostdinc -I ./ -O3 -Wall -o kernel.o kernel.c 

Gut, nun zu den einzelnen Optionen. -c bedeutet, dass wir nicht linken, sondern lediglich den Object-Code haben wollen. -ffreestanding sorgt dafür, dass vom bestehenden OS unabhängiger Code erstellt wirde. Die Option -nostdinc sagt dem Compiler, dass er keine Standard-Libraries einbinden soll (wie z.B. stdlib.o), die brauchen wir nicht und könnten u.U. sogar Probleme machen. -I DIRECTORY erleichtert uns die Programmierarbeit, indem es dafür sorgt, dass DIRECTORY zum standardmäßigen include-Verzeichnis gemacht wird. So können wir im Code die einzubindenden Header in die Klammern ( \< und \> ) stellen und müssen nicht mehr die hässlichen Quotes benutzen. Bei mir befinden sich die Header-Files im selben Verzeichnis wie der Kernel (daher das ./ ), das ist aber jedem selbst überlassen. Weiterhin bringt uns die Option -O3 wunderbare Code-Optimierung, was Platz und Geschwindigkeit angeht. Evtl. könnte das für Probleme sorgen, dann lasst das einfach weg. -Wall sorgt dafür, dass jede noch so unwichtige Warnung ausgegeben wird, denn wir wollen ja perfekten Code schreiben, an dem es absolut gar nichts auszusetzen gibt. -o kernel.o nennt dem Compiler die Ausgabe-Datei, in diesem Fall kernel.o . kernel.c letztendlich ist die Datei, die wir kompilieren wollen. Sollen mehrere Module erstellt werden, ist das auch kein Problem. Einfach genau so kompilieren, wie den Kernel. Dann kann folgendermaßen zusammen gelinkt werden.

       ld -Ttext 0x100000 --oformat elf32-i386 -O 1 -o kernel kernel.o [???.o] 

-Ttext gibt den Offset des sogenannten Entry Points an. Ist jedoch ganz verschieden, je nachdem, welchen Bootloader ihr benutzt und wo dieser den Kernel hin lädt. 0x100000 (HEX) funktioniert zumindest bei GRUB mit Sicherheit. --oformat legt das Ausgabe-Format fest. Ich benutze ELF 32Bit-Code (little endian), da dieses Format von GRUB vollständig unterstützt wird. -O 1 sorgt wieder für Optimierung, -o kernel ist die Ausgabe-Datei, kernel.o ist die zu linkende Object-Datei und die optionalen Dateien ???.o sind Module, die mit verlinkt werden. Gut, das wir das geklärt hätten...

Nachdem wir wissen, wie wir kompilieren, können wir uns jetzt mit einigen Informationen rumschlagen, die wir unbedingt benötigen.

Der Video-Speicher ist ein bestimmter Bereich im Arbeitsspeicher, der - befindet sich der PC im Textmodus - ein Word, also zwei Bytes für jedes Zeichen auf dem Bildschirm bereithält. Das erste Byte ist hierbei ein ganz normales ASCII-Zeichen (wie etwa \`A\`, \`x\` oder \`?\`), das zweite Byte stellt die Attribute dar, wie etwa die Textfarbe, die Hintergrundfarbe und ob der Text bzw. das Zeichen blinken soll. Auf \`normalen\` Architekturen beginnt der Video-Speicher an der Adresse 0xB8000 und ist 4000 Bytes (80 \* 25 Zeichen \* 2 Bytes pro Zeichen) lang bzw. groß. Auf Schwarz-Weiß-Monitoren beginnt der Speicher - soviel ich weiß - an der Adresse 0xB0000. Ich habe mir jetzt aber nicht die Mühe gemacht, das zu überprüfen, da ich nicht davon ausgehe, dass noch jemand so ein Teil besitzt (und benutzt).

Wie bereits erwähnt stehen die Attribute im zweiten Byte eines jeden Zeichen-Words. Der Einfachheit halber stellen wir sie (im Beispiel-Code) als vierstellige Hexadezimal-Zahlen dar (0x0000) und OR\`en sie einfach mit dem Zeichen-Word zusammen. Da wir im Textmodus nur 16 Farben haben, ist der Vorgang denkbar einfach. Die höchste Stelle im der HEX-Zahl (0x1000) stellt die Hintergrundfarbe dar, die zweite Stelle (0x0100) die Vordergrundfarbe.

| Wert | Farbe |
| ------ | ------------------- |
| 0x0 | Schwarz |
| 0x1 | Blau |
| 0x2 | Grün |
| 0x3 | Türkis |
| 0x4 | Rot |
| 0x5 | Magenta |
| 0x6 | Braun |
| 0x7 | Hellgrau |
| 0x8 | Dunkelgrau |
| 0x9 | Hellblau |
| 0xA | Hellgrün |
| 0xB | Helltürkis (Cyan) |
| 0xC | Hellrot |
| 0xD | Hellmagenta |
| 0xE | Gelb |
| 0xF | Weiß |

Jetzt ein paar Beispiele. Das Attribut-Byte 0xC2 ergäbe dunkelgrüne Schrift auf hellrotem Hintergrund. 0x07(00) ist die Standardschrift der meisten Konsolen, nämlich hellgrauer Text auf schwarzem Hintergrund. Wir machen die Attribut-Bytes zu Words, damit wir sie bequemer or\`en können. Beispiel:

       0x0700 <- Attribut (hellgrau / schwarz) als Word
       0x0046 <- ASCII-Zeichen `F` als Word
       ------ <- or-Verknüpfung
       0x0746 <- das fertige Word, ein hellgraues F auf schwarzem Hintergrund 

Natürlich könnte man auch einfach das Attribut- und das ASCII-Byte einzeln in den Speicher schreiben, aber ich denke, so ist es einfacher und übersichtlicher.

Nun zur Ausgabe. Absolut simpel! Alles, was wir machen müssen, ist das aus dem ASCII-Code und den Attributen berechnete Word an die richtige Stelle im Speicher zu kopieren, und schon steht das Zeichen auf dem Schirm. Alles klar? Dann zum Code!

Natürlich ist der Code nicht komplett, aber er dient ja auch nur Anschauungszwecken. Zum Beispiel gibt es noch keine Scroll-Funktion, d.h., sobald wir über die ersten 25 Zeilen weg sind, wird irgendwo in den Speicher geschrieben. Was dann passiert, will ich gar nicht erst wissen... Weiterhin fehlt die Funktion clrscr(), die den Bildschirm leert. Bis jetzt überschreiben wir einfach den Text, der schon auf dem Bildschirm steht. Wer den Code kompiliert und ausprobiert, der wird außerdem merken, dass sich der Cursor nicht automatisch mit dem Text bewegt. Eine Funktion zum Bewegen des Cursors würde aber den Rahmen dieses Tutorials sprengen, deshalb lass ich das mal weg. Außerdem benötigen wir dazu etwas Inline-Assembler, welchen zu erklären noch einmal ein Tutorial füllen würde. Vielleicht ein anderes Mal... Nun gut, hier verabschiede ich mich schon mal und kopiere dann einfach den Code hier her. Viel Spaß und Erfolg beim Ausprobieren!

**Jonas Kramer** lizer@gmx.net

\<c\> /\*

         Memory Printing Example
         Written 2003 by Jonas Kramer
         eMail: lizer@gmx.net
       */
       
       #define COLS 80 /* 80 Spalten */
       #define ROWS 24 /* 25 Zeilen, bei 0 beginnend */
       
       /* globaler Pointer auf den Beginn des Video Memory */
       unsigned short * const pScreen = (unsigned short *) 0xB8000;
       
       unsigned gPos = 0; /* der Cursor */
       unsigned short gAttr = 0x0700; /* die Attribute */
       
       #define GETX (gPos % COLS)
       #define GETY ((gPos - GETX) / COLS)
       
       void gotoxy(unsigned x, unsigned y);
       void putchar(char);
       void puts(const char *);
       
       int main(void) {
         char *msg = "Hello, world!"; /* eine Test-String */
         puts(msg); /* den String ausgeben */
         return 0; /* Das funktioniert nur, wenn der Kernel von GRUB geladen
               wurde, ansonsten muss hier eine Endlosschleife hin */
       };
       
       void gotoxy(unsigned x, unsigned y) {
         gPos = x + (y * COLS);
         return;
       };
       
       void putchar(char ch) {
         switch(ch) {
         case '\n':
           gotoxy(0,GETY + 1);
           break;
         case '\r':
           gotoxy(0,GETY);
           break;
         default:
           pScreen[gPos++] = (unsigned short) ch | gAttr;
           break;
         };
         return;
       };
       
       void puts(const char *s) {
         while(*s)
           putchar(*(s++));
         return;
       };</c>

## Icy Wolf\`s Kolumne

**Über Spiele und zu gute Graphik**

Wer kennt das nicht? Ich bin selber grad mal 14, aber blicke schon in die schöne Zeit zurück, in der ich in meinem zarten Alter am Sega Master System 2 von meinem Bruder saß und Spiele wie Sonic, Wonderboy III, Alex Kid, Shinobi, etc. voller Spannung gespielt habe. Ich war noch zu jung um Sachen wie Emotionen, Logik, etc. aufzubringen, aber die Faszination des Spielspaßes fesselte mich an den Fernseher. Jeder der von klein auf mit Computern zu tun hatte, hat solche Erinnerungen. Ob Sega, Amiga, Nintendo, C64, Geo, Atari oder sonst was. Aber was ist heute? Schon bevor Spiele rauskommen, muss ich den ganzen Spielezeitschriften lesen, dass das Spiel XY eine unfassbar gute Graphik hat und das Beste seiner Art werden wird und natürlich mit der Top Benotung ausgezeichnet wird. In der Schule und sonst überall hört man nur: "Wie, du hast XY wirklich noch nicht gespielt? Das kann nicht sein, das ist das beste Spiel überhaupt." Da man sich denkt, dass es einfach gut sein muss, wenn es so bejubelt wird. Holt man sich also kurzerhand \`ne Raubkopie von den Klassenkameraden, installiert man das 5GB große Game stellt man es auf minimal Anforderungen um es überhaupt spielen zu können und merkt, dass das Spiel stumpfsinnig, ein einfaches witzloses Abschlachten oder sonst was ist.

Diese Situationen regen mich so was von auf. Die Spieleindustrie bringt \`ne Idee, die jedem Kleinkind einfällt und schon Tausende Male durchgekaut wurde, engagieren Programmierer, um unbedingt eine neue Engine zu schreiben, von dessen Sorte es auch schon zu viele gibt, und (wer hätte es gedacht?) Graphiker bis zum Abwinken. Würde es so was nicht geben, würden wir viel weniger an "alte Zeiten" denken, da wir uns einfach Spielspaß wünschen, welcher damals im Vordergrund stand. Aber was kann man dagegen machen? Das Konzept geht prima auf. Als beispielsweise meine (schon 1-2 Jahre älteren) Klassenkameraden mitbekamen, dass Monkey Island zu meinen Lieblings Spielen gehört, kriegten sie sich gar nicht mehr ein. Jedoch fanden sie kein einziges, schlagkräftiges Argument, welches ihr Gelächter gerechtfertigte.

Was mich trotz allem erstaunt, ist dass die Spieleindustrie schon wirklich törichte Aktionen hat. Ich will auf das Spiel "Prince of Persia" anspielen. Mein Kumpel hat sich das Spiel geholt und war voll fasziniert davon. Ich hatte kein Interesse daran, da ich nach einiger Zeit bemerkte, dass der Spielablauf/-aufbau zu linear für mich war. Als er mir dann aber erzählte, dass bei keinen seiner Verwandten lief, wollte ich das Spiel auch bei mir installieren und wollte feststellen, ob es denn bei mir lief. Das Ergebnis war negativ. Und mal ehrlich, kann es klug sein, wenn man ein Spiel rausbringt, welches nicht auf Rechnern läuft, die erst so um die 1,5 Jahre alt sind. Das Spiel läuft nicht auf meinem Rechner bloß weil meine Graphik Karte (eine GeForce2TI) nicht alle High-End Funktionen unterstützt, die für das Spiel benötigt werden. Die Verwandten haben glaub\` ich sogar noch bessere Teile als ich.

Wenn ihr Spieleprogrammierer seid und den Text da gelesen habt, oder auch nicht, hab\` ich jetzt eine Bitte an euch: Lasst die Graphik bei euren Games einen sekundären Rang einnehmen und achtet mehr auf so was wie Spielewitz!!!

**Icy Wolf**

Anmerkung von mastermesh: Du sprichst mir aus der Seele. Wir Retrogamer sollten zusammenhalten. Back to DOS ;-)

## Nachwort

Und das war\`s auch schon wieder mit dieser Ausgabe. Feedback ist natürlich wie immer erwünscht. Im Übrigen werde ich bald ein Lowlevel-Forum aufmachen, wo über alles OS-Dev-mäßige geredet wird. Das mache ich übrigens aus rein egoistischen Gründen (meine Mailbox ist nämlich permanent überfüllt :-). Wie auch immer, ich wünsch euch alles Gute usw. usw. usw.....

**Mastermesh**

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 4](Ausgabe-4 "Ausgabe 4") | **Navigation** | [Ausgabe 6](Ausgabe-6 "Ausgabe 6") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6644/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1470/index.html)

<!-- MediaWiki page 1470; revision 6644; parent 6300; 2009-12-28T01:22:28Z -->
