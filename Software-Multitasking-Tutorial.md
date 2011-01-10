# Software Multitasking Tutorial

| Software Multitasking |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Schwierigkeit**: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif" width="16" height="16" alt="Stern gold.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif" width="16" height="16" alt="Stern gold.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)<br> |  |
| Benötigtes Vorwissen: | [IRQ](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ"), [Scheduler](https://github.com/lowlevel-eu/wiki/wiki/Scheduler "Scheduler") |
| Sprache: | FreeBASIC |

Dieses Tutorial ist für alle gedacht, die in ihrem [Betriebssystem](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") [Multitasking](https://github.com/lowlevel-eu/wiki/wiki/Multitasking "Multitasking") auf Softwarebasis implementieren wollen. Ich bin am Anfang an diesem Thema fast verzweifelt, daher schreibe ich dieses Tutorial, damit andere einen leichten Einstieg in diese Thema haben. Ich werde hier nicht "alles" erklären, aber danach sollte einfache Tests mit zwei Tasks möglich sein.

## Bevor wir anfangen...

Eines vorweg: Du solltest mit deinem Betriebssystem bereits auf einem gewissen Stand sein, d.h. du solltest [IRQs](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "IRQ") verwalten und den [PIT](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "Programmable Interval Timer") umprogrammieren können, eine [Speicherverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Speicherverwaltung "Speicherverwaltung") wird auch benötigt. Ansonsten brauchst du nur noch gesunden Menschenverstand. Wenn du das alles hast, kann es losgehen.

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

Kommen wir nun zum Hauptteil dieses Tutorials: Dem Code. Ich werde hier erst ein Stück [FreeBASIC](https://github.com/lowlevel-eu/wiki/wiki/FreeBASIC "FreeBASIC")-Code zeigen und dann erklären, was dieser Code macht.

Zuerst kommen ein paar Konstanten: \<pascal\>

    const TASK_EMPTY as BYTE = 0
    const TASK_READY as BYTE = 1

\</pascal\>

Die zeigen einfach nur an, ob ein Tabelleneintrag der Task-Tabelle mit einem Task belegt ist. \<pascal\>

    type TaskType
       PID as USHORT
       stack as UINTEGER
       status as BYTE
    end type

    dim shared Tasks(100) as TaskType
    dim shared AllTasks as USHORT
    dim shared currentPID as USHORT

\</pascal\>

Nicht wirklich schwer. Wir machen eine Typendefinition für die Task-Tabelle. Enthalten sind die ProzessID (positive 16bit Zahl), die Stack-Adresse (positive 32bit Zahl) und der Status des Tasks (8bit Zahl). Danach legen wir ein Array an, das wir jetzt mit den Daten füttern können.

Dann legen wir noch zwei Variablen an. "AllTasks" gibt an, wieviele Einträge der Tabelle belegt sind. "currentPID" beinhaltet die ProzessID des aktuell laufenden Tasks. \<pascal\>

    function dec (byref tPTR as UINTEGER PTR) as UINTEGER PTR
        tPTR -= 1
        return tPTR
    end function

\</pascal\>

Das hat jetzt nichts direkt mit Multitasking zu tun, ist aber nützlich. Damit können wir so etwas wie "\*--stack = 0" in FreeBASIC folgendermaßen schreiben: "\*(dec(stack)) = 0". Kurz gesagt, nimmt sie einen UINTEGER-pointer und setzt ihn um 4bytes (also ein UINTEGER) runter. Das macht später einiges einfacher. \<pascal\>

    sub Multitasking_Init
       PIT_Timer_init (100)
       IDT_CreateEntry (Interrupt_IRQ0, @Multitasking_Switch, &h08, &h8E)
    end sub

\</pascal\>

Auch einfach. Wir programmieren den PIT so, dass er 100 mal in der Sekunde (vermutlich kein guter Wert für später) den IRQ 0 auslöst. Dann legen wir in der IDT einen Eintrag an, an der Stelle für IRQ 0. Da tragen wir die Adresse der Task-Switch Routine ein, und geben als Selector den Hex-Wert 0x08 an. Die Flags setzen wir auf 0x8E. \<pascal\>

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

\</pascal\>

Kurz, oder? Als erstes fällt wohl das "naked" auf. Damit sagen wir FreeBASIC (Vorsicht, funktioniert erst aber Version 0.21!), dass er am Anfang und Ende nichts am Stack macht und kein "ret" anfügt. Sonst könnten wir die Routine nicht direkt in die IDT eintragen. Zuerst legen wir die Register auf den Stack. Dann laden wir die Segmentregister wieder mit einem gültigen Wert, damit es keine Probleme gibt (wenn der Task die Werte zerstört hat, und wir das nicht machen würden, würde unser Kernel nicht mehr lange mitspielen). Dann folgt ein kleiner Trick, wie rufen den Scheduler direkt aus dem Assembler-Code auf. Dazu legen wir das Stack-Register (das ist der Stack des unterbrochenen Tasks) auf den Stack, da der Scheduler die Stack-Adresse als Parameter erwartet. Dann rufen wir den Scheduler auf, und er gitb uns eine neue Stackadresse in eax zurück. Diesen Wert laden wir in esp, und schon haben wir den Stack des neuen Tasks.

Wir müssen natürlich auch noch dem PIC sagen, dass wir mit unserem Interrupt fertig sind.

Dann laden wir nur noch die Register wieder vom Stack und gehen mit "iret" zum neuen Task.

\<pascal\>

    function Multitasking_scheduler (stack as UINTEGER) as UINTEGER
       Tasks(currentPID).stack = stack
       
       do
          currentPID += 1
          if currentPID > AllTasks then currentPID = 1
       loop until Tasks(currentPID).status = TASK_READY
       
       return Tasks(currentPID).stack
    end function

\</pascal\>

Auch recht einfach. Wir sichern die Stackadresse im Tabelleneintrag des aktuellen Tasks. Dann erhöhen wir currentPID bis wir einen Task finden, der auf seine Aktivierung wartet. Sollte der Wert in currentPID zu hoch werden, setzen wir ihn wieder auf den Tabellenanfang. Haben wir als einen Task gefunden, geben wir dessen Stackadresse zurück.

\<pascal\>

    sub Task_Create (ID as USHORT, priority as UBYTE, address as any ptr)
        if Tasks(ID).status <> TASK_EMPTY then return
        
        dim stack as UINTEGER PTR
        
        asm cli
        
        stack = cast(UINTEGER PTR, malloc(4096) + 1024)
        
        *(dec(stack)) = &h202                    '// EFLAGS
        *(dec(stack)) = &h08                     '// CS
        *(dec(stack)) = cast(UINTEGER, address)  '// EIP
        
        *(dec(stack)) = &h0                      '// EDI
        *(dec(stack)) = &h0                      '// ESI
        *(dec(stack)) = &h0                      '// EBP
        *(dec(stack)) = &h0                      '// NULL
        *(dec(stack)) = &h0                      '// EBX
        *(dec(stack)) = &h0                      '// EDX
        *(dec(stack)) = &h0                      '// ECX
        *(dec(stack)) = &h0                      '// EAX
        
        *(dec(stack)) = &h10                     '// DS
        *(dec(stack)) = &h10                     '// ES
        *(dec(stack)) = &h10                     '// FS
        *(dec(stack)) = &h10                     '// GS
        
        Tasks(ID).status = TASK_READY
        Tasks(ID).stack = cast(UINTEGER, stack)
        Tasks(ID).PID = ID
        
        AllTasks += 1                                                 '// We now have more tasks than before (what a surprise!)
        
        asm sti                                                       '// allow Interrupts again
    end sub

\</pascal\>

Puh. Auf zur Erklärung: Wir prüfen zuerst, ob die gewünschte ProzessID schon belegt ist. Wenn ja, kerhen wir sofort zurück (besser wäre es, wenn wir einen Fehler-Wert zurückgeben würden). Dann erstellen wir eine Variable, in der wir die Stack-Adresse des Tasks zwischenspeichern.

Wichtig ist, das wir hier mit "cli" die Interrupts ausschalten.

Dann holen wir uns 4kb Speicher und legen die Adresse dazu in "stack" ab (das "+ 1024" ist notwendig, weil der Stack von oben nach unten wächst. Also ist der Stackanfang am oberen Ende des reservierten Speicherbereichs! Zu beachten ist hier, das wir zwar 1024 addieren, aber die Adresse in Wirklichkeit um 4096 Bytes ansteigt. Das liegt daran, das wir das zu einem UINTEGER-Pointer addieren. Das ist also alles korrekt so.)

Jetzt basteln wir den Task-Stack zusammen, und zwar ohne den Stack zu wechseln! Hier wird auch klar, für was unsere Hilfsfunktion genutzt wird. Wir simulieren damit praktisch einen "push"-Befehl. Natürlich legen wir hier keine richtigen Register auf den Stack, sondern nur Anfangs-Werte.Dann sieht es so aus, als ob der Task sofot am Anfang unterbrochen worden wäre, so gibt es keine Probleme beim ersten aktivieren des Tasks.

Würden wir noch ein Register cr3 (für [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging")) dazu legen, müssten wir natürlich auch unsere Switch-Routine anpassen, sonst schrotten wir unseren Stack.

Nun legen wir den Tabelleneintrag für unseren Task an. Wir setzen ihn auf ready und legen die Stackadresse rein. Die Stack-Adresse ist tatsächlich korrekt, dafür hat unsere Hilfsfunktion schon gesorgt. Naja, dann schreiben wir noch die ProzessID rein und erhöhen den Wert von "AllTasks" um eins, da wir ja jetzt einen Task mehr haben.

Abschließend erlauben wir mit "sti" die Interrupts wieder und fertig sind wir.

## Abschließende Worte

Puh. Fertig. Es hat mir Spaß gemacht, dieses Tutorial zu schreiben, und ich hoffe, es hat euch auch Spaß gemacht, es zu lesen. Solltet ihr etwas nicht verstanden haben, könnt ihr eure Fragen im Forum posten. Wahrscheinlich wäre den meisten [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")-Code hier lieber gewesen, aber ich kann nicht gut C, außerdem ist so das Risiko geringer, dass jemand per copy&paste den Code übernimmt ohne ihn zu verstehen ;). Ich hoffe aber trotzdem, das alles verständlich war.

Natürlich sind wir hier noch nicht beim perfekten Multitasking angelangt. Wie gesagt müsste cr3 noch gesichert werden, auch Prioritäten wären wünschenswert. Also hört hier nicht einfach auf, sondern bastelt noch ein wenig, und verbessert euren Code. Dieses Tutorial zeigt euch nur wie es geht, was ihr letztendlich damit anstellt, ist eure Sache ;)

Noch ein Hinweis: Der Code stammt aus meinem Kernel, den ihr hier finden könnt: <http://sourceforge.net/projects/frostkernel>

Happy Coding, TheThing

  

## Links

[Protected-Mode Tutorial der FH-Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/) [Software-Multitasking Tutorial auf google code](http://code.google.com/p/onyxkernel/wiki/SoftwareMultitasking)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9321/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1849/index.html)

<!-- MediaWiki page 1849; revision 9321; parent 9319; 2011-01-10T21:36:04Z -->
