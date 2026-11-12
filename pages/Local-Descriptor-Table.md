# Local Descriptor Table

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Eine Local Descriptor Table ist genau so aufgebaut wie eine [Global Descriptor Table](Global-Descriptor-Table "Global Descriptor Table"), nur dass sie prozessspezifisch ist. Dadurch kann sie als eine Alternative zu [Paging](Paging "Paging") verwendet werden, um jedem Prozess seinen eigenen Speicherbereich zu geben. Eine LDT wird mit dem Befehl "lldt" geladen, wobei ein Selektor zu einem LDT-Deskriptor der GDT angegeben werden muss.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11477/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2014/index.html)

<!-- MediaWiki page 2014; revision 11477; parent 5403; 2020-08-02T23:44:28Z -->
