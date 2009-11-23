# Literatur

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Es gibt so gut wie keinen Menschen, der alles kann. Auch nicht im OS-Development. Deshalb sind gute Nachschlagewerke und Bücher zum Lernen eine gute Sache. Natürlich gibt es eine Fülle von Büchern, die einen besser, die einen schlechter. Um den Überblick zu wahren hier eine kleine Liste von emfehlenswerten Büchern und (Online-)Tutorials.

Leider sind die meisten Fach- und Lehrbücher sehr teuer. Darum sei an dieser Stelle nochmal an die leider viel zu oft vergessenen Bibliotheken verwiesen. Zwar wird man bei seiner Stadtbibliothek oft kein Glück haben, jedoch sind viele Büchereien über Hinweise, welche Fachbücher angeschafft werden sollten, teilweise sehr dankbar. Wenn alle Stricke reißen, dann lohnt sich (auch für Schüler) fast immer eine Mitgliedschaft bei der Bibliothek der nächsten Universität, besonders wenn sie Informatikstudiengänge anbietet. Sollte diese gut erreichbar sein, so ist ein Besuch ein absolutes Muss.

Möchte man dennoch lieber ein Buch besitzen, um beispielsweise im selbigen Notizen zu machen, so sollte man der kleinen Bibliothek von nebenan einen Besuch machen. Dort werden oftmals Reste von Beständen zu sehr günstigen Preisen verkauft, zum Beispiel, wenn von einem Buch eine neue Auflage erschienen ist. Preisersparnisse von bis zu 50% sind keine Seltenheit.

## Bücher: Programmierung

Wer ein OS entwickeln will, sollte schon der Sprache, in der er es machen will, mächtig sein. Wer neue Sprachkenntnisse erlernen möchte, seine Sprachkenntnisse vertiefen möchte oder eine gute Referenz sucht, dem sei diese Liste ans Herz gelegt:

### Assembler

- ["Assembler: Maschinennahes Programmieren von Anfang an von Reiner Backer](http://www.amazon.de/Assembler-Maschinennahes-Programmieren-Anfang-Windows-Programmierung/dp/3499612240)  
  Klasse Buch für den Einstieg in die x86-Programmierung. Es wird die Arbeitsweise eines Prozessors sowie das Zusammenspiel zwischen CPU, RAM, MMU und ALU erklärt. Das Buch ist gut strukturiert und bietet ausführliche Beispiele zu jedem wichtigen Assemblerbefehl. Der Windows-Teil ist allerdings nur mittelmäßig, ist aber für unser Klientel eh nicht von Bedeutung.

  

### C/C++

- ["C/C++ GE-PACKT" von Herbert Schildt](http://www.amazon.de/ge-packt-Schneller-kompletten-Zahlreiche-Produktivität/dp/3826617282/ref=sr_1_1?ie=UTF8&s=books&qid=1249511226&sr=1-1)  
  Eine kurze Übersicht über die Features von C, C++ und den Standard-Bibliotheken.
- ["C++ Objektorientiertes Programmieren von Anfang an" von Helmut Erlenkötter](http://www.amazon.de/C-Objektorientiertes-Programmieren-von-Anfang/dp/3499600773)  
  Das Buch ist optimal, wenn man bereits Programmieren kann, und es einem nur um die Sprache C++ an sich geht. Aber auch für die jenigen die bereits C++ können ist es ein nettes Nachschlagewerg. Alle Features von C++ werden an sehr gut gewählten Beispielen erklärt.
- ["C: Bibliotheksfunktionen sicher anwenden" von Helmut Erlenkötter](http://www.amazon.de/Bibliotheksfunktionen-sicher-anwenden-Helmut-Erlenk%C3%B6tter/dp/3499612232)  
  Gutes Buch, bietet den Einstieg in die Programmierung mit der C-Standard-Bibliothek. Hilft, seine Kennitnisse anhand ausführlicher Beschreibungen und Übungen in C zu vertiefen und dient hervorragend als Nachschlagewerk.
- ["C++ von A bis Z: Das umfassende Handbuch" von Jürgen Wolf](http://www.amazon.de/von-bis-CD-ROM-umfassende-Handbuch/dp/3898428168)  
  Sehr gutes Handbuch zur Programmierung in C++, deckt so gut wie alle Spracheigenschaften und die STL ab. Im hinteren Teil wird auch die Programmierung mit wxWidgets erläutert. Dazu kommt noch eine CD mit der HTML-Version des untenstehenden Buches "C von A bis Z".
- ["C von A bis Z: Das umfassende Handbuch" von Jürgen Wolf](http://www.amazon.de/umfassende-Handbuch-Linux-Unix-Windows/dp/3898426432)  
  Das passende C-Handbuch vom selben Autor, es ist beim Verlag auch als HTML-Version als [kostenloses Openbook](http://openbook.galileocomputing.de/c_von_a_bis_z/) verfügbar. Ist sehr gut zum Lernen, jedoch teilweise verwirrend geschrieben, und für den OS-Entwickler teilweise zu ungenau. Trotzdem insgesamt eine empfehlenswerte Referenz. (ACHTUNG: Im September 2009 erscheint eine neue Auflage. Eventuell lohnt es sich zu warten, um das neue, aktuellere Buch zu kaufen, oder das alte Buch eventuell billiger zu kriegen)

  

## Bücher: OS-Development

Es gibt nicht viele, aber es gibt sie: Bücher, die sich komplett auf die Entwicklung bzw. auf die theoretischen Sachen eines Betriebssystems spezialisieren.

### Bücher über existierende Kernel

- ["Understanding the Linux Kernel - From I/O ports to process management" von Daniel P. Bovet und Marco Cesati](http://www.amazon.de/Understanding-Linux-Kernel-Process-Management/dp/0596000022/ref=sr_1_2?ie=UTF8&qid=1249546324&sr=8-2)  
  Dieses Buch erklärt den [Linuxkernel](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") sehr detailliert, indem Grafiken Abläufe erklären und wichtige Strukturen sowie kurze Codeteile aufgelistet werden. Dabei handelt es unter anderem von [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") (mit Dateibuffering, Swapping und [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "Direct Memory Access")), dem VFS von Linux, [Scheduling](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler"), Signalen, [Interrupts](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt"), Synchronisation im [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und der [IPC](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation").

  

### Bücher über Implementierung

- ["Operating Systems: Design and Implementation" von Andrew S. Tanenbaum](http://www.amazon.de/Operating-Systems-Implementation-Prentice-Software/dp/0131429388)  
  Dieses Lehrbuch beschäftigt sich mit [Minix](https://github.com/lowlevel-eu/wiki/wiki/Minix "Minix"), welches extra als Lehrsystem entwickelt wurde. Bereits Linus Torvalds wusste dieses Buch bevor und während er Linux entwickelte, zu schätzen.

## Bücher: Hardware

Das OS ist quasi der Herr über die Hardware. Es verwaltet selbige sowie den Zugriff darauf usw.. Nur die wenigsten wissen, an welchem Port man ein bestimmtes PCI-Gerät anspricht oder wie sich die Soundkarte dazu überreden lässt, einen Ton auszugeben. Hier eine Liste empfehlenswerter Bücher:

- ["Das Addison-Wesley Handbuch der Hardwareprogrammierung" von Klaus Dembowski](http://www.amazon.de/Das-Addison-Wesley-Handbuch-Hardwareprogrammierung/dp/3827323053)  
  Ein zwei Bände und ca. 1500 Seiten umfassendes Werk über die Hardwareprogrammierung, besonderen Augenmerk legt das Buch auf die Treiberprogrammierung unter Windows, Linux kommt etwas kurz. Aber nichtsdestotrotz ist besonders der erste Band für OS-Developer interessant, wird hier doch genauestens auf die Prozessoren und deren Funktionsweise eingegangen, auch wird Paging erklärt usw.. Mit Codebeispielen in Assembler, C, Pascal und Visual Basic werden die Beispiele vertieft. Der zweite Band widmet sich sehr der Peripherie, wie PCI, USB und Bluetooth. Auf der mitgelieferten DVD findet man alle Specs von Intel und AMD.
- ["PC-Hardwarebuch" von Hans-Peter Messmer und Klaus Dembowski](http://www.amazon.de/PC-Hardwarebuch-Aufbau-Funktionsweise-Programmierung/dp/3827314615)  
  Das Standardwerk, wenn es um Hardwareprogrammierung geht.

## Linkliste

- [Wikibooks Programmiersprachen](http://de.wikibooks.org/wiki/Regal:Programmierung)

<!-- -->

- [Wikibooks Betriebssystemtheorie](http://de.wikibooks.org/wiki/Betriebssystemtheorie)

<!-- -->

- [Wikibooks Betriebssystementwicklung](http://de.wikibooks.org/wiki/Betriebssystementwicklung)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6375/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1930/index.html)

<!-- MediaWiki page 1930; revision 6375; parent 6095; 2009-11-23T20:34:15Z -->
