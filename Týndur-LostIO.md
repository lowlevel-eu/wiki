# Týndur/LostIO

**Noch nicht brauchbar**

LostIO ist der Name der Hauptschnittstelle, die LOST den Treibern zur Verfügung stellt. Das ganze basiert auf einer VFS-ähnlichen Konstruktion. Darauf kann mit den normalen Dateifunktionen zugegriffen werden. Die Pfade sind dabei folgendermassen aufgebaut: Treibername:/Pfad/teil.

# Aufbau

Also, damit wir das gleich geklärt haben: Bei Fragen wendet ihr euch am besten an den \#lost Kanal im euIRC (Server: irc.euirc.net, Kanal: \#lost). Alternativ könnt ihr auch hier im Forum in der Lost-Kategorie fragen. Falls Bugs gefunden werden, sollten sie über unser [Bugzilla](http://lost.famkaufmann.info/bugzilla) gemeldet werden.

LostIO ist wie oben schon gesagt eine abstrakte Schnittstelle für Treiber. Intern basiert sie auf RPC (Remote Procedure Call = das Aufrufen von Funktionen in anderen Prozessen), was sie sehr flexibel einsetzbar macht (Zum Beispiel können damit später (hoffentlich) Treiber auf anderen Computern angesprochen werden).

Der Zugriff auf Treiber mit einer LostIO Schnittstelle erfolgt über die Standard-Dateifunktionen (fopen, fread, fwrite usw.). Das heisst aber keineswegs, dass nur Treiber, die etwas mit Dateien zu tun haben, diese Schnittstelle verwenden können. Dabei wird das bewährte “alles ist eine Datei”-Konzept von Unix/Linux eingesetzt. Wir versuchen es allerdings noch ein wenig konsequenter umzusetzen.

  

## Treiber

Auf der Treiberseite baut LostIO auf einem Dateisystem-Baum (Intern als vfstree benannt) im Speicher auf. Dieser Baum besteht aus sogenannten Knoten(engl. nodes), die alle wieder Kinderknoten haben können. Jeder dieser Knoten hat einen bestimmten Typ, der für die Handhabung dessen eine zentrale Rolle spielt. Dabei ist ein Verzeichnis vom Prizip her genau das selbe wie jede andere Datei. werden muss. In den Knoten wird dabei nur eine Typen-ID abgespeichert. Wird nun von einem Prozess versucht irgend eine Datei oder ein Verzeichnis zu öffnen und auszulesen, wird intern in der Typendatenbank nach dem Typen des zu öffnenden Knotens gesucht, um herauszufinden, wie die Aktion gehandhabt.

Die Typendatenbank beinhaltet die sogenannten Typehandles. Darin sind Pointer auf die Funktionen, die ausgeführt werden, wenn ein Prozess zum Beispiel versucht Daten von einem Knoten dieses Typs zu lesen. Moment können Handler(eben diese Funktionen) für die folgenden Aktionen eingetragen werden: pre_open, post_open, read, write, seek und close. Nun zur Bedeutung der einzelnen Aktionen. Read und write werden, wie unschwer zu erkennen, aufgerufen, wenn versucht wird von einemKnoten dieses Typs zu lesen, beziehungsweise auf ihn zu schreiben.

Dass close beim schliessen einer Datei aufgerufen wird ist auch ersichtlich. Etwas schwieriger ist seek.

Der seek-Handler wird angesprungen, wenn die aktuelle Position des Zeigers in der Datei mit fseek verschoben wird.

Als unklar und nicht unbedingt sinnvol könnte pre- und post_open aufgefasst werden. Warum 2 Funktionen für Open? Nun zuerst zur Funktionsweise: Pre_open wird, wie der Name schon ahnen lässt, vor dem eigentlichen Öffnugs-Vorgang aufgerufen. Das geschieht auch, wenn der Knoten mit dem angegebenen Pfad nicht existiert. Post_open wird erst nach dem öffnen gestartet. Von post_open aus, kann der Vorgang nicht mehr einfach so gestoppt werden, was aus pre_open problemlos möglich ist. Bei “echten” Dateisystemen wie zum Beispiel auf Disketten hat pre_open noch eine spezielle Aufgabe. Da die Verzeichnisbäume von physikalischen Dateisystemen extreme Ausmasse annehmen können, sodass es belastend, oder sogar unmöglich wäre, diese vollständig im Arbeitsspeicher zu haben, besteht die Möglichkeit nur einen Teil davon im Arbeitsspeicher zu haben, und andere Teile nach gebrauch wieder zu entfernen. Und genau hier kommt pre_open wieder ins Spiel. Da er angesprungen wird, egal ob der Pfad exisitert oder nicht, kann daraus bei Bedarf ein Teil des Verzeichnisbaumes geladen werden.

In einem Typehandle müssen nicht alle Handler eingetragen werden. Wenn ein oder mehrere Handles nicht benutzt werden, müssen die entsprechenden Pointer auf NULL gesetzt werden. Um das ganze ein wenig zu vereinfachen existieren vordefinierte Handles, die mit nur einem Funktionsaufruf eingebunden werden können. Im Moment existieren nur directory und ramfile. Directory ist dabei für einfache Verzeichnise gedacht, die dann von den Anwendungen mit Hilfe von directory_open, directory_read und noch ein paar andern Bibliotheksfunktionen ausgelesen werden können.

Ramfile ist für einfache Dinge wie zum Beispiel Versionsinformationen, die nur als String im Arbeitspeicher liegen, und zum Zugreiffen keine Speziellen Massnahmen benötigen, gedacht.

# Funktionen

## LostIO

## VFS-Baum

## Typen

### Verzeichnis

### Ramfile

# Beispiel

Hier folgen ausschnitte aus dem Quellcode des Diskettentreibers(Die Funktionen fuer den Laufwerkszugriff werden hier nicht gezeigt).

\<c\> int main(int argc, char\* argv\[\]) {

       //Beim Init unter dem Namen "floppy" registrieren, damit die anderen
       //Prozesse den Treiber finden.
       init_service_register("floppy");
       
       //LostIO initialisieren(Ist nur bei den Treibern notwendig. Bei 
       //Anwendungen, die nur auf andere Treiber zugreifen wollen sollte
       //das weggelassen werden.
       lostio_init();
       
       //Hier werden 2 vordefinierte Typen benutzbar gemacht: 
       //Verzieichnise und Dateien, die den Inhalt direkt im RAM haben.
       //Dann muessen keine eigenen Handler registriert werden.
       lostio_type_ramfile_use();
       lostio_type_directory_use();
       

       //Speicher fuer ein neues typehandle allokieren
       typehandle_t* typehandle = malloc(sizeof(typehandle_t));
       
       //Die Typen-ID
       typehandle->id          = 255;
       
       //Die Pointer auf unsere Handles setzen. NULL wenn für
       //diejenigen Pointer wofür kein Handler zur Verfügung steht.
       typehandle->pre_open    = NULL;
       typehandle->post_open   = NULL;
       typehandle->read        = &floppy_read_handler;
       typehandle->write       = &floppy_write_handler;
       typehandle->seek        = &floppy_seek_handler;
       typehandle->close       = NULL;

       //Das Typehandle bei LostIO registrieren, damit es verfügbar ist.
       lostio_register_typehandle(typehandle);

  

       //Der Inhalt des Version-Ramfile
       const char* version = "Version 0.0.1";
       //Nun wird das Ramfile erstellt
       vfstree_create_node("/version", LOSTIO_TYPES_RAMFILE, strlen(version) + 1, (void*)version);

       //Zuerst wird das devices-Verzeichnis erstellt
       vfstree_create_node("/devices", LOSTIO_TYPES_DIRECTORY, 0, NULL);
       //Die beiden Nodes fuer die beiden Diskettenlaufwerke erstellt
       vfstree_create_node("/devices/fd0", 255, 1440 * 1024, (void*)0);
       vfstree_create_node("/devices/fd1", 255, 1440 * 1024, (void*)1);

       //Diese Schleife sorgt dafuer, dass der Treiber nicht sofort nach
       //dem Initialisieren wieder geschlossen wird.
       while(TRUE) yield();
       
       return 0;

} \</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1852/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1498/index.html)

<!-- MediaWiki page 1498; revision 1852; parent 1851; 2007-03-09T22:33:28Z -->
