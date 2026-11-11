# Ausgabe 8

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 7](Ausgabe-7 "Ausgabe 7") | **Navigation** | [Ausgabe 9](Ausgabe-9 "Ausgabe 9") » |

## Vorwort

Viel Zeit ist vergangen seit der letzten Ausgabe von Lowlevel. Einige Anstrengungen hat es die Redaktion gekostet, all die Artikel zu schreiben und zusammenzusammeln. Am anstrengendsten ist, die Erwartung der Leser auszuhalten. Ständige Fragen wie "Wann ist das Magazin fertig?" und "Wie weit seit ihr?" haben mich schon das ein oder andere Mal zur Weissglut getrieben. Wir sind keine D-Züge. Wir machen dieses Magazin nicht hauptberuflich, sondern haben nebenbei vorallem im "echten Leben" noch haufenweise andere Sachen zu tun. Wir machen dieses Magazin aus Spass, und den wollen wir uns nicht verderben lassen, weil andere Leute drängeln. Wer unter Druck steht, kann keine befriedigende Leistung abgeben. Ich hoffe, dass sich die entsprechenden Leute auch angesprochen fühlen und einfach auf unsere Statusberichte warten. Wir melden uns im Forum von alleine, wenn sich etwas an der Lage geändert hat. Wir haben es trotzdem versucht und wir hoffen, es hat sich gelohnt und ihr habt viel Spass mit dieser Ausgabe. Viel Spass beim Lesen der achten Ausgabe von Lowlevel diesmal wieder unter der Regie von mir,

Joachim Neu.

## News

### MenuetOS

Die neue Beta-Version des bekannten MenuetOS (0.79 pre 1) wurde zusammen mit der neuen Final-Version (0.78) des Betriebssystems freigegeben. Grössere Änderungen wurden mit einem verbesserten Tastaturtreiber, Warteschlangen im Kernel und verschiedenen neuen Programmen gemacht. (<http://www.menuetos.de>)

### ReactOS

Aber auch bei der "Konkurrenz" tut sich etwas. Besonders beim in der letzten Ausgabe vorgestellten ReactOS wird viel gearbeitet. Eine neue Homepage mit neuen Screenshots zeigen den aktuellen Entwicklungsstand von ReactOS, welcher beachtlich ist. (<http://www.reactos.org/xhtml/en/screenshots.html>) Aber nicht nur das Erscheinungsbild der Website wurde verändert. Am 30.10.2005 wurde die neuste Version 0.2.8 freigegeben, welche auf der Homepage downloadbar ist. (<http://www.reactos.de>)

### SkyOS

Bei SkyOS bestimmen zur Zeit Updates und Bugfixes die Neuerungen. SkyOS besticht bereits durch eine einwandfreie GUI, die es mit allen anderen gängigen aufnehmen kann, jedoch vom Design her vereinzelt andere Wege geht. (<http://www.skyos.org>)

## Thema der Ausgabe

### Paging

(Hauptartikel: [Paging](Paging "Paging"))

#### Ein besonderes PMode Feature

Jeder, der auf niedrigster Ebene oder ein eigenes Betriebssystem programmieren will, wird feststellen, wie viele Features man unter dem Protected Mode einer x86-32 CPU verwenden kann. Einer der wichtigsten dieser Features ist Paging, obwohl es erst mit dem 486er eingeführt wurde und die erste Intel 32-Bit PMode CPU, der 386er, diese Technik noch nicht kannte. Dies dürfte aber heutzutage in der Regel nicht mehr allzusehr ins Gewicht fallen. Im folgenden möchte ich nun diese ganz wichtige Technologie kurz beschreiben und euch einen kleinen Überblick bieten.

#### Wieso Paging?

Paging dient zur Implementierung eines virtuellen Speichermanagers. Dadurch kann ein Betriebssystem den verfügbaren Speicherplatz effektiv verwalten und gegebenenfalls Speicherblöcke auf die Festplatte auslagern. Es ist auch möglich, dass jeder Prozess ganze 4 GB Speicher bekommt, ohne dass so viel physikalischer Arbeitsspeicher überhaupt verfügbar ist. Ausserdem können die einzelnen Prozesse voneinander abgetrennt und geschützt werden.

#### Funktionsweise:

Das erste wäre ersteinmal das PageDirectory. Dieses ist 4 KB gross und hat 1024 Einträge zu je 4 Byte. Jeder Eintrag kennzeichnet eine PageTable, daher gibt es insgesamt 1024 PageTables. Die höheren 20 Bits des Eintrages beschreiben die physikalische Adresse der PageTable, in den restlichen niedrigeren 12 Bits stehen Attribute und Eigenschaften der PageTable, wie z.B. ob die PageTable derzeit verfügbar ist, ob nur Programme mit einem CPL von 0, 1 oder 2 auf diese Page zugreifen können oder ob ein Speicherschutz auf die Page wirken soll. Die PageTable ist ebenfalls 4 KB gross und hat wie die PageDirectory wiederum 1024 Einträge. Diesmal kennzeichnen die Einträge einzelne Pages. Paging wird durch das setzten des Paging-Bits (Bit 31) im CR0-Register aktiviert. Die physikalische Adresse der PageDirectory steht im CR3-Register.

#### Virtuelle Speicheradresse Physikalische Speicheradresse:

Bei aktiviertem Paging wandelt die CPU die Speicheradresse, die virtuelle Adresse, in die physikalische Adresse, die Adresse im „richtigen“ Arbeitsspeicher, um und greift darauf zu. Der virtuelle Adressraum ist normalerweise bis 4 GB gross. Dies ergibt sich aus 1024 PageTables \* 1024 Pages je PageTable \* 4 KB je Page. Der physikalische Adressraum ist so gross wie der vorhandene Arbeitsspeicher. Ein Betriebssystem kann dann für jeden Prozess ein eigenes PageDirectory verwenden und hat somit seine eigenen 4 GB zur Verfügung. Die Verwaltung des physikalischen Speichers liegt alleine in den Händen des Betriebssystems. Es ist auch möglich an mehreren virtuellen Adressen den gleichen physikalischen Speicher hinzumappen, der in Wirklichkeit nur einmal im Arbeitsspeicher existiert.

Für die Adressumwandlung zerlegt die CPU die virtuelle Adresse in 3 Teile:

PageDirectory-Eintrag: Die höchsten 10 Bits (Bits 22 – 31) geben den Index der PageTable in der PageDirectory an.

PageTable-Eintrag: Die folgenden 10 Bits (Bits 12 – 21) geben den Index der Page in der ausgewählten PageTable an.

Page-Offset: Die niedrigen 12 Bits (Bits 0 – 11) geben die Offset Adresse innerhalb der Page an.

#### Aufbau eines PageDirectory-Eintrages:

Der 4 Byte grosse PageDirectory-Eintrag beinhaltet in den höheren 20 Bits die physikalische Adresse der Page. In den restlichen 12 Bits werden Attribute und Eigenschaften der Page festgelegt. Übrigens: Ein PageDirectory-Eintrag und ein PageTable-Eintrag unterscheiden sich voneinander fast gar nicht oder nur unwesentlich.

Sonstige Biterklärungen:

Bit P: Steht für „Present“. Falls dieses Bit gesetzt ist, befindet sich die angegebene Page im Speicher, sonst ist die Page ausgelagert oder nicht verfügbar. Falls versucht wird auf eine nicht verfügbare Page zuzugreifen tritt ein Page Fault Exception auf (Int 14).

Bit R/W: Dieses Bit kennzeichnet, ob auf die Page ein Schreibschutz wirkt oder nicht. Falls dieses Bit gesetzt ist, kann auch auf diese Page schreibend zugegriffen werden.

Bit U/S: Falls dieses Bit gesetzt ist, können nur Programme mit dem Privileg Level von 0, 1 oder 2 auf diese Page zugreifen. Jeder Versuch, mit einem Programm mit Privileg Level von 3 auf diese Page zuzugreifen, endet mit einer Page Fault Exception.

Bit PWT: Das PWT Bit ist neben dem PCD Bit nur im 486er definiert und sollte deshalb gemieden werden. PWT bedeutet soviel wie „page write-through“ und dient zur Steuerung des Caches auf Seitenbasis. Ist das Bit gesetzt werden alle Schreibaktionen sofort in den Arbeitsspeicher geschrieben, sonst werden die Änderungen vorerst nur im Cache vorgenommen.

Bit PCD: Das PCD Bit ist wie das PWT Bit nur im 486er definiert. Falls das Bit gesetzt ist, übernimmt der Prozessor aus dieser Seite geladene Daten nicht in seinen internen Cache.

Bit A: Steht für „accessed“. Dieses Bit wird vom Prozessor selber gesetzt, wenn irgendein Speicherzugriff auf diese Page geschieht (Lese-/Schreibaktion, Programmausführung).

Bit D: Dieses Bit steht für „dirty“ und wird wiederum vom CPU selbst gesetzt. Das Bit wird jedoch nur dann gesetzt, wenn ein Schreibzugriff auf die entsprechende Page stattfindet. Dadurch wird der Speicherverwaltung signalisiert, dass diese Seite nicht ohne zusätzliche Massnahmen aus dem Speicher entfernt werden kann.

  

#### Paging in der Praxis: heutige Betriebssysteme:

Die Betriebssysteme von heute, daruter verstehe ich Windows oder Linux, verwenden alle Paging. Wie oben schon einmal kurz erwähnt bekommt dabei jeder Prozess sein eigenes PageDirectory und daher auch seine eigenen PageTables, sprich jeder Prozess hat ganze 4 GB virtuellen Speicher und alle Prozesse sind voneinander abgetrennt und geschützt. Es können jedoch nicht immer die ganzen 4 GB für den Prozess ganz alleine zur Verfügung stehen. Bei einen API Call oder einem Interrupt springt die CPU ja zu einem Interrupt-Handler, der sich ja auch im Speicher befinden muss. Unter Windows stehen deshalb jedem Prozess 2 GB zur Verfügung, bei bestimmten WinNT-Einstellungen auch 3 GB. Der restliche Speicherplatz wird von Windows selbst beansprucht, wie z.B. für Interrupthandler, Shared Library, usw. Damit der Prozess aber nicht das Betriebssystem zum Absturz bringen kann, kann man mit dem oben beschriebenen U/S Bit in den PageDirectory/PageTable-Einträgen den Betriebssystemspeicher für den Prozess einfach unzugänglich machen.

#### Kleines Beispiel zu Paging:

Im folgenden soll nun anhand eines kleinen Beispieles die Wirkungsweise gezeigt werden, wie man Paging benutzt. Dieses Programm soll ein 512 Byte großer Bootsektor werden, der komplett in Assembler mit NASM Syntax geschrieben wird und der zuerst in den Proteced Mode schalten, danach PageDirectory und PageTables initialisiert und Paging aktiviert. In diesem Beispiel werde ich den Videotextspeicher, der normalerweise an der Position 0xB8000 startet, an die Position 0xC0000000 ( 3 GB ) mappen und darauf zugreifen.

##### Vorbereitungen:

Zuerst initialisiert der Beispiel-Bootloader die Segmentregister und den Stack im RealMode, danach wird in den Protected Mode geschaltet und wiederum alles initialisiert. Da dieses Tutorial vor allem Paging-Kenntnisse vermitteln soll, will ich hier den Anfangscode und den Sprung in den Protected Mode nicht allzu sehr kommentieren.

##### Initialisieren der PageDirectory und PageTables:

Da unser Code an 0x7C00 liegt, reicht es aus, wenn wir das PageDirectory an die Adresse 0x8000 und die zwei PageTables an die Adressen 0x9000 und 0xA000 setzten. Die Adressen von der PageDirectory und den PageTables müssen immer ein Alignment von 4096 haben, heisst alle 4 KB (0x0000, 0x1000, 0x2000, ...). Zuerst füllen wir den Speicherbereich, wo die PageDirectory und die beiden PageTables liegen, mit 0en:

\<asm\>InitPageDirectoryAndPageTables: xor eax,eax ; PageDirectory und 2 PageTables mit 0en füllen mov ecx,1024\*3 ; 1024 double word ≙ 4KB, insgesamt 12kB mov edi,0x8000 rep stosd\</asm\>

Danach schreiben wir in die PageDirectory-Einträge für die beiden PageTables (PageTable 0 und PageTable 768):

\<asm\>WritePageDirectoryEntries: mov DWORD\[0x8000+0\],(0x9000 \| 000000000111b) mov DWORD\[0x8000+3072\],(0xA000 \| 000000000111b)\</asm\>

  
Nun müssen wir nur noch die PageTables vorbereiten. In der PageTable 0 mappen wir die ersten 4 MB vom virtuellen Speicher mit den ersten 4 MB vom physikalischen Speicher. Somit kann nach der Aktivierung von Paging auf die ersten 4 MB beliebig zugegriffen werden. In der PageTable 768 werde ich nur eine einzige Page mappen, heisst den virtuellen Speicherbereich 0xC0000000 bis 0xC0001000. Ich werde diese Page mit der physikalischen Adresse 0xB8000 verknüpfen. Somit kann man also auch auf den Videotextspeicher zugreifen, indem man an die Adresse 0xC0000000 schreibt. Da wir ja auch die ersten 4 MB vorhin gemappt haben (wobei virtuelle Adresse = physikalische Adresse), kann auch durch die Adresse 0xB8000 auf den Videospeicher zugegriffen werden. Und hier der Code:

\<asm\>InitPageTable0: xor ebx,ebx xor edx,edx .Loop1: mov eax,edx or eax,000000000111b mov \[0x9000+ebx\],eax add ebx,4 add edx,4096 cmp edx,4096\*1024 jne .Loop1

InitPageTable768: mov DWORD\[0xA000\],(0xB8000 \| 000000000111b)\</asm\>

##### Paging aktivieren:

So, und zu guter Letzt müssen wir nur noch die Adresse des PageDirectory in das Register CR3 schreiben und das Paging-Bit im Steuerungsregister CR0 setzen:

\<asm\> WritePageDirectoryAddrIntoCR3: mov eax,0x8000 mov cr3,eax

ActivatePaging: mov eax,cr0 or eax,10000000000000000000000000000000b mov cr0,eax\</asm\>

##### Schluss:

So, nun sind wir schon am Ende. Ich hoffe, ich konnte die Grundlagen von Paging deutlich machen und mit dem Beispiel anschaulich demonstrieren, was mit Paging alles möglich ist. Für Kritik, Wünsche und Anregungen kann man sich immer an mich per ICQ (UIN: 338417614) melden.

*Stefan Marcik*

## Designtechnisches HAL

### 1. Einleitung

In diesem Tutorial werde ich erklären, was ein HAL (Hardware Abstraction Layer) ist und welche Vorteile es zum normalen Kernel-Design bietet.

### 2. Beschreibung

Wie der Name schon sagt, handelt es sich beim HAL um eine Software-Schicht zwischen der Hardware und dem eigentlichen Kernel. Aber wozu braucht man sowas? Die Antwort darauf ist einfach: Wer seinen Kernel früher oder später auf andere Plattformen/Architekturen portieren will, muss im schlimmsten Fall den kompletten Kernel umschreiben. Um das so weit wie möglich zu verhindern, sind viele Kernel in ein HAL und den Rest aufgeteilt. Das HAL übernimmt Aufgaben, wie z.B. Port-Zugriffe, Interrupt-Verwaltung, usw. Der Rest des Kernels (also Multitasking, Memory Managment, ...) greifen (so weit das möglich ist) nur über die Funktionen des HALs auf die Hardware zu. Wenn man seinen Kernel dann portieren will, muss man im Idealfall nur das HAL umschreiben – ganz so einfach ist das zwar praktisch nie, aber das Portieren wird dadurch deutlich vereinfacht.

### 3. Was kommt ins HAL?

Die einzige sinnvolle Antwort auf diese Frage ist: Alles was du für hardwarenah hältst. Damit aber nicht der komplette Kernel im HAL landet, habe ich versucht einige wichtige Sachen aufzuzählen:

- Port-Zugriffe
- Direkte Zugriffe auf die Register
- Viele Macros (Größe eines Words, Größe einer Page, ...)
- Interrupts, Exceptions, IDT/IVT, ...

Interrupts sind in Bezug auf Portieren eine echt üble Sache. Man sollte also so schnell wie möglich versuchen, sie in etwas anderes „umzuwandeln“ (z.B. Popup-Threads)

### 4. Implementierung

Im wesentlichen gibt es zwei Ansätze zur Implementierung: Entweder werden die Dateien, die zur HAL gehören wie der restliche Kernel behandelt, das heisst, dass am Ende eine Datei entsteht, oder die HAL wird zu einer eigenen Datei gelinkt und z.B. vom Bootloader mitgeladen. Egal wie man sich entscheidet, sollte man sich schon vorher den Verzeichnisbaum und die Dateinamen überlegen. Ein guter Anfang ist das erstellen einer Datei, die z.B. hal_config.h heisst. In ihr stehen alle hardwarespezifischen Macros, also für i386 in etwa so:

- \#define WORD_LENGTH 32
- \#define MAX_RAM 4194304
- ...

Anschliessend überlegt man sich einen einheitlichen Funktionssatz, der später von allen Architekturen unterstützt werden muss. Für jede Architektur könnte jetzt ein Unterordner mit der Implementierung aller Funktionen existieren. Und je nach verwendeter hal_config.h und angegebenem Unterordner wird der Kernel für eine andere Plattform kompatibel gemacht.

### 5. Schluss

Zum Abschluss gibt es noch ein paar Beispiele:

#### Linux:

Im Unterordner /arch sind alle architekturabhängigen Sachen.

#### Windows (NT, 2000, XP):

In der Datei hal.dll sind die echten Lowlevel-Funktionen implementiert. In Dateien wie ntdll.dll oder ntoskrnl.exe wird noch weiter abstrahiert.

#### ReactOS:

Da es sich hier ja um einen NT-Clone handelt, ist ReactOS natürlich ziemlich identisch mit Windows – sogar die Funktionsnamen sind gleich. Da ReactOS aber Open Source ist, kann man sich da inspirieren lassen.

So, das wars fürs erste, sollte jemand Fragen haben, kann er mir eine PN/Mail schreiben.

## Hardwaretechnisches: Real Time Clock

### 1. Real Time Clock =

Ab den AT befindet sich in dem Computer standardmässig eine batteriebetriebene Uhr. Im Englischen wird sie als RTC (Real Time Clock) bezeichnet. Die Uhr enthält auch noch einen 64 Byte batteriegepufferten RAM, der beschrieben und gelesen werden kann. Dieser RAM-Speicher beinhaltet für die Uhr relevante Informationen, und wird von den Ports 70h – 7Fh angesprochen, wobei nur die Ports 70h und 71h hier von Interesse sind.

### 2. Speicherstellen des RAM-Speichers

| Adr. | Inhalt |
| ------- | ----------------------------------------------------------------- |
| 0 | aktuelle Sekunde |
| 1 | Alarmsekunde |
| 2 | aktuelle Minute |
| 3 | Alarmminute |
| 4 | aktuelle Stunde |
| 5 | Alarmstunde |
| 6 | Tag der Woche |
| 7 | Tage des Monats |
| 8 | Monat |
| 9 | Jahr |
| 10 | Statusregister A der Uhr |
| 11 | Statusregister B der Uhr |
| 12 | Statusregister C der Uhr |
| 13 | Statusregister D der Uhr |
| 14 | Diagnose-Byte |
| 15 | Status beim Herunterfahren des Systems |
| 16 | Diskettenbeschreibung |
| 17 | reserviert |
| 18 | Festplattenbeschreibung |
| 19 | reserviert |
| 20 | Konfiguration |
| 21 | LoByte der Hauptspeichergrösse auf der Hauptplatine in KByte |
| 22 | HiByte der Hauptspeichergrösse auf der Hauptplatine in KByte |
| 23 | LoByte der Hauptspeichergrösse auf einer Zusatzplatine in KByte |
| 24 | HiByte der Hauptspeichergrösse auf einer Zusatzplatine in KByte |
| 25-45 | reserviert |
| 46 | HiByte der Prüfsumme über die Speicherstellen 16 – 32 |
| 47 | LoByte der Prüfsumme über die Speicherstellen 16 – 32 |
| 48 | reserviert |
| 49 | reserviert |
| 50 | die ersten beiden Ziffern des Jahrhunderts in BCDNotation |
| 52-63 | reserviert |

Das Feld „Tag der Woche“ gibt die Nummer des aktuellen Wochentages an, wobei die folgenden Werte für die Wochentage gelten.

| Nummer | Bedeutung | Nummer | Bedeutung |
| -------- | ----------- | -------- | ------------ |
| 1 | Sonntag | 5 | Donnerstag |
| 2 | Montag | 6 | Freitag |
| 3 | Dienstag | 7 | Samstag |
| 4 | Mittwoch | \- | \- |

### 3. Schreiben/Lesen einer Speicherstelle des RAM-Speichers

Um auf irgendeine Speicherstelle des 64 Byte grossen Speichers zugreifen zu können, bedient man sich der Ports 70h und 71h. Als erstes lädt man die zu adressierende Speicherstelle (siehe Tabelle) in das AL-Register, und schickt diesen Wert mit Hilfe von "out" nach Port 70h. Der Chip erkennt nun, dass auf eine Speicherstelle des Speichers zugegriffen wird. Nun kann man entweder mit dem out-Befehl auf den Port 71h etwas in die Speicherstelle schreiben, oder mittels "in" aus Port 71h ein Byte auslesen.

\<asm\>mov al, Speicherstelle out 70h, al in al, 71h\</asm\>

\<asm\>mov al, Speicherstelle out 70h al mov al, NeuerInhalt out 71h, al\</asm\>

### 4. Statusregister A

Die nachfolgende Tabelle zeigt den Aufbau des Statusregisters A, welches 1 Byte gross ist.

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| UIP | Z | Z | Z | F | F | F | F |

F =\> Interrupt-Frequenz  
Z =\> Zeitfrequenz  
wenn UIP = 1 =\> Uhrzeit wird gerade aktualisiert (UIPBit)

Die beiden Felder F und Z werden beim Start von dem BIOS gestzt und danach nicht mehr verändert. Dabei bekommt das Feld F den Wert 0110b zugewiesen, welcher 1024 Interrupts in der Sekunde bedeutet. Das Feld Z bekommt den Wert 010b zugewiesen, und lässt somit eine Zeitfrequenz von 32.768 Kiloherz aus. Wenn das UIP Bit gleich 1 ist, signalisiert es, dass die Uhrzeit gerade aktualisiert wird. Dann können nähmlich Fehler in der Uhrzeit auftreten, z. B. wenn der Sekundenzähler gerade bei 59 inkrementiert wurde, der Minutenzähler aber nicht. Dann gäbe es z. B. einen Sprung von 13:59:59 auf 13:59:00, was aber unlogisch und falsch wäre.

### 5. Statusregister B

Über das Statusregister lassen sich ein paar Einstellungen der Uhr programmieren. Hier sind die Bits der Reihe nach aufgelistet:

0: 0 = Sommerzeit-Umschaltung berücksichtigen  
1: Stundenzähler (0 = 12-Stunden-Format, 1 = 24-Stunden-Format)  
2: Zeit- und Datumsformat (0 = BCD, 1 = binär)  
3: 1 = Rechteckgenerator an  
4: 1 = Interruptaufruf nach Zeitaktualisierung  
5: 1 = AlarmInterrupt aufrufen  
6: 1 = periodischen Interrupt aufrufen  
7: 0 = Zeit aktualisieren  

In dem Bit 0 wird gespeichert, ob Sommerzeit (1) oder Winterzeit (0) ist. Bit 1 entscheidet darüber, ob die Uhr im 12-Stundenmodus (0) oder im 24-Stundenmodus (1) läuft. Im 12-Stundenmodus schaltet sie immer nach 12 Stunden auf 0 Uhr um (Mitternacht und Mittag), während sie im 24 Stundemodus erst nach 24 Stunden umschaltet. Bit 2 gibt Aufschluss, ob das BCD Format (0) oder das binäre Format (1) für die Zeit verwendet wird. Bit 4 entscheidet darüber, ob nach einer Aktualisierung der Zeit ein Interrupt aufgerufen werden soll. Wenn ja, dann muss dieses Bit auf 0 gesetzt werden. Wenn ein Alarm zu einer bestimmten Zeit aufgerufen werden soll, muss Bit 5 auf 1 gesetzt werden. Die Alarmzeit befindet sich dann in den Speicherstellen 1, 3 und 5 (Sekunde, Minute, Stunde) des RAM-Speichers der Uhr. Das AlarmInterrupt wird periodisch aufgerufen, wenn Bit 6 auf eins gesetzt ist. Die Anzahl der Aufrufe hängt von der Interrupt-Frequenz ab. (siehe Statusregister A) Mit dem Bit 7 kann man bestimmen, ob die Zeit aktualisiert werden soll (0) oder nicht (1). Daher sollte man im Falle einer Zeitänderung das Bit 7 vorerst auf 1 setzen, und nach der Aktualisierung wieder auf 0. Im Text steht immer wieder etwas von Interrupts, welche aufgerufen werden. Tatsächlich gibt es für die Zeit aber nur einen Interrupt; egal ob die Alarmzeit erreicht ist, die Zeit aktualisiert worden ist, oder der periodische Interrupt augerufen worden ist, es wird immer der Interrupt 70h ausgelöst.

### 6. Statusregister C

Da der Zeitinterrupt (70h) aus verschiedenen Anlässen aufgerufen werden kann, muss man bestimmen können, wer der Auslöser (Sender) war. Und hier kommt schon das Statusregister C ins Spiel. Man bedient sich einfach der im Registers beinhalteten Informationen. Hierbei sind aber nur die Bits 4, 5 und 6 von Bedeutung. Diese entsprechen den korrespondierenden Bits im Statusregister B. Daher: Wenn z. B. die Alarmzeit erreicht wurde, was nur dann erfolgen kann, wenn das Bit 5 im Statusregister B gesetzt ist, ist auch das Bit 5 im Statusregister gesetzt, um anzuzeigen, dass die Alarmzeit erreicht wurde (oder ist).

0:  
1:  
2:  
3:  
4: 1 = Zeitaktualisierung abgeschlossen  
5: 1 = Alarm-Zeit erreicht  
6: 1 = periodischer InterruptAufruf  
7:  

Die erste Aufgabe der Funktion, die den Int 70h abfängt, ist also, das Statusregister C auszulesen, um den Grund des Aufrufes festzustellen und entsprechend zu reagieren.

### 7. Statusregister D

Das letzte Statusregister ist am dürftigsten belegt. Hier ist nur Bit 7 von Bedeutung. Es zeigt den Zustand der UhrBatterie an. Bei dem Wert 0 im Bit 7 sollte die Batterie gewechselt werden, da sie leer ist.

### 8. Diagnose-Byte

0:  
1:  
2:  
3: 1 = Festplatte oder Controller nicht in Ordnung  
4: 1 = Angabe der Speichergrösse in den Speicherstellen 21 - 24 falsch  
5: 1 = Konfigurations-Byte falsch  
6: 1 = Prüfsumme in den Bytes 46 und 47 falsch  
7: 1 = Batterie der Uhr leer  

### 9. Disketten-Beschreibung

0 - 3: Typ des zweiten Diskettenlaufwerks 4 - 7: Typ des ersten Diskettenlaufwerks

#### Typen:

0000b: kein (zweites) Laufwerk 0001b: 320/360KByteLaufwerk 0001b: 1,2 MByteLaufwerk

### Nachwort

Wie ihr seht, ist die Programmierung der Uhr im Grunde sehr einfach. Vor allem erhält man Unterstützung durch den Interrupt und die Statusregister. Bei den Informationen beziehe ich mich auf den AT. Wenn ihr Fragen habt, quatscht mich im ICQ unter der Nummer 249457459 an oder schreibt mir eine EMail an T0ast3r@gmx.at. © 2005 Toaster Burger

## Software- & Treibertechnisches: Mode 13h

### 1. Geschichte

Der "Mode 13h" war zu DOS-Zeiten einer der beliebtesten Grafikmodi. Im Vergleich zu anderen VGA-Modi lässt sich der Grafikspeicher linear an- sprechen. Der Modus ist auf allen Standard-IBM-VGA-Karten verfügbar und sollte noch heute auf jeder üblichen Grafikkarte laufen. Die Auflösung beträgt 320x200 Pixel bei 8 Bit Farbtiefe (256 Farben). Natürlich ist das sehr wenig für ein OS mit grafischer Benutzeroberfläche, jedoch kann man diese Grafik vielleicht in einem "abgesicherten Modus" verwenden. Ein weiterer beliebter Grafikmodus war "Modus X". Er wurde nie von IBM dokumentiert, obschon er folgende Eigenschaften hatte: 360x480 Pixel bei 8 Bit, Double Buffering, Hardware-Scrolling und mehr. Ich will hier jedoch nicht weiter auf Mode X eingehen.

### 2. Einrichten des Modus

Das Einrichten ist ganz einfach. Man benutzt den BIOS-Interrupt 10h:

\<asm\>MOV AX, 0013h  ; Funktion 13h INT 10h\</asm\>

Diese zwei Assembler-Befehle reichen. Nun hat man bei der Speicheradresse A0000h 64'000 Bytes - nicht 64 KB ;) - Grafikspeicher.

### 3. Farbpalette

Nach dem Umschalten in Modus 13h sollte die Standardfarbpalette geladen sein. Sie ist etwas komisch organisiert. Die ersten 16 Farben entsprechen den Grundfarben (den Farben im 16-Farben-Modus). Danach kommen 16 Grautöne. Danach kommen erweiterte Farben in verschiedenen Tönen. Die Struktur ist jedenfalls nicht wirklich durchdacht.

Diese 256 Standardfarben sind zum Glück nicht konstant. Man kann sich nähmlich aus genau 262'143 Farben eine eigene 256-Farben-Palette zusammenstellen. Das passiert über die VGA-Register, ist aber auch kinderleicht. Um eine einzelne Farbe der 256er-Palette zu ändern, geht man folgendermassen vor:

\<asm\>MOV AL, 193  ; hier soll die Farbe 193 festgelegt werden MOV DX, 03C8h OUT DX, AL  ; an Port 3C8h senden INC DX  ; folgendes an Port 3C9h senden MOV AL, 40h  ; ROT-Anteil OUT DX, AL MOV AL, 2Eh  ; GRÜN-Anteil OUT DX, AL MOV AL, 02h  ; BLAU-Anteil OUT DX, AL\</asm\>

Zuerst sendet man die zu ändernde Farbe an Port 3C8h, dann je ein Byte Rot, Grün und Blau (RGB-Farben). Achtung: Nur Bits 0-6 sind für die Farbanteile signifikant, d.h. höhere Werte als 4Fh sind ungültig.

Das oben beschriebene Verfahren ist mühsam, wenn die gesamte Palette festgelegt werden soll. Um die ganze Palette zu ändern, sendet man 0 an 3C8h und anschliessend alle Farben der Reihe nach (R-G-B-R-G-B-R-G-B...) wiederum an Port 3C9h.

### 4. Speicherzugriff

Das letzte Kapitel ist das einfachste. Der Grafikspeicher bei Mode 13h ist folgendermassen aufgebaut:

\<asm\>Linke Spalte: Speicheradresse (hex) Rechte Spalte: Pixel (X, Y)

+-------+----------------+ \| A0000 \| Pixel ( 0, 0) \| +-------+----------------+ \| A0001 \| Pixel ( 1, 0) \| +-------+----------------+ Um also die Adresse eines Pixels \| A0002 \| Pixel ( 2, 0) \| zu berechnen, muss man die Formel +-------+----------------+ \| A0003 \| Pixel ( 3, 0) \| Adresse = A0000 + Y\*320 + X +-------+----------------+ ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦ benutzen. +-------+----------------+ \| A013F \| Pixel (319, 0) \| +-------+----------------+ \| A0140 \| Pixel ( 0, 1) \| +-------+----------------+ \| A0141 \| Pixel ( 1, 1) \| +-------+----------------+ \| A0142 \| Pixel ( 2, 1) \| +-------+----------------+ ¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦\</asm\>

## Tipps & Tricks

In dieser Ausgabe gibt es Tipps und Tricks zur Codeoptimierung mit Assembler.

### 0) Einleitung

Nur eine ganz kurze Einleitung: Da Assembler die Maschinensprache ist und damit direkt auf die Leistungen der CPU zugreifen kann, ist es möglich, ein- und dasselbe auf mehrere Arten zu machen. Da die unterschiedlichen Befehle auch unterschiedliche Längen haben, und in vielen Fällen die unnötig langen benutzt werden, habe ich mir gedacht, ich schreibe ein kurzes Tut darüber, wie man Codes verkürzen kann. Also, dann fangen wir mal an.

### 1) MOV reg, 0

Hier ist ein häufig benutzter Befehl, der unnötig lange ist: Einen Register Null zu setzen. Hier im Beispiel ax.

\<asm\>mov ax, 0 ; 0xB8, 0x00, 0x00\</asm\>

Also ist dieser Befehl 3 Bytes groß. Das gleiche kann mit XOR oder SUB erreict werden, nur eben kleiner:

\<asm\>sub ax, ax ; 0x29, 0xC0 xor ax, ax ; 0x31, 0xC0\</asm\>

Dieser Befehl braucht nur 2 Bytes, wir haben also ein Byte gespart.

### 2) CMP reg, 0

Sagen wir mal, wir wollen einen Register mit 0 vergleichen:

\<asm\>cmp ax, 0x0 ; 0x83, 0xF8, 0x00 jz irgenwohin ; 0x74, 0x00\</asm\>

5 Bytes, eigentlich zu viel :). Dann versuchen wir es mal kleiner:

\<asm\>test ax, ax ; 0x85, 0xC0 jz irgenwohin ; 0x74, 0x00\</asm\>

4 Bytes, schon mal nicht schlecht, aber es geht noch kleiner:

\<asm\>xchg cx, ax ; 0x91 jcxz irgendwohin ; 0xE3, 0x00\</asm\>

3 Bytes, und damit 2 Bytes eingespart. Das ist ein Erfolg :).

### 3) CMP reg, -1

Was auch oft gebraucht wird, ist der Vergleich eines Registers mit -1. Zuerst die konventionelle Überprüfung, dann die optimierte:

\<asm\>cmp ax, -1 ; 0x83, 0xF8, 0xFF je irgendwohin ; 0x74, 0x00\</asm\>

5 Bytes, aber es geht kleiner:

\<asm\>inc ax ; 0x40 jz irgendwohin ; 0x74, 0x01 dec ax ; 0x48\</asm\>

Damit haben wir ein Byte gespart.

### 4) MOVZX

Wenn wir einen 1-Byte-Wert in ein 16-Bit Register kopieren wollen, müssen wir zuerst das 16-Bit Register löschen, um nicht einen Wert im anderen 1-Byte Teil zu haben.

\<asm\>xor ax, ax ; 0x31, 0xC0 mov al, bl ; 0x88, 0xD8\</asm\>

Und jetzt optimiert:

\<asm\>movzx ax, bl ; 0x0F, 0xB6, 0xC3\</asm\>

Sehr fein, wieder ein Byte weniger :).

### 5) IMUL

Wenn wir zwei Werte multiplizieren wollen, wird mit MUL der Wert von AX multipliziert, der erst nach AX kopiert werden muss:

\<asm\>mov ax, 0x12 ; 0xB8, 0x12, 0x00 mov cx, 0x13 ; 0xB9, 0x13, 0x00 mul cx ; 0xF7, 0xE1\</asm\>

8 Bytes sind schon viel, wenn es auch einfacher geht:

\<asm\>mov ax, 0x12 ; 0xB8, 0x12, 0x00 imul ax, ax, 0x13 ; 0x6B, 0xC0, 0x13\</asm\>

2 Bytes reduziert, sehr schön :).

### 6) Schleifen

Wir müssen ja oft das selbe einige Male ausführen. Meistens sieht der Code dafür dann so oder so ähnlich aus:

\<asm\>xor ax, ax ; 0x31, 0xC0 schleife:

      ...
      inc ax        ; 0x40
      cmp ax, 8 ; 0x83, 0xF8, 0x08

jne schleife ; 0x75, 0xFA\</asm\>

  
Relativ groß, hmm? 8 Bytes nur für die Schleife. Dann machen wir das mal kleiner:

\<asm\>mov cx, 8 ; 0xB9, 0x08, 0x00 schleife:

      ...

loop schleife ; 0xE2, 0xFE\</asm\>

Von 8 auf 5 Bytes reduziert - ein voller Erfolg!

### 7) Nachwort

Das ist ein kleines Tutorial, das aber hilfreich sein kann. Ich muss jetzt den Göttern des Optimierens, Super und Billy Belceb, für ihre Codes und Tuts danken. Das ist alles...

\<asm\> - - - - - - - - - - - - - - -

       Second Part To Hell/[rRlf]
       www.spth.de.vu
       spth@priest.com
       geschrieben am 11.05.2005
       Österreich
     - - - - - - - - - - - - - - -</asm>

## Codeschnippsel

\<asm\>\[ORG 0x7C00\] \[BITS 16\] InitBoot:

       mov ax,0
       mov ds,ax
       mov ss,ax
       mov sp,0xFFFF

       cli    ; Interrupts ausschalten
       lgdt [gdtr] ; GDT Pointer laden

       mov eax,cr0 ; In PMode wechseln, indem das niedrigste
       or al,1; Steuerungsbit von cr0 geändert wird
       mov cr0,eax ; muss über Umweg über ein anderes Register gemacht werden

       jmp codesel:PMode; FarJump zu einer 32-Bit PMode Funktion

\[BITS 32\] PMode:

       mov ax,datasel   ; Segmentregister laden
       mov ds,ax
       mov es,ax
       mov fs,ax
       mov gs,ax
       mov ss,ax
       mov esp,0x90000  ; Stack aufsetzen

PageDirectory    
0x8000 ;;  
0te PageTable    
0x9000 ;;

768te PageTable   
0xA000 ;;

PageDirectory an Adresse 0x8000 initialisieren ;;

InitPageDirectoryAndPageTables:

       mov eax,0
       mov ecx,4096*3   ; PageDirectory und 2 PageTables mit 0en füllen
       mov edi,0x8000
       rep stosd

WritePageDirectoryEntries:

       mov DWORD[0x8000+0],(0x9000 | 000000000111b)    ; 0te PageTable in 

PageDirectory schreiben

       mov DWORD[0x8000+3072],(0xA000 | 000000000111b) ; 768te PageTable in 

PageDirectory schreiben

0te PageTable an Adresse 0x9000 initialisieren  ;;

Virt. Speicher 0-4 MB wird mit phs. Speicher 0-4 MB gemappt ;;

InitPageTable0:

       xor ebx,ebx
       xor edx,edx
       .Loop1:
     mov eax,edx
     or eax,000000000111b
     mov [0x9000+ebx],eax
     add ebx,4
     add edx,4096
     cmp edx,4096*1024
     jne .Loop1

0te PageTable an Adresse 0xA000 initialisieren;;

Virt. Speicher 0xC0000000 bis 0xC0001000 wird mit phs.  ;;

Speicher 0xB8000 bis 0xB9000 gemappt !  ;;

InitPageTable768:

       mov DWORD[0xA000],(0xB8000 | 000000000111b); 0te Page mit phys. Adresse 

beschreiben

Paging im Steuerungsregister CR0 aktivieren ;;

WritePageDirectoryAddrIntoCR3:

       mov eax,0x8000    ; pyhsikalische Adresse von der PageDirectory in CR3 

schreiben

       mov cr3,eax

ActivatePaging:

       mov eax,cr0  ; Paging aktivieren
       or eax,10000000000000000000000000000000b
       mov cr0,eax

An 0xC0000000 schreiben, das dann auf 0xB8000 (Videotextspeicher) ;;

geschrieben wird;;

VideotextspeicherTest:

       mov BYTE[0xC0000000],'P'
       mov BYTE[0xC0000002],'A'
       mov BYTE[0xC0000004],'G'
       mov BYTE[0xC0000006],'I'
       mov BYTE[0xC0000008],'N'
       mov BYTE[0xC000000A],'G'
       jmp $

== GDT == ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

gdtr:  ; Desktiptortabelle

       dw gdt_end-gdt-1   ; Limit
       dd gdt   ; Basisadresse

gdt:

       dd 0,0   ; Null-Deskriptor

codesel equ \$-gdt

       dw 0xFFFF; Segmentgröße 0..15
       dw 0x0000; Segmentadresse 0..15
       db 0x00  ; Segmentadresse 16..23
       db 0x9A  ; Zugriffsberechtigung und Typ
       db 0xCF  ; Zusatzinformationen und Segmentgröße 16...19
       db 0x00  ; Segmentadresse 24..31

datasel equ \$-gdt

       dw 0xFFFF; Segmentgröße 0..15
       dw 0x0000; Segmentadresse 0..15
       db 0x00  ; Segmentadresse 16..23
       db 0x92  ; Zugriffsberechtigung und Typ
       db 0xCF  ; Zusatzinformationen und Segmentgröße 16...19
       db 0x00  ; Segmentadresse 24..31

gdt_end

times 510-(\$-\$\$) db 0 dw 0xAA55\</asm\>

## OS-Showcase

In dieser Ausgabe handelt es sich im OS-Showcase um "StormOS".

### Überblick:

StormOS ist ein OS Projekt, das sich noch früh in der Entwicklung befindet. Ähnlich wie MenuetOS hat StormOS eine nur im Ansatz vorhandene Shell, stattdessen wird eine GUI eingesetzt, die sich aber ebenfalls noch früh in der Entwicklung befindet. Auch wenn es in letzter Zeit anders erschien, an StormOS wird immer noch gearbeitet. Das OS wird derzeit komplett neu in C++ gecodet.

### Entstehung von StormOS:

Mit 16 Jahren hatte Thunder aus Litauen (eine Republik in der ehemaligen UdSSR, auch da werden OS’es gecodet ;) ) die Idee, ein eigenes OS zu bauen. Nach einigem Suchen startete er indem er Assembler und C lernte und viele Tech Docs las. Er schrieb das OS GOOS, das noch komplett im Textmodus lief. Die nächste Version hatte bereits den Namen StormOS und lief im Protected Mode. Nur eine Version später kam die GUI und ersetzte die Shell völlig. Mit StormOS belegte Thunder den dritten Platz eines Computerwettbewerbs in der Kaunas University, bei der er zur Zeit studiert.

#### Features:

Es macht eigentlich wenig Sinn, hier Features aufzuzählen, da man noch nicht viel sieht. Dennoch habe ich die wichtigsten Features rauskopiert:

- GUI works up to 1024x768x32bpp screen resolution using VESA 2.0 LFB

(Linear Frame Buffer)

- Window moving
- Video mode refresh rate control (VESA 3.0 required)
- BMP file support
- Storm OS has its own Tahoma font
- PIT - Programable Interval Timer - set at 100Hz
- RTC - Real Time Clock
- PS/2 mouse
- DIN or PS/2 keyboard
- Determines RAM size
- Determines VRAM LFB start in linear memory

Multitasking, Paging, Memory Managment, Floppy Treiber, usw. sind bis jetzt gar nicht oder erst im Ansatz vorhanden. Die GUI ist ebenfalls noch sehr früh in der Entwicklung, sie beschränkt sich auf Fenstertests.

Source Code: Das OS ist komplett Open Source. Der Source Code ist zwar praktisch ohne Kommentare, ist aber dennoch halbwegs verständlich, da es vergleichsweise wenig Code ist (eigentlich logisch, da ja bisher nur wenige Features vorhanden sind). Nach dem Neuschreiben des Codes in C++ wird der Code weitaus strukturierter sein und eventuell auch mehr Kommentare haben.

Screenshots: Neue Screenshots sind verfügbar, wenn der Kernel neu geschrieben ist.

### Fakten:

**Name:** StormOS  
**Aktuellste Version:** 0.14c  
**Zahl der Entwickler:** 1  
**Name der/des Autor(en):** Thunder  
**Website:** www.stormos.net  
**PMode/RMode:** Protected Mode  
**Programmiersprache:** ASM & C, bald C++  

## Interview

In dieser Ausgabe mit Roshl.

**Redaktion:**  
Wie kamst du zum OS-Dev?

**Roshl:**  
Wir hatten irgendwann bei mir zuhause das Problem, dass mein Dad und ich einen Rechner hatten und wir beide Internet nutzen wollten (gerade zu den DSL-Anfangszeiten). Router hatten wir keinen und über Verbindungssharing von Microsoft wollte es nicht so recht klappen. Zeit verging... Da wir noch einen uralten Rechner übrig hatten, kam mir der Gedanke, man könnte ja mal versuchen, sich was Routendes selbst zu machen. Linux mochte ich persönlich noch nie, also musste theoretisch was neues her. Dann hab ich etwas gesucht und festgestellt, Mensch, könnte schwerer werden als du dachtest, ich konnte da grade mal C ein klein wenig. (Zeitlich kann man das jetzt einordnen 1-2 Monate bevor ich bei LowLevel im Forum gemeldet bin.)

**Redaktion:**  
Ah... Und wie gings dann weiter?

**Roshl:**  
Also habe ich erstmal C fertig gelernt und dann C++ angeschlossen (das dauerte nur 2 Wochen). Irgendwie hatte ich meine Probleme damit zu verstehen was Pointer sind, wozu die gut sind usw. Aber egal, drauf geschissen und Assembler gelernt. 4 Wochen später war Asm sowas wie meine Muttersprache, naja abgesehen davon, dass meine Mutter nicht mal weiss was Asm ist^^. Und da habe ich auch die Pointer kapiert gehabt, in Asm sind die irgendwie logischer. Dann kam ich wieder zurück zur Idee mit dem OS und hab einfach mal gesucht und bin spontan hier bei LowLevel gelandet. Daraufhin habe ich einfach mal das Coding angefangen^^. Mit dem OS-Coding habe ich inzwischen aber mehr oder weniger aufgehört.

**Redaktion:**  
In welchem Stadium befindet sich dein OS?

**Roshl:**  
Um ehrlich zu sein in keinem, dass irgendwie verwendbar wäre. Ich habe an vieles Ecken hier und da gecodet so, dass vieles theoretisch funktionieren könnte, aber es fehlen die bindenen Glieder. Und irgendwie fand ich C / C++ mit der Zeit als relativ ungeeignet zum Programmieren für Betriebssysteme.

**Redaktion:**  
Der Meinung bin ich auch. :-)

**Roshl:**  
Assembler wiederum dauert zu lange um damit anständig zu coden.

**Redaktion:**  

-) Arbeitest du auch beruflich mit deinem Können aus dem OS-Dev-Bereich?

**Roshl:**  
Bin momentan auch wieder dabei eine Programmiersprache zu coden. Hey ich bin Zivi, da braucht man sowas nun wirklich nicht ;-). Aber in Zukunft werde ich auf jeden Fall in eine Richtung gehen, die etwas mit Computern zu tun hat.

**Redaktion:**  
Ah.

**Roshl:**  
Ihr werdet also sicher noch von mir hören \*g\*, entweder wenn ich den Quantencomputer erfunden oder die Weltherrschaft errungen habe^^.

**Redaktion:**  
Siehst du für "berufliche OS-Dever" eine Chanche?

**Roshl:**  
Ja, auf jeden Fall. Bei Microsoft arbeiten viele, die nach meiner Definition OS-Dever sind, und die verdienen ihr Geld damit. Allerdings wird das Wissen, das man beim OS-Coden erlangt, sicher in allen Bereichen der Programmierung hilfreich sein. Z. B. denke ich, dass jeder von uns den CPUID Befehl der x86 CPU's kennt, wenn nun einer in der Spieleentwicklung arbeitet, kann er leicht herrausfinden ob er z. B. SSE und andere Features nutzen kann. Recht hilfreich auf jeden Fall!

**Redaktion:**  
Stimmt. Wie schätzt du die kommerziellen Chancen für neue Betriebssysteme ein?

**Roshl:**  
Momentan eher gering, da Microsoft's Windows doch ein Monopol inne hat. Es ist eigententlich recht Benutzerfreundlich und stabil, bei wem das nicht der Fall ist, der hat einfach seltsame Hardwarekombinationen oder ein Talent Digne nicht zum Laufen zu bekommen. Linux...hm...naja, ich persönlich mag es nicht so. Naja, da gibt es ja natürlich noch andere, Zeta z.B. ist noch recht unbekannt, könnte aber Potential haben, da wird man abwarten müssen. Da ein Betriebssystem nur erfolgreich sein kann wenn auch Software dafür entwickelt wird, ist es für Neulinge schwer, sich zu etablieren, wenn die OS-Entwickler nicht schon alles dazuliefern.

**Redaktion:**  
Wie definierst du überhaupt den Begriff "OS", "Betriebssystem".

**Roshl:**  
Das ist schwer zu beantworten. Einerseits besteht ein OS für hauptsächlich aus dem Kernel. Der würe allerdings unnütz ohne eine API, mit der ja Programme geschrieben werden müssen. Und Ohne Anwendungen ist das tollste OS leider auch nutzlos. Definieren wir es mal so: Ein Betriebssystem ist die Gesamtheit aller Programme (Kernel und Treiber sind dabei auch nur Programme), die die gröstmögliche Funktionalität am Computer bereitstellt. Klingt doch schon fast poetisch oder?

**Redaktion:**  
Ja. :-) Nun gut. Ich denke, wir werden wohl bald zum Ende kommen mit unserem Interview. Abschliessend noch eine Frage, die mich besonderst beschäftigt: Hat sich das Problem mit euren beiden Internetverbindungen, was ja Auslöser deiner Begegnung mit dem OS-Dev war, mittlerweile gelöst und wenn ja, wie?

**Roshl:**  
Ja es hat sich gelöst, wir haben letztlich einfach einen Router gekauft. Manchmal ist es eben doch besser ein altes Rad zu nehmen, als ein neues zu erfinden.

**Redaktion:**  

-) Danke für das Interview.

**Roshl:**  
Kein Problem!

## Kolumne

### Computer sind wie Autos

Mein erster Computer war ein Pentium 1 mit 16 MB RAM und einer 2 GB Festplatte, einer der ersten PCs, der mit Win95 ausgeliefert wurde. Wenn man sich aber nun wirklich mit Computern beschäftigen will, dann kann man sich vorstellen, welche Abstraktion eine GUI, und Windows sowieso, zwischen Hardware und User schafft. Zunächst ist das vollkommen uninteressant, da sich der geneigte Windows User so oder so nicht über den Desktop hinaus wagt. Will man aber nach ein paar Jahren doch über den Tellerrand sehen, so türmen sich schon die ersten Mauern auf. Da wäre zum einen die schiere Menge an Informationen, welche man erst einmal bändigen muss. Hat man sich dann durch die Kilometer langen Texte gelesen, kommt die Anwendung in der Praxis, die auch nicht immer dem theoretischen Vorwissen entspricht. Und so kommt es wie es kommen muss, man stellt fest, dass Erfahrung und Hingabe den Profi vom 08/15 User unterscheidet.

Sicher werdet ihr euch jetzt fragen, was das alles mit Autos zu tun. Die Antwort ist ganz einfach: "nichts". Im Grunde könnte man jede andere ausreichend fortschrittliche Technologie nehmen. Je weiter fortgeschritten die Technik ist, um so schwieriger ist es, meiner Meinung nach, Zugang zu finden.

Mit 15 Jahren habe ich begonnen, mich richtig mit Computern auseinanderzusetzen und habe begonnen, die Kilometer langen Texte durchzulesen. Ich muss sagen, dass mich nichts mehr beindruckt hat. Die Open-Source-Szene ist ja für ihre Dokumentationen bekannt. Langsam öffnete sich das Tor in eine andere Welt.

Besonders beeindruckt war ich vom Konzept des UNIX Betriebssystems. Aber das ist wieder eine andere Geschichte...

## Bericht ausm Forum

Jetzt hat es mit dem CommOS richtig begonnen. Der Name für das neue System wurde auch schon festgelegt, es soll, wie 50% der Befragten meinten, LOST heissen. Nur 34% waren für Isotope und gar nur 15% für LowCOS. Der Bootloader für das System ist jetzt GRUB und nicht mehr der von Roshl geschriebene. Der Kernel Milestone 0 ist fertig, mit Milestone 1 wird bald begonnen. Auch ein Kernel-Team wurde schon gebildet, das den Micro-Nanokernel für das System schreiben wird. Über die GUI wird auch schon heftig diskutiert, sogar jede Menge Designvorschläge sind schon eingegangen und es war auch schon einiges tolles dabei! Leider tut sich momentan recht wenig im Forum des CommOS. Mal sehen, wie es sich entwickelt.

## Vermischtes

### Xen

Xen ist in der Version 2.0.7 am 4.8.2005 erschienen. Xen ist eine Virtualisierungssoftware ähnlich wie VMWare GSX Server und bei <http://www.cl.cam.oc.uk/Research/SR6/netos/xen> erhältlich. Im Unterschied zu VMWare versucht Xen keine 100%ge Emulation. Das hat zur Folge, dass das Gastsystem angepasst werden muss und sich andererseits der Aufwand zur Emulation verringert, um die Performance zu verbessern. Als Hostsystem (Domain 0 genannt) lassen sich modifizierte Linux- und NetBSD-Kernel einsetzen. Die Palette an Gastsystemen (Domain U) ist breiter, dort eignen sich momentan auch Plan 9 und FreeBSD. Windows lässt sich wegen rechtlichen Beschränkungen nicht einsetzen. Es wurde probeweise von einer Universität im Rahmen der Shared Source-Lizenz modifiziert, jedoch erlaubt diese keine Veröffentlichung der Modifikationen. Die Systeme kommunizieren über ein Xen-internes Netzwerk. Um die Arbeitsweise von Xen etwas mehr zu betrachten, sieht man sich am besten den Beispielkernel an. Hier in diesem Artikel betrachten wir den 1. Schritt, den Bootvorgang. Der Start ist unspektakulär, Xen übergibt die Kontrolle an den Kernel und speichert in ESI die Addresse einer Struktur vom typ start_info_t. Dies ist vergleichbar mit GRUB's Verhalten bei Multiboot-Kerneln, man sollte jedoch bedenken das man flexibel sein muss bei seinem Bootcode. Xen ist vollständig frei unter GPL-Lizenz verfügbar, jedoch stellen Kernel, welche das Hypercall-Interface benutzen, keine von Xen abgeleiteten Werke dar. Daher kann man für ein Gastsystem eine beliebige Lizenz benutzen.

## Schluss und Impressum

**Schluss** So. Das war sie. Die lang ersehnte Ausgabe 8. Ich hoffe, sie gefällt euch und erfüllt eure Ansprüche. Abschliessend bleibt mir nur noch, mich bei allen zu bedanken, die so tatkräftig an dieser Ausgabe mitgearbeitet haben und euch ein fröhliches und friedliches Weihnachtsfest und einen guten Rutsch ins neue Jahr zu wünschen. Hoffentlich gehen eure Wünsche und Vorschläge in Erfüllung. Mein Wunsch ist, dass sich an Ausgabe 9 noch mehr Leute beteiligen. :) **Impressum** Alle hier dargestellten Artikel entsprechen der Meinung der Redakteure und spiegeln nicht unbedingt die Meinung der Redaktion wieder. Jeder Redakteur ist für seinen eigenen Beitrag verantwortlich. Zugehörigkeiten entnehmen Sie bitte der Tabelle. Wir bemühen uns nach bestem Wissen unserem Leser nur richtige Informationen zu bieten, jedoch können wir dies nicht garantieren. Jeder in dieser Ausgabe aufgeführte Code ist unter eigener Gefahr zu benutzen und der Ersteller kann nicht für entstehende Schäden zur Haftung gebracht werden. Jede mit diesem Schriftstück verlinkte Seite wird von uns ausgesucht und eingesehen, jedoch haben wir auf sie keinen Einfluss, und somit distanzieren wir uns hiermit von allen rechtswidrigen Schriften auf verlinkten Seiten.

**Artikel**

| Nummer | Name | Redakteur |
| -------- | -------------------------------- | ------------------- |
| 1\. | Die Redaktion | Neu, Joachim |
| 2\. | News | Neu, Joachim |
| 3\. | Thema der Ausgabe | Marcik, Stefan |
| 4\. | Designtechnisches | Kleusberg, Martin |
| 5\. | Architekturtechnisches | Schumann, Robert |
| 6\. | Hardwaretechnisches | Kleissner, Peter |
| 7\. | Software- & Treibertechnisches | Zurfluh, Stefan |
| 8\. | Tipps & Tricks | Sperl, Thomas |
| 9\. | Codeschnippsel | Marcik, Stefan |
| 10\. | OS-Showcase | Kleusberg, Martin |
| 11\. | Interview | Neu, Joachim |
| 12\. | Kolumne | Hellstern, Roland |
| 13\. | Bericht ausm Forum | Braun, Torsten |
| 14\. | Vermischtes | Nock, Joachim |
| 15\. | Schluss & Impressum | Neu, Joachim |

**Redakteure**

| Name | Nick | EMail | MSN | ICQ | WWW |
| ------------------- | ------------------- | --------------------------- | -------------------------- | ------------- | ----------------------------- |
| Kleusberg, Martin | DarkThing | mkleusberg@gmx.net | --- | 330-993-375 | --- |
| Nock, Joachim | Legend | jnock@gmx.de | --- | 135-508-655 | --- |
| Schumann, Robert | Roshl | robschu@hotmail.com | robschu@hotmail.com | 332-061-907 | --- |
| Neu, Joachim | joachim_neu | joachim_neu@web.de | joachim_neu@web.de | 247-390-343 | <http://www.joachim-neu.de> |
| Marcik, Stefan | Stefan2005 | stefan.marcik@web.de | --- | 338-417-614 | --- |
| Sperl, Thomas | SPTH | spth@priest.com | --- | --- | <http://www.spth.de.vu> |
| Zurfluh, Stefan | sz/elfish_rider | stefan@stefan-zurfluh.biz | elfish_rider@hotmail.com | 330-960-734 | --- |
| Kleissner, Peter | Toaster & T0ast3r | T0ast3r@gmx.at | --- | --- | --- |
| Braun, Torsten | T-Head | webmaster@t-head.de | --- | 201-238-515 | <http://www.t-head.de> |
| Hellstern, Roland | mysticforce | mysticforce@gmx.de | --- | --- | --- |

------------------------------------------------------------------------

**By [joachim_neu](mailto:joachim_neu@web.de). Alle Rechte vorbehalten**  
**Eintrag ins Wiki: [PMTheQuick](mailto:pmthequick@gmail.com)**  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 7](Ausgabe-7 "Ausgabe 7") | **Navigation** | [Ausgabe 9](Ausgabe-9 "Ausgabe 9") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7480/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1521/index.html)

<!-- MediaWiki page 1521; revision 7480; parent 7474; 2010-04-01T10:34:44Z -->
