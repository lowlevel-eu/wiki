# Protected Mode

## Vorwort

Dieses Tutorial wird wohl wieder etwas umfangreicher und vor allem mit viel Theorie bestückt sein. Auch wenn Theorie oft langweilig scheint. Bei diesem Thema ist es unerlässlich, da man sich im Protected Mode doch recht gut auskennen sollte, wenn man ein eigenes Betriebssystem schreiben möchte.

Und für die Praxisleute werde ich am Ende auch noch etwas Code bereitstellen, wie man in den Protected Mode wechselt und dort herumspielen kann.

  

## Der Protected Mode

Wenn der PC neu gestartet wird, so befindet er sich im sogenannten Real-Mode. In diesem Modus wird nur 16-Bit Code benutzt, sowie der Speicher, der Adressierbar ist, auf 1 MB begrenzt, da im Real-Mode nur 20 Bit Adressen zur Adressierung des Speichers benutzt werden dürfen(bzw können).

    Hinweis:
    JEDER kompatible x86 Prozessor läuft beim Booten noch im 16-Bit Realmode. Dazu gehören auch Pentium 4,
    Athlon XP und sonstige in dieser Reihe. Für einen Athlon64 sollte das ebenfalls zutreffen, da dessen Archtiektur
    ledliglich auf 64-Bit Register und einen 64-Adressbuch  erweitert wurde. Ob Intel Itanium 1/2 ebenfalls von
    dieser Regel betroffen sind kann ich nicht mit sicherheit sagen, da ich noch keine in den Fingern hatte, jedoch
    gehe ich davon aus.

    (Kommentar: Das stimmt auch für die 64-Bit Prozessoren)

  
Im Real-Mode gibt es entscheidende Nachteile. Die verschiedenen Programme die laufen werden alle gleich behandelt. Das heisst jedes Programm kann ohne Einschränkung auf den kompletten Speicher zugreifen und diesen verändern. Auch der Kernel eines Betriebssystems ist nicht geschützt. Somit ist ein Betriebssystem das im Real-Mode läuft anfällig für jegliche Art von Viren und Programmierfehlern. Selbst ein einfacher Programmierfehler, welcher verursacht das an eine ungewollte Speicheradresse Daten verändert werden kann dazu führen, das das komplette System zum Absturz gebracht wird oder instabil läuft. Auch könnten Ergebnisse anderer Programme die im Speicher sind verändert werden, was den korrekten Ablauf jenes Programms erheblich stören kann.

Microsoft DOS ist ein Betriebssystem das im Real-Mode läuft. Da dieses System früher hauptsächlich von Privatpersonen als Single-User-System genutzt wurde, waren die eben aufgezeigten Sicherheitsrisiken zu vernachlässigen. Zudem kam noch hinzu, das das Internet noch sehr wenig verbeitet war und daher die Gefahr von Viren und dergleichen ebenfalls zu vernachlässigen war.

    Hinweis:
    Das "vernachlässigen" bezieht sich lediglich auf den Entwurf des Betriebssystems, jedoch nicht auf die Gefahren
    die dennoch klar bestanden!

  
Microsoft DOS ist ein gutes Beispiel um die Entwicklung bis hin zum Protected Mode aufzuführen. DOS ist eines der ersten Betriebssysteme die für den Heim-PC entworfen wurden. Dieses war im Gegensatz zu vielen Anderen sehr leicht bedienbar. An Sicherheitsrisiken war damals noch nicht zu denken, da es diese einfach noch nicht gab, mal abgesehen von Programmierfehlern. Zu jener Zeit als DOS erschien, dürfte der Intel 8086 mit 64? KB Speicher wohl gerade das Maß der Dinge gewesen sein. Da begrenzt durch die Rechenleistung und den Arbeitsspeicher es wohl eh kaum in Frage kam, das mehrere Anwendungen "gleichzeitig" laufen würden, war der Entwurf von DOS als Single-Task Betriebssystem wohl ausreichend. Später erschien dann der 80186 und der 80286, welcher schon einen größeren Vorteil mit sich brachte. Zum einen war hier schon ein 20 Bit-Adressbus (dieser wurde soweit ich mich Erinnern kann bereits schon vor dem 286 eingeführt) mit welchem man einen 1 MB großen Arbeitsspeicher ansprechen konnte, sowie eine erste Version des Protected Mode. Da dieser Entwurf des Protected Mode wohl nicht sehr gut durchdacht war und auch (laut meinem Wissen) nicht sehr oft genutzt wurde, wurde dieser nochmal kräftig überholt und im schließlich erscheinenden 386 eingeführt, welcher nun auch einen Adressbus von 32 Bit besaß, womit man einen 4 GB (zu dieser Zeit wohl utopisch) großen Arbeitsspeicher ansprechen konnte. Bevor ich nun jedoch aufzähle und im kurzen erkläre wazu der Protected Mode dient und was er so kann, möchte ich jedoch noch einmal kurz auf einen oft hinterfragten Umstand eingehen; Die Abwärtskompatibilität. Ja wer hat diesen Begriff denn nicht schoneinmal gehört. Damit ist schlichtweg (in diesem Fall) gemeint, das neue Hardware so entworfen wird, das diese auch mit älterer Software zusammenarbeitet. Dies ist auch der hauptsächliche Grund warum selbst ein Pentium 4 (der wohl üblich meist mit Windows2000 und "besser" ausgeliefert wird) heute immernoch im Real-Mode startet. Man könnte also selbst DOS noch auf einem Pentium 4 betreiben, was natürlich eine Verschwendung der Rechenleistung wäre, mal abgesehen von einem Arbeitsspeicher der heutzutage wohl standardmäßig um die 512 MB umfassen dürfte. Aus Gründen besagter Abwärtskompatibilität trifft man gerade als Programmierer immer wieder auf komische Software und vor allem Strukturkonstrukte, die etwas merkwürdig vom Aufbau und Inhalt erscheinen mögen. Dies hat SELTEN etwas mit Effizienz, sondern meist vielmehr mit Abwärtskompatibilität zu tun. Daher erscheint es auch meist mehr als witzig, wenn die Intel-Entwickler in einem Register das eine oder andere Bit als "reserved" ungenutzt lassen um evtl. später bei einem "kleinen" Prozessorupdate dieses auch noch zu nutzen. Witzig ist es gerade deshalb, weil es selten vorkommt, das ein neu entwickelter Prozessor nur so wenig Änderungen mit sich bringt, bei denen gerade dieses bisher ungenutzte Bit nun benutzt wird. Meistens werden gleich komplette neue Register erstellt. Aber soviel dazu.

So nun aber zu den vorteilen die der Protected Mode mit sich bringt.

  

- Es ist es nun möglich Programmen eine Privilegstufe zuordnen zu können. Dadurch kann schon einmal zwischen den Programmen unterschieden werden (Beispiel: Anwendungen, Treiber, Kernel).

<!-- -->

- Nicht jedes Programm darf JEDEN Befehl den der Prozessor zur Verfügung stellt ausführen. Dazu gehören Befehle die hauptsächlich vom Kernel benutzt werden um den Arbeitsablauf des Prozessors zu steuern. Ein normales Anwenderprogramm benötigt diese Befehle meist auch garnicht. Jedoch ist es einfach SICHERER diese erst garnicht zuzulassen. Man denke nur an Viren.

<!-- -->

- Auch wie im Real-Mode "kann" der Arbeitsspeicher in Segmente unterteilt werden. Dieses unterteilen dient hier NICHT MEHR dazu um den kompletten Arbeitsspeicher ansprechen zu können, sondern um Speicherbereiche voneinander abgrenzen zu können. Dazu jedoch später mehr.

<!-- -->

- Multitasking wäre theoretisch auch schon im Real-Mode möglich gewesen, jedoch bietet der Protected-Mode wesentlich bessere Vorraussetzungen dafür.

<!-- -->

- Ein Programmfehler (sofern nicht im Kernel oder in den Treibern) bringt nun nichtmehr das komplette System zum Absturz. Dies KANN zwar auch im Protected Mode noch auftreten, jedoch nur wenn man diesen so einsetzt, das ALLE Programme (Anwendungen, Kernel, Teiber) mit den gleichen Privilegien ausgestattet sind.

<!-- -->

- Ein Programm (sofern nicht der Kernel) kann nun nichtmehr in den Speicher eines anderen Programms schreiben. Auch dies gilt nur bei einer korrekten Anwendung des Protected Mode.

Sicherlich gibt es auch noch weitere Vorteile die der Protected Mode mit sich bringt, jedoch würde es wohl den Rahmen dieses Tutorials sprengen, diese alle bis ins letzte Detail aufzuzählen.

## Segmente im Protected Mode

Wie oben schon erwähnt, gibt es auch im Protected Mode Segmente. Diese haben jedoch eine andere Bedeutung als im Real-Mode. Segmente dienen auch im Protected Mode zur Unterteilung des Speichers, jedoch kann die größe und die Anzahl der Segmente "nahezu" beliebig gewählt werden.

Zudem erhalten Segmente eine ganze Reihe von Attributen die bei jedem Speicherzugriff eines Programms innerhalb eines Segmentes überprüft werden.

So wird einem Segment beispielsweise eine Privilegstufe zugeordnet. So kann ein Programm NUR DANN auf ein Segment zugreifen, wenn die Privilegstufe des Programms höher oder gleich hoch ist. Wenn dem nicht so ist, erkennt der Prozessor diesen Fehler und startet automatisch eine Unterroutine (Exception) die vom Kernel bereitgestellt wird. Im einfachsten Falle veranlasst der Kernel dann einfach, das das betreffende Programm beendet wird und aus dem Speicher entfernt wird. Dies garantiert, das das restliche System ohne Beinträchtigung weiterlaufen kann. Damit der Prozessor weiß welche Attribute ein Segment hat, muss dieses dem Prozessor mitgeteilt werden. Dazu wird eine Tabelle (die Global Deskriptor Table, kurz GDT) erstellt. In dieser Tabelle werden sogenannte Deskriptoren eingetragen. Diese Deskriptoren sind 8 Byte lange Speicherbereiche die Ihrerseits nochmal in einzelnen Bereiche unterteilt werden. Diese Bereiche beschreiben dann im einzelnen die Attribute der Segmente. Die Deskriptoren (to describe) beschreiben also die Eigenschaften der Segmente.

  

## Deskriptoren

Hier werde ich nun nochmal im Detail auf Deskriptoren eingehen. Dabei werde ich genauer beschreiben, wie diese Aufgebaut sind und welche Aufgaben die einzelnen Attribute die dort eingetragen werden haben. Dazu schauen wir uns zuerst einmal den allgemeinen Aufbau eines Deskriptoren an.

![deskriptor.gif](http://www.jay-code.de/pics/deskriptor.gif)

Hier fällt gleich auf, das die Segmentgröße und die Segmentbasisadresse etwas wild verstreut auf die 4 WORDs verteilt sind. Das kommt daher, weil man den Deskriptor zum 286-Prozessor möglichst kompatibel halten wollte.

Um nicht zu viel drum herum zu erzählen werde ich nun mal die einzelnen Felder in diesem Deskriptor erläutern:

### Segmentbasisadresse

Das ist die lineare Adresse an welcher das Segment im Speicher beginnt.

### Segmentgröße

Das ist die Größe des Segments. Für die Größe werden lediglich 20 Bits verwendet. Diese Bits werden jedoch unterschiedlich interpretiert. Entscheidend ist hierfür das Granular-Bit. Dazu jedoch weiter unten mehr.

### Zugriff/Segmenttyp

Hier wird festgelegt welcher Typ(Code,Daten,Stack,System) Segment vorliegt und wie Zugriffsrechte für dieses Segment aussehen.

**Zugriff/Segmenttyp (BITs)**

|  |  |  |  |  |  |  |  |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| **7** | **6** | **5** | **4** | **3** | **2** | **1** | **0** |
| P | DPL |  | S | Type |  |  | A |

  

#### P = Present Bit

Gibt an ob das Segment im Arbeitsspeicher present ist.

#### DPL = Deskriptor Privilege Level

Gibt die Privilegstufe an die ein Programm mindestens besitzen muss um auf dieses Segment zugreifen zu dürfen.

#### S = Segment Bit

Gibt an ob es sich um ein normales Segment(1) oder um ein System-Segment(0) handelt.

#### Type

Gibt an um was für ein Segment es sich handelt. Dazu eine Tabelle weiter unten.

#### A = Accessed Bit

Dieses Bit wird beim Zugriff auf das Segment automatisch vom Prozessor gesetzt. Im Falle der Nutzung eines virtuellen Adressraums, kann anhand dieses Bits entschieden werden, ob ein Segment auf die Festplatte ausgelagert werden kann.

### Zusatz

Die Bits in diesem Feld geben ebenfalls Charakteristika für das Segment an.

**Zusatz (BITs)**

|  |  |  |  |
| ------- | ------- | ------- | ------- |
| **7** | **6** | **5** | **4** |
| G | D | 0 | AVL |

#### G = Granular Bit

Gibt an ob die Segmentgröße in Bytes(0) oder in 4KB(1) Schritten angegeben werden.

#### D

Dieses Bit gibt an ob es sich um ein Segment für den 286 (Datensegment max 64 KB, Code = 16 Bit, Stack = 16 Bit) oder ein Segment für den 386 (Datensegment max 4 GB, Code = 32 Bit, Stack = 32 Bit) handelt.

#### 0

Dieses Bit ist reserviert und sollte immer auf 0 gesetzt sein.

#### AVL = Available

Dieses Bit kann vom Systemprogrammierer frei für eigenen Gebrauch benutzt werden oder einfach ignoriert werden.

  

## Segmenttypen

Hier eine Tabelle der normalen Segmenttypen. Systemsegmente werden später erläutert.

|  |  |
| ---------------------- | ------------------------------------------------------- |
| **TYPE-Feld (BITs)** | **Beschreibung** |
| 000 | Datensegment (Schreibgeschützt) |
| 001 | Datensegment (Beschreibbar, Lesbar) |
| 010 | Reserviert (Nicht benutzen) |
| 011 | Datensegment (Expand-Down) |
| 100 | Codesegment (Nur Ausführbar, nicht lesbar) |
| 101 | Codesegment (Ausführbar und lesbar) |
| 110 | Conforming Codesegment (Nur Ausführbar, nicht lesbar) |
| 111 | Conforming Codesegment (Ausführbar und lesbar) |

Sicherlich sind ein paar Erklärungen zu einzelnen Segmenttypen notwendig, weshalb ich das hier auch gleich mache:

### Datensegment (Expand-Down)

Dieses Datensegment "wächst" nach unten. Es ist extra für Stacks entworfen. Ein Stack beginnt in einem Segment am Ende und wächst nach unten. Sollte es nun vorkommen das der Stack über die Grenzen des Segments hinauswächst, so ist es mit diesem Segmenttyp möglich das Segment nach unten zu vergrößern. Beim anlegen dieses Segmentes ist allerdings etwas zu beachten. Das Segment sollte NICHT die lineare Basisadresse 0 haben. Das würde nämlich bedeuten das das Segment nicht mehr vergrößerbar ist. Also muss das Segment irgendwo im Speicher beginnen, so das die Segmenbasisadresse nicht bei 0 sondern an irgendeinem Wert beginnt.

### Conforming Codesegment

Normalerweise ist es so, das ein Programm das eine Privilegstufe 3 (niedrigste) über ein sog. Call-Gate in ein Codesegment springen kann, das eigentlich nur für ein Programm der Privilegstufe 0 (höchste) gedacht ist. Sollte nun dieser Sprung erfolgen, so erhält das Programm für die Dauer, in der es sich in diesem Codesegment befindet um dort Code auszuführen, die Privilegstufe 0. In einem Conforming Codesegment ist das nicht so. Es ist zwar auch hier möglich durch ein Call-Gate in dieses Codesegment zu springen, jedoch wird das Program weiterhin mit der Privilegstufe 3 ausgeführt. Wozu das im einzelnen dienlich sein kann, kann ich im Moment noch nicht sagen ,weshalb ich dazu rate sich erst einmal mit den normalen Codesegmenten zu begnügen.

  

Um das erstellen von Deskriptoren etwas zu vereinfachen, habe ich ein kleines Konsolenprogramm für Windows geschrieben, mit dem man sich bequem über eine Auswahl den Deskriptor zusammenbauen kann und bekommt diesen dann zum direkten abtippen fertig geliefert.

  

## Systemsegmente

Wie im obigen Abschnitt schon erwähnt gibt es auch sogenannte Systemsegmente. Diese haben alle eine spezielle Aufgabe und stellen auch nicht alle ein Segment im Sinne eines Arbeitsspeicherabschnitts dar. Genauer gesagt handelt es sich bei den meisten Systemsegmenten vielmehr um lediglich Deskriptoren die Informationen für spezielle Zwecke beinhalten.

Hier eine Liste der Systemsegmente und deren Verwendungszweck:

### Local Deskriptor Table Segment

Dieses Segment stellt einen Speicherabschnitt dar, der eine Local Deskriptor Table (LDT) beinhaltet. Um diese LDT zu laden wird der Befehl LLDT mit der Angabe des Selektors für dieses Segment benutzt.

  

### Task State Segment (TSS)

Dies ist ebenfalls ein Speicherabschnitt der Daten beinhaltet um das Multitasking zu realisieren. Bei einem Task-Wechsel müssen alle Register des gerade laufenden Task gesichert werden, um diese später wiederherstellen zu können, damit der Task wieder gestartet werden kann. Das TSS beinhaltet alle Daten die für einen Task gespeichert werden. Daher ist es notwendig, das jeder Task ein eigenes TSS bekommt. Das TSS hat eine Größe von 106 Bytes. Sollte bei dem Deskriptor als Größe ein kleinerer Wert eingetragen werden, so wird beim Versuch den Deskriptor zu laden eine Exception ausgelöst.

|  |  |
| ---------------------- | ---------------------- |
| **31 - 16** | **15 - 0** |
| I/O Map Base Address |  |
|  | LDT Segment Selektor |
|  | GS |
|  | FS |
|  | DS |
|  | SS |
|  | CS |
|  | ES |
| EDI |  |
| ESI |  |
| EBP |  |
| ESP |  |
| EBX |  |
| EDX |  |
| ECX |  |
| EAX |  |
| EFLAGS |  |
| EIP |  |
| CR3 |  |
|  | SS2 |
| ESP2 |  |
|  | SS1 |
| ESP1 |  |
|  | SS0 |
| ESP0 |  |
|  | Previous Task Link |

  

**Task State Segment Deskriptor (BITs) Teil 1**

|  |  |  |  |  |  |  |  |  |  |
| -------------------- | -------- | ------------- | -------- | ------------- | -------- | ------------- | -------- | ------------ | -------------------- |
| **31 - 24** | **23** | **21 - 22** | **20** | **19 - 16** | **15** | **13 - 14** | **12** | **11 - 8** | **0 - 7** |
| Basisadresse 31-24 | G | 0 | AVL | Größe 19-16 | P | DPL | 0 | Type | Basisadresse 16-23 |

**Task State Segment Deskriptor (BITs) Teil 2**

|  |  |
| --------------------- | -------------- |
| **31 - 24** | **16 - 0** |
| Basisadresse 15 - 0 | Größe 15 - 0 |

#### Type = Deskriptor Typ

Hier muß als Wert 1001b eingetragen werden. Die hintere Null wird zusätzlich als Busy-Flag verwendet. Dies wir auf 1 gesetzt, sobald der Task in das System geladen ist und gestartet wurde. Tasks sind nicht redundant. Das heißt sie dürfen sich nicht selbst aufrufen. Dies wird mit dem Busy Flag verhindert.

### Call Gates

In der Regel ist es so, das lediglich das Betriebssystem das mit der Privilegstfue 0 arbeitet zugang zu der Hardware und dem gesamten Speicher hat. Ein Benutzerprogramm, das für gewöhnlich mit der Privilegstufe 3 arbeitet, ist daher sehr eingeschränkt und darf von Haus aus lediglich Standardbefehle ausführen und auch nur Daten im eigenen Adressraum verändern und benutzen. Folglich wäre das Benutzerprogramm sehr unattraktiv und hätte kaum einen nützlichen Verwendungszweck. Daher gibt es die Call Gates. Das sind Deskriptoren in der GDT, die auf ein Codesegment zeigen das eine höhere Privilegstufe besitzt als das Benutzerprogramm. Das Benutzerprogramm kann nun einen Call zu diesem Call Gate machen, was zur Folge hat das es dem Benutzerprogramm gestattet wird, Code in einer höheren Privilegstufe auszuführen. Dieser Code stammt jedoch nicht vom Benutzerprogramm selbst, sondern vom Betriebssystem oder einem Treiber. Außerdem definiert ein Call Gate nicht nur das Code Segment in dem sich der ausführbare, höher privilegierte Code, befindet, sondern auch die genaue Adresse. Sprich das Offset des Codes innerhalb des Segmentes. Somit ist es möglich einem Benutzerprogramm auf eine kontrollierte Art und Weise Zugang zu Systemfunktionen zu gewähren. Hier gibt es noch eine kleine Besonderheit die zu beachten ist. Bei einem Wechsel der Privilegstufe, der für gewöhnlich die Folge eines Call Gate Aufrufs ist, wird ein anderer Stack benutzt. Für jeden Task gibt es für jede Privilegstufe einen eigenen Stack. Damit nun Parameter die VOR dem Call Gate Aufruf auf den alten Stack gepusht wurden, auch in dem neuen Segment benutzt werden können, werden diese beim Aufruf des Call Gates vom alten Stack in den neuen Stack kopiert. Der Deskriptor des Call Gates beinhaltet ein Feld das angibt, wie viele Parameter zwischen den Stacks kopiert werden sollen. Wenn die Routine in dem neuen Segment abgearbeitet wurde und mittels des RET Befehls wieder zurückgesprungen wird, wird wieder der Stack gewechselt und das Programm erhält wieder seine ursprüngliche Privilegstufe.

**Call Gate (BITs) Teil 1**

|  |  |  |  |  |  |  |
| ---------------- | -------- | ------------- | -------- | ------------ | ----------- | ----------- |
| **31 - 16** | **15** | **14 - 13** | **12** | **11 - 8** | **7 - 5** | **4 - 0** |
| Offset 31 - 16 | P | DPL | 0 | Type | 0 | Param |

**Call Gate (BITs) Teil 2**

|  |  |
| ------------- | --------------- |
| **31 - 24** | **16 - 0** |
| Selektor | Offset 15 - 0 |

  

#### Offset 31 - 16

Gibt die Bits 31 bis 16 des 32-Bit Offsets innerhalb des Codesegmentes an in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

#### P = Present

Gibt an ob das Call Gate gültig ist.

#### DPL = Deskriptor Privilege Level

Dieses Feld gibt an welche Privilegstufe ein Programm mindestens besitzen muß um dieses Call Gate nutzen zu können.

#### 0 = Reserviert

#### Type = Deskriptor Typ

Gibt den Deskriptor Typ an. Für ein Call Gate muß hier 1100b eingetragen werden.

#### Param = Parameter Count

Gibt die Anzahl der Parameter an, die zwischen den Stacks kopiert werden soll, wenn das Call Gate benutzt wird.

#### Selektor

Hier wird der Selektor des Code Segmentes eingetragen in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

#### Offset 15 - 0

Gibt die Bits 15 bis 0 des 32-Bit Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Call Gate gesprungen werden soll.

  

### Interrupt Gate

Diese haben in etwa den selben Sinn und Zweck eines Call Gates. Jedoch werden diese in der IDT abgelegt und ein Sprung zu einem Interrupt-Handler erfolgt mittels des Int Befehls. Zudem sind die Interrupt Gates hauptsächlich dazu gedacht Systemfunktionen bereitzustellen, mit der auf das Auftreten eines Hardware-Interrupts reagiert wird. Deshalb wird beim Aufurf eines Interrupt Gates auftomatisch das IF Flag im EFLAGS Register geändert, damit während der Abarbeitung des Interrupt Handlers kein weiterer Interrupt ausgelöst werden kann.

  

**Interrupt Gate (BITs) Teil 1**

|  |  |  |  |  |  |  |  |
| ---------------- | -------- | ------------- | -------- | -------- | ------------ | ----------- | ----------- |
| **31 - 16** | **15** | **14 - 13** | **12** | **11** | **10 - 8** | **7 - 5** | **4 - 0** |
| Offset 31 - 16 | P | DPL | 0 | D | Type | 0 |  |

**Interrupt Gate (BITs) Teil 2**

|  |  |
| ------------- | --------------- |
| **31 - 24** | **16 - 0** |
| Selektor | Offset 15 - 0 |

  

#### Offset 31 - 16

Gibt die Bits 31 bis 16 des 32-Bit Offsets innerhalb des Codesegmentes an in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

#### P = Present

Gibt an ob das Interrupt Gate gültig ist.

  

#### DPL = Deskriptor Privilege Level

Dieses Feld gibt an welche Privilegstufe ein Programm mindestens besitzen muß um dieses Interrupt Gate nutzen zu können.

#### 0 = Reserviert

#### D = Size

Gibt an ob es sich um ein 32-Bit(1) oder ein 16-Bit(0) Segment handelt. Sprich ob sich 32-Bit oder 16-Bit Code darin befindet.

#### Type = Deskriptor Typ

Gibt den Deskriptor Typ an. Für ein Interrupt Gate muß hier 110b eingetragen werden.

#### Selektor

Hier wird der Selektor des Code Segmentes eingetragen in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

#### Offset 15 - 0

Gibt die Bits 15 bis 0 des 32-Bit Offsets innerhalb des Codesegmentes an, in dem sich der Code befindet, zu dem über das Interrupt Gate gesprungen werden soll.

## Beispielcode

So um nicht nur reine Theorie hier zum lesen zu geben folgt natürlich auch ein bisschen Code. Allerdings beschränkt sich das erstmal nur auf einen Codeteil, der in den Protected Mode schaltet und eine Funktion in einem C-Kernel aufruft.

  
Der Code wird ist so ausgelegt, das dieser von einem Bootloader (ich benutze meinen) an die Lineare Adresse 0x10000 (in Realmode: 0x1000:0000) geladen wird.

An dieser Adresse befindet sich dann der Kernel, der aus zwei Teilen besteht. Der eine Teil ist in 16-Bit Code geschrieben. Dieser Teil ist dafür verantwortlich in den Protected Mode zu schalten. Dazu enthält dieser Teil am Ende noch etwas 32-Bit Code um das A20 Gate zu aktivieren und in den C-Kernel zu springen.

  
So wir erstellen zuersteinmal den Kernelteil, der in den Protected Mode springt. Dazu erstellen wir eine neue ASM-Datei. Dort tragen wir als aller Erstes die NASM-Direktive \[Bits 16\] ein. Das signalisiert NASM das er erstmal 16 Bit Code erstellen soll. Dies ist nötig weil wir uns hier NOCH im Real-Mode befinden.

Dann kommt als allererstes ein JMP-Befehl. Dieser Jump soll zu einer Sprungmarke führen, die wir direkt unter den JMP-Befehl schreiben.

Als nächstes definieren wir die Deskriptoren. Dabei müssen alle Deskriptoren ZWISCHEN den JMP-Befehl und der Sprungmarke eingefügt werden. Dadurch erreichen wir, das der Prozessor unsere Deskriptoren überspringt und nicht versucht diese als Code auszuführen, was zu unschönen Ergebnissen führen sollte.

  
Nun benötigen wir aber erstmal die 3 Deskriptoren, die für den Switch in den Protected Mode unerlässlich sind. Der erste, der Null-Deskriptor, ist schnell erzeugt. Dazu werden einfach 8 Bytes mit 0 gefüllt: \<asm\>NULL_Desc: dd 0 ;Ein DWORD mit dem Wert 0 dd 0 ;Ein DWORD mit dem Wert 0\</asm\>Als nächstes brauchen wir einen Deskriptor für ein Code Segment. Diesen erstellen wir ganz einfach mit dem Programm (CalcDesc.exe) das ich als Download zur Verfügung stelle. Von diesem Programm werden ein paar Fragen gestellt. Diese beantworten wir für den Code Deskriptor wie folgt:

Als erstes Wählen wir ein Code Segment (Execute-Read). Damit sagen wir das wir ein Codesegment haben möchten, das sowohl ausführbaren Code enthalten darf und es uns gestattet ist daraus zu lesen.

Als nächstes Sagen wir, das das Segment Present sein soll.

Als Privilegstufe kommt nur 0 in Frage. Wir benötigen für den Kernel schließlich alle Rechte.

Als Segment-Size-Unit nehmen wir "4096 Bytes per Unit". Nur so können wir ein Segment erzeugen das größer als 1 MB ist.

Da wir ein Segment für den 386 (oder höher) haben möchten wählen wir 32-Bit.

So nun müssen wir die Segmentbasisadresse angaben. Diese Angabe muss in Hexadezimalform angegeben werden. Da unser Segment sich über den kompletten 4 GB Adressraum erstrecken soll, müssen wir hier 0 angeben.

Die Segmentgröße müssen wir mit 0xFFFFF angeben (4 GB).

Nun erhalten wir ein Ergebnis, welches wir direkt übernehmen können:\<asm\>CODE_Desc: dw 0xFFFF dw 0 db 0 db 0x9A db 0xCF db 0\</asm\>So nun brauchen wir auch noch ein Daten Segment. Dazu im schnelldurchgang die Angaben für CalcDesc:

1\. Datensegment Read-Write

2\. Segment present

3\. Privilegstufe 0

4\. 4096 Byte per Unit

5\. 32-Bit

6\. Basisadresse: 0

7\. Segmentgröße: 0xFFFFF

Ergebnis:\<asm\>DATA_Desc: dw 0xFFFF dw 0 db 0 db 0x92 db 0xCF db 0\</asm\>So direkt hinter den Deskriptoren, ABER IMMER NOCH VOR DER SPRUNGMARKE, definieren wir folgendes:\<asm\>gdt: Limit dw 0 Base dd 0\</asm\>Diese Variablen werden wir gleich füllen. Das sind dann die Angaben mit denen wir das GDT Register füttern werden.

Jetzt werden wir erstmal die Interrupts deaktivieren und das DS Register so laden, das es auf das selbe Segment wie CS zeigt.

Das erreichen wir mit folgendem Code:\<asm\>cli mov eax, cs mov ds, ax\</asm\>Etwas verwirrend mag erscheinen, das wir das EAX Register mit dem Wert von CS füllen. Auch wenn wir im Real-Mode sind, können wir trotzdem 32 Bit Register benutzen. Das benutzen des EAX Register hat auch eine zweck der im folgenden Codeabschnitt deutlich wird.

Wir haben nämlich ein kleines Problem. Kurz nachdem wir (später) in den Protected Mode geschaltet haben, müssen wir einen FAR JUMP ausführen. Mit diesem erreichen wir, das der Deskriptor für das Code Segment den wir erstellt haben geladen wird. Zusätzlich wird die Prefetch Queue des Prozessors gelöscht. In dieser Warteschlange (Queue) warten nämlich noch 16-Bit Befehle, die der Prozessor schonmal im Vorraus teilweise dekodiert hat. Da wir aber in den Protected Mode springen und wir dort nur mit 32-Bit Befehlen arbeiten, können wir diese 16-Bit Befehle in der Queue nicht gebrauchen.

Das Dumme ist nur, das dieser FAR JUMP eine gewisse Einschränkung hat. Wir können da nämlich nur den Selektor für das Code Segment und eine 16-Bit Offset Adresse angeben. Und genau bei diesen 16 Bit liegt unser Problem. Die meisten Leute (so wie ich) laden ihren Kernel an die Lineare Adresse 0x10000. Diese Adresse ist aber mit einem 16 Bit Wert nicht mehr erreichbar. Das heisst wir können nicht in das Code Segment springen, das ja bei der Linearen Adresse 0 beginnt und gleichzeitig zu dem Offset springen das genau hinter unserem FAR JUMP Befehl liegt. Daher müssen wir uns abhelfen. Um das Problem zu lösen, werden wir zur Laufzeit den Deskriptor für das Code Segment so umschreiben, das seine Lineare Basisadresse nicht mehr bei 0 liegt, sondern bei der Linearen Adresse an welche wir unseren Kernel geladen haben. Nämlich 0x10000. Wir machen das zur Laufzeit, damit wir später auch die Möglichkeit haben unseren Kernel auch an eine andere Speicherstelle laden zu können, ohne den Deskriptor jedesmal von Hand ändern zu müssen.

Um nun den Deskriptor zu ändern, finden wir erstmal heraus in welchem Real-Mode Segment wir uns befinden. Das erreichen wir indem wir das EAX Register mit dem Wert des CS Register laden. Dann verschieben wir das EAX Register um 4 Bits nach links. Damit erhalten wir die Lineare Adresse des Segmentes. Diese tragen wir dann in den Deskriptor ein. Da wie wir schon gesehen haben der Deskriptor die Angabe der Basisadresse etwas in den 8 Bytes verteilt hinterlegt, müssen wir die Angabe etwas splitten. Das wird aber im folgenden Code ersichtlich:\<asm\>shl eax, 4 ;EAX beinhaltet immer noch den Wert von CS (siehe letzten Codeabschnitt) mov \[CODE_Desc+2\], ax ;Den ersten Teil der Linearen Adresse eintragen mov \[DATA_Desc+2\], ax shr eax, 16 mov \[CODE_Desc+4\], al ;Den zweiten Teil der Linearen Adresse eintragen mov \[DATA_Desc+4\], al\</asm\>So nun müssen wir noch die Basisadresse und das Limit für die GDT eintragen. Dazu müssen wir zuerst wieder errechnen wo sich die GDT befindet. Dazu holen wir uns wieder den Wert des CS Registers nach EAX und schieben dieses wieder 4 Bits nach links. Dann addieren wir das Offset NULL_Desc, da dieses das Startoffset der GDT darstellt.

Das Limit errechnen wir, indem wir das Startoffset der GDT (NULL_Desc) vom Offset gdt subtrahieren. Das Offset gdt ist direkt hinter den Deskriptoren und kann somit als Ende der GDT angesehen werden. Wenn die Berechnung korrekt gelaufen ist, sollten wir als Wert 24 (3\*8) erhalten. Jedoch haben wir (siehe GDT Abschnitt) gesagt das immer eins von dem Wert abgezogen werden muss. Also erhalten wir als endgültiges Limit den Wert 23, den wir dann auch eintragen.

Das ganze geschieht in folgendem Code:\<asm\>mov eax, cs shl eax, 4 add eax, NULL_Desc mov \[Base\], eax mov \[Limit\], WORD gdt - NULL_Desc - 1 ;Das passte leider nicht alles hintereinander\</asm\>So nun können wir das GDT Register laden.\<asm\>lgdt \[gdt\]\</asm\>So nun kommt endlich das was wir eigentlich erreichen wollen. Das schalten in den Protected Mode. So banal der folgende Code auch erscheinen mag. Er hat eine große Auswirkung und bedarf daher auch dieser ganzen Vorarbeit.\<asm\>mov eax, cr0 ;Das CR0 Register in EAX laden or eax, 1 ;Das erste Bit (PE Bit) auf 1 setzen mov cr0, eax ;Das CR0 Register mit dem neuen Wert laden\</asm\>Nun befinden wir uns schon im Protected Mode. War doch ganz einfach oder? Jetzt müssen wir nur noch das CS Register laden und die Prefetch leeren. Das errichen wir mit dem folgenden Code. Es sieht zwar so aus als würden wir Variablen deklarieren, jedoch sind die Werte die wir in die Variablen schreiben das Bitmuster das ein FAR JUMP Befehl hat.\<asm\>db 0xea ;Bitmuster für einen FAR JUMP dw PMODE ;Angabe des Offsets zu dem gesprungen werden soll dw 0x8 ;Angabe des Selektors für das Segment zu dem gesprungen werden soll.\</asm\>So nun fehlt nur noch die Deklaration des Labels PMODE. Und da wir von da an mit 32 Bit Code arbeiten teilen wir das NASM noch mit der Direktive \[Bits 32\] mit. Und da wir noch nix weiter an Code haben, lassen wir eine Endlosschleife laufen.\<asm\>\[Bits 32\] PMODE: jmp PMODE\</asm\>Damit wir nun auch ohne Gefahren arbeiten können, müssen wir noch schnell die anderen benötigten Segmentregister laden.

  
Bevor wir das tun, helfen wir uns mit einem kleinen Trick aus einer gewissen "schlechten Lage". Wie oben schon erklärt konnten wir die Startadresse des Codesegmentes nicht auf 0 legen. Folglich haben wir im weiteren ein blödes Problem. Wir haben zum einen 64 KB Speicher auf die wir nicht zugreifen können, da wir diese im Segemten "übersprungen" haben und alle späteren Angaben (z.b. Videospeicheradresse) verschiebt sich ebenfalls ein Stück, da wir ja immer das Offset zum Segmentbeginn angeben. Und wenn unser Segment nunmal NICHT bei 0 beginnt, haben wir etwas kuddel muddel. Wir mussten das so machen, da wir beim FAR JUMP in den Protected Mode nur ein 16 Bit Offset angeben konnten.

Nun befinden wir uns aber im Protected Mode und auch im 32 Bit Bereich. Folglich setzen wir die Segmantbasisadresse der Deskriptoren einfach wieder auf 0 und springen nun mit Hilfe der Angabe eines 32 Bit Offsets an die richtige Stelle. Somit haben wir dann den vollen 4 GB Adressraum zur Verfügung und müssen uns auch nicht mehr um das umrechnen von Adressen kümmern. Um das ganze zu realisieren machen wir folgendes:\<asm\>mov WORD \[CODE_Desc+2\], 0 ;Code Segmentstartaddresse auf 0 setzen mov WORD \[DATA_Desc+2\], 0 ;Daten Segmentstartadresse auf 0 setzen mov BYTE \[CODE_Desc+4\], 0 ;Code Segmentstartaddresse auf 0 setzen mov BYTE \[DATA_Desc+4\], 0 ;Daten Segmentstartadresse auf 0 setzen\</asm\>Nun können wir die Segmente einfach laden.

Dabei gehen wir vorsichtig vor. Wir schreiben zuerst den Wert 2 in ax. Wir wollen den Eintrag der GDT mit dem Index 2 (also der dritte Eintrag), welches das Daten Segment ist, haben. Dann verschieben wir das ganze um 3 Bits nach links.

Man erinnere dazu nochmal schnell an den Aufbau eines Selektors.

Jetzt laden wir das DS, SS und ES Register mit diesem Selektor. Die Register FS und GS laden wir erstmal mit dem Null Deskriptor, da wir für diese vorerst noch keine Verwendung haben. Zusätzlich laden wir noch das ESP Register mit dem Wert 0x1FFFFF um den Stack ausreichend weit von unserem Kernel zu entfernen. Dieser Wert entspricht der 2 MB Grenze. Soviel Speicher sollte jeder Rechner besitzen, weshalb wir somit auch nicht in Gefahr kommen das unser Stack außerhalb des Speichers liegt.

  
Dazu dient folgender Code:\<asm\>mov eax, 2 ;Index 2 der GDT auswählen shl eax, 3 ;Im Selektor beginnt der Index erst ab Bit 3 mov ds, ax mov es, ax mov ss, ax mov eax, 0 mov fs, ax ;FS und GS auf NULL Deskriptor zeigen lassen mov gs, ax mov esp, 0x1FFFFF ;ESP auf 2 MB setzen\</asm\>So nun müssen wir NOCH einen FAR JUMP in das Codesegment machen. Aus dem einfachen Grund, da wir den Deskriptor ja verändert haben und diesen durch den FAR JUMP neu laden müssen.

  
Dazu nutzen wir folgenden Code:\<asm\>jmp 0x8:0x10000 + PMODE2 ;Sprung in das "neue" Codesegment PMODE2:\</asm\>Hier springen wir einfach an eine neue Sprungmarke und müssen zu dem Offset natürlich noch die lineare Adresse addieren, an welche wir unseren Kernel vom Bootloader haben laden lassen.

  
So das wäre es soweit. Von hier aus kann man dann in einen C-Kernel springen oder in ASM weitermachen. Natürlich muss man den Code etwas modifizieren, wenn man die GDT zur Laufzeit erweitern möchte. In diesem Falle wäre es angebracht hinter GDT alle restlichen der 65536 Bytes die die GDT umfassen kann, hier aber nicht genutzt wurden, mit Nullen zu füllen.

  
Hier nun auch noch der Beispielcode und das Programm CalcDesc zum runterladen. Das Programm wird in nächster Zeit noch aktualisiert, so das auch System Segment Deskriptoren damit erstellt werden können.

[Download](http://www.jay-code.de/files/pmode.zip)

  

  
**Anmerkung 1:** Da der Code davon ausgeht, dass er am Anfang eines Segmentes steht, sollte man ihn mit einem geeigeneten Bootloader laden, der dies beachtet. Ein schlankes Beispiel wäre:

\<asm\>mov ax,cs mov ds,ax mov es,ax

cli mov ss,ax mov sp,0x20000 sti

mov ax,0x9000 mov es,ax mov bx,0x0 mov ah,02h mov al,1 mov cl,2 mov ch,0 mov dl,0 mov dh,0 int 13h

jmp 0x9000:0x0

times 510-(\$-\$\$) db 0 dw 0aa55h\</asm\>© by PMTheQuick

Die beiden 0x9000 können natürlich durch irgendeine andere Adresse ersetzt werden, jenachdem wohin man seinen Kernel laden will. Dann kann man die Dateien assemblieren + zusammenkopieren um ein funktionierendes Image zu erhalten:

    nasm -f bin -o kernel16.bin kernel16.asm
    nasm -f bin -o bootsec.bin bootsec.asm
    copy /B bootsec.bin + /B kernel16.bin PM_OS.img

**Anmerkung 2:** Eine weitere, etwas weniger komplizierte Variante in den Protected Mode zu schalten wird [hier](https://github.com/lowlevel-eu/wiki/wiki/Umschalten-in-Protected-Mode "Umschalten in Protected Mode") erklärt.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2175/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1464/index.html)

<!-- MediaWiki page 1464; revision 2175; parent 2174; 2007-10-16T00:58:19Z -->
