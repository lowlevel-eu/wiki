# Common Driver Interface

**Common Driver Interface** (oder kurz **CDI**) ist ein Standard, der vom Týndur-Team entwickelt wird, und der es ermöglichen soll, betriebssystemunabhängige Treiber zu schreiben. Dies funktioniert mithilfe einer Bibliothek, die einmal für ein Betriebssystem implementiert werden muss. Dann können CDI-komforme Treiber einfach mit dieser Bibliothek kompiliert werden. Der CDI-Standard gibt lediglich vor, wie die Funktionsprototypen aussehen müssen, aber nicht wie diese implementiert werden, denn das ist ja von Betriebssystem zu Betriebssystem unterschiedlich.

Ein Link zur Dokumentation der Funktionsprototypen, Strukturen, Enumerationen, usw. ist in dem [Absatz Weblinks](#weblinks) zu finden.

## Module

CDI definiert in seinen Modulen Schnittstellen für unterschiedliche Geräteklassen. Derzeit existieren die folgenden Module:

- **core**: Kernfunktionalität von CDI
- **net**: Netzwerk (vorhandene Treiber: rtl8139, sis900, pcnet, e1000)
- **fs**: Dateisysteme (vorhandene Treiber: ext2, ramdisk)
- **storage**: Massenspeicher (vorhandene Treiber: floppy, ata)

Ein Betriebssystem muss dabei nicht zwingend die Schnittstellen aller Module implementieren. Alle Treiber benutzen Funktionen aus *core*, aber es ist ohne weiteres möglich, z. B. neben *core* nur die Schnittstelle für Netzwerktreiber zu implementieren.

### Core

Die Kernfunktionalität umfasst die folgenden Punkte:

- Verwaltung der Treiber und Geräte
- Zugriff auf I/O-Ports
- Zugriff auf Physischen Speicher
- PCI
- Verkettete Listen

### Net

Ein Netzwerktreiber muss nur eine Funktion bereitstellen um Pakete über eine Karte zu versenden:

- **send_packet**(device, buffer, size)

Die Implementierung stellt dem Treiber eine Funktion zur Verfügung um empfangene Pakete abzuliefern.

### FS

Das Interface für Dateisystemtreiber ist komplexer als bei den anderen Treibern. Hier müssen Funktionen für alle möglichen Dateioperationen zur Verfügung gestellt werden.

Um möglichst alle Dateisysteme unterstützen zu können, verfolgt CDI/FS ein etwas ungewöhnliches Konzept. Im Zentrum stehen dabei so genannte Ressourcen. Diese **Ressourcen können** Datei, Verzeichnis, Symlink, Spezialdatei oder alles gleichzeitig sein. Umgesetzt wird das mit den so genannten **Klassen**. Eine Ressource gehört zu mindestens einer Klasse (andernfalls ist sie nicht persistent). Diese Klassen beschreiben dann jeweils die verfügbaren Operationen. Es existieren momentan 4 verschiedene Klassen:

- **file**: Reguläre Datei
- **dir**: Verzeichnis
- **link**: Symbolische Verknüpfung (symlink)
- **special**: Spezialdateien

Ein Treiber kann jeweils mehrere Klassen des selben Typs anbieten, in denen unterschiedliche Funktionen eingetragen sind.

### Storage

Die Schnittstelle für Massenspeicher-Treiber ist äusserst einfach definiert. Der Treiber muss die folgenden Funktionen bereitstellen:

- **read_blocks**(device, start_block, block_count, buffer)
- **write_blocks**(device, start_block, block_count, buffer)

Diese beiden Funktionen werden von der Implementierung dazu Benutzt Sektoren zu lesen oder zu schreiben. Wieviele Sektoren ein Gerät hat, und wie groß diese sind, wird in der Device-Struktur festgelegt. Die Implementierung muss garantieren, dass die Funktion nur mit, für dieses Gerät sinnvollen, Parametern aufgerufen wird.

## Aufbau eines typischen Treibers

Zunächst eine Vorbemerkung: CDI wurde erstmals in týndur implementiert, das nach wie vor das Referenzsystem für CDI darstellt. týndur ist ein Mikrokernelsystem und aus diesem Grund liegt gelegentlich in Erklärungen die Annahme vor, dass ein Treiber ein eigenständiges Programm ist. CDI funktioniert aber auch mit einem monolithischen Kernel, aus der main-Funktion wird dann eine gewöhnliche Funktion, die zur Initialisierung des Treibers aufgerufen wird.

Sobald diese Funktion aufgerufen wird, registriert sie Datenstrukturen zur Beschreibung des Treibers bei CDI und führt die Initialisierung des Treibers durch. Im Allgemeinen werden dabei Geräte erkannt (z. B. auf dem PCI-Bus) und wiederum bei CDI registriert. Anschließend wird als letzte Aktion im Hauptprogramm die Funktion *cdi_run_drivers* aufgerufen, die bei einem Mikrokernelkonzept die Kontrolle an CDI übergibt und bei einem Monolithen im Allgemeinen leer ist und damit zum Kernel zurückkehrt, der die Treiberinitialisierung aufgerufen hat.

Der Treiber kommt ab diesem Zeitpunkt nur noch über Callbacks ins Spiel. Die Datenstrukturen zur Registrierung des Treibers enthalten Funktionspointer, die von CDI aufgerufen, wenn vom Treiber eine Aktion nötig ist. Das kann beispielsweise sein, wenn ein Interrupt für den Treiber eingetroffen ist oder wenn der Netzwerktreiber ein Ethernet-Paket versenden soll.

## Dinge, die ein Betriebssystem zur Verfügung stellen muss

Hinweis: Der hier angegeben Inhalt der Strukturen ist nur ein Mindestmaß; Man darf beliebig viel in einer CDI-Struktur speichern, wenn das Betriebssystem mehr Informationen benötigt.

### CDI.core

#### Datentypen

\<c\>typedef enum {

     CDI_UNKNOWN = 0,
     CDI_NETWORK = 1,
     CDI_STORAGE = 2,
     CDI_SCSI = 3,

} cdi_device_type_t;\</c\> cdi_device_type_t gibt den Typ eines Gerätes bzw. eines Treibers an. \<c\>struct cdi_device {

     cdi_device_type_t type;
     const char        *name;
     struct cdi_driver *driver;

};\</c\> Diese Struktur repräsentiert ein Gerät. „type“ gibt den Typ an, „name“ den Namen und „driver“ einen Pointer zu einer Struktur, die den Gerätetreiber repräsentiert. \<c\>struct cdi_driver {

     cdi_device_type_t type;
     const char        *name;
     cdi_list_t        devices;
     void (*init_device)(struct cdi_device *device);
     void (*remove_device)(struct cdi_device *device);
     void (*destroy)(struct cdi_driver *driver);

};\</c\> Diese Struktur wiederum repräsentiert einen Gerätetreiber. „type“ gibt den Typ an, „name“ den Namen und „devices“ ist eine Liste der registrierten Geräte. Die Funktion init_device() muss vom Betriebssystem aufgerufen werden, um ein Gerät zu initialisieren, remove_device() entfernt ein Gerät und destroy() deinitialisiert den Treiber. \<c\>struct cdi_pci_device {

     uint16_t bus;
     uint16_t dev;
     uint16_t function;
     uint16_t vendor_id;
     uint16_t device_id;
     uint8_t  class_id;
     uint8_t  subclass_id;
     uint8_t  interface_id;
     uint8_t  rev_id;
     uint8_t  irq;
     cdi_list_t resources;

};\</c\> Mit dieser Struktur wird ein [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Gerät beschrieben. „bus“ ist der Bus, auf dem es sich befindet, „dev“ das Gerät und „function“ die Funktion. „vendor_id“ gibt die Hersteller-ID an, „device_id“ die Geräte-ID. Die Classcodes befinden sich in „class_id“ (Base class), „subclass_id“ (Subclass) und „interface_id“ (Programming interface). „rev_id“ enthält die Revisions-ID. In „irq“ steht der IRQ, den das Gerät verwendet. „resources“ ist eine Liste mit den I/O- und Speicherresourcen, ihre Elemente sind vom Typ „struct cdi_pci_resource“. \<c\>typedef enum {

     CDI_PCI_MEMORY,
     CDI_PCI_IOPORTS

} cdi_res_t;\</c\> „cdi_res_t“ gibt den Typ einer PCI-Resource an (I/O-Ports oder Speicherbereich). \<c\>struct cdi_pci_resource {

     cdi_res_t    type;
     uintptr_t    start;
     size_t       length;
     unsigned int index;
     void         *address;

};\</c\> Informationen zu einer Resource eines PCI-Gerätes erhält man aus dieser Struktur. „type“ gibt den Typ an (I/O-Ports oder Speicherbereich), „start“ den Beginn, „length“ die Länge, „index“ den Index der Resource (0 ist die erste usw.) und „address“ gibt bei Speicherbereichen ihre virtuelle Adresse an (vorher muss der Bereich mit cdi_pci_alloc_memory() reserviert worden sein). \<c\>typedef ??? cdi_list_t;\</c\> „cdi_list_t“ repräsentiert eine Linked-List. Dieser Datentyp muss ein Pointer sein, in týndur ist er ein Pointer auf eine Struktur mit den Elementen „anchor“ (zeigt auf das erste Element der Liste) und „size“ (Anzahl der Elemente in der Liste). Die Elemente der Liste wiederum müssen einen Pointer speichern können (der Wert des Elements) und sollten desweiteren einen Pointer auf das nächste Element enthalten (eine Linked-List eben).

#### Funktionen

##### cdi.h

\<c\>void cdi_init(void);\</c\> Initialisiert die CDI-Strukturen des Betriebssystems, muss vor Benutzung anderer CDI-Funktionen aufgerufen werden – wiederholte Aufrufe müssen ohne Effekt bleiben. \<c\>void cdi_run_drivers(void);\</c\> Diese Funktion startet alle registrierten Treiber. Das Betriebssystem sollte alle registrierten Treiber durchgehen und bei allen für einen Treiber registrierten Geräten (Die Liste „(struct cdi_driver \*)-\>devices“) im Feld „driver“ (in „struct cdi_device“) den entsprechenden Treiber eintragen sowie, wenn „(struct cdi_driver \*)-\>init_device“ ungleich NULL ist, diese Funktion mit dem Gerät als Parameter aufrufen. \<c\>void cdi_driver_init(struct cdi_driver \*driver);\</c\> Initialisiert den angegebenen Treiber. Der Treiber hat bereits alle Felder in „driver“ initialisiert, lediglich die „devices“-Liste muss vom Betriebssystem mittels cdi_list_create() erstellt werden. \<c\>void cdi_driver_destroy(struct cdi_driver \*driver);\</c\> Deinitialisiert den angegebenen Treiber. Ist der Funktionspointer „driver-\>remove_device“ ungleich NULL, so sollte diese Funktion für alle registrierten Geräte (in der Liste „driver-\>devices“) aufgerufen werden. \<c\>void cdi_driver_register(struct cdi_driver \*driver);\</c\> Registriert einen CDI-Treiber. Es bietet sich an, ihn in einer globalen Liste einzutragen und diese Liste dann beim cdi_run_drivers()-Aufruf abzuarbeiten.

##### cdi/misc.h

\<c\>void cdi_register_irq(uint8_t irq, void (\*handler)(struct cdi_device\*), struct cdi_device \*device);\</c\> Registriert eine ISR „handler“ für den angegebenen IRQ „irq“. Der ISR muss beim Aufruf das angegebene CDI-Gerät „device“ als Parameter übergeben werden. \<c\>int cdi_wait_irq(uint8_t irq, uint32_t timeout);\</c\> Wartet, bis der angegeben IRQ aufgetreten ist. „timeout“ gibt die Zeit in Millisekunden an, die maximal gewartet werden soll. Ist der IRQ seit dem letzten cdi_reset_wait_irq() und vor „timeout“ aufgetreten, wird 0 zurückgegeben, sonst -1. \<c\>int cdi_reset_wait_irq(uint8_t irq);\</c\> Setzt den Status (aufgerufen oder nicht) des IRQs zurück. \<c\>int cdi_alloc_phys_mem(size_t size, void \*\*vaddr, void \*\*paddr);\</c\> Reserviert physisch kontinuierlichen Speicher der Größe „size“. Der Beginn wird in „\*\*paddr“ gespeichert, die virtuelle Adresse in „\*\*vaddr“. Bei Erfolg wird 0 zurückgegeben, sonst -1. \<c\>void \*cdi_alloc_phys_addr(size_t size, uintptr_t paddr);\</c\> Reserviert physisch kontinuierlichen Speicher der Größe „size“ an der physischen Adresse „paddr“. Bei Erfolg wird die virtuelle Adresse zurückgegeben, im Fehlerfall hingegen NULL. \<c\>int cdi_ioports_alloc(uint16_t start, uint16_t count);\</c\> Reserviert „count“ I/O-Ports ab dem Port „start“. Bei Erfolg wird 0 zurückgegeben, im Fehlerfall -1. \<c\>int cdi_ioports_free(uint16_t start, uint16_t count);\</c\> Gibt reservierte „count“ I/O-Ports ab „start“ wieder frei. Bei Erfolg ist der Rückgabewert 0, sonst -1. \<c\>void cdi_sleep_ms(uint32_t ms);\</c\> Wartet „ms“ Millisekunden.

##### cdi/pci.h

\<c\>void cdi_pci_get_all_devices(cdi_list_t list);\</c\> Fügt alle vorhandenen PCI-Geräte in die Liste „list“ ein. \<c\>void cdi_pci_device_destroy(struct cdi_pci_device \*device);\</c\> Gibt die Informationen zum PCI-Gerät frei. \<c\>void cdi_pci_alloc_ioports(struct cdi_pci_device \*device);\</c\> Reserviert die I/O-Ports des angegebenen PCI-Geräts. \<c\>void cdi_pci_free_ioports(struct cdi_pci_device \*device);\</c\> Gibt selbige Reservierung wieder frei. \<c\>void cdi_pci_alloc_memory(struct cdi_pci_device \*device);\</c\> Reserviert den Speicher des PCI-Geräts. \<c\>void cdi_pci_free_memory(struct cdi_pci_device \*device);\</c\> Gibt selbigen Speicher wieder frei.

##### cdi/io.h

\<c\>uint8_t cdi_inb(uint16_t port); uint16_t cdi_inw(uint16_t port); uint32_t cdi_inl(uint16_t port);\</c\> Liest ein Byte/Word/DWord vom angegeben I/O-Port ein und gibt es zurück \<c\>void cdi_outb(uint16_t port, uint8_t data); void cdi_outw(uint16_t port, uint16_t data); void cdi_outl(uint16_t port, uint32_t data);\</c\> Gibt ein Byte/Word/DWord am angegebenen I/O-Port aus.

##### cdi/lists.h

\<c\>cdi_list_t cdi_list_create(void);\</c\> Erstellt eine Linked-List (gibt NULL bei Fehler zurück). \<c\>void cdi_list_destroy(cdi_list_t list);\</c\> Gibt eine Liste wieder frei. \<c\>cdi_list_t cdi_list_push(cdi_list_t list, void \*value);\</c\> Fügt ein Element am Anfang der Liste ein und gibt die Liste zurück (oder NULL bei Fehler). \<c\>void \*cdi_list_pop(cdi_list_t list);\</c\> Entfernt ein Element vom Anfang der Liste und gibt seinen Wert zurück (oder NULL bei Fehler). \<c\>size_t cdi_list_empty(cdi_list_t list);\</c\> Gibt 1 zurück, wenn die Liste leer ist, sonst 0. \<c\>void \*cdi_list_get(cdi_list_t list, size_t index);\</c\> Gibt den Wert des Elements am Index „index“ zurück (oder NULL bei Fehler). \<c\>cdi_list_t cdi_list_insert(cdi_list_t list, size_t index, void \*value);\</c\> Fügt ein Element in die Liste an der Position „index“ ein und gibt die Liste zurück (oder NULL bei Fehler). \<c\>void \*cdi_list_remove(cdi_list_t list, size_t index);\</c\> Entfernt das Listenelement an der Stelle „index“ und gibt seinen Wert zurück (oder NULL bei Fehler). \<c\>size_t cdi_list_size(cdi_list_t list);\</c\> Gibt die Anzahl der Elemente in der Liste zurück.

### CDI.net

#### Datentypen

\<c\>struct cdi_net_device {

     struct cdi_device dev;
     uint64_t          mac : 48;
     int               number;
     void (*send_packet)(struct cdi_net_device *device, void *data, size_t size);

};\</c\> Diese Struktur beschreibt ein CDI.net-Gerät. „dev“ ist eine Struktur, die das Gerät im Allgemeinen repräsentiert, „mac“ gibt die MAC-Adresse an und „number“ die Nummer der Netzwerkkarte. Mit der Funktion send_packet() können Pakete gesendet werden, wobei „device“ ein Pointer auf diese Struktur ist, „data“ ein Pointer auf die zu sendenden Daten, während „size“ die Größe des Puffers „data“ angibt. Wichtig: Man darf nicht erwarten, dass send_packet() reentrant (also gegen [Race Conditions](https://github.com/lowlevel-eu/wiki/wiki/Race-Condition "Race Condition") abgesichert) ist! Das Betriebssystem muss somit selbst dafür Sorge tragen, dass diese Funktion immer nur von maximal einem einzigen Prozess durchlaufen wird. \<c\>struct cdi_net_driver {

     struct cdi_driver drv;

};\</c\> Mit dieser Struktur werden CDI.net-Treiber beschrieben. Sie enthält lediglich die Struktur „struct cdi_driver“, die den Treiber im Allgmeinen repräsentiert.

#### Funktionen

\<c\>void cdi_net_driver_init(struct cdi_net_driver \*driver);\</c\> Diese Funktion wird aufgerufen, um einen CDI.net-Treiber „driver“ zu initialisieren. Das Betriebssystem sollte „driver-\>drv.type“ auf CDI_NETWORK setzen und anschließend „cdi_driver_init((struct cdi_driver \*)driver)“ aufrufen. \<c\>void cdi_net_driver_destroy(struct cdi_net_driver \*driver);\</c\> Diese Funktion wiederum deinitialisiert einen CDI.net-Treiber. \<c\>void cdi_net_device_init(struct cdi_net_device \*device);\</c\> Mit dieser Funktion werden CDI.net-Geräte (also Netzwerkkarten) initialisiert. Der Treiber hat alle vorgegebenen Felder in der „cdi_net_device“-Struktur „device“ außer „number“ bereits initialisiert. „number“ muss vom Betriebssystem gesetzt werden. \<c\>void cdi_net_receive(struct cdi_net_device \*device, void \*buffer, size_t size);\</c\> Diese Funktion wird vom CDI.net-Treiber aufgerufen, wenn Daten von einer Netzwerkkarte empfangen wurden. „device“ gibt die Netzwerkkarte an, „buffer“ ist ein Pointer zum empfangenen Paket und „size“ enthält die Größe des Pakets.

## Betriebssysteme, welche CDI benutzen (werden)

- [LF OS](https://github.com/lowlevel-eu/wiki/wiki/LF-OS "LF OS")
- [meinOS](https://github.com/lowlevel-eu/wiki/wiki/MeinOS "MeinOS")
- [µxoµcota](https://github.com/lowlevel-eu/wiki/wiki/%CE%9Cxo%C2%B5cota "Μxoµcota")
- [MyXomycota](https://github.com/lowlevel-eu/wiki/wiki/MyXomycota "MyXomycota")
- [Paloxena](https://github.com/lowlevel-eu/wiki/wiki/Paloxena "Paloxena") (kernel1, kernel2 und kernel3)
- [Pedigree](https://github.com/lowlevel-eu/wiki/wiki/Pedigree "Pedigree")
- [planlOS](https://github.com/lowlevel-eu/wiki/wiki/PlanlOS "PlanlOS")
- [PrettyOS](https://github.com/lowlevel-eu/wiki/wiki/PrettyOS "PrettyOS")
- [týndur](https://github.com/lowlevel-eu/wiki/wiki/T%C3%BDndur "Týndur")
- [universe](https://github.com/lowlevel-eu/wiki/wiki/Universe "Universe")

## Weblinks

- [Dokumentation der CDI-Header-Files von týndur](http://lpt.tyndur.org/cdi)
- [CDI-Referenzimplementierung](http://git.tyndur.org/?p=cdi.git;a=tree)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11358/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1622/index.html)

<!-- MediaWiki page 1622; revision 11358; parent 11015; 2016-08-03T16:33:47Z -->
