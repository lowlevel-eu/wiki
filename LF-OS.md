# LF OS

| LF OS (LittleFox' Operating System) |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [LittleFox](https://lowlevel-eu.github.io/wiki/pages/2674/index.html "Benutzerin:Littlefox") |
| Akt. Version: | \- |
| [Lizenz](Lizenzen "Lizenzen"): | MIT |
| OS-Eigenschaften |  |
| Plattform: | [x86-64](X86-64 "X86-64") |
| [Kernelart](Kernel "Kernel"): | Microkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](C "C"), [C++](C%2B%2B "C++"), [Assembler](Assembler "Assembler") |
| API: | aktuell POSIX via newlib, später asynchrone native API und newlib darauf portiert für Legacy Apps |
| Binärformat: | [ELF](Executable-and-Linking-Format "ELF") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Vor allem shared memory und message passing |
| Homepage |  |

 

- [Eigenes Gitlab mit CI und Issues](https://praios.lf-net.org/littlefox/lf-os_amd64)
- [GitHub Mirror (nur master Branch)](https://github.com/LittleFox94/lf-os_amd64)
- [Doku auf Gitlab Pages](https://littlefox.narf.press/lf-os_amd64)

  
Seit über einem Jahrzehnt schreibe ich nun schon immer mal wieder an Betriebssystemen (meist LF OS). Seit etwa November 2018 schreibe ich mehr oder weniger regelmäßig (quasi jede Zugfahrt und inzwischen auch oft einfach so) an der aktuellsten Variante:

- amd64
- UEFI
- Microkernel

Der Plan ist, quasi alles in Userspace-Prozesse zu packen. Alle Prozesse können Dienste bereitstellen, diese werden im Kernel registriert. Andere Prozesse können sich dann Dienste erfragen und bekommen dann Informationen für IPC um mit diesem Dienstes zu kommunizieren. Dienste sind z.B. Blockdevice-Treiber, FS-Treiber, Grafikserver, Terminals, ...

Welche Implementierung standardmäßig verwendet werden soll, lässt sich von Prozessen konfigurieren und bei `fork()` vererben, dadurch ergibt sich eine Art "Dependency Injection". Darüber lässt sich z.B. `chroot()` abbilden (anderen FS Dienst als Standard setzen), der Compositor stellt selber wieder einen Grafikserver bereit pro Fenster (in dem ein weiterer Compositor laufen kann..), ein Outbound-Firewall Dienst ist auch nur eine Implementierung von *Netzwerkinterface-Dienst* .. so die Idee.

## Was funktioniert bereits

- UEFI Loader
  - lädt Kernel und init
  - bereitet sinnvolle initiale Speichermappings vor und holt memory map von der Firmware
  - bereitet framebuffer für Konsole vor (UEFI GraphicsOutputProtocol)
- Kernel
  - physische Speicherverwaltung mit linked lists
  - virtuelle Speicherverwaltung (nutzt aktuell einfach die Paging-Strukturen, braucht noch mehr Infos für Copy-on-Write Referenzzähler z.B.)
    - es gibt ein Mapping des gesamten physischen Speichers an eine virtuelle Adresse
      - dabei wird sogar ausgewählt ob 2MB oder 1GB Pages sinnvoller sind
  - Scheduler
  - schönes Logging in den Arbeitsspeicher und COM1 (und auf die Framebuffer-Konsole bis ein Prozess den Framebuffer übernimmt)
  - ein paar coole Datenstrukturen, ein paar Unit-Tests für diese
  - ein paar Syscalls - definiert in einer YAML Datei aus der automatisch C-Code generiert wird (Kernel- und Userspace-seitig)
  - genug [ELF](Executable-and-Linking-Format "ELF") Loader für Binaries die LLD ausspuckt (Segmente sind Page-aligned aber irgendwie auch nicht)
  - Panic screen mit Stacktrace (sogar mit Kernel Debug-Symbolen!)
  - Faults werden größtenteils dem Prozess zugeschoben, manche Page-Faults sogar sinnvoll behandelt (Stack)
  - Anfänge von [pthreads](POSIX-Threads "POSIX Threads") -\> aktuell aktivste Baustelle
- init
  - kann sich den Framebuffer holen und lustige Dinge rendern
  - forkt dabei, nutzt pthread_mutex zur synchronisation
- newlib, libc++, libc++abi, compiler-rt, [Clang](Clang "Clang") mit LF OS Kenntnissen
- [Doom](https://twitter.com/0x0a_fox/status/1386095877165551616)
- Bisschen Code der einigermaßen sinnvoll ist und sogar als Referenz hier im Wiki geeignet ist (und teilweise verlinkt)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11529/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2267/index.html)

<!-- MediaWiki page 2267; revision 11529; parent 11518; 2021-04-25T04:20:21Z -->
