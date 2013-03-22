# Μxoµcota

| µxoµcota |  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  |  |
| Entwickler: | [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") |
| Akt. Version: | — |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | GNU [GPL](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "GPL") / BSD ([CDI](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "CDI")-Treiber) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | [Microkernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel#mikrokernel "Microkernel") |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C") |
| API: | Nativ mit POSIX-Wrappern (Paloxena3.5-API) |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | RPC über Popupthreads mit SHM und Message Passing |
| Homepage |  |

[Github](https://github.com/XanClic/muxomucota)

  
*Hinweis:* Der korrekte Titel dieses Artikels lautet „*µxoµcota*“. Diese Schreibweise ist aufgrund technischer Einschränkungen nicht möglich.

µxoµcota (auch myxomycota oder muxomucota) ist [mein](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") erster Versuch an einem Microkernel. Der Name leitet sich von meinem früheren OS [MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota") ab, die „µ“s sind eine unauffällige Anspielung an das „Micro“ im Microkernel.

## IPC

Zur IPC werden Popupthreads verwendet, die entweder asynchron oder synchron (über waitpid) abgesetzt werden können. Jeder Popupthread erhält als Parameter einen Integer (eine Funktionsnummer) und ggf. eine SHM-ID. Zusätzlich kann der Aufrufer eine Nachricht übergeben, die vom Kernel zwischengespeichert wird und vom Popupthread über einen Syscall abgerufen werden kann.

## VFS

Das VFS entspricht aus Nutzersicht fast exakt dem von Paloxena3.5 und Paloxena4, es handelt sich also um ein sehr POSIX-ähnliches VFS mit zu open, close, read und write analogen Funktionen sowie einigen ioctl-artigen Funktionen: Bei diesen Funktionen besitzt eine Datei (eine Pipe) verschiedene Flags, denen Werte zugewiesen oder deren Werte ausgelesen werden können (bspw. Länge der Datei oder Position darin). Es gibt vier Flags, die von jeder Pipe unterstützt werden müssen (F_PRESSURE (auszulesen; verbleibende noch zu lesende Bytes), F_READABLE/F_WRITABLE (auszulesen; es kann gelesen/geschrieben werden) und F_FLUSH (zu setzen; wenn auf 0 gesetzt, soll der Pipeinhalt tatsächlich geschrieben werden (fflush), sonst je nach Pipeart unterschiedliche Funktion)), weitere Flags werden je nach Pipeart unterstützt. Diese Pipearten heißen „Interfaces“ und mit einer bestimmten Funktion kann überprüft werden, ob der Treiber hinter einer bestimmten Pipe ein bestimmtes Interface für diese Pipe implementiert. Einige Beispiele sind:

- I_FILE: Eine Datei, dazugehörige Flags sind F_POSITION und F_FILESIZE.
- I_STATABLE: Es können Informationen für stat ausgelesen werden (bspw. F_GID, F_ATIME oder F_MODE).
- I_SIGNAL: Unter bestimmten Konditionen (bspw. es sind Daten verfügbar) kann diese Pipe ein Signal im Aufruferprozess auslösen (also einen Popupthread erstellen), wenn dies über Setzen von F_SIGNAL auf 1 so gewünscht wird.
- I_ETHERNET, I_IP, I_UDP, I_TCP: Sollte offensichtlich sein.

Das VFS operiert vollständig im Userspace und beinahe vollkommen dezentral. Einzige zentrale Anlaufstelle ist der Service „(root)“, der für alle Pfade Verwendung findet, die nicht mit einem Servicenamen beginnen: Jeder absolute Pfad beginnt mit einem Servicenamen, dabei kann zwischen „(service)/pfad“ und „service://pfad“ gewählt werden. Der Serviceteil ist dabei Name eines Prozesses, der sich zum Service erklärt haben muss. Relative Pfade werden wie unter POSIX üblich zu absoluten Pfaden erweitert, indem das Arbeitsverzeichnis (welches ein absoluter Pfad sein sollte) an den Anfang gehangen wird. Beginnt der entstehende absolute Pfad nicht mit einem Servicenamen, so wird „root“ als Service verwendet (also praktisch „(root)“ vor den Pfad gehangen). Beispielhaft seien die Vorgänge beim Öffnen von „dev/null“ gezeigt, während das Arbeitsverzeichnis „/“ ist:

- create_pipe("dev/null", …)
- Zuerst wird „dev/null“ mit dem Arbeitsverzeichnis zu „/dev/null“ erweitert.
- „/dev/null“ wiederum wird zu „(root)/dev/null“ erweitert.
- Im root-Prozess wird service_create_pipe("/dev/null", …) aufgerufen. Dieser gibt 0 zurück, kann die Datei also nicht öffnen.
- Im Aufrufer wird nun überprüft, ob diese Datei evtl. ein Symlink ist.
- Im root-Prozess wird service_is_symlink("/dev/null", …) aufgerufen. Dieser findet „/dev“ in einer Liste von „Mountpoints“ und stellt fest, dass dies ein Symlink auf „(devfs)/null“ ist.
- Im Aufrufer wird rekursiv create_pipe("(devfs)/null", …) aufgerufen.
- Im devfs-Prozess wird service_create_pipe("/null", …) aufgerufen. Auch hier existiert die Datei nicht direkt, also wird 0 zurückgegeben.
- Auch hier überprüft der Aufrufer wieder, ob die Datei ein Symlink ist.
- Im devfs-Prozess wird service_is_symlink("/null", …) aufgerufen. Tatsächlich ist auch dies wieder ein Symlink, und zwar auf „(thingamabob)/null“.
- Im Aufrufer wird wieder rekursiv create_pipe("(thingamabob)/null", …) aufgerufen.
- Im thingamabob-Prozess wird service_create_pipe("/null", …) aufgerufen, diesmal existiert die Datei und es wird eine ID ungleich 0 zurückgegeben.
- Im Aufrufer speichert create_pipe diese ID zusammen mit der Prozess-ID von thingamabob in einem Array und gibt den Index des Eintrags als Pipe-ID zurück.

Die Symlinkimplementierung ist vielleicht nicht die schönste ihrer Art, aber zumindest funktioniert sie soweit.

All diese VFS-Funktionen laufen transparent über die IPC-Funktionen ab. Der Aufrufer erzeugt für alle VFS-Funktionen kurze Nachrichtenblöcke, die über Message Passing an Popupthreads im Aufrufer weitergegeben werden, sowie für einige (read/write bzw. stream_recv/stream_send) auch SHM-Bereiche, über die größere Datenmengen ausgetauscht werden können. Auf Empfängerseite lesen Bibliotheksfunktionen die Informationen aus den Nachrichtenblöcken wieder aus und geben sie an vom Service bereitgestellte Funktionen wie „service_create_pipe“ weiter, deren Interface beinahe exakt denen der Aufruferfunktionen (wie „create_pipe“) entspricht. Zur VFS-Benutzung ist die Benutzung der IPC-Funktionen also prinzipiell nicht nötig.

Die praktisch absolute Dezentralität hat den Vorteil einer funktionierenden fork-Implementierung (wobei jeder Prozess die von ihm gehaltenen Pipe-IDs im Userspace selbst duplizieren muss (dafür existiert eine „duplicate_pipe“-Funktion)).

## Aktuelle Features

- o\. g. IPC und VFS
- Kooperatives Multitasking – ich vertraue meinen Prozessen
- [CDI.fs und CDI.net](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "Common Driver Interface")
- Netzwerkstack: [Ethernet](https://github.com/lowlevel-eu/wiki/wiki/Ethernet "Ethernet"), [IPv4](https://github.com/lowlevel-eu/wiki/wiki/Internet-Protocol "Internet Protocol"), UDP, DHCP, TCP
- palirc als IRC-Client
- Grieχsche Buchstaben im Namen
- Fortgeschrittener Falschrummodus

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11075/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2634/index.html)

<!-- MediaWiki page 2634; revision 11075; parent 11016; 2013-03-22T21:02:25Z -->
