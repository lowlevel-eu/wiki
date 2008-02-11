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

Ein weit verbreitetes Vorurteil ist, dass man ein Betriebssystem komplett in Assembler schreiben muss. Quatsch. Man kann, wenn man es möchte, aber man muss nicht. Wahr ist, dass man um einige wenige Zeilen Assembler nicht herumkommen wird. Ein grundlegendes Verständnis der Sprache wäre daher hilfreich, jahrelange Erfahrung ist aber nicht nötig.

Ein übliches Vorgehen ist es, nur das nötigste in Assembler zu schreiben und für den Rest eine Hochsprache zu benutzen. Für die Wahl dieser Hochsprache gibt es im großen und ganzen zwei Alternativen:

- Du nimmst C. Fast jeder spricht diese Sprache und Du bekommst Unmengen an Beispielcode in C. Dein Betriebssystem ist eins von vielen und im Forum oder im IRC wird dir fast jeder helfen können.
- Du nimmst nicht C. Du wirst Dich vor allem am Anfang wesentlich seltener beim Kopieren von Code erwischen, weil es einfach nicht geht, ohne ihn in deine Sprache zu übersetzen. Ja, das ist durchaus positiv. Auf der anderen Seite bist du ein Außenseiter und erhältst vielleicht nicht ganz so umfangreich Hilfe und musst Dich möglicherweise öfter selbst durchschlagen - gerade wenn es um Besonderheiten deiner Sprache oder Deines Compilers geht.

Von Mitgliedern der Lowlevel-Community benutzte Alternativen zu C sind beispielsweise C++ oder Pascal (mit FreePascal oder mit Tricks auch Delphi als Compiler). Theoretisch würde auch FreeBASIC funktionieren. Andere Sprachen hat hier meines Wissens noch niemand versucht, könnten natürlich aber trotzdem funktionieren.

### Entwicklungsumgebung und Tools

Um Dein eigenes Betriebssystem zu entwickeln, brauchst Du ein paar Werkzeuge. Auf die wichtigsten davon gehe ich in diesem Abschnitt kurz ein.

Fangen wir vorne an: Du brauchst einen PC. Ja, Du hast recht, Du brauchst natürlich strenggenommen keinen PC. Aber es wäre geschickt, denn ich nehme an, Du willst ein x86-Betriebssystem schreiben. Wenn Du wider Erwarten für eine andere Plattform entwickeln möchtest, teil Dich im Forum mit, das wird auch andere interessieren - allerdings bist dann Du derjenige, der erklären darf. Aber zurück zum PC: Am besten hat dieser ein Diskettenlaufwerk, denn Disketten sind für den Anfang das handlichste. Und ein 386er oder höher sollte es schon sein - aber das sollte heutzutage machbar sein.

Eine Stufe weiter kommen wir zum Betriebssystem. Da Dein eigenes Betriebssystem noch nicht fertig ist, wirst Du vorerst mit einem bestehenden vorlieb nehmen müssen. Hast Du ein Linux installiert? Wunderbar, nimm das. Ich möchte hier nicht lügen, deshalb: Ja, man kann auch Windows nehmen. Aber dazu braucht es schon eine gewisse masochistische Veranlagung. Unter Windows wirst du aller Voraussicht nach eine Weile mit der Umgebung basteln müssen, während es unter Linux einfach läuft. Man könnte jetzt versuchen, einen Kausalzusammenhang herzustellen, warum die Windowsbenutzer häufiger bei Assembler steckenbleiben - aber lassen wir das...

Dann brauchst du Editor und Compiler. Als Editor hast du sicher schon Deinen eigenen Favoriten (nämlich vim) und auch beim Compiler ist die Sache relativ klar: Wenn du C nimmst, wird der Compiler im Allgemeinen gcc sein und unter Linux ist damit alles geklärt. Wenn du gcc unter Windows benutzt, solltest du dir überlegen, ob du nicht einen Crosscompiler benutzt, der ELF-Dateien erzeugt. Bahnhof? Macht nichts, vertrau mir, installier ihn Dir einfach. (Oder natürlich einfach ein Linux)

- [Crosscompiler_für_Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")

Schließlich brauchst Du auch noch eine Möglichkeit, Dein Werk zu testen. Ja, ich weiß, der PC. Aber du willst nicht nach jeder kleinen Änderungen neu booten müssen, richtig? Besorg dir einen Emulator. VMware ist ganz nett, aber hilft Dir beim Debuggen nicht besonders weiter. Nimm qemu oder bochs - oder am besten beides. Wenn Dein System in beiden Emulatoren funktioniert, ist immer noch genug Zeit, es auf den echten PC loszulassen.

- <http://www.qemu.org>
- <http://bochs.sourceforge.net>

## Wo anfangen?

### Der Bootloader

Dein eigenes Betriebssystem möchte am Anfang irgendwie von der Festplatte oder Diskette in den Speicher geladen werden, bevor es irgendwas macht. Daher brauchst du einen Bootloader.

Hier gibt es die großen zwei Möglichkeiten, etwas fertiges zu nehmen oder selbst einen Bootloader zu schreiben. Ein guter Bootloader ist ein Projekt für sich, daher empfehle ich grundsätzlich, GRUB zu benutzen und sich auf das eigentliche Betriebssystem zu konzentrieren. GRUB lädt Dir Deinen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und möglicherweise weitere Module vom Dateisystem auf der Platte oder Diskette, initialisiert Dir den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), bietet ein Bootmenü und einiges mehr.

Die folgenden beiden Artikel werden Dir bei den ersten Schritten mit GRUB helfen:

- C-Kernel mit Grub
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen")

Wenn Du trotz diesen Vorteilen darauf bestehst, Deinen Bootloader selbst zu schreiben - so sei es. In den ersten Ausgaben des [Magazins](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin") findest Du die dazu nötigen Informationen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2573/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1619/index.html)

<!-- MediaWiki page 1619; revision 2573; parent 2566; 2008-02-11T22:32:59Z -->
