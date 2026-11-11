# Windows

| Windows |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | Microsoft |
| Akt. Version: | NT 6.2 (= 8) |
| [Lizenz](Lizenzen "Lizenzen"): | Proprietär |
| OS-Eigenschaften |  |
| Plattform: | [x86](X86 "X86"), [x64](X86-64 "X64"), [ARM](ARM "ARM") (Windows RT-Versionen), früher Alpha (NT 4) |
| [Kernelart](Kernel "Kernel"): | [Makrokernel](Kernel#makrokernel "Makrokernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | C |
| API: | WinAPI |
| Binärformat: | [PE](Microsoft-Portable-Executable-and-Common-Object-File-Format "PE") |
| [IPC-Methode](Interprozesskommunikation "IPC"): | Pipes, Shared Memory, RPC,... |
| Homepage |  |

[www.microsoft.com](http://www.microsoft.com/windows)

Windows ist ein kommerzielles Betriebssystem der Firma Microsoft, das auf einer sehr großen Anzahl von Privat-PCs zum Einsatz kommt. Es ist auf einfache Bedienung ausgelegt.

  

## Design

### NT-Linie

Windows NT, oder besser gesagt der NT-Kernel, wird in allen neuen Betriebssystemen von Microsoft eingesetzt. Der Name bedeutete anfangs N-Ten. Das war der Name der Prozessorarchitektur, für die NT anfangs entwickelt wurde. Der Name wurde später als ein Backronym auf *New Technology* umgedeutet. Mit dem NT-Kernel wollte Microsoft neben der Windows 9x-Linie (welche auf MS-DOS basierte) einen stabilen und sicheren Microkernel entwickeln.

#### Kernel

Über das Design von Windows ist relativ wenig bekannt, da Microsoft relativ wenig Informationen über Schnittstellen etc. offenlegt. Deshalb ist man sich auch nicht wirklich einig, was den [Kernel](Kernel "Kernel") von Windows betrifft. Ursprünglich war Windows als [Mikrokernel](Kernel#mikrokernel "Mikrokernel") geplant, bis Windows NT 3.1 war das auch so. Allerdings wurden dann aus Geschwindigkeitsgründen Teile der [GUI](Graphical-User-Interface "GUI") als Ring-0-Applikationen ausgeführt, genauso wie andere Teile (seit Vista werden die Grafiktreiber wieder als Ring-3-Prozesse angesehen). Deshalb entspricht Windows nicht mehr den Kriterien von [Mikrokernel](Kernel#mikrokernel "Mikrokernel")-Systemen. Daher wird Windows gemeinhin als [Makrokernel](Kernel#makrokernel "Makrokernel") betrachtet.

#### API

Bei der API wird unterschieden zwischen der „nativen NT-API“, die teilweise undokumentiert ist (Syscalls, obwohl sich auch hier bereits einiges an Dokumentation z. B. in ReactOS findet), größtenteils durch das Treiberinterface (Windows WDK bzw. DDK) jedoch sogar gut dokumentiert ist, und der WinAPI (kernel32.dll, user32.dll, gdi32.dll). Seit .NET gibt es nun auch eine dritte, objektorientierte Schicht, die über diese APIs gelegt ist, nämlich das .NET-Framework. Das .NET-Framework war ursprünglich nur eine „Weiterleitung“ an die WinAPI, wurde dann aber später erweitert und von der WinAPI getrennt, sodass es mittlerweile nur mehr sogenannter *Managed Code* ist, der unter einer Laufzeitumgebung in einer virtuellen Maschine läuft, die den Bytecode übersetzt.

## Siehe auch

- [Crosscompiler für Windows](Crosscompiler-f%C3%BCr-Windows "Crosscompiler für Windows")
- [ReactOS](ReactOS "ReactOS")

## Links

- [Windows NT-API für Treiber und Subsystems](http://msdn.microsoft.com/en-us/library/ms795146.aspx)
- [Undocumented Windows 2000 Secrets](http://www.rawol.com/?topic=77)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10933/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1558/index.html)

<!-- MediaWiki page 1558; revision 10933; parent 10931; 2012-11-04T16:03:28Z -->
