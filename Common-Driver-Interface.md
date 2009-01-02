# Common Driver Interface

Common Driver Interface (oder kurz CDI) ist ein Standard, der es ermöglichen soll betriebssystemunabhängige Treiber zu schreiben. Dies funktioniert mithilfe einer Bibliothek, die einmal für ein Betriebssystem implementiert werden muss. Dann können CDI-komforme Treiber einfach mit dieser Bibliothek kompiliert werden. Der CDI-Standard gibt lediglich vor, wie die Funktionsprototypen aussehen müssen, aber nicht wie diese implementiert werden, denn das ist ja von Betriebssystem zu Betriebssystem unterschiedlich.

CDI funktioniert nach dem Prinzip, dass jedes Programm einen oder mehrere Treiber mit einem oder mehreren Geräten anmeldet. Jeder Treiber registriert dabei verschiedene Callback-Funktionen um nachher mit dem System interagieren zu können. Am Ende wird eine Funktion aufgerufen um der CDI-Bibliothek die volle Kontrolle zu geben.

Ein Link zur Dokumentation der Funktionsprototypen, Strukturen, Enumerationen, usw. ist in dem [Absatz Weblinks](#weblinks) zu finden.

## Betriebssysteme welche CDI benutzen

- [LOST](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "LOST")
- [meinOS](https://github.com/lowlevel-eu/wiki/wiki/MeinOS "MeinOS")

## Weblinks

- [Aktuell-gehaltene Dokumentation der CDI-Header-Files von LOST](http://lpt.tyndur.org/cdi)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3805/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1622/index.html)

<!-- MediaWiki page 1622; revision 3805; parent 2947; 2009-01-02T16:11:16Z -->
