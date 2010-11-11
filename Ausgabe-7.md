# Ausgabe 7

|  |  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| © | Dieser Artikel ist urheberrechtlich geschützt.<br>Bitte beachte, dass die üblichen [Lizenzbestimmungen](https://lowlevel-eu.github.io/wiki/pages/1637/index.html "Lowlevel:Urheberrecht") des Wikis für diesen Artikel nicht gelten. |

  

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 6](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-6 "Ausgabe 6") | **Navigation** | [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8 "Ausgabe 8") » |

## Die Redaktion

Hier ist sie also, die neue Ausgabe von "Lowlevel". Nachdem Roshl in letzter Zeit wegen seinem Abitur keine Zeit mehr für das Magazin hatte und die letzte Ausgabe schon fast ein halbes Jahr zurück liegt habe ich mich bereit erklärt, mein Glück zu versuchen und hier ist das Ergebniss, diese Ausgabe.

Zuerst möchte ich mich mal vorstellen, ich heiße Joachim Neu, bin 14 Jahre alt und wohne in München. In meiner Freizeit spiele ich gerne Computer, treffe mich mit Freunden/Freundinnen und programmiere an meinem Betriebssystem "HighOS".

So, nun aber wieder zurück zu dieser Ausgabe. In ihr steht so einiges über Multitasking für die etwas weiteren unter uns aber auch etwas über den Wechsel in den Protected Mode ist dabei. Wer in den letzten Tagen und Wochen wie Roshl wenig Zeit hatte wird das aktuelle im Bericht ausm Forum und dem Newsbereich erfahren. Aber da die (Computer-)Welt nicht nur aus Betriebssystemen besteht gibt es für gelangweilte Programmierer ein bisschen Abwechslung in unserer Kolumne beziehungsweise dem Vermischten Bereich.

An dieser Stelle möchte ich mich nun bei allen bedanken, die bei dieser Ausgabe mitgewirkt haben. Sie haben geholfen, dieses Magazin fertig zu stellen und nicht zu Letzt ihnen ist es zu verdanken, dass es diese Ausgabe gibt. Ich hoffe sie sind auch für andere ein Vorbild, sich ein bisschen für das Magazin einzusetzen und den ein oder anderen Artikel zu schreiben. Alle Daten über die Verfasser der Artikel gibt es im Impressum.

Jetzt möchte ich noch Roshl danken, der es glücklicherweise geschafft hat, uns/mir eine Testplattform für das Design zusammen zu bauen, sodass diese Ausgabe nicht alzu grauslig erscheint, und für das Einbauen einer Möglichkeit bei den BB-Codes, mit der man Text farbig hinterlegen kann, ohne die ich den Artikel im Thema der Ausgabe hätte neu schreiben müssen.

So, nun reichts aber mit dem ganzen Gerede. Viel Spaß beim Lesen der siebten Ausgabe von Lowlevel diesmal unter der Regie von mir,

Joachim Neu.

## News

- bochs: Das 2. Pre-Release des Beliebten x86er-PC-Emulators Bochs ist freigegeben worden.
- ReactOS: Vom Windows NT kompatiblen ReactOS Betriebssystem wurde die Version 0.2.5 freigegeben.
- MenuetOS: Das Final Realease 0.78 des komplett in Assembler geschriebenen MenuetOS wurde mit vielen Neuerungen freigegeben. Außerdem ist wenig später das 1. Pre Release der 0.79er Version erschienen.
- E/OS LX: Die Version 0.2.5 des E/OS LX Projektes ist erschienen. Dieses Betriebssystem kann sowohl Win32/16, Linux, DOS als auch FreeBSD Programme ausführen. Es basiert hauptsächlich auf anderen Projekten, wie Linux, FreeBSD, ReactOS und Wine.
- TinyOS: TinyOS ist in der Version 1.1.11 erschienen.

## Thema der Ausgabe: Multitasking mit TSS

### Einleitung

In diesem Tutorial möchte ich jedem, der gewillt ist, Multitasking in seinem Betriebssystem mit TSS auf Hardwarebasis zu machen, erklären, wie er dies machen kann, bzw. anderen, die nicht beabsichtigen dies zu tun, zeigen, wie Multitasking in der Theorie funktioniert.

In diesem Tutorial werde ich zuerst auf die verschiedenen Formen von Multitasking und einen Teil der Theorie, und danach auf TSS-Multitasking speziell eingehen. Ich hoffe es macht Spaß und wünsche nun viel Verknügen.

### Überblick

Bei Multitasking gibt es 2 wichtige Teile, die man immer braucht. Der erste Teil ist eine Tabelle, in der alle Tasks aufgelistet sind. Im zweiten Teil wird der aktuelle Taskzustand gespeichert. Es ist wichtig, dass der Computer alle Inhalte der CPU-Register speichert, sodass das Programm vom Taskwechsel nichts merkt und davon nicht beeinflusst wird.  
Und genau hier setzten die Unterschiede ein. Bei hardwarebasiertem Multitasking speichert die CPU den Registerzustand automatisch in einer anderen Tabelle, dem TSS genannten TaskStateSegment. Beim softwarebasierenden Multitasking wird dieses Speichern vom Betriebssystem vorgenommen und erfolgt meist auf dem programmeigenen Stack. Daraus resultierend entstehen auch Unterschiede der ersten Tabelle.

Beim hardwarebasierendem Multitasking ist man nur auf einen Eintrag mit der Deskriptornummer angewiesen. Bei softwarebasierendem Multitasking braucht man zwar dies nicht, allerdings muss man SS und ESP speichern. Meist werden noch ein Speicherbereich für eine eindeutige Task-Nummer, die TaskID und einen Bereich, der den Status des Tasks für das System festhält, benutzt. Je nach Scheduling Strategie benutzt man auch noch einen Speicherbereich für die Priorität des Tasks, sodass man den Task mit der höchsten Priorität häufiger oder länger laufen lassen kann. Selten werden für spezielle Scheduling Strategien auch noch Speicherbereiche zur Sicherung der Startzeit oder ähnlichem benutzt.

Es gibt zwei verschiedene Versionen von Multitasking, kooperatives und preemtives. Kooperatives Multitasking vertraut darauf, dass jedes Programm so lange Zeit bekommt, wie es braucht und danach ein Systeminterrupt auslöst, dass die Rechenleistung an den nächsten Task weiterreicht. Dieses Konzept ist in letzter Zeit hinfällig geworden, da es in Zeiten von Viren und Trojanern nichtmehr das Schlauste währe, Programmen die zeitunbegrenzte Kontrolle über den PC zu geben, da diese den ganzen Ablauf stoppen könnten. Neue Ideen mussten her, meist in Form von preemtivem Multitasking. Bei diesem wird dem Programm/Task nach gewissen Zeit vom System durch das TimerIRQ die Kontrolle entzogen. Da dies meiner Meinung nach die einzig sinnvolle Lösung ist, werde ich hier darauf eingehen. Später werden wir noch einige Teile in Assembler zusammen coden, der dir helfen wird, das ganze zu verstehen.

### Aufbau eines TSS

Da wir uns jedoch um Multitasking auf Hardwareebene kümmern wollen, werde ich hier den Aufbau eines TaskStateSegments schildern. Den Aufbau werde ich später noch in einer Tabelle verdeutlichen, jedoch werde ich davor noch wichtige Informationen erleutern. Dadurch, dass es äußerst unsicher währe, den Stack im Userbereich zu belassen, wenn man ein Systeminterrupt oder Systemcall aufruft, da später diese Informationen ausgelesen werden könnten und sowieso Daten im Privileglevel 3 nicht sonderbar geschützt sind, wurden im TaskStateSegment Datenbereiche für Stackdaten eingerichtet. Da der Protected Mode über 4 Privileglevel (0-3) verfügt, Level-3-Daten jedoch sowieso ungeschützt sind, braucht man dafür keinen eigenen Stack, sondern kann den User-Stack benutzen. Es existieren also 3 zusätzliche Stacks, für Privileglevel 0,1 und 2, für die man auch Speicherplatz für die SS-Register und ESP-Register braucht, welcher als SS0, SS1, SS2, ESP0, ESP1 und ESP2 bezeichnet wird. Nun hier aber der Aufbau:

![3_1.png](http://www.joachim-neu.de/public/lowlevel/7/3_1.png)

So. Nun werde ich den Aufbau genauer Erklären. Die gelb hinterlegten Einträge beizeichnen das Offset des Eintrags zum Beginn der Tabelle. Alle rot hinterlegten Einträge haben den Wert 0 und sollten den auch beinhalten. Alle blau hinterlegten Einträge bezeichnen vom Programm beeinflussbare Einträge. Alle lila hinterlegten Einträge müssen vom Betriebssystem gesetzt werden und sind nicht vom Programm beeinflussbar. Alle grün hinterlegten Bereiche werden automatisch gesetzt. Alle orange

hinterlegten Bereiche stehen frei zur Verfügung. Jetzt werde ich die warscheinlich noch unklaren Bereiche erklären. ESPn und SSn hab ich vorher schon erleutert. In BackLink speichert die CPU bei einem Interruptaufruf, bei dem ein TaskGate in der IDT angegeben wurde, die Deskriptornummer des Auslösertasks. Zu diesem kehrt sie bei gesetztem NT-Flag im Flagregister mit einem IRET zurück. Die Bereiche, die die Namen der Register tragen dürften klar sein. Beim Eintrag *I/O Port Bitmap Base* wird das Offset einer Tabelle angegeben, die angibt, auf welche Portadressen der Task Zugriff hat. Bei dem Wert 0 ist diese deaktiviert, sodass der Zugriff alleine durch das IOPL im Flagregister gesteuert ist. Dann ist da noch das T-Flag. Ist dieses gesetzt, so wird nach jedem Taskwechsel zu diesem Task ein Interrupt 1 ausgelöst. Der Bereich nach der Adresse 0x68 steht dem Systemprogrammierer frei zur Verfügung. Das Limit eines TSS muss also mindestens 0x68 betragen. Nach der eigendlichen TSS-Tabelle ist dann Platz für die I/O-Port-Tabelle oder Werte, die das System vom Task noch braucht und nicht in der Task-Tabelle speichern will. Wie ich schon sagte braucht jeder Task ein TSS und dies muss in der GDT eingetragen werden. Ein TSS hat als die 4 Typ-Bits den Wert 1001 als Binärzahl. Dies ist der Aufbau eines TSS-Deskriptors:

![3_2.png](http://www.joachim-neu.de/public/lowlevel/7/3_2.png)

Jede Zeile der Tabelle gibt ein Word wieder, eine 16 Bit lange Zahl. Eigentlich gibt es nichts, was unterschiedlich zu dem normalen Aufbau eines Deskriptors wäre, deswegen erkläre ich nur kurz alle Felder.

- Alle, die mit *Limit* bezeichnet sind geben die Größe des Segments an. \* Alle mit *Basis* bezeichneten geben die Basisadresse im

Speicher an. Das Bit *P* gibt an, ob sich das Segment im Speicher (present) befindet. Es sollte immer auf 1 gesetzt sein, da es meiner Meinung nach nicht zu den schlausten Lösungen zählt, TSSs auszulagern, die man ständig braucht, zumal diese nicht sehr viel Speicher sparen.

- Die 2 Bit lange Stelle *DPL* gibt das DescriptorPrivilegeLevel an.

Damit kann man kontrollieren, welche Privilegstufe Programme brauchen, die auf dieses Segment zugreifen wollen.

- Das Bit *S* ist das System-Bit. Es unterscheidet

spezielle Segmente (wie TSS und alle Gates) von Standartsegmenten (Codesegment, Datensegment). Bei speziellen Segmenten ist es nicht gesetzt, sprich 0.

- Dann gibt es noch das *G*(ranularity)-Bit, das angibt, ob die Größenangabe des Deskriptors in Bytes (=0) oder in Kbytes (=1) zu verstehen ist. Da ich noch kein TSS mit 1 Kbyte oder mehr Speicherverbrauch gesehen habe, sollte dies den Wert 0 haben.
- Das *D*-Bit gibt an, ob

der Deskriptor zu dem 286er kompatibel ist, oder nicht. Dort empfehle ich den Wert 1, also inkompatibel, dann kann man das Segment vergrößern, ohne sich irgendwann man damit wieder auseinander setzen zu müssen.

- Das *AVL*-Flag steht zur freien Verfügung.
- Das *Typ*-Feld haben wir ja schon besprochen, es muss bei einem TSS den Wert 1001b beinhalten.

Wenn ein Task aktiviert wird, so wird sein *Typ*-Feld mit dem Wert *1011* als Binärzahl belegt. Das zeigt, dass das aktuelle Segment aktiv ist und man nicht zu ihm wechseln kann. Davon wissen wir schon, dass man mindestens zwei Tasks braucht, damit Multitasking mit TSS überhaupt richtig funktioniert. Ebenso wird beim Verlassen eines Tasks der Wert wieder zu 1001b.

### Task-Tabelle

Desweiteren braucht man noch, wie besprochen, eine Tabelle, die die Deskriptornummern und TaskIDs speichert. Auch der Status wird dort oft gespeichert, da das System ihn braucht, um zum Beispiel pausierte Tasks zu übergehen, und es umständlich währe, diesen Wert erst aus dem TSS zu lesen, zumal dies nicht als Daten- Segment lesbar ist, was heißt, dass man erst den Platz im Speicher finden und dann über ein anderes Segment auslesen müsste. Außerdem beinhaltet er oft noch eine TaskID, damit man den Task nicht über seine TSS-Nummer identifizieren muss. Da man maximal 8192 TSSs haben kann (maximale Größe der GDT ist 0x10000), allerdings aber noch ein paar Einträge fürs System abgehen, reicht ein Word zum Speichern der TaskID und TSS-Nummer. Als Statusbereich dürfte auch ein Word (16 Bits) reichen. Auch in dieser Tabelle ist eine Zeile ein Word.

![3_3.png](http://www.joachim-neu.de/public/lowlevel/7/3_3.png)

Es gibt 2 Möglichkeiten, das Ende dieser Tabelle aus Task-Tabellen-Einträgen zu finden.

1.  Man speichert in einer Variable, wie viele Einträge man hat und überprüft das aktuelle und das maximale Offset, um einen WrapArround (beim Anfang anfangen) zu vollziehen.
2.  Man gibt am Ende der Tabelle dem nächsten leeren Eintrag die ID 0xFFFF oder ein sonstiges "Endezeichen" und führt einen WrapAround aus, sobald man als ID den Wert des Endezeichens gefunden hat.

Das war eigentlich schon das Wichtigste über die Task-Tabelle.

### TaskGates

Außerdem gehören zu TSS-Multitasking noch TaskGates. TaskGates kann man sowohl in der GDT als auch in der IDT eintragen. Wenn man sie an erste Stelle stellt, so wird der durch das TaskGate angegebene Task bei der 0. Exception gestartet. Ebenso ist es bei allen anderen Interrupts und/oder Exceptions. Ein TaskGate ist wie folgt aufgebaut: (wieder ist jede Zeile ein Word)

![3_4.png](http://www.joachim-neu.de/public/lowlevel/7/3_4.png)

Alle Bereiche, die *Reserviert* sind, sollten den Wert 0 beinhalten. Im Bereich *TSS-Deskriptor-Nummer* wird der Deskriptor festgehalten, auf den das TaskGate verweist.

Die Felder *P*, *DPL* und *S* habe ich vorher schon erklärt, sodass dies hier überflüssig ist. Der *Typ* muss bei einem TaskGate den Wert 0101 als Binärzahl beinhalten.

TaskGates werden an sich eigentlich beim Multitasking selten verwendet, sondern lediglich als Einträge in der IDT, damit bei einer Exception oder einem Interrupt ein eigener Task aufgerufen wird. Dann wird das NT-Flag gesetzt und die CPU wechselt bei IRET zu dem Task, dessen TSS-Deskriptor im BackLink-Feld eingetragen ist.

### Dispatcher

So, nun aber nach dem ganzen Aufbauzeug zur Theorie. Ein Taskwechselalgorithmus sollte idealerweise aus zwei Teilen bestehen, dem Scheduler und dem Dispatcher, um den wir uns nun kümmern wollen.

Der Dispatcher ist dafür verantwortlich, dass der Task die CPU zugeteilt und entzogen bekommt. Er muss alle Register laden bzw speichern und den eigentlichen Taskwechsel veranlassen. Beim softwarebasierenden Multitasking besteht diese Aufgabe des Dispatchers darin, zuerst die Werte des aktuellen Tasks auf dessen Stack zu pushen, dann den neuen Stack zu laden und die Werte des Tasks zu popen. Bei hardwarebasierendem Multitasking besteht die Aufgabe lediglich darin, einen Task-Switch zu veranlassen, in dem die CPU dann eigenständig die Register sichert und die neuen lädt.

### Scheduler

Und hier setzt auch schon der Scheduler an. Während der Dispatcher nur die Taskwerte sichert und die neuen setzt besteht die Aufgabe des Schedulers darin, den nächsten Task auszuwählen. Dies tut er anhand der Scheduling-Strategie. Es gibt verschiedene dieser Strategien, welche wir später noch genauer besprechen werden. Bei der einfachsten Strategie sucht der Scheduler einfach nur den nächsten Task in der Task-Tabelle raus und gibt dessen Werte an den Dispatcher weiter. Bei hardwarebasierendem Multitasking ist dies nur die Nummer des TSS-Deskriptors, bei softwarebasierendem Multitasking ist dies SS und ESP des Tasks.

### Scheduling-Strategien

Dies ist einer der umfangreichsten Punkte und der schwierigste, so meinen Experten. Das Problem sei ihrer Meinung nach nicht das Wechseln der Tasks sondern das Auswählen des Tasks, welcher als nächstes zu bearbeiten ist. Ich bin allerdings der Meinung, dass das Problem anfangs eher das Wechseln an sich ist, weshalb man sich nicht mit warscheinlichkeitsberechnenden Algorithmen rumschlagen sollte, sondern sich anfangs mit dem einfachsten Verfahren abgeben sollte, einfach den nächsten Task zu nehmen, der in der Tabelle kommt. Allgemein werden an eine Scheduling Strategie folgende Anforderungen gestellt:

1.  Sie muss fair sein, was heißt, dass alle Tasks von Grund auf gleich zu behandeln sind, sodass kein Task ständig dran kommt und kein Task nie dran kommt.
2.  Sie darf nicht zu komplex sein, sodass siche die CPU mehr mit dieser als mit den Tasks beschäftigen würde.
3.  Sie muss unabhängig sein, das heißt, sie darf nicht mit der Anzahl der Tasks zusammenhängen, zum Beispiel nur bei 5 laufenden Tasks funktionieren.
4.  Sie sollte berechenbar sein, also nicht auf Zufallswerten basieren oder auf jedem System anderst funktionieren.
5.  Sie darf nicht beeinflussbar oder manipulierbar sein.

Es gibt viele verschiedene Strategien. Die einen benutzen Prioritätsstufen zum Einteilen der Tasks, andere benutzen die Länge der Tasks. Bei Prioritätseinteilungen gibt es entweder die Möglichkeit, den Tasks die Prioritäten nach ihrem Einsatzbereich (Treiber, Programm,...) zu geben, und dadurch zum Beispiel den Treibern mehr Rechenzeit zuzuteilen, oder aber das Privileglevel zu erhöhen, wenn der Task sich selber pausiert und damit anderen den Vortritt lässt, wenn er gerade keine Rechenzeit benötigt. Sehr häufige Scheduling Strategien sind *Round Robin*, *First Task First* und *Shortest Time Left*. Diese und einige andere werde ich nun ein bisschen erläutern:

#### Round Robin

Bei Round Robin werden alle Tasks in einer Kette hintereinander abgearbeitet und jeder bekommt die gleiche Rechenzeit. Wenn man Prioritäten benutzt, so hat man mehrere Task-Tabellen nach denen man die Tasks aussucht. Die andere Möglichkeit ist, dass es jedes Prioritätlevel nur einmal gibt und ein Task beim Erhöhen seines Levels einfach mit seinem direkten oberen Nachbarn tauscht, und dadruch nach oben kommt.

#### First Task First

Dieses Verfahren ist eigendlich mehr für Batchbetrieb, also dem Abarbeiten der Tasks nacheinander als gleichzeitig gedacht. Es folgt dem Sprichwort *wer zuerst kommt mahlt zuerst*, sodass ein Programm also den ersten Task ausführt und aber derzeit auch noch andere annimmt. Und nach Beendigung dieses Tasks wird der nächste genommen. Das Verfahren ist unbrauchbar für Systeme mit Mikrokerneln, bei denen Treiber und Module auch Tasks darstellen, da diese nicht aufgerufen werden können. Desweiteren scheiden sich die Geister, ob diese Methode überhaupt den Namen "Multitasking" verdient, da die Tasks nicht gleichzeitig ausgeführt werden, jedoch aber hintereinander.

#### Shortest Time Left

Dieses Konzept besagt, dass der Task, der die kleinste Zeit in Anspruch nehmen wird zuerst an die Reihe kommt. Meist bemisst man die Zeit anhand der Größe des Tasks. Jedoch müssen diese Werte ständig aktualisiert werden und es ist schwer für das OS zu sagen, was Code und was Daten sind. Ein Task könnte nur ein Ladeprogramm beinhalten, dass den richtigen Task lädt und würde somit als erstes ausgeführt und umgeht damit das System. Somit ist einer der Grundsätze nicht erfüllt.

#### Longest Time Left

Dieses Konzept ist exakt das Gegenteil des vorherigen. Es bevorzugt den längsten Task und wieder gelten hier alle Einwände, welche bei â€žShortest Time Leftâ€œ genannt wurden.

Das waren auch schon die meiner Meinung nach wichtigsten. Es steht jedem frei, weitere dazu zu entwickeln und bestehende zu verfeinern. Ich selber benutze Round Robin ohne jegliche Form von Prioritäten.

### Taskwechsel

Nun aber zum meiner Meinung kompliziertesten Punkt der Praxis, dem Wechsel selber. Das Implementieren eines Round-Robin-Schedulers sollte nicht alzu schwer gewesen sein, aber der Wechsel hat es in sich, er ist der schwierigste Teil, den ich zu bewältigen hatte, als ich TSS für mein Betriebssystem implementierte. Zuerst möchte ich schildern, wodurch ein Taskwechsel an sich ausgelöst wird. Es gibt mehrere Möglichkeiten:

1.  Ein Far-Jump oder Far-Call bei dem als Selektor ein TSS angegeben wird. Der Offsetteil wird hierbei ignoriert.
2.  Ein IRET nachdem ein Task durch ein TaskGate in der IDT aufgerufen wird, also das NT-Flag gesetzt ist.
3.  Ein Far-Jump oder Far-Call auf ein Task-Gate. Auch hier wird der Offsetteil ignoriert.

Es gibt also 2 Möglichkeiten:

- Man macht einen Far-Jump auf ein TSS.
- Man manipuliert das NT-Flag und simuliert den Aufruf als ein Interrupt durch ein

TaskGate.

Die zweite Methode habe ich noch nie erfolgreich zum Laufen gebracht und sie ist zweifellos die schwierigere, da man nicht nur die Flags sondern auch BackLink-Felder und Stacks manipulieren muss. Deswegen werde ich nun auch die erste Methode ausgiebig erläutern.

Nun, man möchte sich nun denken "nichts leichter als das" und schreibt munter in seinen Code `JMP AX,0x00000000`, wobei man gedenkt, AX mit der Deskriptornummer zu beladen. Spätestens beim Versuch zu Assemblieren wird man feststellen: das geht nicht. Man muss sich also was anderes ausdenken. Erstmal möchte ich sicherheitshalber das ganze zu diesem ausbauen: `JMP DWORD AX:0x12345678`. So wird erzwungen, dass der Assembler auch den kompletten Offsetteil mit übersetzt und nicht Teile durch Abkürzen unter den Tisch kehrt. Das Offset habe ich zu dieser Zahlenfolge gemacht, da ich es für noch ein Schritt sicherer halte, dass das ganze nicht gekürzt wird. Noch haben wir aber das Problem mit dem AX nicht geklärt. Da dies auf jeden Fall nicht geht wandeln wir auch das um: `JMP DWORD 0x1234:0x12345678` Dies wird der Assembler zwar problemlos schlucken, aber leider bringt es uns nicht viel. Wie man vielleicht schon merkt setze ich viel darauf, dass der Assembler dies vollständig und ungekürzt in die Opcodes umwandelt, denn das ist unser Angriffspunkt: HexDump. Wir manipulieren einfach den vom Assembler erstellten Maschinencode während der Ausführung. Ein paar Versuche haben ergeben: `JMP DWORD 0x1234:0x12345678` wird vom Assembler in die Bytes 0xED, 0x78, 0x56, 0x34, 0x12, 0x34 und 0x12 umgewandelt. Wir sehen also, dass die letzten zwei Bytes den Selektor angeben. Wir bleiben also weiterhin dabei, in AX unsere TSS-Deskriptornummer zu haben und bauen uns dann also eine Routine, die die Opcodes manipuliert. Da wir die Bytes in anderen Datentypen auslesen als sie normalerweise abgelegt sind kommt es zu derartigen Verdrehungen, da die CPU andere Zahlendarstellungsverfahren benutzt, als der Mensch und die Zahlen konvertiert werden (näheres in meinem Tutorial *Datenveränderungen im RAM*). Wir können also getrost einfach ein Word an die Stelle mit dem Selektor schreiben, der sich 5 Bytes hinter Befehlbeginn befindet. Den Befehlsbeginn finden wir anhand eines Labels und schon haben wir alles zusammen um folgenden Code zu bauen:

\<asm\> PUSH EDI MOV EDI, tss_switch_label ; Offset laden ADD EDI,0x00000005 ; zum Operanten navigieren STOSW ; neuen Wert eintragen tss_switch_label: JMP DWORD 0x1234:0x12345678 ; springen! POP EDI \</asm\>

Der Code verlangt lediglich, dass sich in AX die TSS-Deskriptornummer des Tasks befindet, zu dem gewechselt werden soll. Alles andere macht die CPU. Somit dürfte das Wechseln auch kein Problem mehr sein.

### Implementierung und Praxis

Tja, wir haben jetzt alles wichtige besprochen, Zeit, zusammen mal einen Code zu coden, den ihr in euer TimerIRQ einbauen könnt, und der für euch den Taskwechsel macht. Zuerst einmal brauchen wir den Scheduler. Ich gehe davon aus, dass die Task- Tabelle an der Adresse 0x00005000 liegt. Die Größe wird anhand einer Variable angegeben, die das Offset des Endes beinhaltet, welche *tasking_end* heißt und vom Typ Double Word ist. Außerdem existiert eine Variable mit dem Namen *tasking_current*, welche ebenfalls vom Typ Double Word ist und den aktuellen Punkt in der Tabelle festhält.

In unserem Code bauen wir reines Round Robin, wir brauchen also Task-Tabellen- Einträge nach der Form, welche unter â€ž4. Task-Tabelleâ€œ gezeigt ist. Ein Eintrag ist also 6 Bytes groß.

Coden wir nun einfach mal den Scheduler. Da wir am Anfang des IRQs keinen Dispatcher brauchen, können wir gleich mit dem Scheduler anfangen.

\<asm\> ADD DWORD \[tasking_current\],0x00000006 ;Werte des

aktuellen Tasks überspringen

MOV ESI,\[tasking_end\] ; ask-Tabellen-Ende laden CMP ESI,\[tasking_current\] ;mit Position des zu ladenden

Tasks vergleichen

JNE scheduler_no_resetting ;falls nicht gleich, also

das Ende noch nicht erreicht ist spingen

MOV DWORD \[tasking_current\],0x00005000 ;sonst auf den

Anfang zurücksetzen

scheduler_no_resetting:

hier haben wir in â€žtasking_currentâ€œ die Adresse der

Daten des zu ladenden Tasks

Da wir in diesem Scheduler einige Register verändern und dies natürlich nicht sein darf, müssen wir diese (nur ESI) noch auf dem Stack sichern: PUSH ESI ADD DWORD \[tasking_current\],0x00000006 ;Werte des

aktuellen Tasks überspringen

MOV ESI,\[tasking_end\] ; ask-Tabellen-Ende laden CMP ESI,\[tasking_current\] ;mit Position des zu ladenden

Tasks vergleichen

JNE scheduler_no_resetting ;falls nicht gleich, also

das Ende noch nicht erreicht ist spingen

MOV DWORD \[tasking_current\],0x00005000 ;sonst auf den

Anfang zurücksetzen

scheduler_no_resetting: POP ESI

hier haben wir in â€žtasking_currentâ€œ die Adresse der

Daten des zu ladenden Tasks

Nun müssen wir aus der Tasktabelle die TSS-Deskriptornummer des zu landenden Tasks raussuchen und in AX bekommen: PUSH ESI ADD DWORD \[tasking_current\],0x00000006 ;Werte des

aktuellen Tasks überspringen

MOV ESI,\[tasking_end\] ; ask-Tabellen-Ende laden CMP ESI,\[tasking_current\] ;mit Position des zu ladenden

Tasks vergleichen

JNE scheduler_no_resetting ;falls nicht gleich, also

das Ende noch nicht erreicht ist spingen

MOV DWORD \[tasking_current\],0x00005000 ;sonst auf den

Anfang zurücksetzen

scheduler_no_resetting: POP ESI

hier haben wir in â€žtasking_currentâ€œ die Adresse der

Daten des zu ladenden Tasks

MOV ESI,\[tasking_current\] ; Offset laden ADD ESI,0x00000002 ; zur Deskriptornummer navigieren LODSW ; Nummer in AX laden Da wir wieder die Register verändern müssen wir auch das Stacksichern verändern: PUSH EAX PUSH ESI ADD DWORD \[tasking_current\],0x00000006 ;Werte des

aktuellen Tasks überspringen

MOV ESI,\[tasking_end\] ; ask-Tabellen-Ende laden CMP ESI,\[tasking_current\] ;mit Position des zu ladenden

Tasks vergleichen

JNE scheduler_no_resetting ;falls nicht gleich, also

das Ende noch nicht erreicht ist spingen

MOV DWORD \[tasking_current\],0x00005000 ;sonst auf den

Anfang zurücksetzen

scheduler_no_resetting:

hier haben wir in â€žtasking_currentâ€œ die Adresse der

Daten des zu ladenden Tasks

MOV ESI,\[tasking_current\] ; Offset laden ADD ESI,0x00000002 ; zur Deskriptornummer navigieren LODSW ; Nummer in AX laden POP ESI POP EAX Nun müssen wir nurnoch unseren Dispatcher dahinter hängen und die Stacksicherung wieder verschieben und schon ist der Code fertig: PUSH EAX PUSH ESI ADD DWORD \[tasking_current\],0x00000006 ;Werte des

aktuellen Tasks überspringen

MOV ESI,\[tasking_end\] ; ask-Tabellen-Ende laden CMP ESI,\[tasking_current\] ;mit Position des zu ladenden

Tasks vergleichen

JNE scheduler_no_resetting ;falls nicht gleich, also

das Ende noch nicht erreicht ist spingen

MOV DWORD \[tasking_current\],0x00005000 ;sonst auf den

Anfang zurücksetzen

scheduler_no_resetting:

hier haben wir in â€žtasking_currentâ€œ die Adresse der

Daten des zu ladenden Tasks

MOV ESI,\[tasking_current\] ; Offset laden ADD ESI,0x00000002 ; zur Deskriptornummer navigieren LODSW ; Nummer in AX laden POP ESI PUSH EDI MOV EDI, tss_switch_label ; Offset laden ADD EDI,0x00000005 ; zum Operanten navigieren STOSW ; neuen Wert eintragen tss_switch_label: JMP DWORD 0x1234:0x12345678 ; springen! POP EDI POP EAX \</asm\>

So, fertig ist der Praxisteil. Ich bitte alle Leser, diesen Code nicht einfach nur blind zu kopieren, denn er lässt sich sicher nicht fehlerlos in das System integrieren, und so schwer ist das Implementieren nicht. Also selber versuchen und bei Fragen mich einfach kontaktieren.

Damit dieser Code richtig geht brauchen wir aber auch einen Task, der gerade läuft. Angezeigt wird dieser Task durch das TR, das TaskRegister. Dieses beinhaltet einen Selektor auf den Deskriptor des aktuellen TSS. Um der CPU vorzugaukeln, welcher Task gerade aktiv ist, benutzen wir den Befehl â€žLTR Operantâ€œ. Als Operant wird die Deskriptornummer des Tasks, der gerade aktiv ist angegeben. Beim Wechsel aktualisiert die CPU das TR dann automatisch. Man braucht den Befehl also nur einmal.

### Tipps & Tricks

Jetzt habe ich zu Schluss noch ein paar Tipps zum Programmieren von Multitasking und zum Programmieren allgemein.

1.  Programmiere auf Sicherheit! Es geht nicht um einen Geschwindigkeitsrekord, sondern um ein stabiles Betriebssystem. Deswegen beachte und bedenke jeden Fehler, der auftreten könnte und richte Fehlerbehandlungen ein. Du musst sie nicht gleich rein implementieren, aber schaffe (wenn auch nur leere) Funktionen dafür, die du später erweitern kannst. Somit hast du ein sicheres Gerüst und gerätst nicht in die Falle, dass ein Code nicht geht, weil ein unerwarteter Fehler aufgetreten ist.
2.  Schreibe nicht alles ab! Code den Code selber. Es wird dir helfen, das Zeug zu verstehen und eigener Code lässt sich besser ins System integrieren.
3.  Entscheide dich fest für ein System und mach keine Abstriche. Versuche deine Gedanken durchzusetzen und gib nicht auf, bloß, weil was nicht klappt.
4.  Achte auch die Optimierung deines Codes. Schon kleine Teile könnte vieles verschnellern und dein System sollte das Minimum an Leistung verbrauchen.
5.  Halte alles Modular, sprich baue auch für deinen Scheduler eine Funktion. Das wird es später erleichtern, die Funktion auszutauschen, wenn du eine andere Strategie verwenden willst.
6.  Und als letztes: Kommentiere deinen Code gut. Gerade in Assembler ist das sehr wichtig.

Tja, das waren auch schon meine Tipps.

### Schluss

Wir sind nun schon am Ende dieses Tutorials angelangt. Es ist etwas lang geworden, warscheinlich deshalb, dass Multitasking nunmal ein komplexes Thema ist, dass man nicht so einfach erklären kann. Ich hoffe es hat Spaß gemacht, ein bisschen in die Welt des Multitasking einzutauchen und davon zu hören. Bei Fragen kann ich nur wieder ermuntern, sich bei mir zu melden. Ich helfe, so gut ich kann. Meine Kontaktdaten gibt es im Impressum.

## Designtechnisches: Multitasking

### Einleitung

Dies ist eine Abwägung zwischen zwe Designideen. Ich will die beiden verschiedenen Möglichkeiten von Multitasking (hardwarebasierendes und softwarebasierendes) miteinander abwiegen. Dieser Text soll keine Antwort auf die Frage geben, welches Multitasking besser oder schlechter sei, sondern lediglich die verschiedenen Vor- und Nachteile aufzeigen und abwiegen.

### Grundlagen

Was ist Multitasking? Dieser Text soll sich zwar darum nicht kümmern, trotzdem werde ich die grundlegendsten Grundlagen aufzeigen. Multitasking ist die Fähigkeit eines Betriebssystems, mehrere Programme, sogenannte Tasks gleichzeitig/parallel laufen zu lassen. Dies ist auf einem mehrprozessorigen System leicht zu verstehen, jeder Prozessor bekommt einen Task zugewiesen, was aber, wenn nur ein Prozessor vorhanden ist? Dann muss man diesen unter den verschiedenen Tasks aufteilen, de gerade bereit sind, ausgeführt zu werden. Man muss also den aktuellen Prozessorzustand speichern und den des nächsten Tasks laden. Wichtig dabei ist, dass alle Werte gespeichert werden, die einen Task beschreiben, also Registerinhalte, Flags, aktuelle Position im Code und so weiter. Der Task an sich darf davon nix merken, er darf nicht bemerken, dass er unterbrochen wurde oder, dass etwaige Register nicht die selben Werte wie vorher haben.

Es gibt zwei verschiedene Methoden, Multitasking durchzuführen, kooperativ oder preemptiv. Kooperatives Multitasking besagt, dass das Programm die Kontrolle über den PC von alleine wieder an das Betriebssystem zurück gibt, welches diese dann neu verteilt, preemptives Multitasking besagt, dass dem Task die Kontrolle in bestimmten Zeitabständen vom System entzogen und neu verteilt wird. Meist wird heutzutage preemptives Multitasking verwendet, welches der Meinung aller nach das sicherste ist, weil es im heutigen Zeitalter der Viren und Trojaner sehr unsicher ist, einem Programm die Kontrolle zu übergeben, bis dieses sie selber zurück gibt. Zum regelmäßigen Entzug der CPU braucht man ein immer wiederkehrendes Ereigniss, welches die CPU auslöst und man ungestört nutzen kann. Dazu nimmt man den ersten Timer des PIC, der standartmäßig 18,2 mal pro Sekunde einen Takt auslöst, aber auch auf höhere Frequenzen programmiert werden kann. Dieser Timer löst immer IRQ 0 aus, welches das System umbiegen kann, und somit in regelmäßigen Abständen die Kontrolle über das System zurück erlangt.  
Es gibt auch Mischformen zwischen preemptivem und kooperativem Multitasking, in welchen das System darauf setzt, dass das Programm die Kontrolle von alleine abgibt, dies aber über den Timer überwacht und notfalls einschreitet.

Ein Multitaskingsystem benötigt immer einen Interrupt, das die Kontrolle entzieht, einen Dispatcher, der den Status speichert und beim neuen wieder läd und einen Scheduler, der den Task auswählt, der als nächstes zu starten ist. Der Scheduler wählt diesen Task anhand der Scheduling Strategie aus.

Die Unterschiede zwischen Softwaretasking und Hardwaretasking liegen lediglich im Dispatcher.

### Softwaretasking

So, nun an die echte Arbeit. Softwaretasking. Beim softwarebasierenden Tasking setzt der Dispatcher darauf, den aktuellen Taskstatus auf dem taskeigenen Stack, dem Stapelspeicher zu speichern und später wieder von diesem zu laden. Verfechter dieser Methode behaupten, dass Softwaretasking 300% schneller im Vergleich zu Hardwaretasking sei, was sicherlich ein großer Vorteil ist. Obgleich muss jeder zugeben, dass dies in der heutigen Zeit von immer weiter wachsender Rechenleistung kein sehr großer Vorteil mehr ist, und trotzdem werde ich ihn als einen solchen einordnen. Ein weiterer Vorteil ist ebenfalls, dass man sich wenig um die Positionen der Daten im Speicher kümmern muss, da diese sich immer auf den Stacks befinden. Einen großen Nachteil hingegen sehe ich ebenfalls darin. Sollte man beispielsweise beabsichtigen, für Programme auch den freien Zugriff auf die FPU zu gestatten, so müsste man deren Status auf dem Stack sichern, wozu man allerdings die exakte Position und Größe kennen müsste, damit man dann dort drauf den Status der FPU speichern könnte, was allerdings zu Verwirrungen mit (E)SP und SS führen würde. Ein weiteres Manko besteht darin, dass man SS und (E)SP ständig kennen muss, und es dem Programm damit also nicht frei steht, seinen eigenen Stack festzulegen. Alles in allem ist Softwaretasking ein einfaches System, mit dem man schnell die Grundlagen von Multitasking erfüllen kann. Kompliziert wird es allerdings, wenn man das Konzept ausbauen und verfeinern will. Außerdem kommt man nie ganz um TSS rum, auch bei Softwaretasking braucht man mindestens ein TaskStateSegment.

Auch stehen viele Funktionen des Protected Mode erst mit TSS richtig zur Verfügung, man denke an das explizite Sperren von Ports zum Beispiel. Aber auch deshalb verbraucht das Softwaretasking relativ wenig Speicher. Die Stacks können ausgelagert werden, sodass der Speicherverbrauch im RAM auf das Minimum reduziert wird und man kann auswählen, welche Informationen man speichern will, und welche nicht.

| Vorteile | Nachteile |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| • Hohe Geschwindigkeit beim Taskwechsel<br>• Sehr einfach zu implementieren<br>• Wenig Platzverbrauch<br> | • Verwirrend wegen TSS<br>• Schwer zu erweitern<br>• Nicht alle Möglichkeiten des Protected Mode benutzbar<br> |

### Hardwaretasking

Hardwaretasking. Wie der Name schon sagt setzt das hardwarebasierende Multitasking auf die Möglichkeiten der CPU zum Speichern des aktuellen Taskzustandes. Dazu gibt es ab jedem 286er ein sogenanntes TaskStateSegment, in welchem die CPU den aktuellen Taskzustand speichert. Diese Methode nimmt dem Entwickler des Systems viel Arbeit ab, welche die CPU übernimmt. Die Aufgabe des Dispatchers beschränkt sich bei Hardwaretasking darauf, einen Sprung ins andere TSS zu machen, wodurch die CPU veranlasst wird, den aktuellen Status zu sichern und den neuen zu laden. Dies passiert alles automatisch und ohne Mithilfe des Programmierers, was sicherlich einer der Vorteile ist. Trotzdem ist genau dieser Sprung relativ komplex, da man sich mit den Opcodes auskennen muss und ihn mit einer eigenen Routine immer wieder zu ändern hat, da man für gewöhlich keinen variablen Sprung machen kann. Ebenso dauert das Wechseln etwas länger. Die CPU an sich sichert alle Register und wichtigen Inhalte, sodass ein TSS mindestens 104 Bytes an Speicher braucht. Außerdem gibt es in einem TSS viele Bereiche, die ungenutzt, reserviert sind. Dies ist sicher ein Manko an Hardwaretasking, da es immer unpraktisch ist, viel Speicher fest zu verbrauchen, den man nicht auslagern kann. Allerdings lässt sich ein TSS beliebig in die Länge ziehen wodurch man erreicht, dass man auch hinter die Registerinformationen zum Beispiel noch den FPU-Status sichern kann. Auch ist alles das gleiche, man braucht also nicht wie bei Softwaretasking noch irgendein Segment oder ähnliches, wobei man aber mindestens zwei Tasks braucht, die gerade laufen, da man sonst nicht wechseln kann, weil TSS-Tasks nicht reentrant sind, sprich man einen aktiven Task nicht wieder aktivieren kann.

| Vorteile | Nachteile |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| • Die CPU nimmt viele Aufgaben ab<br>• Man kann alle Möglichkeiten des PM ausschöpfen<br>• Lässt sich leicht erweitern<br> | • Verbraucht viel Platz<br>• Taskwechsel dauert relativ lange<br>• Komplizierter Taskwechsel mit Opcodes<br> |

### Schluss

So, ich hoffe, ich hab mit dem Text hier einigen die Entscheidung zwischen Software- und Hardwaretasking erleichtert. Letztendlich liegt es nur am Programmierer selber, was er am liebsten mag. Bei Fragen bin ich auch wieder durch meine Kontaktdaten im Impressum erreichbar.

## Architekturtechnisches: Datenveränderungen im RAM

### Einleitung

Ich schreibe dieses Tutorial für Leute, die wie ich anfangs das Prinzip des Speicherns von Daten im RAM nicht verstehen. Dabei geht es nicht um Programmiersprachenbefehle, sondern viel mehr darum, was mit den Daten im RAM gemacht wird.

    Dieses "Phänomen" kann man besonders gut sehen, wenn man mal das DWORD 0x12345678 byteweise ausließt. Man erhält 

das hier: 0x78,0x56,0x34 und 0x12. Man stellt sich nun die Frage, warum dies so ist. Nun, vielleicht sind Ihnen BigEndian und LittleEndian ein Begriff. Falls nicht, werde ich dies erstmal erklären.

### BigEndian / LittleEndian

BigEndian ist eine Form, eine Zahl zu speichern. Bei dieser Form speichert man das wichtigste Bit (also das, das bei einer Veränderung die Zahl am meisten beeinflussen würde) an erster Stelle und danach die anderen, also das zweitwichtigste und so weiter. Dies ist das System, nach welchem auch wir unsere Zahlen darstellen. Die höchstwertigste Stelle als erstes.

LittleEndian ist das genaue Gegenteil von BigEndian. Es beginnt mit dem â€žlast significantâ€œ Bit, also dem unwichtigsten im Gegensatz zu dem *most significant* Bit bei BigEndian. Das System von LittleEndian wird in der normalen Zahlenwelt der Menschen nicht benutzt. Jedoch benutzt es der Computer, da diese Art von Datenspeicherung ermöglicht, dass der Computer Zahlenwerte aus dem RAM lesen kann, ohne vorher deren Anzahl von Stellen zu kennen. Bei LittleEndian muss der PC nur Bit für Bit lesen und die Zahl, welche er davor hat mit 2 multiplizieren, um dann das neue Bit zu addieren. Bei BigEndian müsste der Computer wissen, wie viele Stellen die Zahl hat, um dem 1. Bit mit dem passenden Stellenwert zu multiplizieren.

### Auflösung

Da wir nun also geklärt haben, was Big- und LittleEndian sind und deren Aufbau, sowie deren Benutzung geklärt haben, können wir mit einem Beispiel fortfahren. Gegeben ist eine Zahl von der Größe WORD, also 16 Bit. Diese sieht so aus: 0001001000110100. In Hex besitzt sie den Wert 0x1234. Der Computer würde diese Zahl in dieser Bitfolge ablegen: 0010110001001000. Dies ergibt in Hex 0x2C48. Da wir nun aber als kleinste Einheit Byts lesen können würden wir diese Bytes erhalten: 0x34 und 0x12. Die beiden Bytes währen also vertauscht. Wenn man ein DWORD schreibt, und dies in Bytes ausließt, erhält man zuerst das letzte, dann das vorletzte, dann das zweite und dann das erste Byte.

### Einsatz

Wichtig ist diese Kenntnis, wenn wir Tabellen, die wir sehr oft aus Tutorials bekommen in anderen Datentypen belegen und benutzen wollen, als vorgegeben. Wir müssen diese Phönomene erkennen und uns danach richten, damit wir immer die richtigen Stellen in einem Speicherteil benutzen.

### Schluss

So, das war auch schon alles, was ich dazu zu sagen hab. Ich hoffe, alles is klar geworden, falls nicht bin ich immer unter meinen Kontaktdaten erreichbar. Diese stehen im Impressum.

## Hardwaretechnisches: Der PC-Lautsprecher

### Theorie

Wir werden jetzt zuerst ein bisschen Theorie machen und uns danach mit der Praxis beschäftigen. Der PC Lautsprecher wird über den Timer-Baustein angesteuert, der als Zeitgeber und Zähler fungiert. Der Timer-Baustein besteht intern aus 3 verschiedenen unabhängigen Timerkanälen, deren I/O-Ports die Adressen 40h (64d), 41h (65d) und 42h (66d) besitzen, sowie einem Kommandoregister mit der Adresse 43h (67d). Die I/O-Ports sind 8 Bit breit. Die ersten beiden Kanäle werden für die Systemzeit und für das Refreshing des RAMs verwendet. Der dritte Kanal ist mit dem PC-Lautsprecher verbunden. Veränderungen an den ersten beiden Kanälen könnten verhängnissvolle Folgen haben, weshalb im Code immer exakt geprüft werden sollte, ob die Port-Adressen stimmen.  
Jeder dieser 3 Kanäle besitzt ein Latch-Register und ein Counter-Register, die beide 16 Bit breit sind, zwei Signaleingänge (CLOCK und GATE) sowie einen Signalausgang (OUT).

Jetzt zur Funktionsweise: Am Eingang CLOCK liegt eine konstante Frequenz von 1,19318 Mhz an. (Das heißt, dass vom Timer 1193180 mal pro Sekunde eins an den Eingang geschickt wird.) In das Latch-Register wird eine Zahl, der so genannte Teiler, geschrieben. Dieser Wert wird in das Counterregister übertragen und mit jedem Impuls am Eingang CLOCK um 1 dekrementiert. Wenn das Counter-Register den Wert 0 erreicht, wird ein Puls über Ausgang OUT geschickt. Nacheinander entsteht so bei Wiederholung eine Frequenz von 1193180/Teiler, die beim Lautsprecher ankommt, der das ganze dann in einen Ton umwandelt.

Das Kommandoregister wird zum Seuern dieses Bausteins mit dem Kommandobyte geladen, welches z.B. einstellt, welche Betriebsart gewählt wurde. Das Kommandobyte ist so aufgebaut:

![6_1.png](http://www.joachim-neu.de/public/lowlevel/7/6_1.png)

Die Betriebsart bestimmt die Länge der Pulsfolge und, ob sie sich automatisch wiederholt usw. Der Code 011 bestimmt, dass eine Pulsfolge erzeugt wird, die zum Erzeugen von Tönen nützlich ist. Da die Ports ja nur 8 Bit breit sind, das Latch-Register aber 16 Bit, wird im Kommandobyte auch noch festgelegt, ob nur das High-Byte, nur das Low-Byte oder beide hintereinander (zuerst das Low-Byte, dann das High-Byte) bearbeitet werden sollen. Das 0.Bit legt fest, ob die Zahl im Kommandobyte binär- oder BCD-codiert lesen soll.

Hier ein Beispiel: Das Kommandobyte 0xB6 = 10110110 stellt ein, dass...

- der Timer-Kanal 2 programmiert werden soll,
- erst das Low-und dann das High-Byte bearbeitet werden soll
- eine symetrische Pulsfolge erzeugt werden soll,
- das Kommandobyte binär zu interpretieren ist.

Die Programmierung des Timer-Bausteins erfolgt in 2 Schritten:

1.  Kommandobyte in den Kommandoport schreiben, und dadurch die Anweisungen verteilen.
2.  Teiler in den Port des augewählten Timer-Kanals schreiben.

So jetzt könnten wir zwar Töne ausgeben, aber wir müssen dazu zuerst noch den Lautsprecher anstellen (und später wieder ausstellen). Das ist ganz schlau geregelt. Der Lautsprecher ist über ein UND-Gatter, das heißt, dass am Ende nur 1 raus kommt, wenn beide Eingänge 1 haben, mit dem OUT-Ausgang des 2. Timer-Kanals und dem Ausgang des 1. Bits des Port B (0x61) im PPI (=Programmable Peripherical Interface) verbunden. Bit 0 des Port B im PPI ist mir dem GATEEingang des PPI-Ports B verbunden. Das heißt, es wird nur etwas ausgegeben, wenn das 1. Bit des Port B im PPI auf 1 und das 0. Bit auf 0 steht. Wenn beide Bits gelöscht sind, wird der Lautsprecher wieder ausgeschaltet. Das ist eigendlich schon die gesamte Theorie, kommen wir jetzt zur Praxis!

### Praxis

Wir werden jetzt ein paar Funktionen für die Programmiersprache C zusammen entwickeln. Nebenher schreiben wir die Funktionen dann auch noch in Assembler. Also, fangen wir an, ich denke in C dürfte jeder die Funktionen â€žinp()â€œ und â€žoutp()â€œ schon für sein OS implementiert haben, weshalb ich darauf baue. Wir wissen, wir schalten den Lautsprecher an, indem die letzten 2 Bits in Port 0x61 auf 11b stehen. Daraus machen wir schnell eine Funktion:

\<c\> void switch_on() { outp(0x61,inp(0x61) \| 3); } \</c\>

Okay. In Assembler baue ich das schon alles mit in die \_sound-Funktion ein. So, an können wir ihn machen, nur aus noch nicht, aber wir wissen, wenn die beiden letzten Bits in Port 0x61 auf 00b stehen, dann ist der Lautsprecher aus. Das geht also ganz leicht:

\<c\> void switch_off() { outp(0x61,inp(0x61) &~3); } \</c\>

Und in Assembler: \<asm\> \_switch_off: IN AL,61h AND AL,11111100b OUT 61h,AL RET \</asm\>

Fertig. An und aus können wir ihn schon machen, aber das Herzstückt kommt noch! Einen Ton ausgeben. Das geht mit folgendem, diesmal zuerst in Assembler ;-):

\<asm\> \_sound: MOV AX,34DDH ;Die Frequenz wird in BX übergeben. MOV DX,0012H CMP DX,BX JNC DONE1 DIV BX MOV BX,AX IN AL,61H TEST AL,3 JNZ A99 OR AL,3 OUT 61H,AL MOV AL,0B6H OUT 43H,AL A99: MOV AL,BL OUT 42H,AL MOV AL,BH OUT 42H,AL DONE1: RET \</asm\>

So, jetzt in C: \<c\> void sound(unsigned frequenz) { unsigned teiler; teiler = 1193180L/frequenz; outp(0x43,0xB6); outp(0x42,teiler&0xFF); outp(0x42,teiler \>\> 8); switch_on() //wenn der Sound aufhören soll, muss die Funktion //switch_off aufgerufen werden. } \</c\>

### Schluss

So, geschafft! Das waren die Geheimnisse des PC-Lautsprechers! Zwei Sachen muss beim Nachmachen noch beachtet werden: 1. Es muss zwischen den Tönen eine Funktion benutzt werden, die das Programm anhält, denn sonst werden die Töne viel zu schnell abgespielt, und man hört nichts. 2. Die Assembler-Funktionen kann man nicht so in C übernehmen. Dazu muss man sich noch um die C-Calling-Convention kümmern, und die Funktionen ein bisschen umbauen. Ich hoffe ich konnte alles so erklären, dass es verständlich war. Und die ein oder anderen Unklarheiten durch den letzten Praxisteil klären. Ich bedanke mich bei meinem C-Buch, aus dem ich die Informationen hab, bei ASHLEY4 aus dem FlatAssemblerForum (<http://board.flatassembler.net/>) für die Hilfe beim Code und bei allen anderen, die mir geholfen

haben. Meine Kontaktdaten zum Melden bei Problemen finden sich im Impressum.

## Software- & Treibertechnisches: FAT12 Dateizugriff

### Einleitung

Ein Betriebssystem zu schreiben ist wirklich nicht einfach. Will man es jedoch machen, und man hat einen Bootloader und einen simplen Kernel, der einen Text ausgibt, geschrieben, wird man schnell zum nächsten Problem kommen: Dateien! 'Wie/wo/was mache ich?' sind wohl die ersten Fragen. Mit diesem Tutorial möchte ich hier ein bisschen helfen. Wichtig: Ich gehe davon aus, dass ihr 'OS Dev-Tutorial' ([Ausgabe 1](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-1 "Ausgabe 1")) und 'Das FAT12 Dateisystem' ([Ausgabe 4](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-4 "Ausgabe 4")) gelesen und verstanden habt. OK, blabla, let's go!

### Dateien finden

Der erste Schritt, wenn man Dateizugriff machen will, ist natürlich die Dateien finden. Und wie? Hier brauchen wir das 'Root-Directory' (=RD). Kurz: Das RD startet im 19. Sektor. Ein Dateieintrag ist 0x20 (32) Bytes lang, und der Dateiname ist 12 Zeichen lang: Byte 0 - 11. OK, jetzt haben wir keine Probleme mehr. Naja, fast: Wenn eine Datei gelöscht oder umbenannt wird, bleibt der alte Eintrag, nur wird das erste Byte des Namens auf 0xE5 gesetzt. Außerdem gibt es noch etwas seltsame Einträge, hab aber nicht herausgefunden was es für welche sind. Auf alle Fälle ist das 3. Byte dieser Einträge immer 0x00, und so werden sie auch ignoriert. OK, jetzt verstehen wir, wie man theoretisch Dateien finden kann. Und praktisch? Keine Angst, hier ist der Code (Der Code ist der Kernel, den Bootloader müsste man dann schon selber machen. Danke an mastermesh für das Tutorial in LL#1 - Für den Grund hab ich den Code verwendet.):

\<asm\>

\- - - - - \[ Dateien finden - CODE \] - - - - -

        start:

mov ax, 0x2000 ; eax=0x2000 mov es, ax ; Daten werden nach ES:BX geschrieben, ES=0x2000 mov ds, ax mov bx, 0 ; BX=0x0

        loadk:

mov ah, 0x2 ; ah=2: Sektoren lesen mov al, 0x12 ; Wie viele Sektoren wir lesen (18) mov ch, 0 ; Cylinder 0 mov cl, 1 ; Starten bei Sektor 1 xor dx, dx ; dx=0 inc dh ; Head 1: ; Soweit ich das mitbekommen habe, besteht ein ; Cylinder aus 2 Teilen Head0 und Head1. Head0 ; sind die ersten 18 Bytes (0-17) und Head1 sind ; die zweiten 18 Bytes (18-36). Da Root Entry ; auf Sektor 19 liegt, brauchen wir head1. int 0x13 ; BIOS-Call jc loadk ; Wenn Fehler: Nochmal

mov bx, 0x200 ; bx=Adresse des 2. Sektors, den wir in den ; Speicher gelesen haben

        fat12read:

mov ah, \[bx\] ; ah=erstes Byte des Dateinamen cmp ah, 0x0 ; Checken ob das Byte 0 ist: Ende der Einträge je endfat12read ; Wenn es das Ende ist, aufhören zum Lesen cmp ah, 0xE5 ; Checken ob das Byte 0xE5 ist: Gelöschte Datei je fat12next ; Wenn es eine gelöschte Datei ist: Nächster Eintrag push bx ; Speicher bx am Stack, weil es durch 'call putstr' ; geändert wird

mov al, \[bx+2\] ; al=3. Buchstabe des Namens test al, al ; Testen ob null jz fat12next ; Wenn null, dann nächster Eintrag

mov cx, 11 ; cx=11, weil ein Dateiname aus 11 Zeichen besteht mov si, bx ; si=Adresse des Dateinamens im Speicher call putstr ; Schreibe Dateiname

pop bx ; Stellt bx wieder her fat12next: add bx, 0x20 ; Nächster Eintrag jmp fat12read

        endfat12read:

mov ax, 0x1000 ; es und ds aktualisieren, da wir jetzt wieder ; im Speicher auf 0x1000 arbeiten. mov es, ax mov ds, ax

mov cx, 0xFFFF ; cx=0xFFFF: Gibt die Stringlänge an, weil ich aber ; zu faul war, die Zeichenlänge zu überprüfen, ; hab ichs auf das höchste gestellt. Weil ; ein String aber mit 0x00 beendet wird, ist es egal mov si, msg ; si=Adresse des Strings call putstr ; Schreib String mov cx, 0xFFFF ; Nochmal das Gleiche mov si, m_boot ; Nochmal das Gleiche call putstr ; Nochmal das Gleiche call getkey ; Call zu GetKey jmp reboot ; Springe zu reboot

msg db 'Welcome to SPTH-OS 1.1',0 ; String 1 m_boot db 'Press any key...',0 ; String 2

        putstr:              ; Schreib-Funktion

lodsb ; \[si\]-\>al or al, al ; Teste al auf 0x0 (=Ende) jz putstrd ; Wenn Ende des Strings, dann mov ah, 0xE ; ah=0xE: Schreibe Zeichen mov bx, 0x7 ; Zeichenfarbe: 0x7 = weißes Zeichen/schwarzer ; Hintergrund int 0x10 ; call loop putstr ; Nächstes Zeichen

        putstrd:

mov al, 13 ; Schreibe 13 mov ah, 0xE mov bx, 0x7 int 0x10

mov al, 10 ; Schreibe 10 (13,10=Zeilenumbruch) mov ah, 0xE mov bx, 0x7 int 0x10 retn

        getkey:

mov ah, 0 ; ah=0: Get Key BIOS Funktion int 0x16 ; Call ret

        reboot:

db 0xEA ; Hexdump für Reboot: jmp 00FF:FF00 dw 0x0 dw 0xFFFF

\- - - - - \[ Dateien finden - CODE \] - - - - -

\</asm\>

Der Code tut, wie es sein sollte, das, was man von ihm erwartet: Er schreibt alle Dateinamen im Root der Diskette untereinander auf. Also: Passt!

### Dateien erstellen

Nachdem wir jetzt die Dateien gelesen haben, dürften wir kein Problem mehr haben, eine neue Datei zu erstellen. Was ist wichtig? Zuerst müssen wir einen leeren Platz im Root-Directory für den Dateieintrag finden. Haben wir den gefunden, müssen wir den Sektor für die Daten suchen. Hier nehmen wir einfachheitshalber den Sektor des letzten Eintrags+1. Natürlich könnten so nur 512 Byte Dateien gespeichert werden, weil sonst Fehler auftreten können. Aber da ich nicht hunderte von Zeilen schreiben will, um alles zu perfektionieren, hab ich nur die Einfachlösung hier.  
Wenn man größere Dateien speichern möchte, muss man die Dateigröße des letzten Eintrags in Sektoren umrechnen, und dann ist diese Zahl plus die Sektornummer des Eintrags die neue Adresse für den neuen Eintrag. Also, hier ist der Code, wie es funktioniert, eine neue Datei anzulegen.

\<asm\>

\- - - - - \[ Dateien erstellen - CODE \] - - - - -

        start:

mov ax, 0x2000 ; ax=0x2000 mov es, ax ; Daten werden nach ES:BX geschrieben, ES=0x2000 mov ds, ax mov bx, 0 ; BX=0x0

        loadk:

mov ah, 0x2 ; ah=2: Sektoren lesen mov al, 0x12 ; Wie viele Sektoren wir lesen (18) mov ch, 0 ; Cylinder 0 mov cl, 1 ; Starten bei Sektor 1 xor dx, dx ; dx=0 inc dh ; Head 1: ; Soweit ich das mitbekommen hab, besteht ein ; Cylinder aus 2 Teilen Head0 und Head1. Head0 ; sind die ersten 18 Bytes (0-17) und Head1 sind ; die zweiten 18 Bytes (18-36). Da Root Entry auf ; Sektor 19 liegt, brauchen wir head1. int 0x13 ; Interupt 13 jc loadk ; Wenn Fehler: Nochmal

mov bx, 0x200-0x20 ; bx=Adresse des 2. Sektors, den wir in den Speicher ; gelesen haben, -0x20 deshalb, weil wir den ersten ; Eintrag auch checken müssen, und da bx am Anfang ; des loops um 0x20 erhöht wird, müssen wir es verkleinern

        fat12emptyentry:

add bx, 0x20 ; Nächster Eintrag mov al, \[bx\] ; al=Erstes Zeichen des Eintrags test al, al ; Checken ob null

        jnz     fat12emptyentry      ; Wenn Eintrag besetzt ist, dann suche weiter

mov ax, \[bx-6\] ; ax enthält jetzt den Sektor des letzten Eintrags inc ax ; und wir nehmen den nächsten. ACHTUNG: Ich gehe ; davon aus, dass keine Datei größer ist als ; 512 Bytes ist. Wenn man es professionell ; machen will, muss man die Größe der vorherigen ; Datei checken.

mov ax, 0x1000 ; Code im Speicher mov es, ax mov ds, ax

mov \[FAT12Sector\], ax ; ax in den vorbestimmten Bereich schreiben

mov di, bx ; di=unser Teil des Sektors mov bx, NewEntry ; bx=Offset vom neuen Eintrag

Data2Mem: mov ax, 0x1000 ; Code im Speicher mov es, ax mov ds, ax

mov al, byte \[bx\] ; al=Byte zu schreiben

mov cx, 0x2000 ; Sektor im Speicher mov es, cx mov ds, cx

stosb ; AL -\> ES:DI inc bx ; Nächstes Byte cmp bx, 0x20+NewEntry ; Check ob wir alle haben jne Data2Mem ; Wenn nicht, nochmal

mov bx, 0x0 ; ES:BX -\> Databuffer Mem2Disk: mov ah, 0x3 ; AH=3: Schreibe Sektor(en) mov al, 0x12 ; Wir schreiben 18 Sektor mov ch, 0x0 ; Cylinder 0 mov cl, 0x1 ; Sektor 1 xor dx,dx ; dx=0 inc dh ; Head 1! int 0x13 ; Interrupt 13

mov ax, 0x1000 ; es und ds aktualisieren, da wir jetzt wieder ; im Speicher auf 0x1000 arbeiten. mov es, ax mov ds, ax

string: mov cx, 0xFFFF ; cx=0xFFFF: Gibt die Stringlänge an, weil ich aber zu ; faul war, die Zeichenlänge zu überprüfen, hab ichs ; auf das höchste gestellt. Weil ; ein String aber mit 0x0 beendet wird, ist es egal mov si, msg ; si=Adresse des Strings call putstr ; Schreib String mov cx, 0xFFFF ; Nochmal das Gleiche mov si, m_boot ; Nochmal das Gleiche call putstr ; Nochmal das Gleiche call getkey ; Call zu GetKey jmp reboot ; Springe zu reboot

msg db 'Welcome to SPTH-OS 1.1',0 ; String 1 m_boot db 'Press any key...',0 ; String 2

        NewEntry:        db 'FILE    TXT'    ; DIR_NAME

db 0x20 ; DIR_Attribute: Archiv db 0x0 ; DIR_NTRes: Reserviert db 0x0 ; DIR_CrtTimeTenth: Millisekunden des Speicherns ; - ist mir egal :) db 0x6F,0x3E ; Wahrscheinlich Erstellungsdatum, ; ist hier aber egal db 0x9C,0x2B,0x9C,0x2B ; Wahrscheinlich: Letzter Zugriff, letzte Ã„nderung ; - ist hier auch egal db 0x0,0x0 ; Reserviert dd 0x733E9C2B ; Wieder 2 mal Datum - das ist in diesem Tutorial ; aber egal FAT12Sector dw 0x0000 ; Das hier ist wichtig: Der Sektor, in dem die ; Daten liegen dd 0x00000000 ; Dateigröße

  

        putstr:              ; Schreib-Funktion

lodsb ; \[si\]-\>al or al, al ; Teste al auf 0x0 (=Ende) jz putstrd ; Wenn Ende des Strings, dann mov ah, 0xE ; ah=0xE: Schreib Zeichen mov bx, 0x7 ; Zeichenfarbe: 0x7 = weißes Zeichen/schwarzer ; Hintergrund int 0x10 ; call loop putstr ; Nächstes Zeichen

        putstrd:

mov al, 13 ; Schreibe ASCII 13 mov ah, 0xE mov bx, 0x7 int 0x10

mov al, 10 ; Schreibe ASCII 10 (13,10=Zeilenumbruch) mov ah, 0xE mov bx, 0x7 int 0x10 retn

        getkey:

mov ah, 0 ; ah=0: Get Key BIOS Funktion int 0x16 ; Call ret

        reboot:

db 0xEA ; Hexdump für Reboot: jmp 00FF:FF00 dw 0x0 dw 0xFFFF

\- - - - - \[ Dateien erstellen - CODE \] - - - - -

\</asm\>

Es ist alles so einfach und klein wie möglich gehalten. Es fehlen einige JumpCarry, um sich vor Abstürzen zu schützen. Da ich hier aber kein vollständiges OS schreiben will, sondern nur die Infos, wie man so etwas machen kann, hab ich es nicht perfektioniert. Trotzdem: Der Code macht genau was er soll.

### Dateien lesen

Nachdem wir wissen, wie man Dateien im Root-Directory finden kann und neu erstellen kann, kommt jetzt endlich das zum Spiel, wofür Dateien eigentlich gut sind: Daten. Ich habe hier davon abgesehen, nocheinmal die Root-Directory auszulesen, und so weiter, deswegen habe ich einfach einen Eintrag der RootDirectory als Daten in den Code geschrieben. Der Code kann natürlich trotzdem verwendet werden, muss nur Root_Entry in die echte gefundene Adresse geändert werden. Außerdem ist es noch einfacher, da nicht immer zwischen Code (ES=0x1000) und dem gelesenen Sektoren Daten (ES=0x2000) geändert werden.

Der Code ließt die Daten einer Datei, aber höchstens 512 Bytes. Das kann aber einfach geändert werden, habs hier nicht gemacht, weil es eigentlich nichts mit dem zu tun hat, was ich vermitteln möchte: Dateien lesen.

Wie gesagt, der Code ist ganz kurz, bis aufs äußerste reduziert und so weiter. Funktioniert trotzdem :) \<asm\>

\- - - - - \[ Dateien lesen - CODE \] - - - - -

        start:

mov ax, 0x2000 ; ax=0x2000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

        loadk:

mov ah, 0x2 ; ah=2: Sektoren lesen mov al, 0x12 ; Wie viele Sektoren wir lesen (18) mov ch, 0 ; Cylinder 0 mov cl, 1 ; Starten bei Sektor 1 xor dx, dx ; dx=0 inc dh ; Head 1 int 0x13 ; Interupt 13

mov ax, 0x1000 ; ax=0x1000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

mov cl, byte \[Root_entry+26\] ; Der Sektor, in dem unsre Daten liegen add cl, 13 ; Der erste Datensektor ist anscheinend immer ; Sektor 31: -18, weil Head1 mov ax, 0x200 ; 0x200=512: Ein Sektor xor ch, ch ; ch=0 mul cx ; cx\*ax: Sektornummer\*Sektorgröße: Adresse, wo wir lesen mov si, ax ; Resultat der Multiplikation in ax, und jetzt in si

  
mov ax, 0x2000 ; ax=0x2000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

mov cx, 512 ; 512 Bytes schreiben, wenn ein 0x0 ist, wird abgebrochen call putstr ; Schreibe!

mov ax, 0x1000 ; ax=0x1000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

mov cx, 0xFFFF ; cx=0xFFFF: Gibt die Stringlänge an, weil ich aber zu ; faul war, die Zeichenlänge zu überprüfen, hab ichs ; auf das höchste gestellt. Weil ein String aber mit ; 0x0 beendet wird, ist es egal mov si, msg ; si=Adresse des Strings call putstr ; Schreib String mov cx, 0xFFFF ; Nochmal das Gleiche mov si, m_boot ; Nochmal das Gleiche call putstr ; Nochmal das Gleiche call getkey ; Call zu GetKey jmp reboot ; Springe zu reboot

msg db 'Welcome to SPTH-OS 1.1',0 ; String 1 m_boot db 'Press any key...',0 ; String 2 big_file db 'Die Datei ist größer als 512 Bytes...',0

Root_entry db 0x53,0x50,0x54,0x48 ; Das ist ein Root_Entry db 0x20,0x20,0x20,0x20 ; Wie man den bekommt, sieht man db 0x54,0x58,0x54,0x20 ; Oben schon db 0x18,0x9F,0x5D,0x2B db 0x9D,0x2B,0x9D,0x2B db 0x00,0x00,0xC7,0xA0 db 0x9C,0x2B,0x02,0x00 db 0x0D,0x00,0x00,0x00

  

        putstr:              ; Schreib-Funktion

lodsb ; \[si\]-\>al or al, al ; Teste al auf 0x0 (=Ende) jz putstrd ; Wenn Ende des Strings, dann mov ah, 0xE ; ah=0xE: Schreib Zeichen mov bx, 0x7 ; Zeichenfarbe: 0x7 = weißes Zeichen/schwarzer ; Hintergrund int 0x10 ; call loop putstr ; Nächstes Zeichen

        putstrd:

mov al, 13 ; Schreibe ASCII 13 mov ah, 0xE mov bx, 0x7 int 0x10

mov al, 10 ; Schreibe ASCII 10 (13,10=Zeilenumbruch) mov ah, 0xE mov bx, 0x7 int 0x10 retn

        too_big:

mov si, big_file mov cx, 0xFFFF call putstr

        getkey:

mov ah, 0 ; ah=0: Get Key BIOS Funktion int 0x16 ; Call ret

        reboot:

db 0xEA ; Hexdump für Reboot: jmp 00FF:FF00 dw 0x0 dw 0xFFFF

\- - - - - \[ Dateien lesen - CODE \] - - - - -

\</asm\>

Kurz - macht aber, was er soll. Man sollte natürlich, wenn man ein ersthaftes Projekt hat, auch Dateien, die größer sind als 1 Sektor lesen. Das ist aber nicht schwer. Man muss die Sektoren bekommen (shr dateigröße, 9 \| inc), und auf die Cylinder/Head aufpassen. Wenn man es ganz toll machen möchte, könnte man natürlich auch die Schrift in einer schönen Farbe ausgeben lassen. Sieht sicher besonders gut aus ;)

### Dateien schreiben

Was bringt ein Betriebssystem, dass keine Dateien schreiben kann? Nichts. Darum hier der Beispielcode, wie man in eine Datei schreibt. Dieser Code ähnelt sehr dem Lese-Code. Wenn man nun ein OS macht, dann kann man die gleichen Sachen einfach rausnehmen, und spart damit sehr viele Bytes, und es wird wahrscheinlich (kommt drauf an, wie mans macht) viel übersichtlicher.  
Also, der Code ist natürlich wieder beschrieben, darum muss ich hier nichts mehr erklären.

\<asm\>

\- - - - - \[ Dateien schreiben - CODE \] - - - - -

        start:

mov ax, 0x2000 ; ax=0x2000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

        loadk:

mov ax, contentend-content ; ax=Länge des Strings zu schreiben

mov \[Root_entry+28\], ax ; In den Root_Dir_entry schreiben

Hier das neue Root_Directory schreiben. Wird oben schon erklärt wie!

  
mov ah, 0x2 ; ah=2: Sektoren lesen mov al, 0x12 ; Wieviele Sektoren wir lesen (18) mov ch, 0 ; Cylinder 0 mov cl, 1 ; Starten bei Sektor 1 xor dx, dx ; dx=0 inc dh ; Head 1 int 0x13 ; Interupt 13

mov ax, 0x1000 ; ax=0x1000 mov es, ax mov ds, ax mov bx, 0 ; BX=0x0

mov cl, byte \[Root_entry+26\] ; Der Sektor, in den wir schreiben add cl, 13 ; Der erste Datensektor ist anscheinend immer ; Sektor 31: -18, weil Head1 mov ax, 0x200 ; 0x200=512: Ein Sektor xor ch, ch ; ch=0 mul cx ; cx\*ax: Sektornummer\*Sektorgröße: Adresse, ; wo wir lesen mov di, ax ; Wo wir schreiben

mov bx, content ; bx zeigt auf den String, den wir schrieben werden

Data2Mem: mov ax, 0x1000 ; Code im Speicher mov es, ax mov ds, ax

mov al, byte \[bx\] ; al=Byte zu schreiben

mov cx, 0x2000 ; Sektor im Speicher mov es, cx mov ds, cx

stosb ; AL -\> ES:DI inc bx ; Nächstes Byte cmp bx, contentend ; Check ob wir alles haben jne Data2Mem ; Wenn nicht, nochmal

xor bx, bx ; bx=0

mov ah, 0x3 ; AH=3: Schreibe Sektor(en) mov al, 0x12 ; Wir schreiben 1 Sektor mov ch, 0x0 ; Cylinder 0 mov cl, \[Root_entry+26\] ; Wo wir schreiben, aus Root_entry add cl, 1 ; Jetzt haben wir ihn! mov cl, 0x1 ; Sektor 1 xor dx,dx ; dx=0 inc dh ; Head 1! int 0x13 ; Interrupt 13

mov cx, 0x1000 ; Sektor im Speicher mov es, cx mov ds, cx

mov cx, 0xFFFF ; cx=0xFFFF: Gibt die Stringlänge an, weil ich aber zu ; faul war, die Zeichenlänge zu überprüfen, hab ichs ; auf das höchste gestellt. Weil ein String aber mit ; 0x0 beendet wird, ist es egal mov si, msg ; si=Adresse des Strings call putstr ; Schreib String mov cx, 0xFFFF ; Nochmal das Gleiche mov si, m_boot ; Nochmal das Gleiche call putstr ; Nochmal das Gleiche call getkey ; Call zu GetKey jmp reboot ; Springe zu reboot

msg db 'Welcome to SPTH-OS 1.1',0 ; String 1 m_boot db 'Press any key...',0 ; String 2 content db 'Das habe ich mit meinem Betriebssystem geschrieben!',0 contentend:

Root_entry db 0x53,0x50,0x54,0x48 ; Root Entry von einer Datei mit einem Byte db 0x20,0x20,0x20,0x20 db 0x54,0x58,0x54,0x20 db 0x18,0x34,0xBA,0xB5 db 0x9D,0x2B,0x9D,0x2B db 0x00,0x00,0x0F,0xB6 db 0x9D,0x2B,0x02,0x00 db 0x01,0x00,0x00,0x00

  

        putstr:              ; Schreib-Funktion

lodsb ; \[si\]-\>al or al, al ; Teste al auf 0x0 (=Ende) jz putstrd ; Wenn Ende des Strings, dann mov ah, 0xE ; ah=0xE: Schreib Zeichen mov bx, 0x7 ; Zeichenfarbe: 0x7 = weißes Zeichen/schwarzer ; Hintergrund int 0x10 ; call loop putstr ; Nächstes Zeichen

        putstrd:

mov al, 13 ; Schreibe ASCII 13 mov ah, 0xE mov bx, 0x7 int 0x10

mov al, 10 ; Schreibe ASCII 10 (13,10=Zeilenumbruch) mov ah, 0xE mov bx, 0x7 int 0x10 retn

        getkey:

mov ah, 0 ; ah=0: Get Key BIOS Funktion int 0x16 ; Call ret

        reboot:

db 0xEA ; Hexdump für Reboot: jmp 00FF:FF00 dw 0x0 dw 0xFFFF

\- - - - - \[ Dateien schreiben - CODE \] - - - - -

\</asm\> Macht genau was er soll, darum: Passt :)

### Nachwort

Mit diesem Tutorial sollte man in der Lage sein, ein Betriebssystem zu schreiben, das mit Dateien kein Problem hat. Ich hoffe, du hast damit etwas gelernt, und fandest es interessant zu lesen. Wenn nicht, mach es besser oder schick mir Geld, dann mach ichs besser. (verstehst, worauf ich hinaus will?) Egal, ich hatte Spaß beim schreiben und programmieren, und hab natürlich selber auch das ganze dazugelernt (hab vor dem Schreiben keinen Schimmer gehabt, wie ich auf Dateien zugreife - dann hab ich es mir einfach als Ziel gesetzt, das zu schreiben).  
Nun, danke fürs Lesen & versuch es einfach mal mit Dateizugriff! :)

\- - - - - - - - - - - - - -  
Second Part To Hell/\[rRlf\]  
www.spth.de.vu  
spth@priest.com  

geschrieben im Dezember 2004  
Österreich  
- - - - - - - - - - - - - - -

## Tipps & Tricks: INC und DEC

**Vorgeschichte:**  
In diesem Tipp geht um die Sprache Assembler. Oft muss man in Assembler Zahlen um den numerischen Wert eins erhöhen oder erniedrigen. Dieser Tipp ist zwar hauptsächlich für Assembler gedacht, da man nur dort die Codes direkt eingibt, man weiß ja nie, was der C-Compiler alles baut, aber ich denke, dass es auch bei C nicht schadet, diesen Tipp zu verwenden.

**Tipp:**  
Benutze für dies lieber INC und DEC als ADD X,1 oder SUB X,1. Das erste Befehlspaar wird schneller ausgeführt und erzeugt nur ein Byte Opcodes im Vergleich zu den drei Bytes an Maschinencode die durch ADD X,1 und SUB X,1 erzeugt werden.  

**Hintergrund:**  
Der Prozessor stellt zwei speziell für diese Bereiche gefertigte Funktionen/Befehle zur Verfügung. Diese werden schneller abgearbeitet als das andere Befehlspaar, unter anderem, weil die CPU nur ein Byte anstelle

von drei Bytes lesen muss.

## Codeschnippsel: Sprung in den Protected Mode

\<asm\>

Ein kleines Beispiel, wie man in den 32-Bit Protected Mode wechselt

Bei Fragen kann man sich einfach an stefan.marcik@web.de oder

an die ICQ-Nummer 338417614 wenden.

\[BITS 16\] ... ... cli ; Interrupts ausschalten lgdt \[gdtr\] ; GDT Pointer laden

mov eax,cr0 ; In PMode wechseln, indem das niedrigste or al,1 ; Steuerungsbit von cr0 geändert wird mov cr0,eax ; muss über Umweg über ein anderes Register gemacht werden

jmp codesel:PMode ; FarJump zu einer 32-Bit PMode Funktion

\[BITS 32\] PMode: mov ax,datasel ; Segmentregister laden mov ds,ax mov ss,ax mov esp,0x90000 ; Stack aufsetzen ... ...

== GDT == ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

gdtr: ; Desktiptortabelle

      dw gdt_end-gdt-1       ; Limit
      dd gdt            ; Basisadresse

gdt:

      dd 0,0         ; Null-Deskriptor

codesel equ \$-gdt

      dw 0xFFFF          ; Segmentgröße 0..15
      dw 0x0000         ; Segmentadresse 0..15
      db 0x00           ; Segmentadresse 16..23
      db 0x9A           ; Zugriffsberechtigung und Typ
      db 0xCF           ; Zusatzinformationen und Segmentgröße 16...19
      db 0x00           ; Segmentadresse 24..31

datasel equ \$-gdt

      dw 0xFFFF          ; Segmentgröße 0..15
      dw 0x0000         ; Segmentadresse 0..15
      db 0x00           ; Segmentadresse 16..23
      db 0x92           ; Zugriffsberechtigung und Typ
      db 0xCF           ; Zusatzinformationen und Segmentgröße 16...19
      db 0x00           ; Segmentadresse 24..31

gdt_end: \</asm\>

## OS-Showcase: ReactOS

### Screenshots

![10_1.png](http://www.joachim-neu.de/public/lowlevel/7/10_1.png) ![10_2.png](http://www.joachim-neu.de/public/lowlevel/7/10_2.png)

### Geschichte

Nun, ReactOS ist schon eines der älteren Betriebssystemprojekte. Die Entwickler haben schon sehr viel erreicht. Das Betriebssystem ist seit 1996 in Entwicklung. Aber wie es halt meistens so ist (man sieht es an unserem Comm-OS) funktioniert das nicht so leicht. Ursprünglich kam das System als "FreeWin95". Es sollte die Aufgabe eines Windows-Clones erfüllen, aber die Mitglieder verliefen und verstrickten sich in tiefen Design-Theoretischem-Gerede. Es kam nix zustande. 1997 griff Jason Filby das ganze wieder auf und nannte das Projekt um zu "ReactOS", was von dem damals wie heute tief verwurzelten Unbehagen gegen Microsofts Monopolstellung kam.

Im Februar 1998 beginnt also der steinige Aufstieg von ReactOS. Langsam aber sicher erstellen die Programmierer massig Kernelcode, jedoch war es nur wenigen möglich, wirklich am Kernel zu arbeiten. Nachdem der Kernel nach einiger Zeit stabil lief wurde das Schreiben von IDE- und anderen Treibern unerlässlich. Von nun an war es mehr Leuten möglich, in die Entwicklung von ReactOS einbezogen zu werden.

Heute ist ReactOS mit einem stabilen Kernel versehen und die API ist soweit ausgebaut, Möglichkeiten für eine höhere Programmierung von Programmen freizugeben. Heute schreiben viele Leute an Programmen und Funktionsbibliotheken für ReactOS und ihre Zahl ist steigend. Die Entwicklung einfacher Grafiktreiber ebnen den Weg für eine GUI, eine grafische Bedienoberfläche. Aber immernoch sieht man auch anhand dieser GUI das Ziel, für das ReactOS bestimmt war: Ein Clone von Windows zu werden. Die Oberfläche sieht der der Microsoft-Produkte sehr ähnlich.  
Was sieht die Zukunft für ReactOS vor? Nun, keiner kann dies bestimmen oder vorhersagen, aber die Leiter des Projektes sehen die Nahe Zukunft in der Installation von Subsystemen für Java, OS/2 und DOS. ReactOS steht also ein gewaltiges Wachstum bevor, auf das wir alle gespannt sein dürfen.

### Features

Was kann ReactOS? Genaue Auflistungen sind schwer zu bekommen, vielmehr bekommt man auf der Homepage einen Gesamteindruck und eine Übersicht, was funktioniert und was nicht, allerdings keine kongrete Liste von Features.  

Es gibt mittlerweile einige Funktionsbibliotheken für Konsolenanwendungen von ReactOS. Ein Programm für die Konsole von ReactOS ist ein GCC-Compiler. Dadruch wird ReactOS freestanding, sprich es kann von sich selber aus weiter entwickelt werden.Außerdem gibt es noch den GNU Midnight Commander, einen zeilenbasierten Explorer.

Im Bereich grafische Oberfläche sieht es bei ReactOS im Gegenteil zu MenuetOS noch weniger gut aus. Beide Betriebssysteme gehen vollständig andere Wege. Während MenuetOS sich mehr um sein äußeres Erscheinungsbild und die GUI sorgt, scheinen die Programmierer von ReactOS es mehr auf die inneren Fähigkeiten abgesehen zu haben.

Genauso sieht es beim Treiber Support aus. Während ReactOS auf möglichst viel Modularität baut, sind bei MenuetOS noch viele Treiber fest in den Kernel eingecodet. Im Moment wird daran gearbeitet, auch Treiber dritter (zum Beispiel von Microsoft) zum Laufen zu bringen und benutzbar zu machen.

### Daten/Kontakt zum Projekt:

Das Projekt läuft seit 1996. Der Leiter ist Jason Filby schon seit 1997. Erreichbar ist ReactOS über [www.ReactOS.com](http://www.reactos.com). Dort findet man auch sehr viele Informationen für Programmierer und Benutzer von ReactOS. Die Seite macht einen gepflegten Eindruck.

## Interview: Legend von LegendOS

| Person | Text |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sz | Du leitest die Entwicklung von LegendOS. Was machst du, wenn du gerade nicht am planen oder programmieren bist? |
| L. | Ich studiere Informatik an der Uni Bonn im 2. Semester. |
| sz | Welches Hauptziel verfolgt LegendOS? Wie sieht es mit der allgemeinen Architektur aus? |
| L. | Nun, ich hatte vor kurzem einen kompletten Richtungswechsel, weswegen ich vom aktuellen Design noch nichts präsentieren kann. |
| sz | Bist du vom Microkernel abgekommen? |
| L. | Nun, insofern dass ich nun den "Safe Language"-Ansatz verfolge. Dies gibt einem noch ganz andere Möglichkeiten, auch Treiber zu kontrollieren. Der Microkernelansatz war zwar sehr<br>nett und hätte sicher Vorteile gehabt, er wurde jedoch auch sehr kompliziert. |
| sz | Also wird der Kernel nun doch Monolithisch, jedenfalls zum Teil... |
| L. | Nun, der grösste Vorteil meiner Meinung vom Microkernel ist dass ich auch Treiber kontrollieren kann, was z.B. bei Linux nicht geht, da dort jeder Treibver eigendlich<br>die Kontrolle übernehmen kann. |
| sz | An was arbeitest du momentan besonders hart? Zeichnen sich noch keine Probleme ab , nach der "Richtungsänderung"? |
| L. | Im Moment arbeite ich daran, Java für Treiber benutzen zu können, die kann ich dann auch so kontrollieren, wie einen Treiber im User Land von einem Microkernel. Die Implementierung sollte so besser sein als eine VM unter einem anderen OS, da ich mir dadurch z.B. das<br>Page-Directory-Switching ersparen kann beim Task Switch. |
| sz | Also verankerst du schon tief im Kernel eine Java VM? |
| L. | Richtig. Und im Gegensatz zu anderen ähnlichen Projekten habe ich auch vor, parallel eine CLR zu implementieren, ähnlich wie Mono oder .NET. |
| sz | Ganz allgemein, wie lange programmierst du etwa die Woche? |
| L. | Das ist immer sehr unterschiedlich, die letzten Wochen kam ich kaum dazu. |
| sz | Wann kann man nächste Releases erwarten? |
| L. | Ich habe vor, die Virtual Machines für Java und eine CLR zu implementieren. Dann geht die Entwicklung richtig los, dem würde ich aber noch ein bis zwei Monate geben, da ich<br>noch Techniken wie z.B. Corba umsetzen muss. |

## Kolumne: Technischer Fortschritt

Neulich war ich mal wieder (wie in meinem Alter üblich) beim McDonalds im nächsten Kaff. Neben dem Eingang prangert da seit kurzem ein Schild mit der Aufschrift *WLan Hotspot* von T-Online. Das macht mich irgendwie nachdenklich. Letztes Jahr hatte ich in der Chip schon drüber gelesen dass McDonalds plant in den nächsten Jahren in Filialen in größeren Städten Hotspots einzurichten, aber Kaufbeuren (da wohne ich) ist alles andere als eine größere Stadt. Überhaupt ist der technische Fortschritt kaum mehr aufzuhalten. Letztes Jahr habe ich mir einen Palm gekauft, mit einer Wlan SD Karte könnte ich jetzt beim McChicken essen im Internet surfen (nicht dass ich das wollen würde, da ist das INet ausnahmsweise mal Nebensache ^^).

Meinen ersten Kontakt mit Computer hatte ich vor etwas mehr als 10 Jahren. Mein Vater arbeitete damals auf einem 386 mit AutoCAD unter DOS. Das war dann knapp 2 Jahre später mein erster Computer, darauf lief sogar recht flüssig Windows 95. Wieder 2 Jahre später hab ich dann einen Pentium mit 166 Mhz, 48 MB Ram zu Weihnachten gekriegt (Auch gebraucht). Die sind nicht besonders alt, aber trotzdem ist mein Palm mit 400 Mhz wesentlich schneller (und kompakter). Unser ISDN Anschluss war mit 64 k/bit damals der absolute Renner, heute bringt ein Handy mit GPRS fast dieselbe Geschwindigkeit, mit UMTS sogar noch schneller.

Der Fortschritt ist nicht aufzuhalten, Computer nehmen eine immer größere Bedeutung in unserem Leben ein, ohne sie wären wir heutzutage fast verloren, ich würde fast sagen dass sie uns beinahe kontrollieren. Eins sollten wir dabei nicht vergessen: Unsere Identität und das Real Life, also steht nach dem Genuss dieser Lowlevel Ausgabe auf (Natürlich nachdem Ihr das Schlusswort gelesen habt) und macht einen langen Spaziergang. Vielleicht hilft die frische Luft bei der Lösungsfindung zu einem Problem ^-^.

## Bericht ausm Forum

Die Frage, die uns seit längerem beschäftigt ist die, wie es nun weiter geht mit dem Lowlevel-Magazin. Dieses Thema wird schon seid einiger Zeit im Forum heftig diskutiert und man ist zu der Meinung gekommen das man ein Team bildet, welches sich nur zur Aufgabe macht Lowlevel-Magazin Folgen herauszubringen, die qualitativ hochwertig sind und aber auch nicht all zu lange auf sich warten lassen. Ein Mitglied (joachim_neu) hat deswegen schonmal einen Konzept auf die Beine gestellt, welches meiner Meinung doch schon ein recht gutes ist. Zudem denke ich auch, dass es den meisten Mitgliedern im Grossen und Ganzen gefallen hat. Sicherlich lassen sich da noch einige Änderung machen lassen trotzdem ich denke dieses Mitglied hat doch schonmal den Stoss in die richtige Richtung gemacht.

Während diesen Diskussionen kam man auf die Idee ein Projekt zu machen, in dem Teil für Teil ein Betriebssystem entsteht. Es soll sowohl Neulinge den Weg des OS-Developing zeigen als auch erfahrenen Programmierern vielleicht die ein oder andere Idee für sein eigenes OS geben. Dieses Projekt nannte man "commOS".

Natürlich gab es dazu verschiedene Meinungen. Die einen sind hell auf begeistert und wollen sich auch gerne daran beteiligen, die anderen gehen diesem Projekt eher mit Skepsis entgegen, weil sie befürchten, dass die Anfänger nicht direkt draus lernen sondern einfach den dazugehörigen Quellcode einfach bei sich zu einem OS zusammenstellen aber dabei nichts über die eigentliche Sache lernen und verstehen. Dabei ist nun auch die Frage entstanden, ob man diese Projekt in das eigentliche Lowlevel-Magazin einfliessen lassen sollte.

Ich persönlich denke, dass man dieses Projekt als eine Einzelkategorie in das Magazin mit einfliessen lassen sollte. Meiner Meinung nach bekommt man dadurch einen zusätzlichen Ansporn das Magazin weiter zu führen und das Magazin bekommt einen neuen Touch und reizt auch viele Leser zum Lesen auf. Nun ja, urteilt selber und schreibt eure Meinungen dazu, wie es mit dem Magazin und den "CommOS" weitergehen sollte.

## Vermischtes: Meilensteine in der Geschichte von DOS/Windows

Diese Geschichte beginnt mit schon viel früher, als es überhaupt das erste DOS gab. Sie beginnt, mit dem damals sehr jungen Bill Gates, der die noch heute sehr beliebte Programmiersprache BASIC entwickelte. Etwas später entwickelte dann die Firma Digital Research die erste Version von Micro Control Program (CP/M) , das vor allem im Hobby-Sektor genutzt wurde.

Um seine Produkte besser zu vermarkten, gründete Bill Gates zu dieser Zeit die Firma Microsoft, die vor allem BASIC-Produkte und Unix-Systeme verkaufte. 1980 entschied sich dann auch IBM in die Computer-Branche einzutreten. IBM hatte gerade erst den 8086 und seine abgespeckte 8-Bit Version 8088 herausgebracht. Nun fehlte nur noch die Software, die aus Kostengründen für den 8088 entwickelt werden sollte. Da IBM weder Erfahrung noch Entwickler für ein Betriebssystem hatten, wurde der Manager Philip Estridge beauftragt eines zu kaufen.  
Erstriger versuchte es auch bei Gates, der aber ablehnen musste, da die Unix-System, die er vertrieb, für PCs zu umfangreich waren. IBM sprach auch mit Digital Research über ein CP/M, die auch einwilligten. Als Digital Research aber weit hinter dem verabredeten Zeitplan war, sprang IBM ab und wand sich wieder zu Bill Gates. Gates kannte auch das benachbarte Unternehmen Seattle Computer Products, das das CP/M-ähnliche Betriebssystem 86-DOS vetrieb.  
Im April 1981 kaufte dann Microsoft 86-DOS und übernahm seinen Autor Tim Paterson gleich mit. Tim Paterson sollte noch einige Verbesserungen anbringen, um dann das Betriebssytem als MS-DOS (Microsoft Disk Operation System) an IBM zu übergeben. Der Grunstein für den Erfolg war gelegt, da IBM jetzt Hardware und Software als ein Paket anbieten konnte. DOS wurde bis zur Version 4 nur von IBM und Microsoft entwickelt. Später kamen dann PC-DOS von IBM, Der Klone DR-DOS von Digital Research, das dann von der Firma Novell übernommen wurde, sodass Novell-DOS endstand und das MS-DOS der Firma Microsoft.

Schon bald gab es die ersten Firmen, wie Xerox und Apple, die die ersten grafischen Benutzeroberflächen mit Maus-Bedienug entwickelten. Microsoft fühlte sich unter Druck gesetzt und versuchte auch ein solches Betriebssystem zu entwickeln. Daraus entstand mit IBM zusammen das OS/2. Da Microsoft aber nicht der alleinige Inhaber der Lizenzen war musste schnell ein grafischer Aufsatz für das MS-DOS her. So entstand bereits 1983 das System "Interface Manager", das auf Druck des PR-Managers zu Windows umbenannt wurde. Dieses System wurde aber schon lange vor seiner Serienreife vorgestellt, sodass Fehler über Fehler erst spät danach bemerkt wurden. Bill Gates sah zu dieser Zeit das Windows-Projekt als Reinfall, und wollte es erst ganz einstellen, um mit IBM das OS/2 weiter zu entwickeln. Da aber zur gleichen Zeit auch noch Exel entwickelt wurde und man dafür ein halbwegs funktionierendes Betriebsystem brauchte, korrigierten eine handvoll Entwickler die gröbsten Fehler.  
Das Ergebnis war Windows 2.03, das eigenlich stabil lief. Einen gravierenden Fehler gab es jedoch. Windows lief im Real-Mode, was zu Folge hatte, das nur 1 MB Arbeitsspeicher zu Verfügung stand. Es kam dann oft dazu, dass Daten im Arbeitsspeicher überschrieben wurden und man dann nur nuch den "Blue-Screen" sah. Es gab zu dieser Zeit auch schon den 80286, der den Protected Mode brachte, da Bill Gates aber auf OS/2 setzte ließ er den Code nicht neu schreiben.  
Und wieder kam der Zufall zu Hilfe. Microsoft stellte einen neuen Mitarbeiter, wegen eines von ihm selbst geschriebenen Debuggers ein, der prüfen konnte, ob der Code auch im Protected Mode funktioniert. So mussten nur die problematischen Stellen in Windows 2.03 korrigiert werden. Und still und heimlich wurde das Windows 3.00 über Nacht entwickelt, welches im Juni 1990 zum ersten Mal vorgestellt wurde. Dieses Windows wurde zum Verkaufsschlager. Windows war außer Konkurrenz.

Die folgenden Windows-Systeme ähnelten sich sehr, bis im August 1995 Windows 95 vorgestellt wurde. Windows 95 ist bis jetzt immer noch das am meisten verkaufte Betriebssystem. Es fuktionierte problemlos auf allen "neueren" Rechnern, unterstütze 32Bit-Modus und brachte viele sinnvolle Anwendungen zum laufen.  
Das nächste Windows (Windows 98) setzte immer noch auf den Untersatz DOS. Neben den Windows-Versionen für den Heimanwender, wurde auch die Windows NT Reihe entwickelt, die schon ab Version 3.51 DOS nicht mehr brauchte. So wurde Windows 2000 als Verschmelzung von Windows NT und der Heimanwender-Versionen entwickelt.  
Die neusten Versionen von Windows (windows XP) basieren auch heute noch auf Windows 2000 und sind 32Bit-Systeme. Es sollen aber in Zukunft Windows Versionen entwickelt werden, die 64Bit-Systeme sind.

## Schluss & Impressum

### Schluss

So, das war die 7. Ausgabe des Magazins. Sie ist meiner Meinung nach relativ umfangreich geworden und auch die Beiträge gefallen mir. Die Ausgabe habe ich nach dem Erscheinen noch auf Rechtschreibfehler geprüft, dies hier hinzugefügt und geschaut, dass die Seitenabstände stimmen. Zu meiner "Verteidigung" will ich sagen, dass ich euch einfach nichtmehr warten lassen wollte, und dadurch die Ausgabe eben in relativer Rohfassung abgegeben habe. Entschuldigen will ich mich für den Augenkrebs den einige durch meinen Artikel im "Thema der Ausgabe" aufgrund der Farben bekommen haben, aber es ging nunmal nicht anderst :). Bedanken will ich mich bei Roshl für das Vertrauen und bei allen Redakteuren, die bereit waren, ihre Zeit für die Artikel zu opfern. Ich hoffe, an der nächsten Ausgabe arbeiten wieder so viele Leute mit, sodass auch die wieder gut und lang wird. Bis dahin möchte ich mich verabschieden und alle bitten, sich auch zu beteiligen an diesem grandiosen Projekt!

### Impressum

Alle hier dargestellten Artikel entsprechen der Meinung der Redakteure und spiegeln nicht unbedingt die Meinung der Redaktion wieder. Jeder Redakteur ist für seinen eigenen Beitrag verantwortlich. Zugehörigkeiten entnehmen Sie bitte der Tabelle. Wir bemühen uns nach bestem Wissen unserem Leser nur richtige Informationen zu bieten, jedoch können wir dies nicht garantieren. Jeder in dieser Ausgabe aufgeführte Code ist unter eigener Gefahr zu benutzen und der Ersteller kann nicht für entstehende Schäden zur Haftung gebracht werden. Jede mit diesem Schriftstück verlinkte Seite wird von uns ausgesucht und eingesehen, jedoch haben wir auf sie keinen Einfluss, und somit distanzieren wir uns hiermit von allen rechtswidrigen Schriften auf verlinkten Seiten.

**Artikel:**

| Nummer | Name | Redakteur |
| -------- | -------------------------------- | ---------------------- |
| 1\. | Die Redaktion | Neu, Joachim |
| 2\. | News | Urbanietz, Christoph |
| 3\. | Thema der Ausgabe | Neu, Joachim |
| 4\. | Designtechnisches | Neu, Joachim |
| 5\. | Architekturtechnisches | Neu, Joachim |
| 6\. | Hardwaretechnisches | Neu, Joachim |
| 7\. | Software- & Treibertechnisches | Sperl, Thomas |
| 8\. | Tipps & Tricks | Neu, Joachim |
| 9\. | Codeschnippsel | Marcik, Stefan |
| 10\. | OS-Showcase | Neu, Joachim |
| 11\. | Interview | Zurfluh, Stefan |
| 12\. | Kolumne | Görlich, Markus |
| 13\. | Bericht ausm Forum | Robertz, Michael |
| 14\. | Vermischtes | Kienz, Peter |

  

**Redakteure:**

| Name | Nick | EMail | MSN | ICQ | WWW |
| ---------------------- | -------------------- | ----------------------------- | -------------------------- | ------------- | -------------------------------- |
| Neu, Joachim | joachim_neu | joachim_neu@web.de | joachim_neu@web.de | 247-390-343 | <http://www.joachim-neu.de> |
| Robertz, Michael | Silent{Bob} | silentbob@michaelrobertz.de | --- | 323-417-183 | <http://www.michaelrobertz.de> |
| Marcik, Stefan | Stefan2005 | stefan.marcik@web.de | --- | 338-417-614 | --- |
| Görlich, Markus | The-Programmerfish | the-programmerfish@web.de | --- | 346-950-608 | --- |
| Sperl, Thomas | SPTH | spth@priest.com | --- | --- | <http://www.spth.de.vu> |
| Urbanietz, Christoph | chr15 | chr12@web.de | --- | 311-405-426 | <http://www.clinux.de.vu> |
| Zurfluh, Stefan | sz/elfish_rider | stefan@stefan-zurfluh.biz | elfish_rider@hotmail.com | 330-960-734 | --- |
| Kienz, Peter | BlueB | peterkienz@web.de | --- | 250-161-210 | --- |

|  |  |  |
| ------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| « [Ausgabe 6](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-6 "Ausgabe 6") | **Navigation** | [Ausgabe 8](https://github.com/lowlevel-eu/wiki/wiki/Ausgabe-8 "Ausgabe 8") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8862/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1494/index.html)

<!-- MediaWiki page 1494; revision 8862; parent 6646; 2010-11-11T14:17:07Z -->
