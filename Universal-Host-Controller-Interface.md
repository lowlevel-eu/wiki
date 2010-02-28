# Universal Host Controller Interface

**Hinweis:**

Der Autor kannte sich bei Erstellung des Artikels nicht besonders mit dem Thema aus. Da dieses Thema aber dringend nach einem Artikel verlangte (z. B. aufgrund eines Eintrags in der [TODO](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO")-Liste), hat er sich dennoch entschieden, seine Kenntnisse niederzuschreiben.

Wenn **du** dich mit diesem Thema einigermaßen auskennst, dann bist du **jetzt** aufgerufen, diesen Artikel zu erweitern und/oder zu korrigieren (oder natürlich diesen Hinweis zu entfernen, wenn du den Artikel für korrekt befindest)!

Das UHCI ist neben dem [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "Open Host Controller Interface") ein Interface für [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")-1.x-Hostcontroller.

## Interface

Das UHCI ist &#150; wie andere USB-Hostcontrollerinterfaces auch &#150; häufig als [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Gerät ausgeführt. Allen UHCIs gemein ist der Classcode 0x0C (Serielle Buscontroller), der Subclasscode 0x03 (USB-Hostcontrollerinterfaces) und das Programming Interface 0x00 (UHCI). Anhand dieser drei Werte kann man einen UHCI also auf dem PCI-Bus identifizieren und den entsprechenden Treiber aufrufen.

### I/O-Raum

Jedes UHCI besitzt einen I/O-Raum, der aus dem PCI-Konfigurationsraum ausgelesen werden muss. Dieser ist wie folgt aufgebaut:

| Offset | Name | Bits | Bedeutung |
| -------- | ----------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | USBCMD | 16 | Enthält Flags zum Steuern des Hostcontrollers. |
| 0x02 | USBSTS | 16 | Zeigt den Status des Hostcontrollers an. |
| 0x04 | USBINTR | 16 | Gibt an, bei welchen in USBSTS gesetzten Bits ein Interrupt ausgelöst werden soll. |
| 0x06 | FRNUM | 16 | Enthält die aktuelle Framenummer (0 bis 2047, wobei auf dem USB und in der Frameliste nur die unteren 10 Bits (also 0 bis 1023) verwendet werden)). |
| 0x08 | FRBASEADD | 32 | Hier muss der physische Pointer zur Frameliste eingetragen werden (an 4 kB ausgerichtet). |
| 0x0C | SOFMOD | 8 | Gibt an, wie lange ein USB-Frame genau dauern soll. |
| 0x10 | PORTSC1 | 16 | Enthält Flags zum Steuern und Informationen über den ersten Rootport. |
| 0x12 | PORTSC2 | 16 | Dasselbe für den zweiten Rootport. |

Hinweis: Nach PORTSC1 und PORTSC2 können noch weitere Rootport-Ports folgen. Wie viele das sind, muss aus der Länge des I/O-Raums ermittelt werden (Länge ist vom PCI-Treiber festzustellen). Außerdem ist in jedem Port Bit 7 gesetzt (0x0080), sodass man testen kann, ab welchem Port entweder Bit 7 nicht mehr gesetzt oder 0xFFFF zu lesen ist. An der Stelle sind dann die Rootport-Ports zu Ende (wobei mehr als sieben Rootports eher unwahrscheinlich sind, wenn man mehr gefunden hat, sollte man davon ausgehen, dass es nur zwei gibt).

#### USBCMD

| Bit | Name | Bedeutung |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7 | MAXP | Ist dieses Bit gesetzt, so dürfen am Ende eines Frames noch 64-Byte-Pakete gesendet werden, sonst sind nur 32-Byte-Pakete erlaubt. |
| 6 | CF | Dieses Bit hat keine Bedeutung für den Hostcontroller, der Treiber sollte dieses Bit allerdings setzen, wenn er den HC konfiguriert hat, um dies anzuzeigen (so setzt z. B. der BIOS-Legacy-Support-Treiber dieses Bit und kann so als aktiv erkannt werden). |
| 5 | SWDBG | Wenn dieses Flag gesetzt wird, dann wird immer nur eine USB-Transaktion ausgeführt und der HC wird anschließend angehalten, bis das RS-Bit gesetzt wird (danach wird dann wieder nur eine Transaktion durchgeführt, und so weiter). |
| 4 | FGR | Wird dieses Bit gesetzt, dann wird das Resumesignal an allen aktivierten Rootports getrieben. Der HC kann es auch selbstständig setzen, wenn ein entsprechendes Ereignis (Remote Wakeup (K-State), Connect oder Disconnect) eingetreten ist und er sich im globalen Suspendmodus befindet. Das Resumesignal wird erst wieder aufgehoben, wenn dieses Bit gelöscht wird &#150; solch ein Signal sollte 20 ms getrieben werden. |
| 3 | EGSM | Sobald dieses Bit gesetzt wird, werden keine Frames mehr auf dem USB gesendet und der HC befindet sich im globalen Suspendmodus. Dieser muss durch ein globales Resumesignal wieder aufgehoben werden (gleichzeitig muss dann dieses Bit gelöscht werden). |
| 2 | GRESET | Wenn dieses Flag gesetzt wird, dann wird das Resetsignal auf allen Rootports getrieben, außerdem werden u. a. die Rootport-Ports zurückgesetzt. Der HCD muss dieses Bit wieder löschen, um das Signal aufzuheben. |
| 1 | HCRESET | Um den HC so gut wie komplett zurückzusetzen, muss dieses Bit gesetzt werden. Es wird vom UHC automatisch gelöscht, wenn der Reset beendet ist. |
| 0 | RS | Der HC arbeitet nur dann, wenn dieses Bit (Run/Stop) gesetzt ist. Wird es gelöscht, so wird die aktuelle Transaktion beendet und der HC beginnt danach keine weitere, bis dieses Flag wieder gesetzt wird. Der HC selbst kann es in Ausnahmefällen auch selbst löschen, z. B. bei schweren Fehlern (u. a. PCI-Fehler) oder im Debugmodus (SWDBG-Bit). |

Die Bits 8 bis 15 sind reserviert.

#### USBSTS

| Bit | Name | Bedeutung |
| ----- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 5 | HCHalted | Wird gesetzt, wenn das RS-Bit im USBCMD-Register gelöscht wird (egal, von wem). |
| 4 | HC Process Error | Wird gesetzt, falls ein schwerer Fehler auftritt (z. B. eine ungültige Paket-ID in einem TD). Das RS-Bit wird gelöscht (HCHalted dementsprechend gesetzt) und ein IRQ generiert. |
| 3 | Host System Error | Bei schweren Fehlern, die mit dem Hostcontroller selbst und nicht mit dem USB zusammenhängen, wird dieses Bit gesetzt. Dies beinhalted z. B. PCI-Fehler. Wie beim HC Process Error wird das RS-Bit gelöscht und ein IRQ generiert. |
| 2 | Resume Detect | Wenn sich der HC im globalen Suspendmodus befindet und ein USB-Gerät ein Remote-Wakeup-Signal sendet, setzt der UHC dieses Bit. |
| 1 | USB Error | Wird gesetzt, wenn bei einer USB-Transaktion ein Fehler aufgetreten ist. |
| 0 | USBINT | Sobald ein Transferdescriptor mit gesetztem IOC-Bit abgearbeitet wurde (egal, ob mit Fehler oder nicht), wird dieses Bit gesetzt. |

Ist Bit 3 oder 4 gesetzt, dann wird so lange ein IRQ ausgelöst, bis die Bits gelöscht wurden (in diesem Register wird ein Bit gelöscht, indem man es als gesetzt schreibt). Gleiches gilt für die Bits 0 bis 2, allerdings nur dann, wenn im USBINTR-Register die entsprechenden Interrupts aktiviert wurden.

#### USBINTR

| Bit | Name | Bedeutung |
| ----- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 3 | SPI | Wenn dieses Bit gesetzt ist, dann wird ein IRQ ausgelöst, sobald ein zu kurzes Paket empfangen wurde (also kürzer als erwarted). |
| 2 | IOC | Nur wenn dieses Bit gesetzt ist, werden IRQs ausgelöst, wenn Transferdeskriptoren mit gesetztem IOC-Flag bearbeitet wurden. |
| 1 | RI | Wird das Resume-Detect-Bit im USBSTS-Register gesetzt und ist dieses Bit gesetzt, dann wird ein IRQ ausgelöst. |
| 0 | TO/CRC | Gibt es bei einer USB-Transaktion einen Timeout oder einen CRC-Fehler, dann wird bei gesetztem Bit ein IRQ generiert. |

## Weblinks

- [Universal Host Controller Interface (UHCI) Design Guide Revision 1.1](http://www.intel.com/technology/usb/uhci11d.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7210/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1576/index.html)

<!-- MediaWiki page 1576; revision 7210; parent 5202; 2010-02-28T21:58:15Z -->
