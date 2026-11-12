# Hyper-V

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

| Allgemeines |  |
| ------------------------ | ------------------------------------- |
| Name: | Hyper-V |
| Entwickler: | Microsoft |
| Akt. Version: | R2<br>(Stand 24.08.2010) |
| Lizenz: | Proprietär |
| Betriebssystem(e): | Windows Server 2008 (R2), Windows 8 |
| Virtualisiertes System |  |
| Plattform: | x86, x86-64, IA64 |
| SMP: | bis zu vier Prozessoren pro VM |
| Mechanismus: | Hypervisor |
| Homepage |  |

<http://www.microsoft.com/germany/windowsserver2008/virtualisierung.mspx>

**Hyper-V** ist eine Virtualisierungslösung von Microsoft. Hyper-V ist kostenlos für das Server-Betriebssystem Windows Server 2008 als Download verfügbar (ab der Version R2 im Betriebssystem direkt integriert).

Für (Hobby-)Betriebssystementwickler ist Hyper-V aktuell nur bedingt interessant, da wohl die wenigsten Hobbyisten einen legal lizensierten [Windows](Windows.md "Windows") Server bei sich installiert haben. Allerdings wird mit der nächsten Version von Windows - "Windows 8" - Hyper-V auch für den Privatanwender interessant, da es dann Bestandteil des "normalen" Betriebssystem wird und voraussichtlich Windows Virtual PC ablösen wird.

  

## Mechanismus

Hyper-V wandelt das "Hauptbetriebssystem" ebenfalls zu einer VM um die in einer "Parentpartition" auf dem Hypervisor selbst läuft. Neue virtuelle Maschinen sind dann "Childpartitionen" die nicht auf die Hardware direkt sondern auf die virtualisierten Ressourcen zugreift (durch "Pass Through" können diese aber auch direkt auf die Hardware zugreifen).

  

## Linux und Hyper-V

Nachdem lange Zeit [Linux](Linux.md "Linux") nur sehr schlecht unter Hyper-V unterstützt wurde hat Microsoft einiges dafür getan, dass die Linux-Unterstützung verbessert wird und unter anderem eigene GPL-lizensierte Module zum Linux-Kernel beigesteuert.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11230/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2529/index.html)

<!-- MediaWiki page 2529; revision 11230; parent 10450; 2014-12-13T01:15:18Z -->
