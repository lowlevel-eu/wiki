# Týndur/LostIO

**Noch nicht brauchbar**

LostIO ist der Name der Hauptschnittstelle, die LOST den Treibern zur Verfügung stellt. Das ganze basiert auf einer VFS-ähnlichen Konstruktion. Darauf kann mit den normalen Dateifunktionen zugegriffen werden. Die Pfade sind dabei folgendermassen aufgebaut: Treibername:/Pfad/teil.

## Aufbau

Also, damit wir das gleich geklärt haben: Bei Fragen wendet ihr euch am besten an den \#lost Kanal im euIRC (Server: irc.euirc.net, Kanal: \#lost). Alternativ könnt ihr auch hier im Forum in der Lost-Kategorie fragen. Falls Bugs gefunden werden, sollten sie über unser [Bugzilla](https://bugs.tyndur.org) gemeldet werden.

LostIO ist wie oben schon gesagt eine abstrakte Schnittstelle für Treiber. Intern basiert sie auf RPC ([Remote Procedure Call](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation#rpc-remote-procedure-call "Remote Procedure Call") = das Aufrufen von Funktionen in anderen Prozessen), was sie sehr flexibel einsetzbar macht (Zum Beispiel können damit später (hoffentlich) Treiber auf anderen Computern angesprochen werden).

Der Zugriff auf Treiber mit einer LostIO-Schnittstelle erfolgt über die Standard-Dateifunktionen (fopen, fread, fwrite usw.). Das heisst aber keineswegs, dass nur Treiber, die etwas mit Dateien zu tun haben, diese Schnittstelle verwenden können. Dabei wird das bewährte “alles ist eine Datei”-Konzept von Unix/Linux eingesetzt. Wir versuchen es allerdings noch ein wenig konsequenter umzusetzen.

  

### Treiber

Auf der Treiberseite baut LostIO auf einem Dateisystem-Baum (Intern als vfstree benannt) im Speicher auf. Dieser Baum besteht aus sogenannten Knoten(engl. nodes), die alle wieder Kinderknoten haben können. Jeder dieser Knoten hat einen bestimmten Typ, der für die Handhabung dessen eine zentrale Rolle spielt. Dabei ist ein Verzeichnis vom Prinzip her genau das selbe wie jede andere Datei. In den Knoten wird dabei nur eine Typen-ID abgespeichert. Wird nun von einem Prozess versucht irgend eine Datei oder ein Verzeichnis zu öffnen und auszulesen, wird intern in der Typendatenbank nach dem Typen des zu öffnenden Knotens gesucht, um herauszufinden, wie die Aktion gehandhabt werden muss.

Die Typendatenbank beinhaltet die sogenannten Typehandles. Darin sind Pointer auf die Funktionen, die ausgeführt werden, wenn ein Prozess zum Beispiel versucht Daten von einem Knoten dieses Typs zu lesen. Momentan können Handler (eben diese Funktionen) für die folgenden Aktionen eingetragen werden:

- pre_open
- post_open
- read
- write
- seek
- close.

Nun zur Bedeutung der einzelnen Aktionen. *read* und *write* werden, wie unschwer zu erkennen, aufgerufen, wenn versucht wird von einem Knoten dieses Typs zu lesen, beziehungsweise auf ihn zu schreiben. Dass *close* beim schliessen einer Datei aufgerufen wird, ist auch ersichtlich. Etwas schwieriger ist seek. Der *seek*-Handler wird angesprungen, wenn die aktuelle Position des Zeigers in der Datei mit *fseek* verschoben wird.

#### pre_open und post_open

Als unklar und nicht unbedingt sinnvoll könnte *pre_open* und *post_open* aufgefasst werden. Warum 2 Funktionen für Open? Nun zuerst zur Funktionsweise: *pre_open* wird, wie der Name schon ahnen lässt, vor dem eigentlichen Öffnungs-Vorgang aufgerufen. Das geschieht auch, wenn der Knoten mit dem angegebenen Pfad nicht existiert. *post_open* wird erst nach dem Öffnen gestartet. Von *post_open* aus kann der Vorgang nicht mehr einfach so gestoppt werden, was aus *pre_open* problemlos möglich ist.

Bei “echten” Dateisystemen wie zum Beispiel auf Disketten hat *pre_open* noch eine spezielle Aufgabe. Da die Verzeichnisbäume von physikalischen Dateisystemen extreme Ausmasse annehmen können, sodass es belastend, oder sogar unmöglich wäre, diese vollständig im Arbeitsspeicher zu haben, besteht die Möglichkeit nur einen Teil davon im Arbeitsspeicher zu haben, und andere Teile nach gebrauch wieder zu entfernen. Und genau hier kommt *pre_open* wieder ins Spiel. Da er angesprungen wird, egal ob der Pfad existiert oder nicht, kann daraus bei Bedarf ein Teil des Verzeichnisbaumes geladen werden.

#### Typehandles

In einem Typehandle müssen nicht alle Handler eingetragen werden. Wenn ein oder mehrere Handles nicht benutzt werden, müssen die entsprechenden Pointer auf NULL gesetzt werden.

Ein Typehandle ist folgendermassen aufgebaut: \<c\> typedef struct {

       typeid_t        id;

       bool            (*pre_open)(char**, byte, pid_t,io_resource_t);
       void            (*post_open)(lostio_filehandle_t*);
       read_hdl_reply  (*read)(lostio_filehandle_t*,size_t,size_t);
       size_t          (*write)(lostio_filehandle_t*,size_t,size_t,void*);
       int             (*seek)(lostio_filehandle_t*,int,int);
       int             (*close)(lostio_filehandle_t*);

} typehandle_t; \</c\> Der erste Eintrag in der Struktur ist die Typen-ID, sie muss bei allen Typen eindeutig sein, damit keine Anderen überschrieben werden. Danach kommen die Pointer auf die Handler. Der Struct sieht man auch gerade an, wie die Prototypen der Handler aussehen sollten. Dafür können einfach die Klammern um und die der Stern vor dem Member-Namen entfernt werden. Ein Beispiel: \<c\>int (\*seek)(lostio_filehandle_t\*,int,int);\</c\> wird zu \<c\>int seek_handler (lostio_filehandle_t\* filehandle,int offset,int origin);\</c\>

Wenn das Typehandle erstellt wurde, wird es noch nicht automatisch verwendet. Damit es von LostIO auch benutz wird muss es erst mit *lostio_register_typehandle(typehandle);* (typehandle ist vom typ typehandle_t **\***) registiert werden.

Um das ganze ein wenig zu vereinfachen existieren vordefinierte Handles, die mit nur einem Funktionsaufruf eingebunden werden können. Im Moment existieren nur directory und ramfile. Directory ist dabei für einfache Verzeichnise gedacht, die dann von den Anwendungen mit Hilfe von *directory_open*, *directory_read* und noch ein paar anderen Bibliotheksfunktionen ausgelesen werden können. Der Verzeichnis-Typ kann mit *lostio_type_directory_use();* eingebunden werden.

Ramfile ist für einfache Dinge wie zum Beispiel Versionsinformationen, die nur als String im Arbeitspeicher liegen, und zum Zugreifen keine speziellen Massnahmen benötigen, gedacht. Die Ramfiles können mit *lostio_type_ramfile_use();* benutzbar gemacht werden.

## Funktionen

### LostIO

#### lostio_init

**Prototyp:** \<c\>void lostio_init();\</c\> **Beschreibung:**

Initialisiert die LostIO Schnittstelle. Wenn diese Funktion nicht aufgerufen wurde funktioniert LostIO NICHT. Darin werden unter anderem die RPC-Handler registriert und der Root-Knoten wird Vorbereitet.

  

#### lostio_register_typehandle

**Prototyp:** \<c\>void lostio_register_typehandle(typehandle_t\* typehandle);\</c\> **Parameter:**

- typehandle: Pointer auf das zu Registrierende Typehandle

**Beschreibung:**

Trägt ein Typehandle in der Typendatenbank ein. Danach kann es bei den Knoten verwendet werden.

### VFS-Baum

### Typen

#### Verzeichnis

#### Ramfile

## Beispiel

Hier folgen Ausschnitte aus dem Quellcode des Diskettentreibers(Die Funktionen fuer den Laufwerkszugriff werden hier nicht gezeigt).

Der Diskettentreiber soll die folgende Verzeichnistruktur zur Verfügung stellen:

| Pfad | Typ | Beschreibung |
| -------------- | ----------- | --------------------------------------- |
| / | directory | Oberste Ebene im Verzeichnisbaum |
| /version | ramfile | Beinhaltet die Version des Treibers |
| /devices | directory | Hier drin liegen die Laufwerks-Knoten |
| /devices/fd0 | floppy | Knoten fuer das erste Laufwerk. |
| /devices/fd1 | floppy | Knoten fuer das zweite Laufwerk. |

*directory* und *ramfile* sind, wie weiter oben schon erwähnt, eingebaute Typen, die mit nur einem Funktionsaufruf aktiviert werden. *floppy* hingegen ist ein eigener Typ, der vom Modul selbst erstellt wird.

Hier folgt nun der Code der Main-Funktion. Diese sorgt eigenlich nur fuer die Initialisierung und wartet danach in einer Endlosschleife auf RPCs von anderen Prozessen. \<c\> int main(int argc, char\* argv\[\]) {

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
           
       //Beim Init unter dem Namen "floppy" registrieren, damit die anderen
       //Prozesse den Treiber finden. Darf erst geschehen, sobald wir bereit 
       //sind.
       init_service_register("floppy");

       //Diese Schleife sorgt dafuer, dass der Treiber nicht sofort nach
       //dem Initialisieren wieder geschlossen wird.
       while(TRUE) yield();
       
       return 0;

} \</c\>

Dieser Code reicht noch nicht ganz. Nun müssen noch die Handler, die oben schon ins Typehandle eingetragen wurden definiert werden:

\<c\> read_hdl_reply floppy_read_handler(lostio_filehandle_t\* filehandle, size_t blocksize, size_t blockcount) {

       //Dient als Rückgabewert
       read_hdl_reply reply;

       //Die übergebenen Grössen in Bytes umrechen
       size_t size = blocksize * blockcount;

       //Überprüfen ob nicht über die Diskette heraus gelesen werden soll.
       if(size + filehandle->pos > filehandle->node->size)
       {
           //Falls dem so ist, nur soviel lesen wie möglich
           size = filehandle->node->size - filehandle->pos;
       }

       //...

       //Buffer allokieren
       static byte* buffer = NULL;
       buffer = realloc(buffer, sector_count * 512);

       int i;
       //Sektoren in den Buffer einlesen
       for(i = 0; i < sector_count; i++)
       {
           floppy_read_sector(sector_start + i, (void*)((dword)buffer + 512 * i));
       }

       //Die Antwort-Struktur befüllen
       reply.data = buffer;
       reply.size = size;

       //Antwort zurückgeben
       return reply;

}

  
size_t floppy_write_handler(lostio_filehandle_t\* filehandle, size_t blocksize, size_t blockcount, void\* data) {

       //Die übergebenen Grössen in Bytes umrechen
       size_t size = blocksize * blockcount;

       //Überprüfen ob nicht über die Diskette heraus geschrieben werden soll.
       if(size + filehandle->pos > filehandle->node->size)
       {
           size = filehandle->node->size - filehandle->pos;
       }

       //Wenn die Groesse 0 ist, dann ist hier Endstation
       if(size == 0)
       {
           return 0;
       }

       //...

       int i;
       //Die Sektoren auf die Diskette schreiben
       for(i = 0; i < sector_count; i++)
       {
           floppy_write_sector(sector_start + i, data);
       }

       //Die Anzahl der geschriebenen Bytes zurückgeben
       return size;

}

  
int floppy_seek_handler(lostio_filehandle_t\* filehandle , int offset, int origin) {

       //Die neue Position des Cursors muss je nach angegebenem Bezugspunkt 
       //unterscheidlich berechnet werden
       switch(origin)
       {
           //Absolute Angabe der neuen Position
           case SEEK_SET:
           {
               //Die neue Cursorposition liegt ausserhalb der Datei
               if(offset > filehandle->node->size)
               {
                   //Abbrechen
                   return -1;
               }

               //Neue Position setzen
               filehandle->pos = offset;
               break;
           }

           //Neue Position relativ zur aktuellen Position
           case SEEK_CUR:
           {
               //Die neue Cursorposition liegt ausserhalb der Datei
               if((offset + filehandle->pos) > filehandle->node->size)
               {
                   //Abbrechen
                   return -1;
               }
               filehandle->pos += offset;
               break;
           }

           //Der Cursor soll ans Dateiende gesetzt werden
           case SEEK_END:
           {
               filehandle->pos = filehandle->node->size;
               break;
           }
       }

       return 0;

} \</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11465/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1498/index.html)

<!-- MediaWiki page 1498; revision 11465; parent 10903; 2020-08-02T22:35:01Z -->
