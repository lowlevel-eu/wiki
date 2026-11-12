# Physical Address Extension

**Löschhinweis:**

Dieser Artikel wurde zum Löschen vorgeschlagen.

Eigentlich nun alles in [Paging](Paging.md "Paging") eingepflegt denke ich -- [Littlefox](https://lowlevel-eu.github.io/wiki/pages/2674/index.html "Benutzerin:Littlefox") (Diskussion) 17:41, 8. Sep. 2020 (CEST)

  
Die **Physical Address Extension** (PAE) erweitert den physischen Adressraum auf 64 GiB. Das bedeutet, dass sich die physischen Adressen von 32 Bits auf 36 Bits und die Einträge in den [Page Tables](Paging.md "Paging") auf 64 Bits vergrößern. Damit sind nur noch 512 Einträge pro Page Table möglich. Page Directories erhalten ein Flag, das bei aktiviertem PAE ermöglicht, 2 MiB große Pages zu verwenden.

Außerdem wird die Page Directory Pointer Table (PDPT) als dritte Stufe in die Paging Hierarchie über die Page Directories eingeführt. Diese Tabelle enthält 4 Einträge, die auf Page Directories verweisen. Das Register [CR3](Control-Register.md#cr3 "Control Register") verweist bei aktiviertem PAE auf die PDPT.

## Siehe auch

Intel Manual - Volume 3A - Kapitel 3.8

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11515/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1982/index.html)

<!-- MediaWiki page 1982; revision 11515; parent 11478; 2020-09-08T15:41:13Z -->
