# Paging Tutorial

Willkommen zu meinem zweiten Tutorial hier auf lowlevel. Diesmal geht es um [Paging](Paging.md "Paging"), einem [Protected-Mode](Protected-Mode.md "Protected Mode") Feature, das mit dem 80386 eingeführt und im 80486 verbessert wurde.

## Was ist Paging?

Wenn ihr einen [Kernel](Kernel.md "Kernel") schreibt, habt ihr mit Sicherheit schon Einträge in der [GDT](Global-Descriptor-Table.md "Global Descriptor Table") gemacht. Dort konnte man Segmente festlegen, und hatte so schon ein wenig Speicherschutz. Allerdings hat das ganze auch noch einige Nachteile, weshalb schlaue Leute bei Intel Paging einführten. Bei Paging bekommen die Programme virtuellen Arbeitsspeicher (4 GB), der in 4kb-Blöcken mittels Tabellen verwaltet wird. Wenn Paging eingeschaltet wurde, kann jeder Task seinen eigenen Adressraum haben, und kann auch nur auf seinen eigenen zugreifen. Das interessante an Paging ist, dass der virtuelle Adressraum nicht komplett im physischen Speicher liegen muss, ungenutzte Teile können auf die Festplatte ausgelagert werden (swapping).

Die bereits erwähnten Tabellen heißen Page-Directory und Page-Table. Das Page-Directory enthält 1024 Einträge zu je 4 Byte (also 4kb), jeder Eintrag verweist auf eine Page-Table, die auch 1024 Einträge zu je 4 Byte hat (alle Page-Tables zusammen haben 4MB!). Die Einträge der Page-Table verweisen dann auf 4kb große Blöcke im physischen Speicher.

Eine virtuelle Adresse sieht zwar wie eine physische Adresse aus, lässt sich jedoch ein 3 Teile zerlegen:

**10bit Page-Directory-Index, 10bit Page-Table-Index, 12bit offset**

Wir können daraus eine Formel ableiten, und daraus eine Funktion machen. Dieser Funktion geben wir eine virtuelle Adresse, und sie berechnet daraus die Einträge der Tabellen, die wir verändern müssen.

Ein Eintrag in den Tabellen sieht so aus:

**20bit Adresse, 12bit Flags**

Die Adresse verweist entweder auf eine Tabelle (Einrag im Page-Directory) oder auf eine 4kb-Page (Eintrag in einer Page-Table). Die Flags geben z.B. an, wer auf diesen Speicherbereich zugreifen darf, oder ob dieser Speicherbereich überhaupt existiert.

## Einige Überlegungen

Auch beim Paging sollte man erst einmal genau darüber nachdenken, bevor man den Code schreibt.

- Generelles
  - Wir benötigen ein Page-Directory und 1024 Page-Tables, jede Tabelle ist 4kb groß. Daraus folgt: 4kb für das Page-Directory, 4MB für die Page-Tables

<!-- -->

- Page-Directory initialisieren
  - Wir müssen die Einträge des Page-Directorys auf die Page-Tables verweisen lassen und die richtigen Flags setzen

<!-- -->

- 4kb-Block (Page) mappen
  - Eine Routine, die einen 4kb Block physischen Speicher in den virtuellen Speicherbreich mappt. Wir übergeben ihr eine physische Adresse (der 4kb Block) und eine virtuelle Adresse (wo der Block hin soll).

<!-- -->

- Speicherbereich mappen
  - Eine Routine, die einen Bereich physichen Speicher in den virtuellen Adressraum mappt. Sie geht in 4kb Schritten vor und ruft unsere "4kb-Block-mappen"-Routine auf. Wir übergeben ihr drei Adressen: Wo der Block Speicher beginnt, wo er aufhört, und wo er in den virtuellen Adressraum hingemappt werden soll.

<!-- -->

- Page-Directory-Adresse setzen
  - Eine sehr kleine Routine, die die Adresse des Page-Directory ins [Register](Control-Register.md "Control Register") cr3 einträgt, damit die CPU weiß, wo unser Page-Directory liegt

<!-- -->

- Paging aktivieren
  - Die wohl wichtigste Routine. Wir setzen einfach nur das Paging-Bit im Register cr0 und fertig.

## Der Code

Und nun zum Hauptteil des Tutorials. Auch hier brauchen wir zuerst ein paar Konstanten: \<freebasic\>

    '// constants for all Paging-tables
    const Page_present = &b1
    const Page_writeable = &b10
    const Page_noUsermodeAccess = &b100
    const Page_noWriteThrough = &b1000
    const Page_noCache = &b10000

    '// constants only for the PageDirectory
    const Page_bigPage = &b10000000

    '// constants only for the PageTable
    const Page_noTLBupdate = &b100000000

\</freebasic\>

Die benutzen wir später um die Flags der Tabellen-Einträge zu setzen.

\<freebasic\>

    dim shared PageDirectoryPTR as UINTEGER PTR = cast(UINTEGER PTR, 2*1024*1024 - 4*1024) '// The PageDirectory lies at 2MB-4kb
    dim shared PageTablesPTR as UINTEGER PTR = cast(UINTEGER PTR, 2*1024*1024)             '// The PageTables lie at 2MB

\</freebasic\>

Hier setzen wir Pointer, wo die Tabellen später liegen. Warum ich das so mache? So kann ich festlegen, das die Tabellen 4kb-aligned sind, und muss mich nicht auf irgendwelche seltsamen Memory-Manager verlassen.

\<freebasic\>

    sub Paging_initDirectory
        dim counter as UINTEGER
        dim DirectoryPTR as UINTEGER PTR = PageDirectoryPTR
        
        for counter = cast(UINTEGER, PageTablesPTR) to cast(UINTEGER, PageTablesPTR)+4*1024*1024 step 4096
            *DirectoryPTR = counter OR Page_present OR Page_writeable
            DirectoryPTR += 1
        next
    end sub

\</freebasic\>

Wir setzen hier die Einträge des Page-Directory so, dass sie auf die Page-Tables verweisen. Man kann hier sehen, das wir zwei Flags setzen. Damit sorgen wie dafür, das wir auf diesen Speicherbereich schreiben dürfen, und wie sagen der CPU das der Speicherbereich im physischen Speicher liegt, also present ist.

\<freebasic\>

    sub Paging_map4kb (vmem as UINTEGER, pmem as UINTEGER)
        dim PDentry as UINTEGER
        dim PTentry as UINTEGER
        
        PDentry = vmem shr 22
        PTentry = (vmem shl 10) shr 22
        
        '// no error-checking here. hm.
        *(PageTablesPTR+PTentry+PDentry*1024) = pmem OR Page_present OR Page_writeable
    end sub

\</freebasic\>

Das ist also unsere Routine, die einen 4kb Block in den virtuellen Speicher mappt. Wer oben aufgepasst hat, weiß auch, wie wir die Einträge der Tabellen berechnen:

Wir schieben die Bits um 22 nach rechts, und übrig bleiben die linken 10bit, der Page-Directory-Eintrag.

Wir schieben die Bits um 10 nach links (Page-Directory-Eintrag-bits fallen weg) und das dann 22 bits nach rechts, übrig bleiben die mittleren 10bit, der Page-Table-Eintrag.

Auch hier setzen wir ein paar Bits.

\<freebasic\>

    sub Paging_mapPhysicalMemory (vstart as UINTEGER, pstart as UINTEGER, pend as UINTEGER)
        dim vmemPTR as UINTEGER = vstart
        dim pmemPTR as UINTEGER = pstart
        
        do while pmemPTR < pend
            Paging_map4kb (vmemPTR, pmemPTR)
            vmemPTR += 4096
            pmemPTR += 4096
        loop
    end sub

\</freebasic\>

Diese Routine mappt den Speicher von pstart bis pend an die virtuelle Adresse vstart. Sie ruft dabei in 4kb-Schritten unsere obige Routine auf. Damit können wir große Speicherbereiche schnell und einfach mappen.

\<freebasic\>

    sub SetPageDirectoryAddress (address as UINTEGER PTR)
        '// we set the address when we write it into cr3
        ASM
            mov eax, [address]                                 '// get the address into eax
            mov cr3, eax                                       '// get the value of eax into cr3
        END ASM
    end sub

\</freebasic\>

Wir schreiben die Adresse zuerst in eax, und laden den Wert dann nach cr3, damit der Prozessor weiß wo unser Page-Directory liegt.

\<freebasic\>

    sub Paging_activate
        '// we activate paging by enabling the last bit of cr0.
        ASM
            mov eax, cr0                                       '// get the value of cr0 into eax
            or eax, &b10000000000000000000000000000000         '// set the bit
            mov cr0, eax                                       '// get the new value of eax into cr0
        END ASM
    end sub

\</freebasic\>

Hier holen wir den Inhalt von cr0 nach eax, setzen das Paging-Bit und schreiben den neuen Wert zurück. Und schon ist Paging aktiviert!

## Ein sehr kleines Beispiel

Als Beispiel zeige ich hier einen Auszug aus meinem Kernel [FROST](FROST.md "FROST"):

\<freebasic\>

    print "Initializing page-directory..."
    Paging_initDirectory
    print "Mapping 10MB physical memory..."
    Paging_mapPhysicalMemory (0, 0, 10*1024*1024)
    print "Setting page-directory address..."
    SetPageDirectoryAddress (PageDirectoryPTR)
    print "Enabling paging..."
    Paging_activate

\</freebasic\>

Das ganze geschieht nach dem initialisieren der IDT und vor dem initialisieren von Multitasking.

Wir initialisieren das Page-Directory, mappen die ersten 10MB mit identity-mapping (virtuelle Adresse = physische Adresse), setzen die Page-Directory-Adresse und schalten Paging ein. Der Kernel merkt gar nicht, das er ab jetzt auf virtuellen Speicher zugreift, und läuft wunderbar weiter. Sollte er jedoch versuchen, auf Speicher oberhalb der 10MB zuzugreifen, wird Exception 14 ausgelöst (Page fault).

Und da ich hier Multitasking schon erwähnt habe: Es ist zu beachten, das wir für jeden Task eigene Tabellen anlegen, und für jeden Task das Register cr3 sichern!

## Abschließende Worte

Auch das hätten wir geschafft. Obwohl das Thema etwas verzwickt ist, hoffe ich, dass dieses Tutorial einen guten Einstieg bietet. Wenn noch Fragen offen sind, fragt im Forum oder wendet euch an Mr. Google ;)

Noch ein Hinweis: Der Code stammt aus meinem Kernel, den ihr hier finden könnt: <http://sourceforge.net/projects/frostkernel>

Happy Coding, TheThing

  

## Links

[Protected-Mode Tutorial der FH-Zwickau](http://www.fh-zwickau.de/doc/prmo/pmtutor/text/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6880/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1850/index.html)

<!-- MediaWiki page 1850; revision 6880; parent 6877; 2010-01-11T09:26:30Z -->
