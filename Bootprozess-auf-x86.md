# Bootprozess auf x86

Am Anfang ist das Nichts. So könnte man wohl den Zustand vor einem Bootvorgang beschreiben. Aber was passiert, wenn man den PC einschaltet? Das soll hier kurz erläutert werden.

## Nach dem Einschalten

Zuerst ist nichts geladen. Keine Software, keine Treiber, kein sonstiger Code, denn der Inhalt das RAM ist undefiniert. Die CPU-Register sind leer, und die CPU befindet sich im [Real Mode](Real-Mode "Real Mode"). In dem Moment wird in CS (Codesegment) der Wert 0xF000, und in EIP 0xFFF0 geladen – hier befindet sich der Einsprung für das [BIOS](Basic-Input-Output-System "BIOS"), welches grundlegende Initialisierungen durchführt. Das BIOS befindet sich nicht im RAM, sondern in einem ROM, das in den Adressraum eingeblendet ist, und kann deswegen bereits von der CPU ausgeführt werden.

## Im BIOS

Wenn das BIOS die Kontrolle erhält, wird (bei neueren zumindest) zuerst ein kleiner CPU-Check durchgeführt – in erster Linie um die Frage zu beantworten, was denn genau verbaut ist. Danach wird der Speicher gezählt, und im folgenden weitere Hardware erkannt und gegebenenfalls initialisiert. (dieser Vorgang beruht mitunter schon auf eigenen Einstellungen). Sobald zuletzt die vorhandenen Massenspeichergeräte erkannt wurden, werden diese in (konfigurierter) Reihenfolge auf gültige [Bootsektoren](Bootsektor "Bootsektor") durchsucht. Hierzu wird der erste Sektor jedes Gerätes nach 0x7C00 geladen und die letzten 2 Bytes mit der Magic Number 0x0AA55 verglichen. Ist diese korrekt, wird zum Start des Bootsektors gesprungen.

## Der Bootsektor

Ab hier ist es nicht mehr eindeutig, was passiert, generell kann man schon einen kleinen Kernelansatz mit FS-Treiber (für Realmode) in den Bootsektor einbauen und damit weiteren Code laden. Manchmal wird (im Rahmen eines Bootloaders) zuerst etwas mehr von der Platte gelesen, da sich vor der Partitionstabelle noch für Bootcode nutzbarer Platz befindet. Im Regelfall werden dann aber die Partitionen erkannter Festplatten auf ein „bootfähig“-Flag geprüft. Ist dieses gesetzt, wird weiterer Code aus den ersten Sektoren der Partition geladen, hier befindet sich zumeist ein spezieller Bootloader.

## Der Bootloader

Bootloader kann man generell in zwei Varianten unterteilen: Betriebssystemabhängige (bspw. NTLDR für Windows bis XP) und -unabhängige (bspw. [GRUB](Grand-Unified-Bootloader "GRUB")). Diese laden möglicherweise noch Konfigurationsdateien nach, laden aber im Endeffekt alles, was weiter benötigt wird, um ein Betriebssystem zu starten (d.h. den Kernel und gegebenenfalls die ersten Treiber, je nach Architektur des Systems). Zu beachten ist hierbei, dass die meisten Bootloader auch die Möglichkeit besitzen, anderen Bootcode zu laden (sog. „chainloading“, „Kettenladen“) – hierdurch können auch Systeme geladen werden, die von einem bestimmten Bootloader nicht unterstützt werden (indem einfach ein anderer geladen wird).

## Alles weitere

Nachdem der Bootloader seine Arbeit beendet hat, befindet man sich im eigenen Zuständigkeitsbereich – dem eigenen Kernel. Wie dieser weitermacht, müsst ihr für euer Projekt entscheiden – auch wenn die Grundstruktur oft ähnlich ist (Speicherverwaltung und Prozessverwaltung laden, Treiber laden, Anwendungen starten). Die grundlegenden Aufgaben des Kernels sind ausführlicher im Artikel [Kernel](Kernel "Kernel") aufgelistet.

  

## Siehe auch

- [Ausgabe 1](Ausgabe-1 "Ausgabe 1"), Abschnitte „Etwas Systemtheorie“ und folgende.
- [Bootsektor](Bootsektor "Bootsektor")
- [Bootloader](Bootloader "Bootloader")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9437/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1852/index.html)

<!-- MediaWiki page 1852; revision 9437; parent 7932; 2011-02-05T12:49:33Z -->
