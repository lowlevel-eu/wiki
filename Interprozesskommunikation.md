# Interprozesskommunikation

Als **Interprozesskommunikation** (**IPC**, engl. **inter-process communication**) bezeichnet man den Datenaustausch und die Synchronisation zwischen mehreren Prozessen. Da Prozesse normalerweise in unterschiedlichen Adressräumen laufen und eigene Kopien der Prozessorregister besitzen, kann dieser Datenaustausch so ohne Weiteres nicht über den Hauptspeicher oder die Prozessorregister geschehen. Vor allem in einem [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist dieser Datenaustausch essentiell, da jeder Treiber ein eigener Prozess ist und natürlich normale Anwendungen mit dem Treiber kommunizieren müssen, um beispielsweise Tastatureingaben zu erhalten oder um vom Dateisystem zu lesen.

## Message passing

## Message Queues

## RPC (=Remote procedure call)

## Shared-memory

Der Begriff **shared-Memory** bezeichnet einen Speicherbereich, welcher in mehreren Adressräumen gleichzeitig eingeblendet ist, d.h. es können mehrere Prozesse prinzipiell gleichzeitig auf den gleichen physischen Speicher zugreifen. Da der Zugriff gleichzeitig sein kann, muss der Zugriff bei mehreren schreibenden Prozessen synchronisiert werden. Dies kann über Semaphoren/Spinlocks/Mutexe oder über eine zweite Form der Interprozesskommunikation (beispielsweise Messages) erreicht werden. Zu beachten ist, dass generell keine Zeiger/Referenzen (und damit beispielsweise auch C++ Klassen welche Teil einer Klassenhierarchie sind) über den *shared-memory* übergeben werden sollten, da Zeiger nur innerhalb eines Adressraums gültig sind bzw. auf das gleiche Objekt verweisen. Ein einzelner *shared-memory*-Bereich ist auch nicht zwingend an der gleichen virtuellen Adresse in allen Prozessen.

## Pipes

## Semaphore

## Monitore

## Event Groups

## Links

- [Forumsthread über die Implementation von RPC](http://lowlevel.brainsware.org/forum/index.php?topic=1787.0)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2817/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1530/index.html)

<!-- MediaWiki page 1530; revision 2817; parent 2816; 2008-03-25T03:19:31Z -->
