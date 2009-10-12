# Page Size Extension

Dieses Feature von [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")-Prozessoren wurde mit dem Pentium-Prozessor eingeführt. Es ermöglicht [Paging](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") mit Pages, die größer als 4 kB sind - nämlich 4 MB. Dadurch wird weniger Speicherplatz für Page Tables verbraucht und außerdem kann der Translation Lookaside Buffer besser arbeiten, da es weniger Pages gibt. Außerdem können, wenn PSE aktiviert ist, gleichzeitig 4-kB- und 4-MB-Pages verwendet werden.

Ein großer Nachteil ist, dass eine 4-MB-Page einfach auch 4 MB Speicher benötigt. Wird z. B. nur ein Megabyte benötigt, dann werden drei Megabyte verschwendet. PSE kann im [Long Mode](https://github.com/lowlevel-eu/wiki/wiki/Long-Mode "Long Mode") nicht verwendet werden, da dort automatisch [PAE](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "PAE") genutzt wird.

## Funktionsweise

Um PSE zu aktivieren, muss das Bit 4 (PSE) im [Kontrollregister](https://github.com/lowlevel-eu/wiki/wiki/Control-Register "Control Register") CR4 gesetzt werden. Anschließend wird das Bit 7 (S-Bit) im [Page Directory](https://github.com/lowlevel-eu/wiki/wiki/Paging "Paging") gültig. Ist es nicht gesetzt, so zeigt der jeweilige Eintrag auf eine Page Table, welche wiederum 4-kB-Pages enthält, ist es gesetzt, so zeigt er direkt auf eine 4-MB-Page.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6024/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1999/index.html)

<!-- MediaWiki page 1999; revision 6024; parent 5450; 2009-10-12T17:28:47Z -->
