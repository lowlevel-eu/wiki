# Tastatur

Die Tastatur ist das wichtigste Eingabegerät eines konsolenbasierten Computers, wird jedoch auch für die Bedienung einer [GUI](Graphical-User-Interface.md "GUI") vielfach benutzt. Zur Ansteuerung der Tastatur verfügen x86-basierte Systeme seit jeher über einen [Keyboard-Controller (KBC)](Keyboard-Controller.md "Keyboard Controller"); Die elektrische Verbindung erfolgt dabei über einen DIN-Stecker oder den PS/2-Anschluss. Heutzutage werden Tastaturen jedoch häufig über [USB](Universal-Serial-Bus.md "USB") angeschlossen.

## KBC

Siehe Artikel [Keyboard Controller](Keyboard-Controller.md "Keyboard Controller").

## USB

Aus Kompatibilitätsgründen stellt das BIOS der meisten Computer einen sog. "Legacy USB Support" bereit, sodass sich auch Tastaturen, die mit einem USB-Kabel angeschlossen sind, wie eine PS/2-Tastatur über den KBC ansteuern lassen. Unterstützt das BIOS jedoch keinen "Legacy Support", oder übernimmt das Betriebssystem die Kontrolle über den USB Host-Controller, entfällt diese Möglichkeit, sodass ein Treiber für eine USB-Tastatur notwendig wird.

Die Spezifikation "Device Class Definition for Human Interface Devices (HID)" definiert in Version 1.11 neben zahlreichen flexiblen Konfigurationsmöglichkeiten ein sog. "Boot Interface" für Mäuse und Tastaturen, über das bereits das BIOS mit diesen kommunizieren kann, ohne dass ein umfangreicher Treiber notwendig wäre. Der Emfpang von Eingaben über diese Schnittstelle erfolgt an dem von der Tastatur bereitgestellten Interrupt-Endpoint (IN). Die Steuerung der LEDs erfolgt über EP0 oder optional einen Out-Interrupt-Endpoint.

Am Interrupt-Endpoint (IN) einer "Boot-Tastatur" werden Pakete von folgender Struktur empfangen:

| Byte | Beschreibung |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0 | Status der "Modifier-Keys". Bit 0: Strg (links), Bit 1: Umschalt (links), Bit 2: Alt (links), Bit 3: GUI (links)<br>Bit 4: Strg (rechts), Bit 5: Umschalt (rechts), Bit 6: Alt (rechts), Bit 7: GUI (rechts)<br> |
| 1 | Reserviert (konstant). |
| 3-7 | Gedrückte Tasten 1-6 (Usage-IDs) |

Im Gegensatz zu PS/2-Tastaturen (N-Tasten-Rollover) sind USB-Boot-Tastaturen auf 6-Tasten-Rollover beschränkt (es können maximal 6 gleichzeitige Tastendrücke erfasst werden). Die von der Tastatur gesendeten Codes sind die "Usage ID"-Werte, die der "HID Usage Tables" (Version 1.12) entnommen werden können.

Die Kommunikation erfolgt - im Gegensatz zum PS/2-Port - in festen Intervallen (standardmäßig: alle 500ms), sowie zusätzlich beim Eintreten einer Änderung am Gerät (Tastendruck). Das Gerät meldet dabei nur, welche Tasten zum Abfragezeitpunkt gedrückt sind, sodass der Treiber das Loslassen von Tasten anhand einer ausbleibenden Tastendruck-Meldung erkennen muss.

Die LEDs (Caps-Lock, Scroll-Lock, Num-Lock) können mittels eines Out-Reports gesteuert werden. Dieser besteht aus einem Byte mit unten stehender Kodierung. Dieses Byte kann an den optional vorhandenen Interrupt-Out-Endpoint oder alternativ als Control-Transfer an EP0 gesandt werden. Der Control-Transfer folgt dabei der üblichen Struktur:

    SETUP: type=0x21, req=0x09, hiVal=2, loVal=0, index=Interfacenummer, length=1
    OUT:   1 Byte; Bits entsprechen gewünschtem Status der LED (an/aus)
           Bit 0: Num-Lock, Bit 1: Caps-Lock, Bit 2: Scroll-Lock
    IN:    Handshake, keine Daten

## Weblinks

- [http://www.usb.org/developers/hidpage/ (USB-HID-Spezifikation und HID-Usage-Tables)](http://www.usb.org/developers/hidpage/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11442/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1929/index.html)

<!-- MediaWiki page 1929; revision 11442; parent 11270; 2020-08-02T21:55:43Z -->
