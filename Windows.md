# Windows

Windows ist ein kommerzielles Betriebsystem der Firma Microsoft, das auf einer sehr großen Anzahl von Privat-PCs zum Einsatz kommt. Es ist auf Bedienerfreundlichkeit ausgelegt. Es gibt einen "Windows Klon" - [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS"). Das Open Source Projekt versucht eine komplette Windows Nachbildung zu schaffen, auf der mittlerweile auch schon eineige Programme gut und stabil laufen.

| Windows |  |
| ----------------------------------------------------------------------------------------------------- | ---------------------------------- |
|  |  |
| Entwickler: | Microsoft |
| Akt. Version: | NT 6.0 (=Vista) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Proprietär |
| OS-Eigenschaften |  |
| Plattform: | x86, x64 und Intel-MAC(BootCamp) |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybrid Kernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): |  |
| API: | WinAPI |
| Binärformat: | Portable Exuctable |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Pipes, Shared Memory, RPC,... |
| Homepage |  |

[www.microsoft.com](http://www.microsoft.com/windows)

## OS-Dev unter Windows

### Pro

Für Leute die noch nie mit Linux gearbeitet haben ist der Einstieg sicher etwas schwerer, vor allem wenn man gleich mit OS-Programmierung anfängt. Wer gewohnt ist mit Windows zu arbeiten der wird sich nicht bemühen bash oder Sonstiges zu lernen, wenn er mit \*.bat Dateien vertraut ist. So wird es Windows-Leuten wohl einfacher fallen ihr eigenes Betriebssystem zu entwickeln. Und die Programme, die benötigt werden (Compiler,...) existieren mittlerweile auch schon für Windows und müssen nur mehr heruntergeladen werden. (Binutils, Crosscompiler, MingGW CygWin,...)

### Contra

Das wohl größte Argument gegen Windows als Entwicklerplattform für Betriebssysteme ist wohl, dass viele Programme erst heruntergeladen werden müssen, damit man mit dem Programmieren anfangen kann. (gcc, make, ...) Außerdem fehlen Windows noch ein paar Kommandozeilen-Programme, welche die OS-Programmierung erleichtern. (dd, ...) Sicherlich ist auch der Funktionsumfang von Batch-Dateien eher gering, was aber in diesem Einsatzgebiet wohl eher nicht so wichtig ist.

## Design

### Kernel

Über das Design von Windows (ich beziehe mich hier ausschließlich auf die Windows NT Linie) ist relativ wenig bekannt, da von Microsoft relativ wenig Informationen über Schnittstellen etc. offenlegt. Deshalb ist man sich auch nicht wirklich einig, was den Kernel von Windows betrifft. Ursprünglich war Windows als Mikrokernel geplant, bis Windows NT 3.1 war das auch so. Allerdings wurden dann aus Geschwindigkeitsgründen Teile der GUI als Ring-0 Applikationen ausgeführt, genauso wie andere Teile. (mittlerweile - in Vista - werden die Grafiktreiber wieder als Ring-3 Prozesse angesehen) Deshalb entspricht Windows nicht mehr den Kriterien von Mikrokernel-Systemen. Daher wird Windows gemeinhin als Hybridkernel betrachtet.

### API

Bei der API wird unterschieden zwischen der "nativen NT-API", die undokumentiert ist, und der WinAPI(kernel32.dll, user32.dll, gdi32.dll). Seit .NET gibt es nun auch eine dritte, objektorientierte Schicht, die über diese APIs gelegt ist, das .NET Framework. .NET Framework war usrprünglich nur eine "Weiterleitung" an die WinAPI, wurde dann aber später erweitert und von der WinAPI getrennt, sodass es mittlerweile nur mehr Managed Code ist, der unter einer Laufzeitumgebung in einer virtuellen Maschine läuft, die den Bytecode übersetzt.

## Links

- [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")
- [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS") - OpenSource Windows Clone
- [Undocumented Windows 2000 Secrets](http://www.rawol.com/?topic=77)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2891/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1558/index.html)

<!-- MediaWiki page 1558; revision 2891; parent 2878; 2008-04-05T15:34:04Z -->
