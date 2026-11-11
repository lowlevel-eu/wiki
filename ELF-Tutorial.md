# ELF-Tutorial

| ELF-Tutorial |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Schwierigkeit**: [<img src="assets/Stern_gold.gif" width="16" height="16" alt="Stern gold.gif" />](assets/Stern_gold.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)[<img src="assets/Stern_wei%C3%9F.gif" width="16" height="16" alt="Stern weiß.gif" />](assets/Stern_wei%C3%9F.gif)<br> |  |
| Benötigtes Vorwissen: | [Paging](Paging "Paging") |
| Sprache: | FreeBasic |

  
Und wieder einmal schreibe ich ein Tutorial für euch. Diesmal geht es um ELF, ein Format für ausführbare Dateien. Sich mit ELF zu beschäftigen ist sinnvoll, denn irgendwann braucht man eben ein gescheites Dateiformat für seine Treiber und sonstigen Programme.

Meine Wahl für das Format fiel damals auf ELF, das liegt an verschiedenen Dingen:

- Es wird von allen gängigen Compilern und Linkern unterstützt (NASM, gcc, as, ld, fbc...)
- Es ist ein offenes Format
- Es ist plattformübergreifend
- Man findet Spezifikationen usw im Internet
- Viele andere OS-Projekte nutzen es, daher bekommt man Hilfe
- Linux benutzt es ;)

Auch hier wird vorausgesetzt, dass euer OS bereits bestimmte Dinge beherrscht. Ihr solltet [Multitasking](Multitasking "Multitasking") und [Paging](Paging "Paging") nutzen können (wenn nicht, sucht hier im Wiki. Für diese Themen habe ich bereits [Tutorials](Kategorie-Tutorials "Kategorie:Tutorials") geschrieben). In diesem Tutorial werde ich nicht erklären, wie ihr die Dateien in den Speicher bekommt, das ist eure Sache. Aber ich empfehle euch, die Dateien einfach von [GRUB](Grand-Unified-Bootloader "GRUB") als Module laden zu lassen. Solltet ihr kein GRUB nutzen, ändert das. Es gibt mehr als genügend Gründe dafür, aber die werde ich hier nicht aufzählen. Aber wenn wir schon dabei sind: GRUB kann Kernel im ELF-Format laden.

  

## Hinweis

Bevor es richtig los geht, zwei Hinweise: Der Code in diesem Tutorial ist in [FreeBASIC](FreeBASIC "FreeBASIC") geschrieben und die Funktionsweise, die hier erklärt wird, gilt nur für den 32-Bit-Modus.

  

## Schön langsam...

Wie immer lassen wir uns erstmal alles durch den Kopf gehen, bevor wir Code schreiben. Es schwirren euch sicher einige Fragen durch den Kopf: "**Wie ist eine ELF-Datei aufgebaut?**", "**Wie lade ich die Daten korrekt in den Speicher?**", "**Wo liegt der ausführbare Code?**" usw.

  
**Kümmern wir uns einmal um die erste Frage: Wie ist eine ELF-Datei aufgebaut?**

ELF-Dateien haben einen ELF-Header, der Dinge wie eine "Magic-Number" (zur Identifizierung) enthält. Da ELF ein plattformübergreifendes Format ist, sind hier auch einige wichtige Angaben gespeichert, z. B. für welche Architektur diese Datei gedacht ist. Der ELF-Header liegt immer direkt am Anfang einer ELF-Datei.

  
**Nun zur zweiten Frage: Wie lade ich die Daten korrekt in den Speicher?**

Die Daten einer ELF-Datei liegen in einzelnen Abschnitten vor, die in die "Programmheader-Tabelle" eingetragen sind. Der ELF-Header enthält Einträge, die angeben, wo diese Tabelle liegt, wie groß die Einträge sind usw. Die Einträge dieser Tabelle enthalten die Angaben, wo der Speicherbereich liegt, wie groß er in der Datei ist, wie groß er im Speicher sein sollte, wo dieser Speicherbereich im Speicher liegen soll und noch einiges mehr. ELF-Dateien können auch einen Section-Header haben, der ist für uns aber uninteressant.

  
**Und jetzt die dritte Frage: Wo liegt der ausführbare Code?**

Das Feld "e_entry" im ELF-Header gibt die virtuelle Adresse an, an der der ausführbare Code später liegt. Wenn wir einen Task erstellen, geben wir ihm einfach diesen Wert als EIP-Register. Bei Linux beträgt dieser Wert meist 0x805F540, der ausführbare Code liegt also ungefähr bei 128 MB. Aber dank Paging braucht der PC gar nicht so viel RAM.

## Weitere Überlegungen

Also, was brauchen wir denn alles?

Zuerst einmal die Konstanten (das ist verständlicher als direkt Werte zu verwenden) und die benötigten Datentypen (für den ELF-Header, die Program-Header-Einträge usw.).

Außerdem brauchen wir eine Routine, die überprüft, ob die ELF-Datei überhaupt auf diesem System lauffähig ist, sie also für diese Architektur gedacht ist usw. Die Routine überprüft folgende Dinge:

- Magic Number (ist diese Datei überhaupt eine ELF-Datei?)
- Dateityp (sollte ausführbar sein)
- Architektur (sollte Intel 386 sein)
- Dateiklasse (32 oder 64 bit)
- Bytereihenfolge (Little oder Big Endian)
- Dateiversion (alt oder current)

Zuletzt noch eine Routine, die zuerst die Check-Routine aufruft, dann die Program-Header-Entries in den Speicher kopiert und zuletzt den Task erstellt.

## Typen und Konstanten

Zuerst ein paar Definitionen: In FreeBasic: \<freebasic\>

    type Elf32_Addr  as UINTEGER
    type Elf32_Half  as USHORT
    type ELF32_Off   as UINTEGER
    type Elf32_Sword as INTEGER
    type Elf32_Word  as UINTEGER
    type Elf32_Uchar as UBYTE

\</freebasic\>

  
Beginnen wir nun mal mit dem ELF-Header.

Wieder FreeBasic: \<freebasic\>

    type ELF_IDENT_HEADER
        EI_MAGIC as UINTEGER                       '// ELF-Magic Number
        EI_CLASS as UBYTE                          '// 32 or 64 bit?
        EI_DATA as UBYTE                           '// Little or Big Endian?
        EI_VERSION as UBYTE                        '// same as ELF_HEADER.e_version
        EI_PAD as UINTEGER                         '// reserved (zero)
        EI_PAD2 as UINTEGER                        '// reserved (zero)
        EI_NIDENT as UBYTE                         '// ?
    end type

    type ELF_HEADER
        e_ident     as ELF_IDENT_HEADER            '// IDENT-HEADER (see above)
        e_type      as Elf32_Half                  '// type of the ELF-file (relocatable, executeable, shared-object...)
        e_machine   as Elf32_Half                  '// processor-type
        e_version   as Elf32_Word                  '// ELF-version
        e_entry     as Elf32_Addr                  '// virtual address of the entrypoint
        e_phoff     as Elf32_Off                   '// offset of the program-header. zero if no program-header exists
        e_shoff     as Elf32_Off                   '// offset of the section-header. zero if no section-header exists
        e_flags     as Elf32_Word                  '// processor-specific flags
        e_ehsize    as Elf32_Half                  '// size of the ELF-header
        e_phentsize as Elf32_Half                  '// size of one program-header entry
        e_phnum     as Elf32_Half                  '// number of entries in the program-header. zero if no program-header exists
        e_shentsize as Elf32_Half                  '// size of one section-header entry
        e_shnum     as Elf32_Half                  '// number of entries in the section-header. zero if no section-header exists
        e_shstrndex as Elf32_Half                  '// tells us which entry of the section-header is linked to the String-Table
    end type

\</freebasic\>

So. Wofür ist jetzt "ELF_IDENT_HEADER" gut? Ganz einfach, er gibt uns erst mal ein paar grundlegende Infos, z. B. ob die Datei Little oder Big Endian ist. Das ist wichtig, da der Rest der Datei diesen Regeln folgt! (Eigentlich ist dieser Header etwas anders eingeteilt, aber der Einfachheit halber habe ich das mal so gelöst. Wie es wirklich richtig ist, kann man in den ELF-Spezifikationen nachlesen)

So, jetzt überlegen wir mal, welche Teile des Headers außer dem Ident-Header für uns wichtig sind. Naja, e_type auf jeden Fall, denn wir wollen nur ausführbare Dateien ausführen. e_machine sollte auch überprüft werden, damit wir nicht Code ausführen, der für einen anderen Prozessor gedacht war. e_version zeigt uns, dass wir eine aktuelle ELF-Datei vor uns haben, also auch wichtig. e_entry ist wohl das wichtigste, das ist unser Einsprungpunkt in den Code. e_phoff, e_phentsize und e_phnum sind wichtig, da sie uns sagen, wie und wo wir die Segmente der ELF-Datei in den Speicher kopieren müssen. Der Rest ist für uns momentan noch unwichtig.

Nun schmeiße ich euch wieder ein paar Konstanten an den Kopf: \<freebasic\>

    const ELF_MAG0 as UBYTE = &h7f
    const ELF_MAG1 as UBYTE = &h45
    const ELF_MAG2 as UBYTE = &h4C
    const ELF_MAG3 as UBYTE = &h46
    const ELF_MAGIC as UINTEGER = (ELF_MAG0) OR (ELF_MAG1 SHL 8) OR (ELF_MAG2 SHL 16) OR (ELF_MAG3 SHL 24)

    const ELF_CLASS_NONE as UBYTE = &h00
    const ELF_CLASS_32 as UBYTE = &h01             '// 32bit file
    const ELF_CLASS_64 as UBYTE = &h02             '// 64bit file

    const ELF_DATA_NONE as UBYTE = &h00
    const ELF_DATA_2LSB as UBYTE = &h01
    const ELF_DATA_2MSB as UBYTE = &h02

\</freebasic\>

Die sind alle für den Ident-Header. Zuerst die Magic-Number, dann die Klasse (gibt nur an ob wir eine 32-Bit- oder eine 64-Bit-ELF-Datei vor uns haben) und dann die Angabe, ob wir Little oder Big Endian haben. Die werden später wieder verwendet.

\<freebasic\>

    const ELF_ET_NONE as USHORT = &h0000           '// no type
    const ELF_ET_REL as USHORT = &h0001            '// relocatable
    const ELF_ET_EXEC as USHORT = &h0002           '// executeable
    const ELF_ET_DYN as USHORT = &h0003            '// Shared-Object-File
    const ELF_ET_CORE as USHORT = &h0004           '// Corefile
    const ELF_ET_LOPROC as USHORT = &hFF00         '// Processor-specific
    const ELF_ET_HIPROC as USHORT = &h00FF         '// Processor-specific

    const ELF_EM_NONE as USHORT = &h0000           '// no type
    const ELF_EM_M32 as USHORT = &h0001            '// AT&T WE 32100
    const ELF_EM_SPARC as USHORT = &h0002          '// SPARC
    const ELF_EM_386 as USHORT = &h0003            '// Intel 80386
    const ELF_EM_68K as USHORT = &h0004            '// Motorola 68000
    const ELF_EM_88K as USHORT = &h0005            '// Motorola 88000
    const ELF_EM_860 as USHORT = &h0007            '// Intel 80860
    const ELF_EM_MIPS as USHORT = &h0008           '// MIPS RS3000

    const ELF_EV_NONE as UINTEGER = &h00           '// invalid version
    const ELF_EV_CURRENT as UINTEGER = &h01        '// current version

\</freebasic\>

So, die sind für den ELF-Header. Zuerst die Konstanten für den Dateityp, dann für die Architektur. Und schließlich die Konstanten, damit wir erkennen, dass es eine aktuelle Version des ELF-Formats ist.

So, was fehlt noch? Achja, richtig, der Program-Header. Los gehts. \<freebasic\>

    type ELF_PROGRAM_HEADER_ENTRY
        p_type as Elf32_Word                         '// type of the segment (see constants above)
        p_offset as Elf32_Off                        '// offset of the segment (in the file)
        p_vaddr as Elf32_Addr                        '// virtual address to which we should copy the segment
        p_paddr as Elf32_Addr                        '// physical address
        p_filesz as Elf32_Word                       '// size of the segment in the file
        p_memsz as Elf32_Word                        '// size of the segment in memory
        p_flags as Elf32_Word                        '// flags (combination of constants above)
        p_align as Elf32_Word                        '// alignment. if zero or one, then no alignment is needed, otherwise the alignment has to be a power of two
    end type

\</freebasic\>

Das wird später alles noch klarer. Und damit dieser Header nicht so alleine ist, bekommt er auch ein paar Konstanten: \<freebasic\>

    const ELF_PT_NULL as UINTEGER = &h00           '// invalid segment
    const ELF_PT_LOAD as UINTEGER = &h01           '// loadable segment
    const ELF_PT_DYNAMIC as UINTEGER = &h02        '// dynamic segment
    const ELF_PT_INTERP as UINTEGER = &h03         '// position of a zero-terminated string, which tells the interpreter
    const ELF_PT_NOTE as UINTEGER = &h04           '// universal segment
    const ELF_PT_SHLIB as UINTEGER = &h05          '// shared lib
    const ELF_PT_PHDIR as UINTEGER = &h06          '// tells position and size of the program-header
    const ELF_PT_LOPROC as UINTEGER = &h70000000   '// reserved
    const ELF_PT_HIPROC as UINTEGER = &h7FFFFFFF   '// reserved

    const ELF_PF_X as UINTEGER = &h01              '// executeable segment
    const ELF_PF_W as UINTEGER = &h02              '// writeable segment
    const ELF_PF_R as UINTEGER = &h04              '// readable segment

\</freebasic\>

Zuerst die Konstanten für den Segment-Typ. Uns interessieren momentan nur die PT_LOAD-Segmente, die anderen brauchen wir (noch) nicht. Die anderen Konstanten können wir momentan getrost ignorieren. Die geben nur ein paar Flags an ;).

## Der Code

Jetzt gehts richtig los.

\<freebasic\>

    function ELF_check (ELFheader as ELF_HEADER) as BYTE
        '// first, we check the MAGIC-string
        if ELFheader.e_ident.EI_MAGIC <> ELF_MAGIC then return 2
        '// now the type of the file
        if ELFheader.e_type <> ELF_ET_EXEC then return 3
        '// next we check the architecture
        if ELFheader.e_machine <> ELF_EM_386 then return 4
        '// now the class
        if ELFheader.e_ident.EI_CLASS <> ELF_CLASS_32 then return 5
        '// and now the data
        if ELFheader.e_ident.EI_DATA <> ELF_DATA_2LSB then return 6
        '// and at last the version
        if ELFheader.e_version <> ELF_EV_CURRENT then return 7
        '// everything OK?
        return -1
    end function

\</freebasic\>

Eigentlich müsste man hier nicht wirklich erklären, oder? Ich tus trotzdem. Also, wir geben dieser Funktion einen ELF-Header. Zuerst überprüfen wir den MAGIC-String (0x7f, 'E', 'L', 'F'). Dann stellen wir sicher, dass die Datei auch zum Ausführen gedacht ist, anschließend prüfen wir, ob es auch die richtige Architektur ist. Dann sehen wir nach, dass wir eine 32-Bit-ELF-Datei haben, schauen nach dem richtigen Datenformat (ihr wisst schon, Endian...) und zum Schluss überprüfen wir die Dateiversion.

Sollte irgendeiner dieser Werte nicht stimmen, können wir die Datei nicht ausführen! Daher geben wir einen Fehlercode zurück, den man später auswerten könnte. Ist alles glatt gelaufen, geben wir TRUE zurück.

Und nun zum wichtigsten, aber auch gemeinsten Code: \<freebasic\>

    sub ELF_Create_Task (ID as USHORT, priority as UBYTE, address as any ptr)
        dim ELFheader as ELF_HEADER ptr = cast(ELF_HEADER ptr, address)
        
        if ELF_check (*ELFheader) = -1 then
            print "ELF-check OK!"
        else
            print "Error: "; ELF_check (*ELFheader)
            return
        end if
        
        dim PHentry as ELF_PROGRAM_HEADER_ENTRY PTR
        
        for counter as UINTEGER = 0 to ELFheader->e_phnum
            PHentry = cast(ELF_PROGRAM_HEADER_ENTRY PTR, (cast(UINTEGER, ELFheader)+cast(UINTEGER, ELFheader->e_phoff)+(cast(UINTEGER, ELFheader->e_phentsize)*counter)))
            
            if PHentry->p_type <> ELF_PT_LOAD then continue for
            
            Paging_mapPhysicalMemory (PHentry->p_vaddr, cast(UINTEGER, (PHentry->p_offset+ELFheader)), cast(UINTEGER, (PHentry->p_offset+ELFheader+PHentry->p_filesz)))
            
            '// Eintrag von PHentry->p_phaddr+ELFheader nach PHentry->p_vaddr kopieren
            
            '// PHentry->p_memsz-PHentry->p_filesz Nullen anhängen
        next
        
        ' Dem Task ein korrektes PageDir und die PageTables übergeben
        ' Dann eip des Tasks auf ELFheader.e_entry setzen und freuen :)
        
        Task_Create (ID, priority, cast(any ptr, ELFheader->e_entry))
    end sub

\</freebasic\>

Die Funktion kümmert sich um die Erstellung eines Tasks. Dazu geben wir ihm die gewünschte Task-ID und die Priorität (kann man natürlich auch weglassen), und natürlich einen Pointer auf die ELF-Datei (bekommt ihr von GRUB in der Multiboot-Info-Struktur).

Als erstes lassen wir natürlich den ELF-Header prüfen. Ist alles glatt gelaufen, machen wir weiter.

Danach durchlaufen wir alle Einträge des Program-Header, um die Segmente zu laden. e_phnum gibt die Anzahl der Einträge an, e_phoff die Position des Headers vom Anfangs der Datei aus, und e_phentsize ist die Größe eines Eintrags. So, wofür die ganzen "cast"s? Hehe, würden wir das nicht machen, würde das ganz übel ausgehen. Wir wandeln hier zuerst die Pointer in Zahlen um, bevor wir damit rechnen. Das ist wichtig, sonst kommt Unsinn raus.

Dann überprüfen wir, ob das ein PT_LOAD-Segment ist. Wenn nicht, machen wir mit dem nächsten Eintrag weiter. Wenn ja, mappen wir das Segment in den virtuellen Speicher. Und das alles so lange, bis wir alle Einträge durch haben.

Zu guter Letzt erstellen wir noch den Task mit e_entry als Startadresse und fertig.

  
Natürlich ist der Code so noch nicht "fertig"! Wenn ich das in einem "fertigen" Kernel sehen sollte, bekommt der Programmierer was zu hören. Wir schummeln in diesem Code nämlich. Erstens kopieren wir die Segmente nicht, sondern wir mappen sie nur. Zweitens teilt sich der Kernel hier den virtuellen Adressraum mit seinen Tasks. Drittens ignorieren wir, das ein Segment im Speicher eventuell größer sein muss als in der Datei, den Rest müsste man mit Nullen auffüllen. Und viertens hat der Task hier Kernelrechte.

Also hinsetzen und Code verbessern! Das hier soll nur erklären, wie es geht, übernehmt den Code so nicht! Für jeden Task sollte ein eigenes PageDir erzeugt werden, und die oben genannten Kritikpunkte sollten verbessert werden. Vielleicht fragt ihr euch, warum ich es nicht gleich richtig gemacht habe. Naja, \*ähem\*, das liegt daran, dass mein Speichermanager nur Unfug treibt. Würde der funktionieren, hätte ich das von Anfang an anders umgesetzt. Vielleicht ändere ich dieses Tutorial noch, wenn alles läuft.

Also, ich hoffe, es hat euch Spaß gemacht, dieses Tutorial zu lesen. Wenn ihr Fragen habt, wie gesagt, stellt sie im Lowlevel-Forum, oder ihr werft mal einen Blick in die Spezifikationen.

Kleiner Hinweis: Auch dieser Code stammt wieder aus meinem Kernel: <http://sourceforge.net/projects/frostkernel>

Happy Coding, The Thing

## Siehe auch

- [Executable and Linking Format](Executable-and-Linking-Format "Executable and Linking Format")

## Weblinks

- [Beschreibung des ELF-Formats (PDF)](http://www.linux-kernel.de/appendix/ap05.pdf)
- [ELF-Spezifikation](http://www.skyfree.org/linux/references/ELF_Format.pdf)
- [Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification Version 1.2 (PDF)](http://refspecs.freestandards.org/elf/elf.pdf)
- [Tool Interface Standard (TIS) Executable and Linking Format (ELF) Specification Version 1.2 (PDF)](http://www.acm.uiuc.edu/sigops/rsrc/pfmt11.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9373/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1854/index.html)

<!-- MediaWiki page 1854; revision 9373; parent 6913; 2011-01-23T20:58:29Z -->
