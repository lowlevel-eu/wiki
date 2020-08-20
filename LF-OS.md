# LF OS

| LF OS (LittleFox' Operating System) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [LittleFox](https://lowlevel-eu.github.io/wiki/pages/2674/index.html "Benutzerin:Littlefox") |
| Akt. Version: | \- |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | MIT |
| OS-Eigenschaften |  |
| Plattform: | [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++"), [Assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | aktuell POSIX via newlib, später asynchrone native API und newlib darauf portiert für Legacy Apps |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Vor allem shared memory und message passing |
| Homepage |  |

<https://praios.lf-net.org/littlefox/lf-os_amd64>

  
Seit über einem Jahrzehnt schreibe ich nun schon immer mal wieder an Betriebssystemen (meist LF OS). Seit etwa November 2018 schreibe ich mehr oder weniger regelmäßig (quasi jede Zugfahrt und inzwischen auch oft einfach so) an der aktuellsten Variante:

- amd64
- UEFI
- Microkernel

Der Plan ist, quasi alles in Userspace-Prozesse zu packen. Alle Prozesse können Dienste bereitstellen, diese werden im Kernel registriert. Andere Prozesse können sich dann Dienste erfragen und bekommen dann PID und Channel ID für IPC um mit dieser Instanz des Dienstes zu kommunizieren. Dienste sind z.B. Blockdevice-Treiber, FS-Treiber, Grafikserver, Terminals, ...

Wenn Dienste von Prozessen implementiert werden und diese Forken, werden die Dienste direkt als Standardimplementierung im fork verwendet. So kann ein Terminal-Emulator z.B. den Terminal Dienst implementieren und in eine Shell forken, die dann automatisch auf diesen Terminal Emulator rendert.

Bis das so weit läuft wirds aber wohl noch etwas dauern ... gerade funktioniert schon

- UEFI Loader
  - lädt Kernel und init
  - bereitet sinnvolle initiale Speichermappings vor
  - Holt Framebuffer vom UEFI für Konsole
- Kernel
  - physische Speicherverwaltung mit linked lists
  - virtuelle Speicherverwaltung unter Verwendung der Datenstrukturen die die CPU selbst verwendet
    - es gibt ein Mapping des gesamten physischen Speichers an eine virtuelle Adresse
    - Informationen wofür Pages verwendet werden ist aktuell in Arbeit
  - Scheduler
  - schönes Logging in den Arbeitsspeicher und COM1 (und auf die Konsole bis ein Prozess den Framebuffer übernimmt)
  - ein paar coole Datenstrukturen, ein paar Unit-Tests für diese
  - ein paar Syscalls - definiert in einer YAML Datei und automatisch zu C-Code gemacht (Kernel- und Userspace-seitig)
  - Anfänge von [pthreads](https://github.com/lowlevel-eu/wiki/wiki/POSIX-Threads "POSIX Threads") -\> aktuell aktivste Baustelle
- init
  - kann sich den Framebuffer holen und lustige Dinge rendern
  - forkt dabei, nutzt pthread_mutex zur synchronisation
- newlib, libc++, libc++abi, compiler-rt, [Clang](https://github.com/lowlevel-eu/wiki/wiki/Clang "Clang") mit LF OS Kenntnissen

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11512/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2267/index.html)

<!-- MediaWiki page 2267; revision 11512; parent 11493; 2020-08-20T14:09:55Z -->
