# C-Kernel starten

**Warnung**

Es wird davon abgeraten dieses Tutorial zu verwenden. Empfohlen wird von unserer Seite aus [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger") und das dort gelinkte Tutorial [C-Kernel mit GRUB](https://github.com/lowlevel-eu/wiki/wiki/C-Kernel-mit-GRUB "C-Kernel mit GRUB").

  

## Vorwort

Da im letzten Tutorial ([Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode")) es leider nicht mehr ganz geklappt hat schiebe ich dieses Tutorial noch nach. Hier werde ich zeigen wie man einen eigenen [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") der in [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") geschrieben ist starten kann. Auch dazu ist etwas Arbeit nötig und meine Methode ist vielleicht nicht die bequemste, jedoch funktioniert sie und ich werde auch wieder selbst geschriebene Tools bereitstellen, um die Arbeit möglichst zu erleichtern.

  

## Booten

Das erste was passieren muss ist das der PC booten muss. Es gibt viele bereits fertig [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") die einen großen Umfang an Funktionen bieten. Ich bin jedoch eher der Ansicht das man es selbst machen sollte. Da ich mir einen eigenen Bootloader geschrieben habe, der eigentlich recht bequem funktioniert, stützte ich mich hier darauf. Der Bootloader lädt eine binäre Datei aus dem Hauptverzeichnis einer Diskette, welche mit dem [FAT12](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "File Allocation Table") [Dateisystem](https://github.com/lowlevel-eu/wiki/wiki/Dateisystem "Dateisystem") arbeitet. Daher kann man seinen Kernel später ganz bequem auf die Diskette kopieren und starten lassen. Da ich den Bootloader bereits in einem Tutorial vorgestellt habe, werde ich hier nicht näher darauf eingehen, sondern lediglich am Ende nochmal den Quelltext bereitstellen.

  

## Zwei Kernel

Es mag komisch klingen, aber man benötigt, zumindest für meine Version, zwei Kernel. Streng genommen sind es sogar drei. Dabei bestehen zwei Kernel aus reinem Assembler und der andere ist dann der eigentliche, in C geschriebene Kernel, auf den wir hinaus wollen.

Der erste Kernel dient lediglich dazu eine kleine [Global Descriptor Table](https://github.com/lowlevel-eu/wiki/wiki/Global-Descriptor-Table "GDT") einzurichten und in den Protected Mode zu schalten. Das ist nämlich Grundvoraussetzung, wenn wir im weiteren mit einem C-Kernel arbeiten möchten.

Der zweite Kernel (wenn man das so bezeichnen kann) ist ein kleiner Zwang den mit der Linker aus den GNU Binutils auferzwungen hat. Dieser erklärte mir nämlich ganz höflich das er sich nicht dazu überreden lässt eine Objektdatei zu linken, die teilweise 16-Bit Code enthält. Und diesen 16-Bit Code benötigen wir in dem ersten Kernel, welcher in den Protected Mode schaltet. Dort sind wir nämlich, solange wir den Protected Mode noch nicht endgültig aktiviert haben, im Real-Mode und haben somit auch 16-bit Code.

Daher also brauchen wir diesen zweiten Kernel. Dieser beinhaltet eigentlich nur einen JUMP-Befehl. Und zwar den Jump zur Main-Funktion des C-Kernels.

Die klingt banal, hat aber einen Grund. Wenn wir im C-Kernel arbeiten, haben wir auch bestimmt mit Strings (char \*Text = "hallo") zu tun. Und C-Compiler haben die Angewohnheit solche Strings die ja fest im Programmcode stehen an den Anfang der compilierten Datei zu schreiben. Und um diese Strings zu überspringen benötigen wir den zweiten Kernel, der einen Jump direkt (über die Strings hinweg) zur Main-Funktion macht.

So und dann haben wir natürlich noch den dritten, eigentlichen Kernel, der in C geschrieben wird. Sobald wir also erstmal in der Main-Funktion des C-Kernels drin sind, haben wir es ans sichere Ufer geschafft. Von hier aus können wir einen Großteil in C schreiben und auch Assemblerfunktionen bequem aufrufen ohne uns Gedanken um deren Startadressen zu machen. Das erledigt dann alles der Linker für uns.

  

## Sprung in den Protected Mode

Kommen wir also gleich zum Kernel nummer Eins. Dieser wurde ziemlich eingehend im Protected Mode Tutorial behandelt. Deshalb gibts auch hier nur am Ende wieder den Quellcode zum runterladen.

Dieser Kernel muß zu einer binären Datei compiliert werden. Und das bewerkstelligen wir mit der folgenden Befehlszeile:

    nasmw -f bin -o kernel16.bin kernel16.asm

Zur Erläuterung:

"nasmw" ist der Name des Netwide Assemblers. Dieser Name bezieht sich auf die Windows-Version. Unter Linux und DOS heißt es nur "nasm".

"-f bin" gibt an, das wir als Ausgabeformat eine binäre Datei haben möchten. Das heisst das der Quelltext so wie er ist in Maschinencode umgewandelt wird und ohne irgendwelcher Zusatzinformationen gespeichert wird.

"-o kernel16.bin" gibt an, das wir als Ausgabe gerne die Datei mit dem Namen "kernel16.bin" erstellt haben möchten.

"kernel16.asm" ist schließlich der Name der Quellcode-Datei die wir gerne assembliert haben möchten.

## Aufruf der Main-Funktion

Das wird nun der zweite "Mini"-Kernel, welcher lediglich die Main-Funktion des C-Kernels aufruft.

Dazu wird folgender Assemblercode benötigt:

\<asm\>

    [Bits 32]
        extern  _main
        global  start
    start:
        call    _main
    Stop:
        jmp     stop

\</asm\>

Auch hier wieder eine Erläuterung:

"\[Bits 32\]" teilt NASM mit, das wir 32-Bit Code erstellt haben möchten.

"extern \_main" teilt NASM mit, das er sich keine Sorgen machen muß, wenn er das Label "\_main" nicht in dem Quelltext finden kann, da dieses Label extern, also in einer anderen Datei definiert wird.

Der Unterstrich bei "\_main" ist nötig, da C-Compiler den Funktionsnamen beim kompilieren immer einen Unterstrich voranstellen.

"global start" ist praktisch das Gegenstück zu "extern \_main". NASM wird einen Vermerk beim kompilieren in die Datei machen, das das Label "start" für andere Datein verfügbar gemacht wird. Das bedeutet, das eine weitere Datei, welche das Label "start" als "extern" gekennzeichnet hat, dieses Label beim Linken hier finden kann.

Dieses Label muss aber nur vom Linker selbst gefunden werden, da dieser beim Linken gerne ein Label angegeben haben möchte, das an welchem er sich ausrichten kann. Dazu jedoch später mehr.

Das Label "Stop" und der Befehl "jmp Stop" definieren eine Endlosschleife. Sollte unsere Main-Methode aus dem C-Kernel nämlich beenden, dann springt der Prozessor nämlich wieder in diesen Code zurück und führt die Befehle nach dem "call \_main" aus. Und damit dann nichts unkontrolliertes passiert, lassen wir eine Endlosschleife laufen.

  
So nun speichern wir diese Datei unter dem Namen "kernel32.asm" ab und lassen sie assemblieren. Dabei gehen wir diesmal ein bisschen anderes vor, als beim vorherigen Abschnitt. Die Befehlszeile die wir hier benötigen lautet:

    nasmw -f aout -o kernel32.obj kernel32.asm

Erläuterung:

Hier fällt auf das wir nun anstatt "-f bin" die Angabe "-f aout" machen. Das bewirkt, das wir nun nichtmehr eine binäre Datei erhalten, sondern eine sog. Objektdatei. Diese Objektdatei enthält nun nicht nur den reinen übersetzen Maschinencode, sondern auch Zusatzinformationen. Und zwar Informationen über externe Labels die in dieser Datei noch nicht aufgelöst wurden.

Das bedeutet das in diesem Code ein Sprung oder ein Call zu einer Funktion gemacht wird, die aber in dieser Datei nicht bekannt ist. Daher wird ein entsprechender Vermerkt in die Objektdatei getätigt. Wenn wir dann später den C-Kernel, welcher die gesuchte Main-Funktion beinhaltet, und den hier aufgeführten Kernel zusammen Linken, dann werden die beiden Dateien förmlich aneinanderkopiert und die Adressen der Funktionen und Labels dort eingesetzt, wo sie noch nicht eingetragen werden konnte, weil sie noch nicht bekannt waren. Das nennt man Auflösen von Funktionen oder Labeln.

Wir haben also nun schonmal zwei Dateien. Eine binäre Datei (kernel16.bin) und eine Objektdatei (kernel32.obj).

  

## Der C-Kernel

Nun kommen wir zum interessanten Teil. Den C-Kernel. Dort wollen für gewöhnlich alle hin, weil sie

- kein Assembler können
- Assembler nicht mögen
- Assembler ihnen zu aufwendig ist
- in C eh alles viel schneller geht

Die Gründe können eigentlich völlig wurst sein. In C arbeitet es sich einfach wesentlich bequemer. Dennoch wird man feststellen, das man auch hier noch auf ein paar Funktionen in Assembler angewiesen ist und das es manche Funktionen gibt, die sich in Assembler einfach besser umsetzen lassen. Jedenfalls können wir dann jede Assemblerdatei bequem in eine Objektdatei assemblieren lassen und mit der Objektdatei des C-Kernels zusammenlinken. Somit können wir dann bequem Assembler-Funktionen von C aus aufrufen und vice versa.

Der C-Kernel kann Anfangs erstmal sehr einfach aussehen. Daher genügt erstmal folgender Code:

\<c\>

    int main()
    {
        return(0);
    }

\</c\>

Es gibt viele Leute die sich darum streiten ob die Funktion nun "void" oder "int" als Returnwert haben soll oder muss. Laut Standard soll es "int" sein, was auch Sinn macht, da darüber ein Return-Wert an das Betriebssystem zurückgegeben werden kann, anhand dessen das Betriebssystem feststellen kann, ob die Anwendung korrekt oder mit einem Fehler beendet wurde.

Hier sind WIR aber das Betriebssystem und wir brauchen auch keinen Returnwert. Daher würde es genügen wenn man "void" nimmt. Da aber in diesem Fall der GCC-Compiler meckert, hab ich es beim "int" belassen.

Damit wir aber auch einen Beweis haben, das das mit unserem C-Kernel geklappt hat, erweitern wir die Main-Funktion um ein klein wenig Code um uns zumindest mal eine kleine Meldung auf den Monitor auszugeben.

Dazu müsste man nun nachschlagen, das man direkt in den Videospeicher schreiben kann. Dieser beginnt im 25x80 Modus an der Adresse 0xB8000.

25x80 bedeutet das wir im Textmodus sind und wir hier 80 Zeichen pro Zeile und 25 Zeilen auf einer Bildschirmseite haben. Da wir für jeden Buchstaben 2 Bytes benötigen (eins für den ASCII-Code des Zeichens und eins für den Farbwert) ist der Bildspeicher für eine Seite genau

25x80 = 2000

2000x2 = 4000

Bytes lang.

Erweitern wir nun also wie folgt den C-Code:

\<c\>

    int main()
    {
        char *Text = "Welcome to Protected Mode";
        char *VideoMem = (char*)0xB8000;
        while(*Text)
        {
            *VideoMem = *Text;
            VideoMem++;
            *VideoMem = 7;
            VideoMem++;
            Text++;
        }
        return(0);
    }

\</c\>

Eigentlich sollte ich erwarten, das man C kann, wenn man schon das Tutorial liest. Dennoch will ich nicht so sein und erkläre auch hier kurz was passiert:

Als erstes definieren wir einen Text "Welcome to Protected Mode". Der C-Compiler ist so nett und fügt an das Ende automatisch ein Null-Byte an, weshalb wir uns darum keine Sorgen machen müssen.

Als nächstes erstellen wir einen Char-Pointer der auf die Startadresse des Videospeichers(0xB8000) zeigt.

Dann haben wir eine Schleife laufen. Diese prüft bei jedem Durchgang ob das Zeichen auf das "Text" gerade Zeigt ungleich 0 ist. Wenn das Zeichen jedoch eine Null ist, wird die Schleife beendet.

Dann schreiben wir das Zeichen auf das "Text" zeigt in den Videospeicher.

Der Pointer für den Videospeicher wird um 1 erhöht, so das er nun auf das zweite Byte zeigt, welches den Farbwert für das erste Zeichen aufnimmt.

Dort schreiben wir dann eine 7 rein. Das bedeutet das wir hellgrauen Text auf schwarzem Hintergrund haben möchten.

Folglich erhöhen wir den Pointer für den Videospeicher wieder um 1, damit er nun auf das dritte Byte zeigt, wo im folgenden das nächste Zeichen untergebracht wird.

Auch den Pointer "Text" erhöhen wir um 1, damit dieser nun auf das nächste Zeichen im String zeigt.

Und dann wiederholt sich die Schleife.

Am Ende sollten wir dann in der oberen linken Ecke den Text "Welcome to Protected Mode" lesen können.

  
So nun fehlt natürlich auch hier noch die Befehlszeile, mit welcher wir den C-Kernel in eine Objektdatei compilieren können. Diese lautet wie folgt:

    gcc -ffreestanding -c -Os -o ckernel.obj kernel.c

Erläuterung:

"gcc" ist der Name des Compilers. Dieser wird eigentlich für Linux verwendet. Es gibt jedoch portierte Versionen für Windows. DJGPP heißt eine davon, welche ich hier benutze.

"-ffreestanding" teilt dem Compiler mit, das er keine Standardbibliotheken benutzen soll. Dies würde uns auch nichts nützen, da diese Bibliotheken meist komplett oder zum Teil Betriebssystemabhängig sind. Und da wir ein eigens Betriebssystem schreiben........

"-c" bedeutet das der Compiler lediglich eine Objektdatei erstellt, diese aber "noch" nicht linkt. Da wir mehrere Dateien miteinander verlinken werden, macht es keinen Sinn diese Datei getrennt linken zu lassen.

"-Os" Diese Option lässt den Compiler den erzeugten Code etwas optimieren und trimmt Ihn so, das er möglichst kurz ist. Die Option ist eigentlich nicht nötig. Da GCC aber manchmal (ohne diese Option) etwas komischen und unlogischen Code erstellt, habe ich diese Option immer mit dabei.

"-o ckernel.obj" benennt den Dateinamen den wir gerne für die Objektdatei haben möchten.

"kernel.c" ist die C-Datei die unseren C-Kernelquelltext enthält.

  
So nun haben wir schon drei Dateien. Die "kernel16.bin", die "kernel32.obj" und die ckernel.obj.

  

## Linken

Damit das ganze auch Gestalt annimmt, müssen wir das ganze noch zusammen durch einen Linker jagen. Dieser kopiert uns die Objektdateien zu einer zusammen und löst die verbleibenden Funktionen und Label auf. Damit erhalten wir dann schon "fast" unseren fertigen Kernel.

Fast nur deshalb, weil wir die "kernel16.bin" nicht mit durch den Linker jagen können, da es sich hier nur um eine binäre Datei handelt. Diese muß aber auch untergebracht werden. Und dabei müssen wir sicherstellen das der Code der darin enthalten ist zu allererst ausgeführt werden muss. Das erreichen wir ganz einfach, indem wir den "verlinkten" Kernel und die "kernel16.bin" zusammenkopieren. Dabei muss so kopiert werden, das die "kernel16.bin" am Anfang der neuen Datei steht. Für dieses Zusammenkopieren könnte man ganz gewöhnlich den Copy-Befehl (für Linux "cp) benutzen. Da ich dem aber nicht so ganz traue, habe ich auch hier ein kleines Tool geschrieben, das diesen Schritt erledigt. Auch dieses kann am Ende heruntergeladen werden.

So nun aber zum verlinken der beiden Dateien "kernel32.obj" und "ckernel.obj". Dazu benutzen wir den Linker "ld" der ebenfalls bei DJGPP enthalten ist. Für diesen erstellt man sich am besten eine "Linkerfile". Diese enthält die nötigen Angaben und Einstellungen die der Linker benötigt. Auch diese Datei wird zur Verfügung gestellt. Trotzdem erkläre ich hier noch ein paar kleine Einzelheiten zu dieser Datei, da diese evtl. später mal geändert werden müssen.

Da hätten wir als allererstes folgende Zeile:

    INPUT(kernel32.obj ckernel.obj)

Hier werden in den Klammern alle Objektdateien angegeben, die zusammengelinkt werden sollen. Wichtig dabei ist, das die "kernel32.obj" zuerst angegeben wird, damit diese auch zuerst in der fertigen Datei steht. Sollten später mal weitere Objektdateien erzeugt werden, können diese ganze einfach ebenfalls in diese Klammer eingetragen werden und werden somit beim nächsten Linken berücksichtigt.

Dann hätten wir da noch folgende Zeile:

    .text 0x10200 : {

Die genaue Bedeutung ist ansich unrelevant. Wissenswert ist lediglich das die Zahl "0x10200" (Dezimal: 66048) angibt an welcher Adresse der Kernel im Speicher beginnt. Das muß der Kernel wissen, da er nur mit dieser Angabe die Adressen für Funktionen und Variablen korrekt berechnen kann.

Hier ist allerdings die Adresse anzugeben, welcher der Kernel innerhalb des Codesegmentes ist. Unser Kernel beginnt an der Adresse 0 im Code-Segment. Da wir jedoch die Datei "kernel16.bin" noch VOR den hier zu verlinkenden Kernel kopieren müssen. Mit der Anweisung "times" innerhalb der Datei "kernel16.asm" habe ich dafür gesorgt das die erstellte Datei "kernel16.bin" 512 Bytes groß wird. Das mag nach Verschwendung klingen, hat aber einen Grund. Beim Linken versucht der Linker immer ein Alignment zu erzeugen. Sprich er beginnt ungern an ungeraden Adressen. Und daher könnte es leicht passieren, das wir vielleicht im Nachhinein nochmal etwas an der Datei "kernel16.asm" ändern möchten und somit Gefahr laufen das das Ergebnis (kernel16.bin) eine ungerade Bytezahl annimmt. Wenn wir das nicht bemerken und versuchen das ganze zusammenzufügen werden wir wohl Überraschungen erleben, weil der Linker dann noch ein paar Nullen einfügt die da nicht hinsollen. Daher sorgen wir also dafür das die Datei "kernel16.bin" 512 Byte größe hat und das der Linker den restlichen Kernel so linkt, das er an der Adresse 0x10200 (Dezimal: 66048) beginnt.

Und auch hier wieder die Befehlszeile für den Linker:

    ld -T link.txt -o c32kernel.bin

Erläuterung:

"ld" Name des Linkers.

"-T link.txt" teilt dem Linker mit, das wir eine "Linkerfile" benutzen und das deren Namen "link.txt" ist.

"-o c32kernel.bin" besagt den Namen der Datei die wir gerne als Ergebnis haben möchten.

So nun sind wir schon ein Stück weiter und haben eigentlich nur noch zwei relevante Dateien. Nämlich die "kernel16.bin" und die "c32kernel.bin".

  

## Alles Zusammenfügen

Jetzt haben wir es fast geschafft. Wir müssen nur noch die beiden Dateien "kernel16.bin" und "c32kernel.bin" zusammenkopieren.

Dies kann man mit dem Tool(MergeKernel) das ich geschrieben habe und zum Download am Ende mit angebe bewerkstelligen.

Dazu gibt man folgenden Syntax an:

    MergeKernel kernel.bin kernel16.bin c32kernel.bin

    Anmerkung: Unter Linux geht das am einfachsten so: 
     cat kernel16.bin c32kernel.bin > kernel.bin

Damit wird die Datei "kernel.bin" erstellt und die Inhalte der Dateien "kernel16.bin" und "c32kernel.bin" werden in diese kopiert. Wichtig ist dabei, das "kernel16.bin" zuerst, also direkt nach "kernel.bin", angegeben wird.

Nun haben wir den fertigen Kernel(kernel.bin).

Damit wir diesen auch starten können müssen wir zunächst meine Bootloader auf eine Diskette bekommen. Dazu benutzt man am besten das Tool Rawrite. Ich persöhnlich habe es mit dem Programm HexWorks erledigt. Damit kann man nämlich Datenträger Sektorweise öffnen und beschreiben.

Wenn wir das nun haben, kopieren wir einfach die "kernel.bin" in das Hauptverzeichnis der Diskette und booten entweder einen PC damit, oder wir starten den Emulator "Bochs" mit der Angabe das er vom realen Diskettenlaufwerk booten soll.

  

## Anmerkungen

Wenn man es soweit geschafft hat und man ein "Welcome to Protected Mode" auf dem Bildschirm lesen konnte, dann kann man nun selbst weitermachen und seinen C-Kernel weiterentwickeln. Zu beachten ist nur, das der Kernel jedes Mal neu compiliert, gelinkt, zusammenkopiert und auf Diskette kopiert werden muß, bevor man es ausprobieren kann. Um nicht so viel Tipparbeit zu haben, sollte man sich, so wie ich, ein paar Batch-Dateien schreiben, die einem die Arbeit etwas abnehmen.

  

## Nachwort

Wie üblich kann dieser Text frei kopiert, gedruckt und weitergegeben werden, solange wenigstens mein Name, sowie E-Mail Adresse mitgereicht werden.

  
Hier noch das Packet an Tools und Quelltexten: [ckernel.zip](http://lowlevel.brainsware.org/wiki/images/ckernel.zip)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10630/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1458/index.html)

<!-- MediaWiki page 1458; revision 10630; parent 7051; 2012-07-02T08:20:10Z -->
