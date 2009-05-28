# Bootprozess auf x86

Am Anfang ist das nichts. So könnte man wohl den Zustand vor einem Bootvorgang beschreiben. Aber was passiert wenn man den PC einschaltet? Das soll hier kurz erläutert werden.

## Nach dem Einschalten

Zuerst ist nichts geladen. Keine Software, kein Treiber, kein sonstiger Code, selbst die CPU-Register sind leer. In dem Moment wird CS (Codesegment) der Wert 0xFFFF geladen - hier befindet sich der Einsprung für das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS"), welches grundlegende Initialisierungen durchführt.

## Im BIOS

Wenn das BIOS die Kontrolle erhält, wird (bei neueren zumindenst) zuerst ein kleiner CPU-Check durchgeführt - in erster Linie um die Frage zu beantworten, was denn genau verbaut ist. Dannach wird der Speicher gezählt, und im folgenden weitere Hardware erkannt und gegebenenfalls initialisert. (dieser Vorgang beruht mitunter schon auf eigenen Einstellungen). Sobald zuletzt die vorhandenen Massenspeichergeräte erkannt werden, werden diese in (konfigurierter) Reihenfolge auf gültige [Bootsektoren](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor") durchsucht. Hierzu wird der erste Sektor jedes Gerätes nach 0x7C00 geladen und die letzten 2 Bytes mit der Magic Number 0x0AA55 verglichen. Ist diese korrekt wird zum Start des Bootsektors gesprungen.

## Der Bootsektor

Ab hier ist es nicht mehr eindeutig was passiert, generell kann man schon einen kleinen Kernelansatz mit FS-Treiber (für Realmode) in den Bootsektor einbauen und damit weiteren Code laden. Manchmal wird (im Rahmen eines Bootloaders) zuerst etwas mehr von der Platte gelesen, da sich vor der Partitionstabelle noch für Bootcode nutzbarer Platz befindet. Im Regelfall werden dann aber die Partitionen erkannter Festplatten auf ein "bootfähig"-Flag geprüft, ist dieses gesetzt, wird weiterer Code aus den ersten Sektoren der Partition geladen, hier befindet sich zumeist ein spezieller Bootloader.

## Der Bootloader

Bootloader kann man generell in 2 Varianten unterteilen: Betriebssystem-abhängige (bspw. NTLDR für Windows bis XP) und -unabhängige (bspw. [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB")). Diese laden möglicherweise noch Konfigurationsdateien nach, laden aber im Endeffekt alles was weiter benötigt wird um ein Betriebssystem zu starten (d.h. den Kernel und gegebenenfalls die ersten Treiber, je nach Architektur des Systems). Zu beachten ist hierbei, das die meisten Bootloader auch die Möglichkeit besitzen anderen Bootcode zu laden (sog. "chainloading", "Ketten-laden") - hierdurch können auch Systeme geladen werden, die von einem bestimmten Bootloader nicht unterstützt werden (indem einfach ein anderer geladen wird).

## Alles weitere

Nachdem der Bootloader seine Arbeit beendet hat, befindet man sich im eigenen Zuständigkeitsbereich - dem eigenen Kernel. Wie dieser weitermacht, müsst ihr für euer Projekt entscheiden - auch wenn die Grundstruktur oft ähnlich ist (Speicherverwaltung und Prozessverwaltung laden, Treiber laden, Anwendungen starten).

  

  

## Siehe auch

- [Ausgabe 1](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1 "Ausgabe 1"), Abschnitte "Etwas Systemtheorie" und folgende.
- [Bootsektor](https://github.com/lowlevel-eu/wiki/wiki/Bootsektor "Bootsektor")
- [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4415/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1852/index.html)

<!-- MediaWiki page 1852; revision 4415; parent 0; 2009-05-28T16:19:33Z -->
