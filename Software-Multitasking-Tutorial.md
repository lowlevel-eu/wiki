# Software Multitasking Tutorial

Dieses Tutorial ist für alle gedacht, die in ihrem Betriebssystem Multitasking auf Softwarebasis implementieren wollen. Ich bin am Anfang an diesem Thema fast verzweifelt, daher schreibe ich dieses Tutorial, damit andere einen leichten Einstieg in diese Thema haben. Ich werde hier nicht "alles" erklären, aber danach sollte einfache Tests mit zwei Tasks möglich sein.

## Bevor wir anfangen...

Eines vorweg: Du solltest mit deinem Betriebssystem bereits auf einem gewissen Stand sein, d.h. du solltest IRQs verwalten und den PIT umprogrammieren können, eine Speicherverwaltung wird auch benötigt. Ansonsten brauchst du nur noch gesunden Menschenverstand. Wenn du das alles hast, kann es losgehen.

## Einige Überlegungen

Einfach drauflos zu coden ist hier der falsche Weg. Überlegen wir uns zuerst einmal, wie Software-Multitasking überhaupt funktioniert.

- Generelles:
  - Wir benötigen eine Tabelle mit den Tasks, in der Stack, ProzessID und der Status gespeichert werden. Dann noch eine Variable, in der wir die ID des aktuellen Prozesses festhalten.

<!-- -->

- Initialisierung:
  - Wir sagen dem PIT, wie oft er in der Sekunde einen IRQ feuern soll. Danach erzeugen wir in der IDT an der Stelle des IRQs 0 einen Eintrag, der auf unsere Task-Switch Routine verweist.

<!-- -->

- Task-Switch:
  - Wir legen die Register auf den Stack (das ist der Stack des unterbrochenen Tasks). Dann rufen wir unseren Scheduler auf. Er legt die übergebene Stackaddresse in der Task-Tabelle ab, sucht den nächsten Task heraus und gibt dessen Stackaddresse zurück. Die Task-Switch Routine lädt dann die Register von dem neuen Stack und kehrt mit einem IRET zurück zum Task.

<!-- -->

- Task erstellen:
  - Diese Routine erhält als Parameter die ID, an der der Task in der Tabelle eingetragen werden soll, und die Adresse des Codes. Wir blocken dann die Interrupts mit CLI und holen uns erst einmal Speicher für den Stack. Wir sichern dann die Adresse des Kernelstacks und laden den neuen. Dann benutzen wir einen kleinen Trick: Wir lassen den Stack des Tasks so aussehen, als wäre der Task gleich am Anfang unterbrochen worden, also legen wir die vorbereiteten Register auf den Stack. Dann stellen wir einfach den Kernelstack wieder her, tragen den Tasks in die Tabelle ein, erlauben die Interrupts wieder und fertig.

## Der Code

Kommen wir nun zum Hauptteil dieses Tutorials: Dem Code. Ich werde hier erst ein Stück FreeBASIC-code zeigen und dann erklären, was dieser Code macht.

Zuerst kommen ein paar Konstanten:

    const TASK_EMPTY as BYTE = 0
    const TASK_READY as BYTE = 1

Die zeigen einfach nur an, ob ein Tabelleneintrag der Task-Tabelle mit einem Task belegt ist.

    type TaskType
       PID as USHORT
       stack as UINTEGER
       status as BYTE
    end type

    dim shared Tasks(100) as TaskType
    dim shared AllTasks as USHORT
    dim shared currentPID as USHORT

Nicht wirklich schwer. Wir machen eine Typendefinition für die Task-Tabelle. Enthalten sind die ProzessID (positive 16bit Zahl), die Stack-Adresse (positive 32bit Zahl) und der Status des Tasks (8bit Zahl). Danach legen wir ein Array an, das wir jetzt mit den Daten füttern können.

Dann legen wir noch zwei Variablen an. "AllTasks" gibt an, wieviele Einträge der Tabelle belegt sind. "currentPID" beinhaltet die ProzessID des aktuell laufenden Tasks.

    sub Multitasking_Init
       PIT_Timer_init (100)
       IDT_CreateEntry (Interrupt_IRQ0, @Multitasking_Switch, &h08, &h8E)
    end sub

Auch einfach. Wir programmieren den PIT so, dass er 100 mal in der Sekunde (vermutlich kein guter Wert für später) den IRQ 0 auslöst. Dann legen wir in der IDT einen Eintrag an, an der Stelle für IRQ 0. Da tragen wir die Adresse der Task-Switch Routine ein, und geben als Selector den Hex-Wert 0x08 an. Die Flags setzen wir auf 0x8E.

    sub Multitasking_Switch naked
       asm
          pusha
          push ds
          push es
          push fs
          push gs
          
          mov eax, &h10
          mov ds, eax
          mov es, eax
          mov fs, eax
          mov gs, eax
          
          push esp
          call MULTITASKING_SCHEDULER
          mov esp, eax
          
          mov al, &h20
          out &h20, al
          
          pop gs
          pop fs
          pop es
          pop ds
          popa
          
          iret
       end asm
    end sub

Kurz, oder? Als erstes fällt wohl das "naked" auf. Damit sagen wir FreeBASIC (Vorsicht, funktioniert erst aber Version 0.21!), dass er am Anfang und Ende nichts am Stack macht und kein "ret" anfügt. Sonst könnten wir die Routine nicht direkt in die IDT eintragen. Zuerst legen wir die Register auf den Stack. Dann laden wir die Segmentregister wieder mit einem gültigen Wert, damit es keine Probleme gibt (wenn der Task die Werte zerstört hat, und wir das nicht machen würden, würde unser Kernel nicht mehr lange mitspielen). Dann folgt ein kleiner Trick, wie rufen den Scheduler direkt aus dem Assembler-Code auf. Dazu legen wir das Stack-Register (das ist der Stack des unterbrochenen Tasks) auf den Stack, da der Scheduler die Stack-Adresse als Parameter erwartet. Dann rufen wir den Scheduler auf, und er gitb uns eine neue Stackadresse in eax zurück. Diesen Wert laden wir in esp, und schon haben wir den Stack des neuen Tasks.

Wir müssen natürlich auch noch dem PIC sagen, dass wir mit unserem Interrupt fertig sind.

Dann laden wir nur noch die Register wieder vom Stack und gehen mit "iret" zum neuen Task.

    function Multitasking_scheduler (stack as UINTEGER) as UINTEGER
       Tasks(currentPID).stack = stack
       
       do
          currentPID += 1
          if currentPID > AllTasks then currentPID = 1
       loop until Tasks(currentPID).status = TASK_READY
       
       return Tasks(currentPID).stack
    end function

Auch recht einfach. Wir sichern die Stackadresse im Tabelleneintrag des aktuellen Tasks. Dann erhöhen wir currentPID bis wir einen Task finden, der auf seine Aktivierung wartet. Sollte der Wert in currentPID zu hoch werden, setzen wir ihn wieder auf den Tabellenanfang. Haben wir als einen Task gefunden, geben wir dessen Stackadresse zurück.

    sub Task_Create (ID as USHORT, address as any ptr)
       if Tasks(ID).status <> TASK_EMPTY then return
       
       dim stack as UINTEGER
       dim kernelstack as UINTEGER
       
       asm cli
       
       stack = cast(UINTEGER, malloc(4096))+4096
       
       asm
          mov eax, esp
          mov [kernelstack], eax
          
          mov eax, [stack]
          mov esp, eax
          
          mov eax, &h202
          push eax
          
          mov eax, &h08
          push eax
          push [address]
          
          mov eax, &h0
          push eax
          push eax
          push eax
          push eax
          push eax
          push eax
          push eax
          push eax
          
          mov eax, &h10
          push eax
          push eax
          push eax
          push eax
          
          mov eax, [kernelstack]
          mov esp, eax
       end asm
       
       Tasks(ID).status = TASK_READY
       Tasks(ID).stack = stack-60
       Tasks(ID).PID = ID
       
       AllTasks += 1
       
       asm sti
    end sub

Puh. Auf zur Erklärung: Wir prüfen zuerst, ob die gewünschte ProzessID schon belegt ist. Wenn ja, kerhen wir sofort zurück (besser wäre es, wenn wir einen Fehler-Wert zurückgeben würden). Dann erstellen wir zwei Variablen, in denen wir Stackadressen zwischenspeichern werden.

Wichtig ist, das wir hier mit "cli" die Interrupts ausschalten.

Dann holen wir uns 4kb Speicher und legen die Adresse dazu in "stack" ab (das "+ 4096" ist notwendig, weil der Stack von oben nach unten wächst. Also ist der Stackanfang am Ende des reservierten Speicherbereichs!)

Dann sichern wir den Kernelstack in der "kernelstack"-Variable. Schließlich brauchen wir unseren Stack ja noch! Dann laden wir unseren frisch reservierten Stack.

Wir legen nun die Register auf den Stack. Nein, halt, wir legen nicht die richtigen Register auf den Stack, sondern Anfangs-Werte. Dann sieht es so aus, als ob der Task sofot am Anfang unterbrochen worden wäre, so gibt es keine Probleme beim ersten aktivieren des Tasks.

Danach holen wir unseren geliebten Kernelstack wieder zurück.

Nun legen wir den Tabelleneintrag für unseren Task an. Wir setzen ihn auf ready und legen die Stackadresse rein. Aber moment: "stack-60"? Wie gesagt, der Stack wächst von oben nach unten. Und da wir 60 bytes auf den Stack gelegt haben (wers nicht glaubt kann ja nachzählen), müssen wir 60 bytes abziehen. Würden wir z.B. das Register cr3 (für Paging) mitsichern, müssten wir noch 4 bytes zusätzlich abziehen (dann wären es 64). Naja, dann schreiben wir noch die ProzessID rein und erhöhen den Wert von "AllTasks" um eins, da wir ja jetzt einen Task mehr haben.

Abschließend erlauben wir mit "sti" die Interrupts wieder und fertig sind wir.

## Abschließende Worte

Puh. Fertig. Es hat mir Spaß gemacht, dieses Tutorial zu schreiben, und ich hoffe, es hat euch auch Spaß gemacht, es zu lesen. Solltet ihr etwas nicht verstanden haben, könnt ihr eure Fragen im Forum posten. Wahrscheinlich wäre den meisten C-Code hier lieber gewesen, aber ich kann nicht gut C, außerdem ist so das Risiko geringer, dass jemand per copy&paste den Code übernimmt ohne ihn zu verstehen ;). Ich hoffe aber trotzdem, das alles verständlich war.

Noch ein Hinweis: Der Code stammt aus meinem Kernel, den ihr hier finden könnt: <http://sourceforge.net/projects/frostkernel>

Happy Coding, TheThing

  

## Links

[Protected-Mode Tutorial der FH-Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/)

[Software-Multitasking Tutorial auf google code](http://code.google.com/p/onyxkernel/wiki/SoftwareMultitasking)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4417/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1849/index.html)

<!-- MediaWiki page 1849; revision 4417; parent 4409; 2009-05-29T18:47:21Z -->
