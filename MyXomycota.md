# MyXomycota

| MyXomycota |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | 0.004 (pre-alpha) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Gnu [GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") |
| OS-Eigenschaften |  |
| Plattform: | x86 |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Monolithischer Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#monolithischer-kernel "Monolithischer Kernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | Int 0x80 |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Keine (bis jetzt) |
| Homepage |  |

[Sourceforge](http://sourceforge.net/projects/myxomycota)

  
Der Name "MyXomycota" ist vom Namen der Schleimpilze (Myxomyceten) abgeleitet - das scheinen ziemlich kluge Dinger zu sein, auch wenn man es ihnen nicht zutraut. Es handelt sich bei diesem Betriebssystem um ein einfaches Hobbybetriebssystem, das im ProtectedMode läuft und über eine simple Kommandozeile verfügt.

## Entwickler

- [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic")

## Das Mountsystem

Herz des Systems sind das Mountsystem und das virtuelle Dateisystem. Dieses VFS läuft in einer zehn Megabyte großen RamDisk und sorgt für jegliche Kommunikation mit Geräten oder dem Kernel, wenn sie nicht über int 0x80 ablaufen muss. In ihm können hierzu virtuelle Dateien erstellt werden, die vom Mountsystem registriert werden. Solche Dateien können Geräte ("/dev/console", "/dev/pci/0-0-0", "/dev/audio"), Kommunikationskanäle zum Kernel ("/sys/mount") oder jegliche Art von Dateisystemen ("/proc", "/mnt/fda", "/mnt/addon", "/mnt/auto/hda1") sein. Ein Gerät wird im Kernel durch eine einfache Funktion repräsentiert, die ein paar Parameter bekommt (ID-Nummer, Position innerhalb der "Datei", Zugriffsart, Länge des Zugriffs, ...) und einen Wert zurückgeben kann. Eine Dateisystemfunktion erhält statt einer ID-Nummer das Handle der Datei, auf der sich das Dateisystem befindet. Daher kann man auch normale Dateien und nicht nur Gerätedateien mounten (z. B. "/dev/hda1" -\> "/mnt/auto/hda1", "/mnt/auto/hda1/floppy.img" -\> "/home", "/home/test.img" -\> "/tmp"; also auch über mehrere Dateisysteme hinweg). Wichtig ist, dass ein Dateisystem natürlich nicht wirklich physisch vorhanden sein muss: Von Relevanz ist lediglich, was die Funktion an das Mountsystem zurückgibt. Daher sind auch virtuelle Dateisysteme wie das procfs ("/proc") oder das pipefs ("/sys/pipe", noch in Arbeit) möglich. Das ProcFS beispielsweise zeigt Informationen zu allen Prozessen im System an, wobei pro Prozess eine Datei existiert. Die Informationen können mit dem Programm "top" ausgelesen werden.

## Aktuelle Features

- Multibootkernel
- Präemptives Multitasking
- Einfache StdCLib (myxlib) mit etwas POSIX
- Dateisystem: SMXFFS (Small MyXomycota Floppy FS), experimentell FAT32 (beide read-only); MRFS als VFS
- AC'97-Treiber (zumindest ICH)
- Paging (2 GB pro Prozess)
- ELF-Programme

## Wichtigste Programme

- µsh: Die Shell
- FASM 1.67.26: Der Flatassembler
- Aargh: Interpreter für eine esoterische Programmiersprache
- Gnu Ed 1.2: Ein "Editor"
- MyXomycota Ed 0.01: schneller als Gnu Ed, dafür mit weitaus weniger Funktionen
- Brainfuck 0.1: Compiler
- Maumau: Mau-Mau spielen, Regeln unter "maumau --help" oder "/mnt/fda/home/Mau-Mau-Regeln.txt"; benutzt die libmaumau-0.3 (#lost am 22. März 2009)

## TODO

- HD-Audio-Treiber
- Bei "großen" Festplatten funktionierender Festplattentreiber
- Funktionierender FAT32-Treiber
- Schreibzugriff auf SMXFFS-Dateisysteme
- PipeFS fertigstellen
- Diskettentreiber
- Treiber im Usermode laden können
- StdCLib vervollständigen, POSIX-Kompatibilität stark verbessern

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4493/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1861/index.html)

<!-- MediaWiki page 1861; revision 4493; parent 4492; 2009-06-27T08:57:41Z -->
