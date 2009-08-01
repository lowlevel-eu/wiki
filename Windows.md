# Windows

Windows ist ein kommerzielles Betriebssystem der Firma Microsoft, das auf einer sehr großen Anzahl von Privat-PCs zum Einsatz kommt. Es ist auf Bedienerfreundlichkeit ausgelegt. Als freie Alternative zu Windows gibt es [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS") .

| Windows |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Microsoft |
| Akt. Version: | NT 6.0 (= Vista) |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | Proprietär |
| OS-Eigenschaften |  |
| Plattform: | x86, x64 und Intel-MAC(BootCamp), ältere Versionen auch andere |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Makrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#makrokernel "Makrokernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | Unbekannt, da nicht Open-Source(vermutlich [C](https://github.com/lowlevel-eu/wiki/wiki/C "C")) |
| API: | WinAPI |
| Binärformat: | Portable Executable |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | Pipes, Shared Memory, RPC,... |
| Homepage |  |

[www.microsoft.com](http://www.microsoft.com/windows)

## OS-Dev unter Windows

### Pro

Für Leute, die noch nie mit Linux gearbeitet haben ist der Einstieg sicher etwas schwerer, vor allem wenn man gleich mit OS-Programmierung anfängt. Wer gewohnt ist, mit Windows zu arbeiten, der wird sich nicht bemühen, Bash oder Sonstiges zu lernen, wenn er mit \*.bat Dateien vertraut ist. So wird es Windows-Leuten wohl einfacher fallen, ihr eigenes Betriebssystem zu entwickeln. Und die Programme, die benötigt werden (Compiler,...) existieren mittlerweile auch schon für Windows und müssen nur mehr heruntergeladen werden. (Binutils, Crosscompiler, MingGW CygWin,...)

### Contra

Das wohl größte Argument gegen Windows als Entwicklerplattform für Betriebssysteme ist wohl, dass viele Programme erst heruntergeladen werden müssen, damit man mit dem Programmieren anfangen kann. (gcc, make, ...) Außerdem fehlen Windows noch ein paar Kommandozeilen-Programme, welche die OS-Programmierung erleichtern. (dd, ...) Sicherlich ist auch der Funktionsumfang von Batch-Dateien eher gering, was aber in diesem Einsatzgebiet wohl eher nicht so wichtig ist.  
  
Es gab über dieses Thema eine Diskussion, siehe [Diskussion:OS-Dev für Einsteiger](https://lowlevel-eu.github.io/wiki/pages/1654/index.html "Diskussion:OS-Dev für Einsteiger").

## Design

### NT-Linie

#### Kernel

Über das Design von Windows ist relativ wenig bekannt, da von Microsoft relativ wenig Informationen über Schnittstellen etc. offenlegt. Deshalb ist man sich auch nicht wirklich einig, was den [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") von Windows betrifft. Ursprünglich war Windows als [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel") geplant, bis Windows NT 3.1 war das auch so. Allerdings wurden dann aus Geschwindigkeitsgründen Teile der [GUI](https://github.com/lowlevel-eu/wiki/wiki/Graphical-User-Interface "GUI") als Ring-0 Applikationen ausgeführt, genauso wie andere Teile. (mittlerweile - in Vista - werden die Grafiktreiber wieder als Ring-3 Prozesse angesehen) Deshalb entspricht Windows nicht mehr den Kriterien von [Mikrokernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Mikrokernel")-Systemen. Daher wird Windows gemeinhin als Macrokernel betrachtet.

#### API

Bei der API wird unterschieden zwischen der "nativen NT-API", die teilweise undokumentiert ist (Syscalls, obwohl sich auch hier bereits einiges an Dokumentation zB in ReactOS findet), größtenteils durch das Treiberinterface (Windows WDK bzw DDK) jedoch sogar gut dokumentiert ist, und der WinAPI(kernel32.dll, user32.dll, gdi32.dll). Seit .NET gibt es nun auch eine dritte, objektorientierte Schicht, die über diese APIs gelegt ist, das .NET Framework. .NET Framework war ursprünglich nur eine "Weiterleitung" an die WinAPI, wurde dann aber später erweitert und von der WinAPI getrennt, sodass es mittlerweile nur mehr Managed Code ist, der unter einer Laufzeitumgebung in einer virtuellen Maschine läuft, die den Bytecode übersetzt.

## Siehe auch

- [Crosscompiler für Windows](https://github.com/lowlevel-eu/wiki/wiki/Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")
- [ReactOS](https://github.com/lowlevel-eu/wiki/wiki/ReactOS "ReactOS")

## Links

- [Windows NT-API für Treiber und Subsystems](http://msdn.microsoft.com/en-us/library/ms795146.aspx)
- [Undocumented Windows 2000 Secrets](http://www.rawol.com/?topic=77)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4957/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1558/index.html)

<!-- MediaWiki page 1558; revision 4957; parent 4956; 2009-08-01T13:29:35Z -->
