# Týndur/Interprozesskommunikation

Dieser Artikel bezieht sich ausschließlich auf die Interprozesskommunikation unter [LOST](Kategorie-T%C3%BDndur.md "Kategorie:Týndur"). Eine allgemeingültige Erklärung findet sich unter [Interprozesskommunikation](Interprozesskommunikation.md "Interprozesskommunikation").

## Kernelseitiges RPC

Zwei der verbreitetsten Möglichkeiten, IPC zu implementieren, sind über Nachrichten (Message Queues) oder über Funktionsaufrufe in den fremden Prozess (Remote Procedure Call, RPC). Während nachrichtenbasierte IPC oft asynchron ist (der Absender läuft weiter sobald die Nachricht gesendet ist, ohne darauf zu warten, dass die Nachricht verarbeitet wurde) und RPC oft synchron ist (der Aufrufer wartet auf einen Rückgabewert des aufgerufenen Prozesses), benutzt LOST asynchrones RPC.

Umgesetzt wird dieses Konzept durch folgende Syscalls:

- SYSCALL_ADD_INTERRUPT_HANDLER (Interrupts werden als RPC-Aufrufe vom Kernel realisiert)
- SYSCALL_SET_RPC_HANDLER
- SYSCALL_RPC

## Sychrones RPC im Userspace

## Asynchrones RPC im Userspace

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/6725/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1500/index.html)

<!-- MediaWiki page 1500; revision 6725; parent 5597; 2010-01-02T17:42:32Z -->
