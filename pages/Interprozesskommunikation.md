# Interprozesskommunikation

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Als **Interprozesskommunikation** (**IPC**, engl. **inter-process communication**) bezeichnet man den Datenaustausch und die Synchronisation zwischen mehreren Prozessen. Da Prozesse normalerweise in unterschiedlichen Adressräumen laufen und eigene Kopien der Prozessorregister besitzen, kann dieser Datenaustausch so ohne Weiteres nicht über den Hauptspeicher oder die Prozessorregister geschehen. Vor allem in einem [Microkernel](Kernel "Kernel") ist dieser Datenaustausch essentiell, da jeder Treiber ein eigener Prozess ist und natürlich normale Anwendungen mit dem Treiber kommunizieren müssen, um beispielsweise Tastatureingaben zu erhalten oder um vom Dateisystem zu lesen.

## Message Passing

Beim Message Passing werden Nachrichten direkt zwischen zwei Prozessen versendet. Dies erfolgt meist mit einer Adressierung mithilfe der PID oder einer Portnummer.

## Message Queues

Message Queues sind abgeschottete Nachrichtenräume. Jeder Prozess der einer MessageQueue angehört, kann Nachrichten in sie hinein schreiben oder Nachrichten aus ihr heraus lesen.

## RPC (=Remote procedure call)

Bei RPC werden Funktionen zwischen Prozessen geteilt, d.h ein Prozess kann Funktionen zur Verfügung stellen, die dann ein anderer Prozess in Anspruch nimmt. Das RPC-System sollte dabei die Übertragung von Parametern und Rückgabewerten übernehmen.

## Shared-memory

Der Begriff **shared-Memory** bezeichnet einen Speicherbereich, welcher in mehreren Adressräumen gleichzeitig eingeblendet ist, d.h. es können mehrere Prozesse prinzipiell gleichzeitig auf den gleichen physischen Speicher zugreifen. Da der Zugriff gleichzeitig sein kann, muss der Zugriff bei mehreren schreibenden Prozessen synchronisiert werden. Dies kann über Semaphoren/Spinlocks/Mutexe oder über eine zweite Form der Interprozesskommunikation (beispielsweise Messages) erreicht werden. Zu beachten ist, dass generell keine Zeiger/Referenzen (und damit beispielsweise auch C++ Klassen welche Teil einer Klassenhierarchie sind) über den *shared-memory* übergeben werden sollten, da Zeiger nur innerhalb eines Adressraums gültig sind bzw. auf das gleiche Objekt verweisen. Ein einzelner *shared-memory*-Bereich ist auch nicht zwingend an der gleichen virtuellen Adresse in allen Prozessen.

## Pipes

*Hauptartikel: [Pipe](Pipe "Pipe")*

Es gibt 2 Arten Pipes:

- **Unbenannte:** Unbenannte Pipes werden normalerweise zur Kommunikation von Vater- zu Kind-Prozess genutzt. Dabei werden die Daten, die von dem Kind-Prozess auf die Ausgabe geschrieben werden, von dem Vater-Prozess als Eingabe gelesen.
- **Benannte:** Benannte Pipes sind ein Dateityp. Sie können mittels Fileopen/Fileclose geöffnet und geschlossen werden und mit Fileread/Filewrite kann von ihnen gelesen werden, bzw. auf sie geschrieben werden.

## Semaphore

Semaphore dienen nicht direkt zur Informationsübertragung, sie dienen viel mehr zum Exklusiven Zugriff auf spezielle Resourcen.

## Monitore

## Event Groups

## Links

- [Forumsthread über die Implementation von RPC](https://lowlevel-eu.github.io/forum/topics/1787/index.html)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11476/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1530/index.html)

<!-- MediaWiki page 1530; revision 11476; parent 11475; 2020-08-02T23:43:36Z -->
