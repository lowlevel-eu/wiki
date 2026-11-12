# PXE

## Motivation

Wenn man seinen Kernel oder sein OS auch mal auf einer realen Plattform testen möchte, ist es durchaus praktisch, nicht nach jedem Build einen neuen Bootstick zu erstellen.

Eine mögliche Lösung dafür ist [PXE](https://de.wikipedia.org/wiki/Preboot_Execution_Environment), welches einen Boot über Netzwerk erlaubt. Damit kann man dann folgenden Workflow nutzen:

1.  Compilieren
2.  Kernel in einen Ordner kopieren
3.  Testrechner rebooten

Die folgende Anleitung ist unter der Annahme, dass man einen Multiboot-Kernel booten möchte. Wenn man ein anderes Kernelformat verwenden möchte, sollte man sich die Anleitung für SYSLINUX durchlesen.

## Vorarbeit

Um einen PXE-Boot im lokalen Netzwerk zu ermöglichen, benötigt man einen [DHCP-Server](https://de.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) unter der eigenen Kontrolle und einen [TFTP-Server](https://de.wikipedia.org/wiki/Trivial_File_Transfer_Protocol). Wenn man ein Gerät besitzt, welches keinen PXE-Support besitzt, benötigt man noch ein [gPXE](http://etherboot.org/wiki/index.php)-Bootmedium, welches den PXE-Support quasi nachrüstet.

### DHCP

Es gibt verschiedene Implementierungen für einen DHCP-Server, ich verwende hier den "klassischen" [dhcp](https://wiki.archlinux.de/title/Dhcpd) auf Arch Linux, das Paket sollte aber auch auf anderen Linux-Distributionen verfügbar sein.

Um den DHCP-Server zu installieren und zu konfigurieren ließt man sich am besten den verlinkten Artikel zum Arch-Wiki durch, dort ist die Installation ausführlich erklärt. Man darf auch nicht vergessen, den dementsprechenden Daemon zu starten.

Um euch die Konfiguration etwas zu erleichtern, hier einmal mein dhcp-Konfigurations-File: `authoritative; `

`allow booting; allow bootp; `

`subnet 192.168.2.0 netmask 255.255.255.0 { `

           range 192.168.2.100 192.168.2.199;
           option routers 192.168.2.1;
           option domain-name-servers 8.8.8.8, 8.8.4.4;
           default-lease-time 600;
           max-lease-time 7200;

           # Das hier ist wichtig: Lege den TFTP-Server auf 192.168.2.11 fest und
           # sage PXE, es soll "pxelinux.0" im Root-Verzeichnes eben dessen laden.
           next-server 192.168.2.11;
           filename "/pxelinux.0";

`} `

Man möchte vor dem Start des DHCP-Servers nochmal daran denken, dass es nur einen DHCP-Server in einem Netzwerk geben darf. Von daher empfiehlt es sich, den DHCP-Server des Routers zwischendurch auszuschalten oder einen getrennten Port für den hier verwendeten DHCP zu verwenden.

### TFTP

Als TFTP-Server habe ich [tftp-hpa](https://wiki.archlinux.de/title/Tftp-hpa) verwendet, ein sehr einfacher TFTP-Server. Die Installation ist durchaus einfach, man installiert das Paket und startet den entsprechenden Daemon (tftpd).

Wer sein TFTP-Root-Verzeichnis ändern möchte, passt die Datei /etc/conf.d/tftpd (oder /etc/default/tftpd-hpa) an und ersetzt den dort angegebenen Pfad durch den eigenen.

### gPXE

**To be done**

Ein passendes gPXE-Bootimage lässt sich praktisch unter [rom-o-matic.net](http://rom-o-matic.net/) generieren.

## Setup

Nach der Installation der benötigten Services muss man noch ein paar Vorbereitungen treffen:

### Bereitstellung von pxelinux.0

pxelinux ist eine modifizierte Variante des Bootloaders [SYSLINUX](https://de.wikipedia.org/wiki/SYSLINUX), welche einen Boot über Netzwerk ermöglicht und via PXE gebootet werden kann.

Ein passendes pxelinux-Image erhält man unter <https://www.kernel.org/pub/linux/utils/boot/syslinux/>. Einfach die gewünschte Zip-Datei runterladen und entpacken.

Um jetzt unseren Netzwerk-Bootloader bereitzustellen, kopieren wir folgende Dateien aus der Zip-Datei in das TFTP-Verzeichnis (Normalerweise /srv/tftp/):

- \$ZIP/bios/com32/mboot/mboot.c32
- \$ZIP/bios/com32/lib/libcom32.c32
- \$ZIP/bios/core/pxelinux.0

Alte Boot-ROMs sind oft buggy, was manchmal dazu führt, dass pxelinux einfach abstürzt. Wenn das der Fall ist, kann es helfen, eine ältere Version von pxelinux auszuprobieren (dann wird libcom32.c32 nicht benötigt). Alternativ kann man auch gPXE selbst vom Boot-ROM laden lassen und dann von dort aus pxelinux booten.

Jetzt benötigen wir noch eine Konfigurationsdatei für pxelinux. Dafür erstellen wir einen **Ordner** mit dem Namen *pxelinux.cfg* in unserem TFTP-Verzeichnis und erstellen darin eine Datei mit dem Namen *default*. In diese Datei schreiben wir folgende Konfiguration:

`DEFAULT default`

Unser TFTP-Verzeichnis sollte also jetzt folgenden Inhalt haben:

` [felix@qlaptop ~]$ ls /srv/tftp/ libcom32.c32 mboot.c32 pxelinux.0 pxelinux.cfg `

`[felix@qlaptop ~]$ ls /srv/tftp/pxelinux.cfg/ default `

### Testen!

Wenn wir jetzt unser TFTP-Verzeichnis erstellt haben und alle Daemons gestartet wurden, können wir jetzt mal unsere Installation testen.

Zuerst fangen wir damit an, zu prüfen, ob unser TFTP-Server auch wirklich läuft und Dateien ausspuckt:

` [felix@qlaptop ~]$ tftp 192.168.2.11 tftp> get /pxelinux.0 tftp> quit [felix@qlaptop ~]$ ls pxelinux.0 ... `

Wenn das *get* länger braucht als eine Sekunde, solltest du deine Installation nochmal prüfen. TFTP gibt leider keine sonderlich zuverlässigen Fehlermeldungen aus, von daher kann ein bisschen Ausprobieren nicht schaden.

Nachdem unser TFTP läuft, prüfen wir, ob der DHCP-Server richtig tut und auch schön brav Leases verteilt. Dazu schnappt man sich einfach ein zweites netzwerkfähiges Gerät und ruft dort 'dhcpcd' oder ähnliche Tools auf, um ein DHCP-Lease zu erhalten. Wenn man jetzt eine passende IP-Adresse hat, sollte dieser Schritt auch klappen.

Falls kein oder ein falsches Lease vergeben wird, kann es daran liegen, dass zwei DHCP-Server im Netzwerk laufen. Dies sollte vermieden werden, da sonst viele Geräte nicht mehr richtig funktionieren werden und die Nachvollziehbarkeit dieser Fehler doch sehr niedrig ist.

Wenn wir soweit gekommen sind, starten wir zum ersten mal unser PXE-fähiges Gerät und warten ein bisschen. Wenn alles gut läuft, springt der PXE-Boot an und wir erhalten folgende Ausgabe auf dem Bildschirm:

` Loading default... failed: No such file or directory `

Damit sagt uns pxelinux, dass es die von uns angegebene Konfiguration "default" nicht gefunden hat. Wir sind ready to go!

### Bereitstellen unseres Kernels

Jetzt kommen wir zum spannenden Teil: Die Bereitstellung unseres eigenen Kernels.

Unser erster Schritt hier ist die Kopie unseres Kernels in das TFTP-Verzeichnis. Dabei ist der Name der Datei nicht ausschlaggebend, wir können die Datei also nennen wie wir wollen. Wichtig ist, dass es hier eine Datei sein muss und keine symbolische Verknüpfung!

Nachdem wir den Kernel in das Verzeichnis kopiert haben, öffnen wir wieder unser Konfigurationsfile */srv/tftp/pxelinux.cfg/default* und ändern den Inhalt wiefolgt ab:

` DEFAULT kernel-base `

`LABEL kernel-base `

           KERNEL mboot.c32
           APPEND /kernel-base.ker

DEFAULT gibt hier an, welches der folgenden LABEL wir booten möchten. LABEL definiert einen bestimmten Boot-Einstiegspunkt. Die Option KERNEL bei einem LABEL gibt an, welches Kernelmodul gestartet wird. Hier geben wir nicht unseren Kernel an, sondern verwenden die mboot.c32, welches ein Multiboot-Bootloader ist. APPEND gibt dann die Parameter für mboot.c32 an, es muss in dem Fall mindestens der Dateiname unseres Kernels angeben werden.

Wenn diese zwei Schritte erledigt sind, starten wir einfach die PXE-Maschine neu und sollten dann wenige Sekunden später unseren eigenen Kernel gebootet haben.

Voilà!

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11346/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2659/index.html)

<!-- MediaWiki page 2659; revision 11346; parent 11345; 2016-05-03T09:15:31Z -->
