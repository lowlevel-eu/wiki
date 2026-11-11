# Basic Input Output System

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Das **BIOS** (**B**asic **I**nput/**O**utput **S**ystem) ist die Firmware eines x86-PCs. Es wird meistens auf einem Flash-Speicher auf dem Motherboard gespeichert. Die Einstellungen des BIOS werden im [CMOS](CMOS "CMOS") gespeichert. Im Realmode werden vom BIOS außerdem Funktionen für das Ansprechen der Hardware bereitgestellt.

  

## Aufgaben des BIOS

Das BIOS ist das „Ur-Programm“ eines x86-Rechners (im Nachfolgendem nur noch „PC“ genannt). Es sitzt in einem beschreibbaren Flash-Speicher und wird direkt beim Starten des PCs ausgeführt. Es unternimmt nun den sogenannten [POST](Power-On-Self-Test "POST"), den **P**ower-**O**n **S**elf-**T**est, welcher den verfügbaren Arbeitsspeicher hochzählt und verschiedene Laufwerke anspricht sowie ihre Daten ausliest.

Nach dem POST versucht es von einer Liste von Laufwerken einen Bootloader zu laden. Dieser wird an Adresse 0x7C00 geladen und dann ausgeführt; Ab da hat das Betriebssystem die volle Kontrolle über den PC.

Dennoch bleibt das BIOS im Hintergrund aktiv: Solange sich der Kernel des aktiven Betriebssystems im [Real Mode](Real-Mode "Real Mode") befindet, kann er durch Interrupts, ähnlich denen bei [DOS](Microsoft-Disk-Operating-System "DOS") und [Linux](Linux "Linux"), auf Funktionen des BIOS zurückgreifen. Dadurch kann beispielsweise ein einfacher Bootloader mit Hilfe des BIOS den Kernel laden, indem er den passenden Interrupt aufruft und somit den Kernel lädt, und das alles ohne Treiber im Bootloader. *In diesem Fall bräuchte man den Interrupt Nr. 13 mit AH = 02 "DISK - READ SECTOR(S) INTO MEMORY".* Weitere Funktionen sind etwa das Umschalten zwischen verschiedenen Grafikmodi oder auch das Auslesen der Größe des Arbeitsspeichers, was ohne das BIOS überhaupt nicht möglich wäre.

Diese Funktionalität geht allerdings verloren, wenn man in den [Protected Mode](Protected-Mode "Protected Mode") oder gar in den [Long Mode](Long-Mode "Long Mode") schaltet. Wenn man trotzdem noch eine BIOS-Funktion benötigt, kann man beispielsweise den [Virtual 8086 Mode](Virtual-8086-Mode "Virtual 8086 Mode") einsetzen. Da die Treiber des BIOS jedoch in der Regel ziemlich langsam sind, sollte man die entsprechenden Treiber im Kernel implementieren, soweit dies möglich ist (z.B. [Floppy](Floppy-Disk-Controller "Floppy")-Treiber).

## Weblinks

- [<img src="assets/Flag_of_the_United_Kingdom.png" title="englisch" width="20" height="12" alt="englisch" /> BIOS Central](http://bioscentral.com/)
- [<img src="assets/Flag_of_the_United_Kingdom.png" title="englisch" width="20" height="12" alt="englisch" /> Die Interruptliste von Ralph Brown](http://ctyme.com/intr/int.htm)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11447/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1616/index.html)

<!-- MediaWiki page 1616; revision 11447; parent 10925; 2020-08-02T21:59:26Z -->
