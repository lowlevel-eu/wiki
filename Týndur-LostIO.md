# Týndur/LostIO

**Noch nicht brauchbar**

LostIO ist der Name der Hauptschnittstelle, die LOST den Treibern zur Verfügung stellt. Das ganze basiert auf einer VFS-ähnlichen Konstruktion. Darauf kann mit den normalen Dateifunktionen zugegriffen werden. Die Pfade sind dabei folgendermassen aufgebaut: Treibername:/Pfad/teil.

  

# Funktionen

# Beispiel

Hier folgen ausschnitte aus dem Quellcode des Diskettentreibers(Die Funktionen fuer den Laufwerkszugriff werden hier nicht gezeigt).

int main(int argc, char\* argv\[\]) { //Beim Init unter dem Namen "floppy" registrieren, damit die anderen //Prozesse den Treiber finden. init_service_register("floppy"); //Diskettenlaufwerk initialisieren //TODO: Das 2. Diskettelaufwerk auch initialiseren falls vorhanden register_intr_handler(0x26, &floppy_irq_handler); floppy_select_drive(0); floppy_reset(); floppy_set_motor(FALSE); //Den Dateisystem-Baum bereit machen lostio_init(); lostio_type_ramfile_use(); lostio_type_directory_use(); typehandle_t\* typehandle = malloc(sizeof(typehandle_t)); typehandle-\>id = 255; typehandle-\>pre_open = NULL; typehandle-\>post_open = NULL; typehandle-\>read = &floppy_read_handler; typehandle-\>write = &floppy_write_handler; typehandle-\>seek = &floppy_seek_handler; typehandle-\>close = NULL; lostio_register_typehandle(typehandle); const char\* version = "Version 0.0.1"; vfstree_create_node("/version", LOSTIO_TYPES_RAMFILE, strlen(version) + 1, (void\*)version); vfstree_create_node("/devices", LOSTIO_TYPES_DIRECTORY, 0, NULL); vfstree_create_node("/devices/fd0", 255, 1440 \* 1024, (void\*)0); vfstree_create_node("/devices/fd1", 255, 1440 \* 1024, (void\*)1); //Diese Schleife sorgt dafuer, dass der while(TRUE) yield(); return 0; }

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1836/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1498/index.html)

<!-- MediaWiki page 1498; revision 1836; parent 0; 2007-03-09T11:49:08Z -->
