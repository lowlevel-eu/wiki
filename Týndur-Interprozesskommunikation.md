# Týndur/Interprozesskommunikation

Als [Interprozesskommunikation](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "Interprozesskommunikation") (IPC) bezeichnet man den Datenaustausch zwischen unterschiedlichen Prozessen, die grundsätzlich getrennte Adressräume besitzen. Gerade für ein Microkernelsystem ist die IPC ein zentrales Merkmal, das dem System überhaupt erst erlaubt, sinnvolle Dinge -- Programme müssen beispielsweise auf einen Tastaturtreiber-Prozess zugreifen können, da ein solcher Treiber nicht in einem Microkernel enthalten ist.

## Kernelseitiges RPC

Zwei der verbreitetsten Möglichkeiten, IPC zu implementieren, sind über Nachrichten (Message Queues) oder über Funktionsaufrufe in den fremden Prozess (Remote Procedure Call, RPC). Während nachrichtenbasierte IPC oft asynchron ist (der Absender läuft weiter sobald die Nachricht gesendet ist, ohne darauf zu warten, dass die Nachricht verarbeitet wurde) und RPC oft synchron ist (der Aufrufer wartet auf einen Rückgabewert des aufgerufenen Prozesses), benutzt LOST asynchrones RPC.

Umgesetzt wird dieses Konzept durch folgende Syscalls:

- SYSCALL_ADD_INTERRUPT_HANDLER (Interrupts werden als RPC-Aufrufe vom Kernel realisiert)
- SYSCALL_SET_RPC_HANDLER
- SYSCALL_RPC

## Sychrones RPC im Userspace

## Asynchrones RPC im Userspace

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1843/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1500/index.html)

<!-- MediaWiki page 1500; revision 1843; parent 0; 2007-03-09T15:49:19Z -->
