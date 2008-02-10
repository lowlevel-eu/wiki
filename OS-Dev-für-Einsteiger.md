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

Hier könnte man irgendwann was dazu hinschreiben. ;-)

## Wo anfangen?

### Der Bootloader

Dein eigenes Betriebssystem möchte am Anfang irgendwie von der Festplatte oder Diskette in den Speicher geladen werden, bevor es irgendwas macht. Daher brauchst du einen Bootloader.

Hier gibt es die großen zwei Möglichkeiten, etwas fertiges zu nehmen oder selbst einen Bootloader zu schreiben. Ein guter Bootloader ist ein Projekt für sich, daher empfehle ich grundsätzlich, GRUB zu benutzen und sich auf das eigentliche Betriebssystem zu konzentrieren. GRUB lädt Dir Deinen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") und möglicherweise weitere Module vom Dateisystem auf der Platte oder Diskette, initialisiert Dir den [Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode"), bietet ein Bootmenü und einiges mehr.

Die folgenden beiden Artikel werden Dir bei den ersten Schritten mit GRUB helfen:

- C-Kernel mit Grub
- [GRUB-Image erstellen](https://github.com/lowlevel-eu/wiki/wiki/GRUB-Image-erstellen "GRUB-Image erstellen")

Wenn Du trotz diesen Vorteilen darauf bestehst, Deinen Bootloader selbst zu schreiben - so sei es. In den ersten Ausgaben des [Magazins](https://lowlevel-eu.github.io/wiki/pages/1411/index.html "Kategorie:Magazin") findest Du die dazu nötigen Informationen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2566/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1619/index.html)

<!-- MediaWiki page 1619; revision 2566; parent 0; 2008-02-10T22:13:50Z -->
