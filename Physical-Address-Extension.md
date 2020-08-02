# Physical Address Extension

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Die **Physical Address Extension** (PAE) erweitert den physischen Adressraum auf 64 GiB. Das bedeutet, dass sich die physischen Adressen von 32 Bits auf 36 Bits und die Einträge in den [Page Tables](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") auf 64 Bits vergrößern. Damit sind nur noch 512 Einträge pro Page Table möglich. Page Directories erhalten ein Flag, das bei aktiviertem PAE ermöglicht, 2 MiB große Pages zu verwenden.

Außerdem wird die Page Directory Pointer Table (PDPT) als dritte Stufe in die Paging Hierarchie über die Page Directories eingeführt. Diese Tabelle enthält 4 Einträge, die auf Page Directories verweisen. Das Register [CR3](https://github.com/lowlevel-eu/wiki/wiki/Control-Register#cr3 "Control Register") verweist bei aktiviertem PAE auf die PDPT.

## Siehe auch

Intel Manual - Volume 3A - Kapitel 3.8

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11478/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1982/index.html)

<!-- MediaWiki page 1982; revision 11478; parent 9988; 2020-08-02T23:45:45Z -->
