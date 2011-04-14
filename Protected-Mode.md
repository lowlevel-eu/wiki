# Protected Mode

## Vorwort

Dieses Tutorial wird wohl wieder etwas umfangreicher und vor allem mit viel Theorie bestückt sein, auch wenn Theorie oft langweilig scheint. Bei diesem Thema ist es unerlässlich, da man sich im Protected Mode doch recht gut auskennen sollte, wenn man ein eigenes Betriebssystem schreiben möchte.

Und für die Praxisleute werde ich am Ende auch noch etwas Code bereitstellen, wie man in den Protected Mode wechselt und dort herumspielen kann.

  

## Der Protected Mode

Wenn der PC neu gestartet wird, so befindet er sich im sogenannten [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode"). In diesem Modus werden nur 16-Bit-Zeiger benutzt, sowie der Speicher, der adressierbar ist, auf 1 MiB begrenzt, da im Real Mode nur 20-Bit-Adressen zur Adressierung des Speichers gebildet werden können.

**Hinweis:**

*Jeder* kompatible x86-Prozessor läuft beim Booten noch im 16-Bit-Real Mode. Dazu gehören auch Pentium 4, Athlon XP und sonstige in dieser Reihe. Für einen Athlon64 sollte dies ebenfalls zutreffen, da dessen Architektur lediglich auf 64-Bit-Register und einen breiteren Adressbus erweitert wurde. Dagegen wurde er beim Intel Itanium 1/2 abgeschafft, da diese nicht x86-kompatibel sind.

*(Kommentar: Das stimmt auch für die 64-Bit-Prozessoren)*

  
Im Real Mode gibt es entscheidende Nachteile. Die verschiedenen laufenden Programme werden alle gleich behandelt. Das heißt, jedes Programm kann ohne Einschränkung auf den kompletten Speicher zugreifen und diesen verändern. Auch der Kernel eines Betriebssystems ist nicht geschützt. Somit ist ein Betriebssystem das im Real Mode läuft anfällig für jegliche Art von Viren und Programmierfehlern. Selbst ein einfacher Programmierfehler, welcher verursacht, dass an eine ungewollte Speicheradresse Daten geschrieben werden, kann dazu führen, dass das komplette System zum Absturz gebracht wird oder instabil läuft. Auch könnten Ergebnisse anderer Programme die im Speicher sind verändert werden, was den korrekten Ablauf jenes Programms erheblich stören kann.

Ältere Microsoft DOS Betriebssysteme das im Real Mode läuft. Da dieses System früher hauptsächlich von Privatpersonen als Single-User-System genutzt wurde, waren die eben aufgezeigten Sicherheitsrisiken zu vernachlässigen. Zudem kam noch hinzu, dass das Internet noch sehr wenig verbreitet war und daher die Gefahr von Viren und dergleichen ebenfalls zu vernachlässigen war.

**Hinweis:**

Das „vernachlässigen“ bezieht sich lediglich auf den Entwurf des Betriebssystems, jedoch nicht auf die Gefahren, die dennoch klar bestanden!

  
[Microsoft DOS](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Disk-Operating-System "Microsoft Disk Operating System") ist ein gutes Beispiel, um die Entwicklung bis hin zum Protected Mode aufzuführen. DOS ist eines der ersten Betriebssysteme, die für den Heim-PC entworfen wurden. Dieses war im Gegensatz zu vielen anderen sehr leicht zu bedienen. An Sicherheitsrisiken war damals noch nicht zu denken, da es diese einfach noch nicht gab, mal abgesehen von Programmierfehlern. Zu jener Zeit als DOS erschien, dürfte der Intel 8086 mit 64 KiB Speicher wohl gerade das Maß der Dinge gewesen sein. Da die Rechenleistung und der Arbeitsspeicher begrenzt waren, und es wohl sowieso kaum in Frage kam, dass mehrere Anwendungen „gleichzeitig“ laufen würden, war der Entwurf von DOS als Single-Task-Betriebssystem wohl ausreichend. Später erschien dann der 80186 und der 80286, welcher schon einen größeren Vorteil mit sich brachte. Zum einen war hier schon ein 20-Bit-Adressbus (dieser wurde, soweit ich mich erinnern kann, schon vor dem 286 eingeführt) mit welchem man einen 1 MiB großen Arbeitsspeicher ansprechen konnte, sowie eine erste Version des Protected Mode. Da dieser Entwurf des Protected Mode wohl nicht sehr gut durchdacht war und auch (meines Wissens nach) nicht sehr oft genutzt wurde, wurde dieser nochmal kräftig überholt und im schließlich erscheinenden 386 eingeführt, welcher nun auch einen Adressbus von 32 Bit besaß, womit man einen 4 GiB (zu dieser Zeit wohl utopisch) großen Arbeitsspeicher ansprechen konnte. Bevor ich nun jedoch aufzähle und im kurzen erkläre, wozu der Protected Mode dient und was er so kann, möchte ich jedoch noch einmal kurz auf einen oft hinterfragtem Umstand eingehen: Die Abwärtskompatibilität. Ja, wer hat diesen Begriff denn nicht schon einmal gehört. Damit ist schlichtweg (in diesem Fall) gemeint, dass neue Hardware so entworfen wird, dass diese auch mit älterer Software zusammenarbeitet. Dies ist auch der hauptsächliche Grund, warum selbst ein Pentium 4 (der wohl üblich meist mit Windows 2000 und „besser“ ausgeliefert wird) heute immer noch im Real Mode startet. Man könnte also selbst DOS noch auf einem Pentium 4 betreiben, was natürlich eine Verschwendung der Rechenleistung wäre, mal abgesehen von einem Arbeitsspeicher, der heutzutage wohl standardmäßig um die 512 MiB umfassen dürfte. Aus Gründen besagter Abwärtskompatibilität trifft man gerade als Programmierer immer wieder auf komische Software und vor allem Strukturkonstrukte, die etwas merkwürdig vom Aufbau und Inhalt erscheinen mögen. Dies hat *selten* etwas mit Effizienz, sondern meist vielmehr mit Abwärtskompatibilität zu tun. Daher erscheint es auch meist mehr als witzig, wenn die Intel-Entwickler in einem Register das eine oder andere Bit als „reserved“ ungenutzt lassen um evtl. später bei einem „kleinen“ Prozessorupdate dieses auch noch zu nutzen. Witzig ist es gerade deshalb, weil es selten vorkommt, das ein neu entwickelter Prozessor nur so wenig Änderungen mit sich bringt, bei denen gerade dieses bisher ungenutzte Bit nun benutzt wird. Meistens werden gleich komplette neue Register erstellt. Aber soviel dazu.

So, nun aber zu den Vorteilen, die der Protected Mode mit sich bringt:

  

- Es ist es nun möglich, Programmen eine Privilegstufe zuzuordnen. Dadurch kann schon einmal zwischen den Programmen unterschieden werden (Beispiel: Anwendungen, Treiber, Kernel).

<!-- -->

- Nicht jedes Programm darf *jeden* Befehl, den der Prozessor zur Verfügung stellt, ausführen. Dazu gehören Befehle, die hauptsächlich vom Kernel benutzt werden, um den Arbeitsablauf des Prozessors zu steuern. Ein normales Anwenderprogramm benötigt diese Befehle meist auch gar nicht. Jedoch ist es einfach *sicherer*, diese erst gar nicht zuzulassen. Man denke nur an Viren.

<!-- -->

- Auch wie im Real Mode „kann“ der Arbeitsspeicher in Segmente unterteilt werden. Dieses Unterteilen dient hier *nicht mehr* dazu, den kompletten Arbeitsspeicher ansprechen zu können, sondern um Speicherbereiche voneinander abgrenzen zu können. Dazu jedoch später mehr.

<!-- -->

- Multitasking wäre theoretisch auch schon im Real Mode möglich gewesen, jedoch bietet der Protected Mode wesentlich bessere Voraussetzungen dafür.

<!-- -->

- Ein Programmfehler (sofern nicht im Kernel oder in den Treibern) bringt nun nicht mehr das komplette System zum Absturz. Dies *kann* zwar auch im Protected Mode noch auftreten, jedoch nur wenn man diesen so einsetzt, dass *alle* Programme (Anwendungen, Kernel, Treiber) mit den gleichen Privilegien ausgestattet sind.

<!-- -->

- Ein Programm (sofern nicht der Kernel) kann nun nicht mehr in den Speicher eines anderen Programms schreiben. Auch dies gilt nur bei einer korrekten Anwendung des Protected Mode.

Sicherlich gibt es auch noch weitere Vorteile, die der Protected Mode mit sich bringt, jedoch würde es wohl den Rahmen dieses Tutorials sprengen, diese alle bis ins letzte Detail aufzuzählen.

## Segmente im Protected Mode

Wie oben schon erwähnt, gibt es auch im Protected Mode Segmente. Diese haben jedoch eine andere Bedeutung als im Real Mode. Segmente dienen auch im Protected Mode zur Unterteilung des Speichers, jedoch kann die Größe, die Position im Speicher und die Anzahl der Segmente „nahezu“ beliebig gewählt werden.

Zudem erhalten Segmente eine ganze Reihe von Attributen, die bei jedem Speicherzugriff eines Programms innerhalb eines Segmentes überprüft werden.

So wird einem Segment beispielsweise eine Privilegstufe zugeordnet. Dadurch kann ein Programm *nur dann* auf ein Segment zugreifen, wenn die Privilegstufe des Programms höher oder gleich hoch ist. Wenn dem nicht so ist, erkennt der Prozessor diesen Fehler und startet automatisch eine Unterroutine (Exception), die vom Kernel bereitgestellt wird. Im einfachsten Falle veranlasst der Kernel dann einfach, dass das betreffende Programm beendet und aus dem Speicher entfernt wird. Dies garantiert, dass das restliche System ohne Beinträchtigung weiterlaufen kann. Damit der Prozessor weiß, welche Attribute ein Segment hat, muss dieses dem Prozessor mitgeteilt werden. Dazu wird eine Tabelle (die Global Deskriptor Table, kurz GDT) erstellt. In dieser Tabelle werden sogenannte Deskriptoren eingetragen. Diese Deskriptoren sind 8 Byte lange Speicherbereiche, die ihrerseits nochmal in einzelne Bereiche unterteilt werden. Diese Bereiche beschreiben dann jeweils die Attribute der Segmente. Die Deskriptoren (to describe) beschreiben also die Eigenschaften der Segmente.

## Deskriptoren

Hier werde ich nun im Detail auf Deskriptoren eingehen. Dabei werde ich genauer beschreiben, wie diese aufgebaut sind und welche Aufgaben die einzelnen dort eingetragenen Attribute besitzen. Dazu schauen wir uns zuerst einmal den allgemeinen Aufbau eines Deskriptoren an.

<table>
<tbody><tr>
<th>
</th>
<th>Bit 15
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>
</th>
<th>Bit 0
</th></tr>
<tr>
<th>Word 1
</th>
<td colspan="16">Segmentgröße Bit 0 – 15
</td></tr>
<tr>
<th>Word 2
</th>
<td colspan="16">Segmentbasisadresse Bit 0 – 15
</td></tr>
<tr>
<th>Word 3
</th>
<td colspan="8">Zugriff / Segmenttyp
</td>
<td colspan="8">Segmentbasisadresse Bit 16 – 23
</td></tr>
<tr>
<th>Word 4
</th>
<td colspan="8">Segmentbasisadresse Bit 24 – 31
</td>
<td colspan="4">Zusatz
</td>
<td colspan="4">Segmentgröße Bit 16 – 19
</td></tr>
<tr>
<th>
</th>
<th colspan="8">High Byte
</th>
<th colspan="8">Low Byte
</th></tr></tbody></table>

Hier fällt gleich auf, dass die Segmentgröße und die Segmentbasisadresse etwas durcheinander auf die 4 Words verteilt sind. Dies resultiert aus der Kompatibilität zum Protected Mode des 80286.

Um nicht zu viel drum herum zu erzählen werde ich nun die einzelnen Felder in diesem Deskriptor erläutern:

### Segmentbasisadresse

Das ist die lineare Adresse, an welcher das Segment im Speicher beginnt.

### Segmentgröße

Das ist die Größe des Segments. Für die Größe werden lediglich 20 Bits verwendet, deren Wert jedoch in Abhängigkeit vom Granularity-Bit unterschiedlich interpretiert wird (s. u.).

### Zugriff/Segmenttyp

Hier wird festgelegt, welchen Typ (Code, Daten, Stack, System) das Segment aufweist und wie die Zugriffsrechte für dieses Segment aussehen.

**Zugriff/Segmenttyp (BITs)**

| **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| P | DPL |  | S | Type |  |  | A |

  

#### P = Present Bit

Gibt an, ob das Segment im Arbeitsspeicher vorhanden (*present*) ist.

#### DPL = Deskriptor Privilege Level

Gibt die Privilegstufe an, die ein Programm mindestens besitzen muss, um auf dieses Segment zugreifen zu dürfen.

#### S = Segment Bit

Gibt an, ob es sich um ein normales Segment (1) oder um ein System-Segment (0) handelt.

#### Type

Gibt an, um was für ein Segment es sich handelt. Dazu eine Tabelle weiter unten.

#### A = Accessed Bit

Dieses Bit wird beim Zugriff auf das Segment automatisch vom Prozessor gesetzt. Im Falle der Nutzung eines virtuellen Adressraums kann anhand dieses Bits entschieden werden, ob ein Segment auf die Festplatte ausgelagert werden kann.

### Zusatz

Die Bits in diesem Feld geben ebenfalls Charakteristika für das Segment an.

**Zusatz (BITs)**

| **7** | **6** | **5** | **4** |
| ------- | ------- | ------- | ------- |
| G | D | 0 | AVL |

#### G = Granular Bit

Gibt an, ob die Segmentgröße in Bytes (0) oder in 4-kB-Schritten (1) angegeben wird.

#### D

Dieses Bit gibt an, ob es sich um ein Segment für den 286 (Datensegment max. 64 kB, Code = 16 Bit, Stack = 16 Bit) oder ein Segment für den 386 (Datensegment max. 4 GB, Code = 32 Bit, Stack = 32 Bit) handelt.

#### 0

Dieses Bit ist reserviert und sollte immer auf 0 gesetzt sein.

#### AVL = Available

Dieses Bit kann vom Systemprogrammierer frei für eigenen Gebrauch verwendet oder einfach ignoriert werden.

## Segmenttypen

Hier eine Tabelle der normalen Segmenttypen, Systemsegmente werden später erläutert.

| **TYPE-Feld (BITs)** | **Beschreibung** |
| ---------------------- | ------------------------------------------------------- |
| 000 | Datensegment (Schreibgeschützt) |
| 001 | Datensegment (Beschreibbar, Lesbar) |
| 010 | Reserviert (Nicht benutzen) |
| 011 | Datensegment (Expand-Down) |
| 100 | Codesegment (Nur ausführbar, nicht lesbar) |
| 101 | Codesegment (Ausführbar und lesbar) |
| 110 | Conforming Codesegment (Nur ausführbar, nicht lesbar) |
| 111 | Conforming Codesegment (Ausführbar und lesbar) |

Sicherlich sind ein paar Erklärungen zu einzelnen Segmenttypen notwendig, weshalb ich das hier auch gleich mache:

### Datensegment (Expand-Down)

Dieses Datensegment „wächst“ nach unten, es wurde speziell für Stacks entworfen. Ein Stack beginnt in einem Segment am Ende und wächst nach unten. Sollte es nun vorkommen, dass der Stack über die Grenzen des Segments hinauswächst, so ist es mit diesem Segmenttyp möglich, es nach unten zu vergrößern. Beim Anlegen dieses Segmentes ist allerdings etwas zu beachten: Es sollte *nicht* die lineare Basisadresse 0 haben. Das würde nämlich bedeuten, dass das Segment nicht mehr vergrößerbar ist. Also muss das Segment irgendwo im Speicher beginnen, sodass die Segmenbasisadresse nicht bei 0 sondern an irgendeinem Wert beginnt.

### Conforming Codesegment

Normalerweise ist es so, dass ein Programm mit Privilegstufe 3 (niedrigste) über ein sog. Call-Gate in ein Codesegment springen kann, welches eigentlich nur für ein Programm der Privilegstufe 0 (höchste) gedacht ist. Sollte nun dieser Sprung erfolgen, so erhält das Programm für die Dauer, in der es sich in diesem Codesegment befindet, um dort Code auszuführen, die Privilegstufe 0. In einem Conforming Codesegment ist das nicht so. Es ist zwar auch hier möglich durch ein Call-Gate in dieses Codesegment zu springen, jedoch wird das Program weiterhin mit der Privilegstufe 3 ausgeführt. Wozu das im einzelnen dienlich sein kann, kann ich im Moment noch nicht sagen, weshalb ich dazu rate, sich erst einmal mit den normalen Codesegmenten zu begnügen.

  

## Systemsegmente

Wie im obigen Abschnitt schon erwähnt, gibt es auch sogenannte Systemsegmente. Diese haben alle eine spezielle Aufgabe und stellen auch nicht alle ein Segment im Sinne eines Arbeitsspeicherabschnitts dar. Genauer gesagt handelt es sich bei den meisten Systemsegmenten vielmehr um Deskriptoren, die Informationen für spezielle Zwecke beinhalten.

Hier eine Liste der Systemsegmente und deren Verwendungszweck:

### Local Deskriptor Table Segment

Dieses Segment stellt einen Speicherabschnitt dar, der eine Local Deskriptor Table (LDT) beinhaltet. Um diese LDT zu laden wird der Befehl LLDT mit der Angabe des Selektors für dieses Segment benutzt.

  

### Task State Segment (TSS)

Siehe: [Task State Segment](https://github.com/lowlevel-eu/wiki/wiki/Task-State-Segment "Task State Segment")

### Call Gates

In der Regel ist es so, dass lediglich das Betriebssystem, welches mit der Privilegstufe 0 arbeitet, Zugang zur Hardware und dem gesamten Speicher hat. Ein Benutzerprogramm, das für gewöhnlich mit der Privilegstufe 3 arbeitet, ist daher sehr eingeschränkt und darf von Haus aus lediglich Standardbefehle ausführen und auch nur Daten im eigenen Adressraum verändern und benutzen. Folglich wäre das Benutzerprogramm sehr unattraktiv und hätte kaum einen nützlichen Verwendungszweck, da es z. B. keine Möglichkeit besitzt, irgendetwas auszugeben. Daher gibt es die Call Gates. Das sind Deskriptoren in der GDT, die auf ein Codesegment mit einer höheren Privilegstufe als das Benutzerprogramm zeigen. Dieses kann nun einen Call zu diesem Call Gate ausführen, mit der Folge, dass es dem Benutzerprogramm gestattet wird, Code in einer höheren Privilegstufe auszuführen. Dieser Code stammt jedoch nicht vom Benutzerprogramm selbst, sondern vom Betriebssystem oder einem Treiber. Außerdem definiert ein Call Gate nicht nur das Codesegment, in dem sich der auszuführende höher privilegierte Code befindet, sondern auch die genaue Adresse, also das Offset des Codes innerhalb des Segmentes. Somit ist es einem Benutzerprogramm möglich, auf eine kontrollierte Art und Weise Zugang zu Systemfunktionen zu gewähren. Hier gibt es noch eine kleine Besonderheit, die es zu beachten gilt. Bei einem Wechsel der Privilegstufe, den ein Call-Gate-Aufruf häufig zur Folge hat, wird ein anderer Stack benutzt. Für jeden Task gibt es für jede Privilegstufe einen eigenen Stack. Damit nun Parameter, die vor dem Aufruf auf den alten Stack gelegt wurden, auch in dem neuen Segment benutzt werden können, werden diese beim Aufruf vom alten Stack in den neuen Stack kopiert. Der Deskriptor des Call Gates beinhaltet ein Feld mit der Angabe, wie viele Parameter zwischen den Stacks kopiert werden sollen. Wenn die Routine in dem neuen Segment abgearbeitet wurde und mittels RET-Befehl wieder zurückgesprungen wird, wird wieder der Stack gewechselt und das Programm erhält seine ursprüngliche Privilegstufe zurück.

*s. auch [Syscalls](https://github.com/lowlevel-eu/wiki/wiki/Syscall "Syscall")*

**Call Gate (BITs) Teil 1**

| **31 – 16** | **15** | **14 – 13** | **12** | **11 – 8** | **7 – 5** | **4 – 0** |
| ---------------- | -------- | ------------- | -------- | ------------ | ----------- | ----------- |
| Offset 31 – 16 | P | DPL | 0 | Type | 0 | Param |

**Call Gate (BITs) Teil 2**

| **31 - 24** | **16 - 0** |
| ------------- | --------------- |
| Selektor | Offset 15 – 0 |

  

#### Offset 31 – 16

Gibt die Bits 31 bis 16 des 32-Bit-Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

#### P = Present

Gibt an, ob das Call Gate gültig ist.

#### DPL = Deskriptor Privilege Level

Dieses Feld gibt an, welche Privilegstufe ein Programm mindestens besitzen muss, um dieses Call Gate nutzen zu können.

#### 0 = Reserviert

#### Type = Deskriptortyp

Gibt den Deskriptortyp an. Für ein Call Gate muss hier 1100b eingetragen werden.

#### Param = Parameter Count

Gibt die Anzahl der Parameter an, die zwischen den Stacks kopiert werden soll, wenn das Call Gate benutzt wird.

#### Selektor

Hier wird der Selektor des Code Segmentes eingetragen, in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

#### Offset 15 – 0

Gibt die Bits 15 bis 0 des 32-Bit-Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

  

### Interrupt Gate

Diese haben in etwa den selben Sinn und Zweck eines Call Gates. Jedoch werden diese in der IDT abgelegt und ein Sprung zu einem Interrupt-Handler erfolgt mittels des INT-Befehls. Zudem sind die Interrupt Gates hauptsächlich dazu gedacht, Systemfunktionen bereitzustellen, mit denen auf das Auftreten eines Hardware-Interrupts reagiert wird. Deshalb wird beim Aufruf eines Interrupt Gates auftomatisch das Interruptflag im EFLAGS-Register geändert, damit während der Abarbeitung des Interrupthandlers kein weiterer Interrupt ausgelöst werden kann.

**Interrupt Gate (BITs) Teil 1**

| **31 – 16** | **15** | **14 – 13** | **12** | **11** | **10 – 8** | **7 – 0** |
| ---------------- | -------- | ------------- | -------- | -------- | ------------ | ----------- |
| Offset 31 – 16 | P | DPL | 0 | D | Type | 0 |

**Interrupt Gate (BITs) Teil 2**

| **31 – 24** | **16 – 0** |
| ------------- | --------------- |
| Selektor | Offset 15 – 0 |

  

#### Offset 31 – 16

Gibt die Bits 31 bis 16 des 32-Bit-Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

#### P = Present

Gibt an, ob das Interrupt Gate gültig ist.

  

#### DPL = Deskriptor Privilege Level

Dieses Feld gibt an, welche Privilegstufe ein Programm mindestens besitzen muss, um dieses Interrupt Gate per INT nutzen zu können.

#### 0 = Reserviert

#### D = Size

Gibt an ob es sich um ein 32- (1) oder ein 16-Bit-Segment (0) handelt, also ob sich 32- oder 16-Bit-Code darin befindet.

#### Type = Deskriptortyp

Gibt den Deskriptortyp an. Für ein Interrupt Gate muss hier 110b eingetragen werden.

#### Selektor

Hier wird der Selektor des Codesegmentes eingetragen, in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

#### Offset 15 – 0

Gibt die Bits 15 bis 0 des 32-Bit-Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

## Beispielcode

Eine knappe Variante, um in den Protected Mode zu schalten, wird [hier](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode") erklärt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9669/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1464/index.html)

<!-- MediaWiki page 1464; revision 9669; parent 7902; 2011-04-14T19:37:59Z -->
