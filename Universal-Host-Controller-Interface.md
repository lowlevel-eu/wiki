# Universal Host Controller Interface

**Hinweis:**

Der Autor kannte sich bei Erstellung des Artikels nicht besonders mit dem Thema aus. Da dieses Thema aber dringend nach einem Artikel verlangte (z. B. aufgrund eines Eintrags in der [TODO](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO")-Liste), hat er sich dennoch entschieden, seine Kenntnisse niederzuschreiben.

Wenn **du** dich mit diesem Thema einigermaßen auskennst, dann bist du **jetzt** aufgerufen, diesen Artikel zu erweitern und/oder zu korrigieren (oder natürlich diesen Hinweis zu entfernen, wenn du den Artikel für korrekt befindest)!

Das UHCI ist neben dem [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "Open Host Controller Interface") ein Interface für [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")-1.x-Hostcontroller.

## Verwendete Datenstrukturen

Relativ wenig der tatsächlichen Steuerung des UHC findet über die unten genannten Register (s. [\#I/O-Raum](#io-raum)) ab. Er wird meist nur einmal initialisiert und später werden nur Gründe für Interrupts ausgelesen oder der aktuelle Status der Rootports abgefragt.

Die eigentlichen USB-Transaktionen werden jedoch über Datenstrukturen abgewickelt, die im Hauptspeicher liegen und deren Wurzel die Frameliste ist. Diese verzweigt dann zu Warteschlangenköpfen (Queue Heads, QH) und zu Transferdeskriptoren (Transfer Descriptors, TD), welche dann einzelne Transaktionen steuern.

### Frameliste

Die Frameliste ist ein Array mit 1024 Einträgen zu je vier Byte, das im Speicher an einer 4-kB-Grenze liegen muss (die unteren 12 Bit der Adresse sind also 0). Jeder dieser Einträge entspricht einem Frame und weist den Hostcontroller zu bestimmten Transaktionen an (bzw. weist auf den Beginn einer Liste von Transaktionen).

Ein Eintrag ist wie folgt aufgebaut:

| Bits | Bezeichnung | Bedeutung |
| ------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | Frame List Pointer | Dieses Feld enthält die physische Adresse eines QH oder eines TD. Der Wert entspricht den Bits 31 &#150; 4 dieser Adresse, welche also an 16 Byte ausgerichtet sein muss. |
| 1 | QH/TD Select | Ist dieses Bit gesetzt, dann zeigt der FLP auf einen QH, sonst zeigt er auf einen TD. |
| 0 | Terminate | Der Link ist nur gültig, wenn dieses Bit gelöscht ist. Ist es gesetzt, so wird der HC dem Link nicht folgen. |

### Warteschlangenköpfe

Jeder QH kann einerseits auf das nächste Element in der Liste (horizontal) und andererseits auf eine Warteschlange zeigen (vertikal). Es muss immer an einer 16-Byte-Grenze im Speicher liegen.

| Offset | Bezeichnung |
| -------- | ----------------------------------- |
| 0x00 | Queue Head Link Pointer (QHLP) |
| 0x04 | Queue Element Link Pointer (QELP) |

#### QHLP

| Bits | Bezeichnung | Bedeutung |
| ------------- | -------------- | -------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | QHLP | Physische Adresse des nächsten Elements in der horizontalen Liste (entweder ein QH oder ein TD). |
| 1 | QH/TD Select | Gibt an, ob es sich um einen QH oder einen TD handelt (wieder 1 für QH und 0 für TD). |
| 0 | Terminate | Ist dieses Bit 1, so ist dieser QH das letzte Element in der Liste. |

#### QELP

| Bits | Bezeichnung | Bedeutung |
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | QELP | Physische Adresse des ersten Elements in der hier beginnenden vertikalen Liste (entweder QH oder TD). |
| 1 | QH/TD Select | Gibt wieder an, ob es sich um einen QH oder einen TD handelt. |
| 0 | Terminate | Der Link ist nur gültig, wenn dieses Bit gelöscht ist (sonst gibt es keine vertikale Liste). |

### Transferdeskriptoren

Ein Transferdeskriptor bezeichnet einen einzelnen USB-Transfer (wobei man sich nicht um Dinge wie NAK, ACK oder ähnliches kümmern muss). Solche Transfers sind SETUP-, IN- und OUT-Pakete. Ebenso wie QHs müssen sie immer an 16-Byte-Grenzen im Speicher liegen.

| Offset | Bezeichnung |
| -------- | -------------------- |
| 0x00 | Link Pointer (LP) |
| 0x04 | Control and Status |
| 0x08 | Token |
| 0x0C | Buffer Pointer |

#### LP

*TODO*

#### Control and Status

*TODO*

#### Token

*TODO*

#### Buffer Pointer

*TODO*

### Zusammenspiel

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/52d4009af5bf1cb705f6.png" width="300" height="194" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cc8925c9c6aa817eee9c.png) [](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cc8925c9c6aa817eee9c.png "vergrößern")Schema aus der UHCI-Spezifikation

Wie spielen nun diese Datenstrukturen zusammen? Wie bereits gesagt ist die Frameliste die Wurzel des ganzen. Dort trägt man in jedes Feld einen Pointer auf die spezifisch in diesem Frame auszuführenden periodischen Transfers (Isochronous-TDs oder Interrupt-QHs mit deren TDs) ein. Am Ende dieser Liste von periodischen Transfers sollte dann der erste QH der aperiodischen Transfers folgen. Womit ein QH korrespondiert, ist ziemlich egal. Er kann einer USB-Pipe entsprechen, man kann aber auch einfach einen einzigen QH für alle aperiodischen Transfers anlegen, an den alle Transferdeskriptoren angehangen werden.

*TODO*

## Interface

Das UHCI ist &#150; wie andere USB-Hostcontrollerinterfaces auch &#150; häufig als [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Gerät ausgeführt. Allen UHCIs gemein ist der Classcode 0x0C (Serielle Buscontroller), der Subclasscode 0x03 (USB-Hostcontrollerinterfaces) und das Programming Interface 0x00 (UHCI). Anhand dieser drei Werte kann man einen UHCI also auf dem PCI-Bus identifizieren und den entsprechenden Treiber aufrufen.

### I/O-Raum

Jedes UHCI besitzt einen I/O-Raum, der aus dem PCI-Konfigurationsraum ausgelesen werden muss. In ihm kann man den Status der Rootports sowie des Hostcontrollers allgemein auslesen oder verändern, sowie letzteren initialisieren und dabei auch den Beginn der Frameliste eintragen. Dieser ist wie folgt aufgebaut:

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

#### FRNUM

| Bit | Name | Bedeutung |
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10 &#150; 0 | Frame number | Aktuelle Framenummer, als Index in der Frameliste werden nur die Bits 0 bis 9 (Werte 0 bis 1023) verwendet, diese werden auch in SOF-Token auf dem USB verwendet. |

#### FLBASEADD

| Bit | Name | Bedeutung |
| -------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 12 | Base Address | Physische Adresse der Frameliste (bzw. die oberen 20 Bit davon, die unteren 12 Bit müssen auf 0 gesetzt sein (d. h., der Bereich muss an 4 kB ausgerichtet werden)). |
| 11 &#150; 0 | Reserved | Müssen als 0 geschrieben werden, der Hostcontroller kann hier während des Benutzens der Liste den Offset des aktuellen Elements eintragen (sodass das gesamte Register dann die physische Adresse des aktuell bearbeiteten Elements enthält). |

#### SOFMOD

Das oberste Bit in diesem Register ist reserviert, mit den unteren sieben kann man die genaue Länge eines Frames modifizieren. Sie beträgt 11936 ms + der eingetragene Wert (normalerweise wird 64 eingetragen, sodass die Framelänge 12000 ms beträgt).

#### PORTSC

Wie bereits angedeutet gibt es für jeden Rootport ein solches Register am Ende des I/O-Raums. Laut UHCI-Spezifikation sind dies normalerweise zwei Ports, sodass sich ein PORTSC-Register (PORTSC1) am Offset (im I/O-Raum) 0x10 und das für den zweiten Rootport (PORTSC2) bei 0x12 befindet (PORTSC3 wäre dann bei 0x14, PORTSC4 bei 0x16, usw.).

| Bit | Name | Bedeutung |
| ----- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12 | Suspend | Gibt an, ob sich der Port im Suspendmodus befindet. Dieses Bit sollte nicht gleichzeitig mit dem Global Suspend Mode verwendet werden. |
| 9 | Port Reset | Wird dieses Bit gesetzt, dann wird das Resetsignal auf dem USB getrieben. Der HCD muss dafür Sorge tragen, dass es nach der vorgesehen Zeit (50 ms) wieder gelöscht wird. |
| 8 | Low Speed Device Attached | Dieses Flag gibt an, ob ein Low-Speed-Gerät angeschlossen ist. Wenn es nicht gesetzt ist, dann ist logischerweise ein Full-Speed-Gerät angeschlossen (oder gar keins, wenn Current Connect Status 0 ist). |
| 7 | Reserved | Dieses Bit wird immer als 1 gelesen und kann daher dazu dienen, die tatsächliche Anzahl der Rootports herauszufinden (s. Hinweis bei [I/O-Raum](https://github.com/lowlevel-eu/wiki/wiki/Universal-Host-Controller-Interface#io-raum "Universal Host Controller Interface")). |
| 6 | Resume Detect | Wenn ein Gerät ein Remote Wakeup sendet, dann wird dieses Bit gesetzt. Außerdem kann der HCD dieses Bit setzen, um selektiv an diesem Port ein Resumesignal zu treiben. Nach der von der USB-Spezifikation vorgesehenen Zeitspanne (sollten 20 ms sein) muss es vom HCD wieder aufgehoben werden. |
| 4/5 | Line Status | Gibt den Status der Datenleitungen (D+/D-) wieder. So können einige Fehler entdeckt werden (sind z. B. beide Leitungen gleich, dann hängt vermutlich kein Gerät am Bus). D+ entspricht Bit 4, D- Bit 5. |
| 3 | Port Enable/Disable Change | Hat der HC den Rootport selbst deaktiviert (wegen eines schweren Fehlers oder dem Disconnect des Geräts), dann wird dieses Bit gesetzt. Analog zum Connect-Status-Change-Bit muss es durch Schreiben einer 1 gelöscht werden. |
| 2 | Port Enabled/Disabled | Um den Port zu aktivieren, muss dieses Flag auf 1 gesetzt werden. Ist es 0, so werden keine Daten am Port ausgegeben und auch keine in Empfang genommen. Dieses Bit kann auch vom HC selbst gelöscht werden, wenn ein schwerer Fehler aufgetreten ist oder das Gerät entfernt wurde. |
| 1 | Connect Status Change | Wenn ein Gerät angesteckt oder entfernt wird, dann wird dieses Bit gesetzt. Um es zu löschen, muss eine 1 hineingeschrieben werden. |
| 0 | Current Connect Status | Ist ein Gerät an diesen Rootport angeschlossen, so ist dieses Bit 1. Es kann vom HCD nicht beschrieben werden. |

## Weblinks

- [Universal Host Controller Interface (UHCI) Design Guide Revision 1.1](http://www.intel.com/technology/usb/uhci11d.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7241/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1576/index.html)

<!-- MediaWiki page 1576; revision 7241; parent 7239; 2010-03-02T15:18:46Z -->
