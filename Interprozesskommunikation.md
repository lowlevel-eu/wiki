# Interprozesskommunikation

Als Interprozesskommunikation (IPC, engl. inter-process communication) bezeichnet man den Datenaustausch zwischen zwei Prozessen. Da Prozesse normalerweise in unterschiedlichen Adressräumen laufen und eigene Kopien der Prozessorregister besitzen, kann dieser Datenaustausch so ohne Weiteres nicht über den Hauptspeicher oder die Prozessorregister geschehen. Vor allem in einem [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") ist dieser Datenaustausch essentiell, da jeder Treiber ein eigener Prozess ist und natürlich normale Anwendungen mit dem Treiber kommunizieren müssen, um beispielsweise Tastatureingaben zu erhalten oder um vom Dateisystem zu lesen.

# Message passing

# RPC (=Remote procedure call)

# Shared-memory

# Links

- \[[Forumsthread über die Implementation von RPC](http://lowlevel.brainsware.org/forum/index.php?topic=1787.0)\]

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1984/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1530/index.html)

<!-- MediaWiki page 1530; revision 1984; parent 0; 2007-05-10T18:49:14Z -->
