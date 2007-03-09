# Týndur/LostIO

**Noch nicht brauchbar**

LostIO ist der Name der Hauptschnittstelle, die LOST den Treibern zur Verfügung stellt. Das ganze basiert auf einer VFS-ähnlichen Konstruktion. Darauf kann mit den normalen Dateifunktionen zugegriffen werden. Die Pfade sind dabei folgendermassen aufgebaut: Treibername:/Pfad/teil.

  

# Funktionen

## LostIO

## VFS-Baum

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1845/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1498/index.html)

<!-- MediaWiki page 1498; revision 1845; parent 1844; 2007-03-09T19:22:47Z -->
