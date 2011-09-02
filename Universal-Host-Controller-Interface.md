# Universal Host Controller Interface

**Hinweis:**

Der Autor kannte sich bei Erstellung des Artikels nicht besonders mit dem Thema aus. Da dieses Thema aber dringend nach einem Artikel verlangte (z. B. aufgrund eines Eintrags in der [TODO](https://github.com/lowlevel-eu/wiki/wiki/TODO "TODO")-Liste), hat er sich dennoch entschieden, seine Kenntnisse niederzuschreiben.

Wenn **du** dich mit diesem Thema einigermaßen auskennst, dann bist du **jetzt** aufgerufen, diesen Artikel zu erweitern und/oder zu korrigieren (oder natürlich diesen Hinweis zu entfernen, wenn du den Artikel für korrekt befindest)!

Das UHCI ist neben dem [OHCI](https://github.com/lowlevel-eu/wiki/wiki/Open-Host-Controller-Interface "Open Host Controller Interface") ein Interface für [USB](https://github.com/lowlevel-eu/wiki/wiki/Universal-Serial-Bus "USB")-1.x-Hostcontroller.

## Verwendete Datenstrukturen

Relativ wenig der tatsächlichen Steuerung des UHC (Universal Host Controller) findet über die unten genannten Register (s. [I/O-Raum](#io-raum)) ab. Er wird meist nur einmal initialisiert und später werden nur Gründe für Interrupts ausgelesen oder der aktuelle Status der Rootports abgefragt.

Die eigentlichen USB-Transaktionen werden jedoch über Datenstrukturen abgewickelt, die im Hauptspeicher liegen und deren Wurzel die Frameliste ist. Diese verzweigt dann zu Warteschlangenköpfen (Queue Heads, QH) und zu Transferdeskriptoren (Transfer Descriptors, TD), welche dann einzelne Transaktionen steuern.

Vorweg sei gesagt: Wenn in einem DWord ein Pointer anzugeben ist, dann wird er immer komplett in dieses DWord geschrieben. Felder, die nicht zum Pointer gehören, bedeuten, dass die entsprechenden Bits der Adresse 0 sein müssen. Sind z. B. die Bits 4 &#150; 31 für den Pointer reserviert (und der restliche Platz für andere Felder), dann müssen dort die Bits 4 &#150; 31 des Pointers eingetragen werden. Die niederwertigsten vier Bit der Adresse müssen dann 0 sein, d. h. der Puffer ist an 16 Byte auszurichten.

Alle nicht erwähnten Bits sind reserviert und (wenn nicht anders ausgezeichnet) auf 0 zu setzen.

### Frameliste

Die Frameliste ist ein Array mit 1024 Einträgen zu je vier Byte, das im Speicher an einer 4-kB-Grenze liegen muss (die unteren 12 Bit der Adresse sind also 0). Jeder dieser Einträge entspricht einem Frame und weist den Hostcontroller zu bestimmten Transaktionen an (bzw. weist auf den Beginn einer Liste von Transaktionen).

Ein Eintrag ist wie folgt aufgebaut:

| Bits | Bezeichnung | Bedeutung |
| ------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | Frame List Pointer | Dieses Feld enthält die physische Adresse eines QH oder eines TD. |
| 1 | QH/TD Select | Ist dieses Bit gesetzt, dann zeigt der FLP auf einen QH, sonst zeigt er auf einen TD. |
| 0 | Terminate | Der Link ist nur gültig, wenn dieses Bit gelöscht ist. Ist es gesetzt, so wird der HC (Hostcontroller) dem Link nicht folgen. |

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
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | QELP | Physische Adresse des ersten Elements in der hier beginnenden vertikalen Liste (entweder QH oder TD). Dieser Wert wird vom HC angepasst, wenn er das nächste Element in der Warteschlange lädt. |
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

| Bits | Bezeichnung | Bedeutung |
| ------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 4 | Link Pointer | Pointer zum nächsten TD (oder auch QH) in der Warteschlange (oder allgemeiner Liste, wenn der TD sich in keiner Warteschlange befindet) |
| 2 | Depth/Breadth Select | Ist nur gültig, wenn sich der TD in einer Warteschlange befindet. Gibt an, ob die Warteschlangen horizontal oder vertikal abgearbeitet werden. Ist es gesetzt, so wird vertikal gearbeitet, das heißt, diese Warteschlange ist komplett abzuarbeiten, bis der nächste QH an die Reihe kommt (nützlich z. B., wenn man nur einen einzigen QH hat oder nach Priorität sortieren möchte). Wenn es gelöscht ist, wird hingegen horizontal gearbeitet, sobald ein TD aus der Warteschlange fertig ist, geht der HC sofort zum nächsten QH (nützlich, wenn man für jede USB-Pipe einen QH hat). |
| 1 | QH/TD Select | Zeigt an, ob es sich beim nächsten Element um einen TD oder einen QH handelt. |
| 0 | Terminate | Ist das Bit gesetzt, so ist der TD der letzte in der Liste. |

#### Control and Status

| Bits | Bezeichnung | Bedeutung |
| ------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 29 | SPD | Gibt an, ob weniger Bytes als erwartet empfangen wurden (gilt nur, wenn sich der TD in einer Warteschlange befindet). Der HC setzt dieses Bit nur, wenn kein Fehler aufgetreten ist. |
| 28/27 | C_ERR | Gibt die Anzahl von Fehlern an, bis die Übertragung als fehlgeschlagen gewertet werden soll und der TD als inaktiv markiert wird. Ist dieser Wert 0, dann gibt es keine Fehlerbegrenzung. Entsprechende Fehler sind: CRC-Fehler, Timeout, Pufferfehler oder Bitstufffehler (bei STALL oder Babble wird die Übertragung unabhängig von diesem Wert sofort als fehlgeschlagen angesehen). Bei einem NAK beachtet der HC diesen Wert nicht und beginnt die Übertragung einfach erneut. |
| 26 | LS | Ist gesetzt, wenn eine Low-Speed-Transaktion durchgeführt werden soll. |
| 25 | IOS | Muss gesetzt werden, um einen Isochronous-Transfer durchzuführen. Der HC markiert den TD dabei in jedem Fall als inaktiv, unabhängig davon, wie die Übertragung beendet wurde. |
| 24 | IOC | Ist dieses Flag gesetzt, dann wird beim Abschluss der Übertragung ein Interrupt ausgelöst. Der Hostcontroller kann sich damit allerdings Zeit lassen, häufig wird er erst am Ende des Frames ausgelöst. |
| 23 | Active | Muss vom HCD gesetzt werden, um die Transaktion durchzuführen. Der HC löscht das Bit, sobald der Transfer beendet ist. |
| 22 | Stalled | Gibt *nicht* ausschließlich, wie man denken könnte, an, ob ein STALL-Handshake empfangen wurde, sondern „nur“, ob ein so schwerer Fehler aufgetreten ist, dass der TD als inaktiv markiert wurde. Dazu gehört unter anderem auch ein STALL-Handshake, tritt ein solcher bei SETUP-Transaktionen auf, so wird gleichzeitig das CRC/Timeout-Bit gesetzt. |
| 21 | Data Buffer Error | Falls gesetzt, ist ein Pufferfehler aufgetreten (Overrun: Daten zu schnell empfangen, HC kommt mit der Verarbeitung nicht nach; Underrun: Daten können nicht schnell genug gesendet werden). In beiden Fällen wird die Übertragung beim Zielgerät automatisch ungültig gemacht. |
| 20 | Babble Detected | Wenn mehr Daten als erwartet empfangen wurden, ist dieses Bit gesetzt. Es zeigt einen schweren Fehler an, da ein Gerät so anderen Geräten Busbandbreite „stehlen“ kann. Der HC setzt das Stalled-Bit, deaktiviert den TD und fährt sofort mit dem nächsten Frame fort. |
| 19 | NAK Received | Falls ein NAK empfangen wurde, wird dieses Bit gesetzt (kein Fehler, Transaktion wird automatisch neu begonnen). Wurde dieses NAK beim Senden eines SETUP-Pakets empfangen, wird zusätzlich das CRC/Timeout-Flag gesetzt. |
| 18 | CRC/Time Out Error | Wird bei IN-Transaktionen gesetzt, wenn ein CRC-Fehler aufgetreten ist und bei OUT- oder SETUP-Transfers, falls kein Handshake erhalten wurde (was auf einen CRC-Fehler hindeutet, natürlich kann aber auch einfach gar kein Verbindung bestehen). |
| 17 | Bitstuff Error | Wird gesetzt, wenn beim Empfang mehr als sechs gesetzte Bits hintereinander empfangen wurden (das USB-Bitstuffing sollte genau das verhindern). |
| 10 &#150; 0 | Actual Length | Gibt die Anzahl von Bytes minus eins an, die tatsächlich übertragen wurden. Wurden keine Daten übertragen, beträgt der Wert 0x7FF. |

#### Token

| Bits | Bezeichnung | Bedeutung |
| -------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 21 | Maximum Length | Gibt an, wie viele Bytes übertragen werden sollen, minus eins. Der Wert 0x007 steht also für 8 Bytes. Ist der Wert 0x7FF, so werden keine Daten übertragen. Werte zwischen 0x500 und 0x7FE (über 1280) sind nicht erlaubt und resultieren in einem HC-Fehler (1280 ist die maximale Anzahl von Bytes, die in einen Frame passen, von der USB-Spezifikation sind nur 1024 erlaubt). Zu beachten ist jedoch, dass der UHC keine Kenntnis von der maximalen Paketgröße hat, die der Endpoint besitzt, sodass er alle Daten in einem Rutsch sendet (dieser Wert sollte die maximale Paketgröße des Endpoints also nicht überschreiten; **TODO:** *Stimmt das wirklich?*). |
| 19 | Data Toggle | Muss für Isochronous-Transfers immer 0 sein. Für alle anderen Übertragungen gibt es das zu verwendende oder zu erwartende Toggle-Bit an (0 für DATA0 und 1 für DATA1). Für SETUP-Transfers ist es laut USB-Spezifikation ebenfalls immer 0. |
| 18 &#150; 15 | Endpoint | Enthält die Nummer des Endpoints. |
| 14 &#150; 8 | Device Address | Enthält die Geräteadresse. |
| 7 &#150; 0 | Packet Identification | Enthält den Typ des Pakets, ein Nibble ist jeweils das Einerkomplement des anderen. Erlaubt sind nur IN (0x69), OUT (0xE1) und SETUP (0x2D). Alle anderen Werte resultieren in einem HC-Fehler. |

#### Buffer Pointer

Dieses DWord enthält die physische Adresse des Puffers, in den empfangene Daten geschrieben (IN) oder aus dem Daten gelesen und gesendet werden (OUT, SETUP) sollen. Da das komplette Feld für die Adresse reserviert ist, muss dieser Speicherbereich nur an Bytegrenzen (also praktisch gar nicht) ausgerichtet werden.

### Zusammenspiel

[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/52d4009af5bf1cb705f6.png" width="300" height="194" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cc8925c9c6aa817eee9c.png) [](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/cc8925c9c6aa817eee9c.png "vergrößern")Schema aus der UHCI-Spezifikation

Wie spielen nun diese Datenstrukturen zusammen? Wie bereits gesagt ist die Frameliste die Wurzel des ganzen. Dort trägt man in jedes Feld einen Pointer auf die spezifisch in diesem Frame auszuführenden periodischen Transfers (Isochronous-TDs oder Interrupt-QHs mit deren TDs) ein. Am Ende dieser Liste von periodischen Transfers sollte dann der erste QH der aperiodischen Transfers folgen. Womit ein QH korrespondiert, ist ziemlich egal. Er kann einer USB-Pipe entsprechen, man kann aber auch einfach einen einzigen QH für alle aperiodischen Transfers anlegen, an den alle Transferdeskriptoren angehangen werden.

Jeder QH enthält also einen Pointer zum Beginn einer Warteschlange, die nach und nach vom HC abgearbeitet wird. Diese Warteschlange wird in den meisten Fällen nur TDs enthalten. Jedes TD korrespondiert (wie bereits gesagt) zu einem USB-Transfer, dabei gibt es die Möglichkeiten SETUP, IN und OUT. Der HCD (Host Controller Driver, also Hostcontrollertreiber) hängt somit nach und nach neue Transaktionen in die Warteschlange ein, die vom HC dann abgearbeitet werden. Dieser aktualisiert dazu immer den Pointer zum nächsten Transfer in der Warteschlange im QH.

## Interface

Das UHCI ist &#150; wie andere USB-Hostcontrollerinterfaces auch &#150; häufig als [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Gerät ausgeführt. Allen UHCIs gemein ist der Classcode 0x0C (Serielle Buscontroller), der Subclasscode 0x03 (USB-Hostcontrollerinterfaces) und das Programming Interface 0x00 (UHCI). Anhand dieser drei Werte kann man einen UHCI also auf dem PCI-Bus identifizieren und den entsprechenden Treiber aufrufen.

### I/O-Raum

Jedes UHCI besitzt einen I/O-Raum, der aus dem PCI-Konfigurationsraum ausgelesen werden muss. In ihm kann man den Status der Rootports sowie des Hostcontrollers allgemein auslesen oder verändern, sowie letzteren initialisieren und dabei auch den Beginn der Frameliste eintragen. Dieser ist wie folgt aufgebaut:

| Offset | Name | Bits | Bedeutung |
| -------- | ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| 0x00 | USBCMD | 16 | Enthält Flags zum Steuern des Hostcontrollers. |
| 0x02 | USBSTS | 16 | Zeigt den Status des Hostcontrollers an. |
| 0x04 | USBINTR | 16 | Gibt an, bei welchen in USBSTS gesetzten Bits ein Interrupt ausgelöst werden soll. |
| 0x06 | FRNUM | 16 | Enthält die aktuelle Framenummer (0 bis 2047, wobei in der Frameliste nur die unteren 10 Bits (also 0 bis 1023) verwendet werden). |
| 0x08 | FRBASEADD | 32 | Hier muss der physische Pointer zur Frameliste eingetragen werden (an 4 kB ausgerichtet). |
| 0x0C | SOFMOD | 8 | Gibt an, wie lange ein USB-Frame genau dauern soll. |
| 0x10 | PORTSC1 | 16 | Enthält Flags zum Steuern und Informationen über den ersten Rootport. |
| 0x12 | PORTSC2 | 16 | Dasselbe für den zweiten Rootport. |

Hinweis: Nach PORTSC1 und PORTSC2 können noch weitere Rootport-Ports folgen. Wie viele das maximal sind, muss aus der Länge des I/O-Raums ermittelt werden (Länge ist vom PCI-Treiber festzustellen). Außerdem ist in jedem Port Bit 7 gesetzt (0x0080), sodass man testen kann, ab welchem Port entweder Bit 7 nicht mehr gesetzt oder 0xFFFF zu lesen ist. An der Stelle sind dann die Rootport-Ports zu Ende (wobei mehr als sieben Rootports eher unwahrscheinlich sind, wenn man mehr gefunden hat, sollte man davon ausgehen, dass es nur zwei gibt).

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
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| 10 &#150; 0 | Frame number | Aktuelle Framenummer, als Index in der Frameliste werden nur die Bits 0 bis 9 (Werte 0 bis 1023) verwendet. |

#### FLBASEADD

| Bit | Name | Bedeutung |
| -------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 31 &#150; 12 | Base Address | Physische Adresse der Frameliste (bzw. die oberen 20 Bit davon, die unteren 12 Bit müssen auf 0 gesetzt sein (d. h., der Bereich muss an 4 kB ausgerichtet werden)). |
| 11 &#150; 0 | Reserved | Müssen als 0 geschrieben werden, der Hostcontroller kann hier während des Benutzens der Liste den Offset des aktuellen Elements eintragen (sodass das gesamte Register dann die physische Adresse des aktuell bearbeiteten Elements enthält). |

#### SOFMOD

Das oberste Bit in diesem Register ist reserviert, mit den unteren sieben kann man die genaue Länge eines Frames modifizieren. Sie beträgt 11936 Bitzeiten + der eingetragene Wert (normalerweise wird 64 eingetragen, sodass die Framelänge 12000 Bitzeiten beträgt, das ist genau eine Millisekunde).

#### PORTSC

Wie bereits angedeutet gibt es für jeden Rootport ein solches Register am Ende des I/O-Raums. Laut UHCI-Spezifikation sind dies normalerweise zwei Ports, sodass sich ein PORTSC-Register (PORTSC1) am Offset (im I/O-Raum) 0x10 und das für den zweiten Rootport (PORTSC2) bei 0x12 befindet (PORTSC3 wäre dann bei 0x14, PORTSC4 bei 0x16, usw.).

| Bit | Name | Bedeutung |
| ----- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12 | Suspend | Gibt an, ob sich der Port im Suspendmodus befindet. Dieses Bit sollte nicht gleichzeitig mit dem Global Suspend Mode verwendet werden. |
| 9 | Port Reset | Wird dieses Bit gesetzt, dann wird das Resetsignal auf dem USB getrieben. Der HCD muss dafür Sorge tragen, dass es nach der vorgesehen Zeit (50 ms) wieder gelöscht wird. |
| 8 | Low Speed Device Attached | Dieses Flag gibt an, ob ein Low-Speed-Gerät angeschlossen ist. Wenn es nicht gesetzt ist, dann ist logischerweise ein Full-Speed-Gerät angeschlossen (oder gar keins, wenn Current Connect Status 0 ist). |
| 7 | Reserved | Dieses Bit wird immer als 1 gelesen und kann daher dazu dienen, die tatsächliche Anzahl der Rootports herauszufinden (s. Hinweis bei [I/O-Raum](https://github.com/lowlevel-eu/wiki/wiki/Universal-Host-Controller-Interface#io-raum "Universal Host Controller Interface")). |
| 6 | Resume Detect | Wenn ein Gerät ein Remote Wakeup sendet, dann wird dieses Bit gesetzt. Außerdem kann der HCD dieses Bit setzen, um selektiv an diesem Port ein Resumesignal zu treiben. Nach der von der USB-Spezifikation vorgesehenen Zeitspanne (sollten 20 ms sein) muss es vom HCD wieder aufgehoben werden. |
| 5/4 | Line Status | Gibt den Status der Datenleitungen (D+/D-) wieder. So können einige Fehler entdeckt werden (sind z. B. beide Leitungen gleich, dann hängt vermutlich kein Gerät am Bus). D+ entspricht Bit 4, D- Bit 5. |
| 3 | Port Enable/Disable Change | Hat der HC den Rootport selbst deaktiviert (wegen eines schweren Fehlers oder dem Disconnect des Geräts), dann wird dieses Bit gesetzt. Analog zum Connect-Status-Change-Bit muss es durch Schreiben einer 1 gelöscht werden. |
| 2 | Port Enabled/Disabled | Um den Port zu aktivieren, muss dieses Flag auf 1 gesetzt werden. Ist es 0, so werden keine Daten am Port ausgegeben und auch keine in Empfang genommen. Dieses Bit kann auch vom HC selbst gelöscht werden, wenn ein schwerer Fehler aufgetreten ist oder das Gerät entfernt wurde. |
| 1 | Connect Status Change | Wenn ein Gerät angesteckt oder entfernt wird, dann wird dieses Bit gesetzt. Um es zu löschen, muss eine 1 hineingeschrieben werden. |
| 0 | Current Connect Status | Ist ein Gerät an diesen Rootport angeschlossen, so ist dieses Bit 1. Es kann vom HCD nicht beschrieben werden. |

## Initialisierung

Leider enthält die UHCI-Spezifikation keine Anleitung, wie dies zu bewerkstelligen ist (im Gegensatz zur OHCI- oder EHCI-Spezifikation). Deshalb sei hier ein Weg dargestellt, der vielleicht ein Overkill ist, aber zumindest bei mir funktioniert.

### Informationen vom PCI-Treiber holen

Zuerst muss die Adresse des I/O-Raums (und wenn möglich auch dessen Größe) sowie die IRQ-Nummer vom PCI-Treiber herausgefunden werden. Anschließend sollten beide Resourcen registriert bzw. reserviert werden, außerdem sollten sowohl I/O-Raum als auch die Busmasterfunktionalität aktiviert werden (indem 0x05 ins Commandregister geschrieben wird).

### Reset

Nun muss der UHCI nicht nur zurückgesetzt, sondern auch komplett in Besitz genommen werden (es ist sehr gut möglich, dass das BIOS derzeit über den Controller verfügt).

#### USB-Reset und Rootports

Zuerst sollte ein globaler USB-Reset auf allen aktivierten Ports getrieben werden. Dies geschieht, indem das GRESET-Bit im USBCMD-Register (USBCMD.GRESET) gesetzt wird. Außerdem kann man hierbei auch gleich alle anderen Bits in diesem Register löschen, sodass der Controller anhält. Nach 50 Millisekunden muss das Resetsignal wieder aufgehoben werden, indem das GRESET-Bit wieder gelöscht wird.

Jetzt muss die Anzahl der vorhanden Rootports in Erfahrung gebracht werden. Hierzu nimmt man zunächst die Größe des I/O-Raums minus 0x10 und geteilt durch 2 als Obergrenze und 2 als Untergrenze. Jetzt wird für jeden Rootport überprüft, ob sowohl Bit 7 gesetzt ist (0x0080) als auch der Gesamtwert nicht 0xFFFF ist. Ist das Bit nicht gesetzt oder beträgt der Wert 0xFFFF, so handelt es sich beim verwendeten Port um keinen I/O-Port für einen Rootport mehr. Beispielcode:

\<c\>int root_ports = (io_space_size - 0x10) / 2; for (int i = 2; i \< root_ports; i++) {

       if (!(inw(io_space + 0x10 + i*2) & 0x0080) || (inw(io_space + 0x10 + i*2) == 0xFFFF))
       {
           root_ports = i;
           break;
       }

}\</c\>

Mehr als sieben Rootports sind unwahrscheinlich, in diesem Fall sollten nur zwei verwendet werden.

#### Deaktivieren des Legacy Supports

Normalerweise ist der USB-Legacy-Support etwas tolles. Mit ihm können USB-Sticks oder -Diskettenlaufwerke per int 13h angesprochen werden und Tastaturen und Mäuse verhalten sich wie PS/2-Geräte. Wenn wir selbst die Kontrolle über einen USB-Hostcontroller übernehmen wollen, ist dieser Support oft lästig, weil sich das BIOS oft regelrecht am Controller festgesaugt hat. So genügt es nicht, den Controller einfach nur zurückzusetzen und die Interrupts abzufangen, da das BIOS sich vom HC einen SMI generieren lässt, sodass wir am Ende in die Röhre schauen, falls dieser nicht abgeschaltet wird (da man normale IRQs (also PCI-IRQs) benutzen möchte).

Zuerst ist festzustellen, ob der HC überhaupt schon benutzt wurde. Wenn nicht, so können wir uns den folgenden Reset sparen. Ein Reset ist nötig, wenn entweder USBCMD.RS, USBCMD.CF oder ein Bit im USBINTR-Register gesetzt sind. Er ist außerdem notwendig, wenn das USBCMD.EGSM-Bit gelöscht ist. Weiterhin gibt es im PCI-Konfigurationsraum des Geräts das LEGSUP-Register (Legacy Support). Es befindet sich am Offset 0xC0 und ist 16 Bit lang. Wenn eine binäre UND-Operation mit dem Wert 0x00BF ein Ergebnis ungleich 0 liefert, so muss ebenfalls ein kompletter Reset durchgeführt werden (da dann der Legacy Support aktiviert ist).

Dieser Reset beginnt mit dem Reset des Hostcontrollers an sich. Dazu wird 0x3F ins USBSTS-Register geschrieben, damit der Controller keine Interrupts auslöst. Anschließend sollte eine Millisekunde gewartet werden, damit der HC auf jeden Fall angehalten ist. Nun werden alle Legacy-Support-Statusbits im LEGSUP-Register gelöscht, dies geschieht, indem 0x8F00 hineingeschrieben wird. Danach kann der HC wirklich selbst zurückgesetzt werden, indem das Bit USBCMD.HCRESET gesetzt wird. Der HC löscht dieses Bit selbstständig, sobald der Reset abgeschlossen ist.

Jetzt ist es ratsam, 0 ins USBINTR-Register zu schreiben, ebenfalls, damit keine IRQs auftreten. Danach sollte auch ins USBCMD-Register 0 geschrieben werden, genau wie in alle Rootportregister (um alle Rootports zu deaktivieren).

Nun sollte der Reset abgeschlossen sein.

### Konfiguration

Das UHCI ist jetzt bereit, konfiguriert zu werden. Als erstes kann man die Länge eines Frames mit dem SOFMOD-Register verstellen, ratsam ist hier der Standardwert von 0x40 für eine Millisekunde. Anschließend sollte die physische Adresse der Frameliste eingetragen (Register FRBASEADD) und die aktuelle Framenummer (FRNUM) auf 0 zurückgesetzt werden.

Um PCI-IRQs generieren zu lassen, ist es notwendig, dies im LEGSUP-Register im PCI-Konfigurationsraum (s. [Deaktivieren des Legacy Supports](#deaktivieren-des-legacy-supports)) deutlich zu machen, indem 0x2000 hineingeschrieben wird.

Der Hostcontroller ist jetzt bereit, die Abarbeitung der Frameliste zu beginnen. Dies wird mit dem Setzen von USBCMD.RS und USBCMD.CF ausgelöst. Es ist möglich, USBCMD.MAXP zu setzen. Anschließend sollte USBCMD.FGR für 20 ms gesetzt werden, um den HC (falls nötig) aus dem globalen Suspendmodus zu befreien, damit auch wirklich SOF-Token gesendet werden und der USB benutzt werden kann. Danach muss dieses Bit wieder gelöscht werden, um das Resumesignal aufzuheben. Nun sollte wohl noch ca. 10 ms gewartet werden, bis alle Geräte betriebsbereit sind.

  
An diesem Punkt arbeitet der UHC die Frameliste und alle verlinkten Warteschlangen und die Transfers darin ab. Allerdings sind vermutlich alle Rootports deaktiviert und müssen manuell aktiviert werden (oder sind in einem undefinierten Zustand, wenn sie nicht im Zuge des Komplettresets deaktiviert wurden).

## Weblinks

- [Universal Host Controller Interface (UHCI) Design Guide Revision 1.1](http://download.intel.com/technology/usb/UHCI11D.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10116/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1576/index.html)

<!-- MediaWiki page 1576; revision 10116; parent 7318; 2011-09-02T15:50:19Z -->
