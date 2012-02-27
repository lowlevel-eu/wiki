# Teil 1 - Entwicklungsumgebung

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| « [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger") | **Navigation** | [Teil 2 - Assembler 101](https://github.com/lowlevel-eu/wiki/wiki/Teil-2-Assembler-101 "Teil 2 - Assembler 101") » |

## Ziel

Das Ziel dieses Artikels ist es, eine Entwicklungsumgebung aufzusetzen und zumindest ansatzweise zu verstehen, mit der Du sinnvoll in die OS-Entwicklung einsteigen kannst. Vor allem sollten damit alle Voraussetzungen abgedeckt sein, damit Du die Beispiele in den folgenden Kapiteln selbst nachvollziehen kannst.

## Dein Computer

Fangen wir vorne an: Du brauchst einen PC. Ja, Du hast recht, Du brauchst natürlich strenggenommen keinen PC. Aber es wäre geschickt, denn ich nehme an, Du willst ein x86-Betriebssystem schreiben. Wenn Du wider Erwarten für eine andere Plattform entwickeln möchtest, teil Dich im Forum mit, das wird auch andere interessieren - allerdings bist dann in vielen Fällen Du derjenige, der erklären darf. Vielleicht findest Du aber auch andere Interessierte, die Dir dabei helfen, im Dunkeln herumzustochern.

Aber zurück zum PC: Am besten hat dieser ein Diskettenlaufwerk, denn Disketten sind für den Anfang das handlichste. Und ein 386er oder höher sollte es schon sein - aber das sollte heutzutage machbar sein.

## Dein Betriebssystem

Eine Stufe weiter kommen wir zum Betriebssystem. Da Dein eigenes Betriebssystem noch nicht fertig ist, wirst Du wohl vorerst mit einem bestehenden vorliebnehmen müssen. Ist eine Version von [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") installiert? Wunderbar, nimm das. Oder eine BSD-Variante. Wenn Du kein Linux installiert hast, kannst Du auch eine Linux-Live-CD wie z.B. Knoppix verwenden. Es ist natürlich auch möglich, ein Linux-System auf einer virtuellen Maschine wie [VMware Server](https://github.com/lowlevel-eu/wiki/wiki/VMware "VMware"), [VirtualBox](https://github.com/lowlevel-eu/wiki/wiki/VirtualBox "VirtualBox") oder [Microsoft Virtual PC](https://github.com/lowlevel-eu/wiki/wiki/Microsoft-Virtual-PC "Microsoft Virtual PC") zu installieren. Der Vorteil eines solchen Systems ist, dass alle benötigten Werkzeuge nativ verfügbar sind und Du ohne großartige Einrichtung einfach loslegen kannst.

Wenn Du es dennoch bevorzugen solltest, mit Windows zu arbeiten, kannst Du Dir mit ein wenig Vorarbeit auch dort eine Entwicklungsumgebung einrichten. Dabei empfiehlt sich die Installation einer Cross-Toolchain und von MSYS, damit Du Deine Makefiles durch Verwendung von Unixbefehlen einigermaßen portabel halten kannst. Für andere Dinge wie die Bearbeitung von Disketten- und Festplattenimages wirst Du zusätzliche Tools wie z.B. VFD benötigen.

## Dein Editor

Dann brauchst Du Editor und Compiler. Als Editor hast Du sicher schon Deinen eigenen Favoriten (nämlich vim), aber wenn nicht, dann findest Du vielleicht in der folgenden Liste einen für Dich passenden. Häufig benutzt werden:

- Unter Linux: vim, Kate, gedit, KDevelop, Eclipse
- Unter Windows: Notepad++, Eclipse

Vielleicht gefällt Dir ja einer aus [dieser](https://github.com/lowlevel-eu/wiki/wiki/Editor "Editor") Liste.

## Dein Compiler

Auch beim Compiler ist die Sache relativ klar: Wenn Du als Programmiersprache [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") nimmst (in dieser Reihe wird C für die Beispiele benutzt), wird der Compiler im Allgemeinen gcc sein und unter [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux") ist damit alles geklärt.

Wenn Du gcc unter [Windows](https://github.com/lowlevel-eu/wiki/wiki/Windows "Windows") benutzen willst, solltest Du Dir überlegen, ob Du nicht einen Crosscompiler benutzt, der ELF-Dateien erzeugt. Du brauchst in diesem Fall sowohl gcc als auch binutils in einer Cross-Variante. Der Artikel [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows") beschreibt, wie Du dabei vorgehen musst.

Außerdem brauchst Du einen Assembler. Wenn gcc läuft, hast Du schon einen: *as* ist der GNU-Assembler und ist in binutils enthalten. Ansonsten werden bei der Betriebssystementwicklung häufig [NASM](https://github.com/lowlevel-eu/wiki/wiki/Netwide-Assembler "NASM") oder [FASM](https://github.com/lowlevel-eu/wiki/wiki/Flat-Assembler "FASM") verwendet.

## Dein Emulator

Schließlich brauchst Du auch noch eine Möglichkeit, dein Werk zu testen. Ja, ich weiß, der PC. Aber du willst nicht nach jeder kleinen Änderungen neu booten müssen, richtig? Besorg dir einen Emulator. VMware ist ganz nett, aber hilft Dir beim Debuggen nicht besonders weiter. Nimm [QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") oder [Bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") - oder am besten beides. Wenn Dein System in beiden Emulatoren funktioniert, ist immer noch genug Zeit, es auf den echten PC loszulassen.

### bochs

[bochs](https://github.com/lowlevel-eu/wiki/wiki/Bochs "Bochs") ist ein echter PC-Simulator. Er liest Befehl für Befehl ein und führt ihn aus, ist also ein Interpreter für x86-Maschinencode. Dadurch ist bochs relativ langsam und kann mit der Zeit mühsam zu benutzen werden. Er bietet aber gerade für den Anfang den Vorteil, dass er bei höchstem Loglevel sehr viele hilfreiche Fehlermeldungen ausgibt, während man bei anderen Emulatoren raten muss, was genau schiefgelaufen ist.

Unter <http://bochs.sourceforge.net> gibt es die jeweils neueste Version herunterzuladen - sowohl den Quellcode als auch Binärpakete u.a. für Linux und Windows.

### QEMU

[QEMU](https://github.com/lowlevel-eu/wiki/wiki/QEMU "QEMU") verfolgt einen Ansatz: Wenn bochs ein Interpreter ist, ist qemu ein (JIT-)Compiler. Wenn ein Stück Code des Gastbetriebssystems zum ersten Mal ausgeführt wird, übersetzt er es in Maschinencode, der statt auf den richtigen Prozessor auf den qemu-Prozessorzustand im Speicher zugreift. Dadurch wird die Codeausführung sehr viel schneller.

Herunterzuladen ist qemu an folgenden Orten

- <http://www.qemu.org> hat die aktuelle stabile Version
- Unter git://git.savannah.nongnu.org/qemu.git befindet sich die Entwicklerversion
- <http://lowlevel.brainsware.org/download/qemu-0.11.50-c988bfa.tar.bz2> ist ein inoffizielles Binärpaket für Windows

Nachdem der Quellcode heruntergeladen ist (entweder die stabile Version entpackt oder die Entwicklerversion aus dem git ausgecheckt), wird qemu folgendermaßen gebaut:

    ./configure --target-list=x86_64-softmmu
    make
    make install

## Deine Versionsverwaltung

Um ein größeres Stück Software zu entwickeln (erfahrenere Programmierer werden mir zustimmen, dass "größer" hier bei mehr als einem Hello-World-Programm anfängt), ist es unverzichtbar eine [Versionsverwaltung](https://github.com/lowlevel-eu/wiki/wiki/Versionsverwaltung "Versionsverwaltung") zu benutzen. Das gilt vor allem bei der Entwicklung im Team, aber auch bei Ein-Mann-Projekten ist sie sinnvoll. Die Grundidee ist, dass jedesmal, wenn ein Stück Arbeit erfolgreich erledigt ist, der aktuelle Quellcode in der Versionsverwaltung mit einer passenden Beschreibung gesichert wird. Dadurch kann man später nachvollziehen, wer wann was warum geändert hat. Wenn etwas schiefläuft, kann man zu einer alten Version zurückkehren, entweder um die seither gemachten Änderungen rückgängig zu machen oder um die Änderung herauszufinden, die einen Fehler verursacht hat.

Welche Software Du dazu benutzt, ist mehr oder weniger egal, solange Du überhaupt eine benutzt. Mein Vorschlag an dieser Stelle ist [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git"), das in seinem eigenen Artikel näher beschrieben wird.

## Bevor es nun richtig losgeht...

Leider müssen wir immer wieder feststellen, dass angehende Betriebssystementwickler den Kernel aus diesem Tutorial blind kopieren für ihr eigenes Betriebssystem und im IRC dann fragen stellen, getreu dem Motto: "Ich habe hier den Kernel einfach kopiert und er funktioniert nun nicht, bitte helft mir!" (damit wird jetzt nicht das Klonen des Kernel aus dem [Repository](http://git.tyndur.org/?p=tutorial.git;a=summary) und Kompilieren gemeint, sondern die Übernahme des Codes 1:1 in das eigenes Betriebssystem). Nicht nur, dass das bloße Kopieren keinerlei Lerneffekt mich sich bringt, es ist auch nicht erlaubt: Der Code in diesem Tutorial untersteht dem deutschen Urheberrecht und der Autor ist taljeth.

Natürlich dürft ihr den Code als "Inspiration" nutzen, doch lasst euch euch gesagt sein: Einfach kopieren bringt euch nichts und schadet vor allem nur eurer Reputation, vor allem, wenn ihr im IRC fragt, ob jemand euren kopierten Code fixen kann.

|  |  |  |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| « [OS-Dev für Einsteiger](https://github.com/lowlevel-eu/wiki/wiki/OS-Dev-f%C3%BCr-Einsteiger "OS-Dev für Einsteiger") | **Navigation** | [Teil 2 - Assembler 101](https://github.com/lowlevel-eu/wiki/wiki/Teil-2-Assembler-101 "Teil 2 - Assembler 101") » |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10477/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1919/index.html)

<!-- MediaWiki page 1919; revision 10477; parent 10476; 2012-02-27T15:22:27Z -->
