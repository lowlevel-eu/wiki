# MyXomycota

| MyXomycota |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | 0.004 (pre-alpha) |
| [Lizenz](Lizenzen.md "Lizenzen"): | Gnu [GPL](Lizenzen.md "GPL") / BSD ([CDI](Common-Driver-Interface.md "CDI")-Treiber) |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86.md "X86") |
| [Kernelart](Kernel.md "Kernel"): | [Monolithischer Kernel](Kernel.md#monolithischer-kernel "Monolithischer Kernel") mit Unterstützung für Userlandtreiber |
| [Sprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"): | [C](C.md "C") |
| API: | [Int 0x80](Syscall.md "Syscall") |
| Binärformat: | [ELF](Executable-and-Linking-Format.md "ELF"), [Shell](Shell.md "Shell")-Scripts |
| [IPC-Methode](Interprozesskommunikation.md "IPC"): | Keine (bis jetzt) |
| Homepage |  |

[Sourceforge](http://sourceforge.net/projects/myxomycota)

  
Der Name "MyXomycota" ist vom Namen der Schleimpilze (Myxomyceten) abgeleitet - das scheinen ziemlich kluge Dinger zu sein, auch wenn man es ihnen nicht zutraut. Es handelt sich bei diesem [Betriebssystem](Betriebssystem.md "Betriebssystem") um ein einfaches Hobbybetriebssystem, das im ProtectedMode läuft und über eine simple [Kommandozeile](Shell.md "Shell") verfügt.

**HINWEIS:** Dieses Projekt wurde zugunsten von [Paloxena](Paloxena.md "Paloxena") auf unbestimmte Zeit verschoben. Ich konnte das ewige "Das ist kaputt." einfach nicht mehr ertragen. ;-)

**This product includes software developed by the tyndur Project and its contributors.** ([CDI](Common-Driver-Interface.md "CDI")-Treiber)

## Entwickler

- [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic")

## Das Mountsystem

Herz des Systems sind das Mountsystem und das virtuelle Dateisystem. Dieses VFS läuft in einer zehn Megabyte großen RamDisk und sorgt für jegliche Kommunikation mit Geräten oder dem [Kernel](Kernel.md "Kernel"), wenn sie nicht über [int](Interrupt.md "Interrupt") 0x80 ablaufen muss. In ihm können hierzu virtuelle Dateien erstellt werden, die vom Mountsystem registriert werden. Solche Dateien können Geräte ("/dev/console", "/dev/pci/0-0-0", "/dev/audio"), Kommunikationskanäle zum Kernel ("/sys/mount") oder jegliche Art von [Dateisystemen](Dateisystem.md "Dateisystem") ("/proc", "/mnt/fda", "/mnt/addon", "/mnt/auto/hda1") sein. Ein Gerät wird im Kernel durch eine einfache Funktion repräsentiert, die ein paar Parameter bekommt (ID-Nummer, Position innerhalb der "Datei", Zugriffsart, Länge des Zugriffs, ...) und einen Wert zurückgeben kann. Eine Dateisystemfunktion erhält statt einer ID-Nummer das Handle der Datei, auf der sich das Dateisystem befindet. Daher kann man auch normale Dateien und nicht nur Gerätedateien mounten (z. B. "/dev/hda1" -\> "/mnt/auto/hda1", "/mnt/auto/hda1/floppy.img" -\> "/home", "/home/test.img" -\> "/tmp"; also auch über mehrere Dateisysteme hinweg). Wichtig ist, dass ein Dateisystem natürlich nicht wirklich physisch vorhanden sein muss: Von Relevanz ist lediglich, was die Funktion an das Mountsystem zurückgibt. Daher sind auch virtuelle Dateisysteme wie das procfs ("/proc") oder das pipefs ("/sys/pipe", noch in Arbeit) möglich. Das ProcFS beispielsweise zeigt Informationen zu allen Prozessen im System an, wobei pro Prozess eine Datei existiert. Die Informationen können mit dem Programm "top" ausgelesen werden.

### Zugriff auf Netzwerkfunktionen

Noch gibt es kein offizielles Release mit Netzwerkfunktionalität, das soll im nächsten Release anders sein. Zugriff darauf erhält man dann mit folgenden Spezialdateisystemen unter den ebenfalls folgenden Mountpoints:

- "ipfs" - "/net/ip"
- "tcpfs" - "/net/tcp"
- "udpfs" - "/net/udp"

#### /net/ip

Um eine IP-"Verbindung" aufzubauen, öffnet man eine Datei mit Lese- und Schreibzugriff ("r+") in /net/ip. Der Dateiname lautet "interface:IP". Um eine Verbindung zu www.google.de (74.125.39.106) über das Interface "eth0" aufzubauen, geht man folgendermaßen vor:

\<c\>FILE \*ipcon; ipcon = fopen("/net/ip/eth0:74.125.39.106", "r+")\</c\>

Danach kann man einfach Daten empfangen ("fread") und senden ("fwrite") sowie die Verbindung wieder beenden ("fclose"). Zu beachten ist, dass nur ganze Pakete gesendet und empfangen werden können (ca. 1500 Bytes).

#### /net/tcp

Bei TCP geht man ähnlich vor, nur dass man den Port an den Dateinamen anhängt. Eine Verbindung zum Webserver (Port 80) unter www.google.de (74.125.39.106) über eth0 sieht dann so aus:

\<c\>FILE \*tcpcon; tcpcon = fopen("/net/tcp/eth0:74.125.39.106:80", "r+")\</c\>

Hier kann man dann ebenso Daten empfangen ("fread") und senden ("fwrite") und natürlich auch die Verbindung beenden ("fclose").

#### Weitere /net-Dateisysteme

- /net/udp - Verbindung ähnlich wie bei /net/tcp, es können aber nur ganze Pakete empfangen/gesendet werden

## Aktuelle Features

- [Multibootkernel](Multiboot.md "Multiboot")
- Präemptives [Multitasking](Multitasking.md "Multitasking")
- Einfache StdCLib (myxlib) mit etwas [POSIX](POSIX.md "POSIX")
- Dateisystem: SMXFFS (Small MyXomycota Floppy FS), experimentell FAT32 (beide read-only); MRFS als VFS
- [AC'97](AC97.md "AC97")-Treiber (zumindest ICH)
- [Paging](Paging.md "Paging") (2 GB pro Prozess)
- [ELF](Executable-and-Linking-Format.md "ELF")-Programme
- [Netzwerkstack](Kategorie-Netzwerk.md "Kategorie:Netzwerk"): [Ethernet](Ethernet.md "Ethernet"), [ARP](Address-Resolution-Protocol.md "Address Resolution Protocol"), [IP](Internet-Protocol.md "Internet Protocol"), UDP, TCP
- CDI-Interfaces: core, fs, net, storage

## Wichtigste Programme

### Im offiziellen Release (0.004-pa-0)

- µsh: Die Shell
- FASM 1.67.26: Der Flatassembler
- Aargh: Interpreter für eine esoterische Programmiersprache
- Gnu Ed 1.2: Ein "Editor"
- MyXomycota Ed 0.01: schneller als Gnu Ed, dafür mit weitaus weniger Funktionen
- Brainfuck 0.1: Compiler
- Maumau: Mau-Mau spielen, Regeln unter "maumau --help" oder "/mnt/fda/home/Mau-Mau-Regeln.txt"; benutzt die libmaumau-0.3 (#lost am 22. März 2009)

### Noch "unter Verschluss"

- dig 0.001: Wandelt einen Hostnamen in eine IP-Adresse um
- myxirc: Ein (einfacher) IRC-Client
- ftp: Ein (kaputter) FTP-Client
- http: Lädt eine Datei via HTTP (maximal 64 kB)
- html: Zeigt ein bisschen was aus einer HTML-Datei an

## TODO

- TODO-Liste abarbeiten
- HD-Audio-Treiber
- Funktionierender FAT32-Treiber
- Schreibzugriff auf SMXFFS-Dateisysteme
- PipeFS fertigstellen
- Diskettentreiber
- StdCLib vervollständigen, POSIX-Kompatibilität stark verbessern
- sysenter-Unterstützung

## Syscalls (Auszug)

[Syscalls](Syscall.md "Syscall") geschehen über den Interrupt 0x80. Die Parameter werden in Registern übergeben, eax enthält die Funktionsnummer. An sich sind die Systemfunktionen für eine StdCLib und nicht für POSIX ausgelegt.

| Nummer (eax) | Funktion | Beschreibung |
| -------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00000000 | \<c\>FILE \*eax = fopen(const char \*ebx, const char \*esi)\</c\> | StdCLib (öffnet eine Datei) |
| 0x00000001 | \<c\>fclose(FILE \*edx)\</c\> | StdCLib (schließt eine Datei) |
| 0x00000002 | \<c\>size_t eax = fread(void \*edi, size_t ebx, size_t ecx, FILE \*edx)\</c\> | StdCLib (liest Daten aus einer Datei) |
| 0x00000003 | \<c\>size_t eax = fwrite(void \*esi, size_t ebx, size_t ecx, FILE \*edx)\</c\> | StdCLib (schreibt Daten in eine Datei) |
| 0x00000100 | \<c\>void \*eax = malloc(size_t ecx)\</c\> | StdCLib (reserviert einen Speicherbereich) |
| 0x00000101 | \<c\>free(void \*ebx)\</c\> | StdCLib (gibt einen Speicherbereich frei) |
| 0x00000200 | \<c\>exit(int edx)\</c\> | StdCLib (beendet das Programm) |
| 0x00000202 | \<c\>pid_t eax = exec(char \*ebx, char \*\*esi)\</c\> | Erstellt einen neuen Prozess und führt darin das Programm ebx mit der Parameterliste esi aus. |
| 0x0000020A | \<c\>sleep(int ecx)\</c\> | Legt den Prozess für (mindestens) ecx Millisekunden schlafen. |
| 0x00000300 | \<c\>int eax = mount(const char \*esi, const char \*edi, const char \*ebx)\</c\> | Hängt die Gerätedatei esi in den Ordner edi ein. ebx gibt das Dateisystem an, wenn ebx==NULL, dann wird versucht, ein passendes Dateisystem zu finden. |
| 0xFFFFFF00 | \<c\>int eax = rand()\</c\> | StdCLib (Liefert eine Zufallszahl) |
| 0xFFFFFFFF | \<c\>reboot()\</c\> | Startet das System neu, funktioniert nur, wenn der aufrufende Prozess zum Benutzer root gehört. |

Die ersten sechs Stellen der Hexfunktionsnummer (also Funktionsnummer&0xFFFFFF00) geben den Typ an: 0x000000xx sind Dateifunktionen, 0x000001xx sind Speicherfunktionen, 0x000002xx sind Prozessfunktionen, 0x000003xx sind Gerätefunktionen und 0xFFFFFFxx sind andere Funktionen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5672/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1861/index.html)

<!-- MediaWiki page 1861; revision 5672; parent 5290; 2009-08-19T20:11:13Z -->
