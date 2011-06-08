# Multiboot

Multiboot ist ein Standard um Betriebssystemen eine einheitliche Startumgebung zu gewährleisten. Ein sehr bekannter Multiboot-Bootloader ist [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB").

## Ausgangsstatus

Unmittelbar nachdem die Kontrolle von GRUB an den Kernel übergeben wurde, sind folgende Zustände festgesetzt:

|  |  |
| ---------- | -------------------------------------------------------------------------------------------- |
| EAX | Beinhaltet magicnumber 0x2BADB002 |
| EBX | Pointer zur Multiboot-Structure |
| CS | Ein Codesegment mit der Basisadresse 0 und der Größe 0xFFFFFFFF |
| DS | Ein Datensegment mit der Basisaddresse 0 und der Größe 0xFFFFFFFF |
| ES | Ein Datensegment mit der Basisaddresse 0 und der Größe 0xFFFFFFFF |
| FS | Ein Datensegment mit der Basisaddresse 0 und der Größe 0xFFFFFFFF |
| GS | Ein Datensegment mit der Basisaddresse 0 und der Größe 0xFFFFFFFF |
| SS | Ein Datensegment mit der Basisaddresse 0 und der Größe 0xFFFFFFFF |
| A20 Gate | A20 Gate ist enabled |
| CR0 | Bit 31 (PG) ist zurückgesetzt. Bit 0 (PE) ist gesetzt. Alle anderen Bits sind undefiniert. |
| EFLAGS | Bit 17 (VM) und Bit 9 (IF) ist zurückgesetzt. Alle anderen Bits sind undefiniert. |

## Multiboot-Header

Der Multiboot-Header sollte in den ersten 8192 Bytes des OS-Images liegen. Der Multiboot-Header sieht folgendermaßen aus:

| Offset | Größe | Inhalt | Anwesend wenn mbh_flags\[X\] gesetzt |
| -------- | ------- | ------------------------------- | -------------------------------------- |
| 0x00 | 4 | [mbh_magic](#mbh_magic) | immer |
| 0x04 | 4 | [mbh_flags](#mbh_flags) | immer |
| 0x08 | 4 | [mbh_checksum](#mbh_checksum) | immer |
| 0x0C | 4 | mbh_header_addr | 16 |
| 0x10 | 4 | mbh_load_addr | 16 |
| 0x14 | 4 | mbh_load_end_addr | 16 |
| 0x18 | 4 | mbh_bss_end_addr | 16 |
| 0x1C | 4 | mbh_entry_addr | 16 |
| 0x20 | 4 | mbh_mode_type | 2 |
| 0x24 | 4 | mbh_mode_width | 2 |
| 0x28 | 4 | mbh_mode_height | 2 |
| 0x2C | 4 | mbh_mode_depth | 2 |

### mbh_magic

Dient GRUB zum Finden des Multiboot-Headers. Muss 0x1BADB002 sein.

### mbh_flags

Bits 0-15 sind Flags die unbedingt benötigt werden. Wenn der Bootloader eines dieser Flags nicht kennt, bricht er den Bootvorgang ab. Bits 16-31 sind optionale Flags. Es gibt die folgenden Flags

| Bit | Auswirkung |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Module werden 4k-aligned geladen |
| 1 | Ermittelt [mbs_mem_lower](#mbs_mem_lower) und [mbs_mem_upper](#mbs_mem_upper). Wenn möglich auch [mbs_mmap_length](#mbs_mmap_length) und [mbs_mmap_addr](#mbs_mmap_addr) |
| 16 | Informationen über das OS-Image werden aus den Feldern 0x0C-0x1C des Multiboot-Headers entnommen. |

### mbh_checksum

Ein u32-Wert der Zusammen mit [mbh_magic](#mbh_magic) und [mbh_flags](#mbh_flags) 0 ergeben soll. Man kann ihn so berechnen:

    -(mbh_magic + mbh_flags)

## Multiboot-Structure

Die Multiboot-Structure beinhaltet Informationen, die vom Bootloader vorher ausgelesen wurden. Die Adresse der Multiboot-Structure ist unmittelbar nach dem Starten des Kernels in *EBX* gespeichert.

| Offset | Größe | Inhalt | Anwesend wenn mbs_flags\[X\] gesetzt |
| -------- | ------- | ----------------------------------------------- | -------------------------------------- |
| 0x00 | 4 | [mbs_flags](#mbs_flags) | immer |
| 0x04 | 4 | [mbs_mem_lower](#mbs_mem_lower) | 0 |
| 0x08 | 4 | [mbs_mem_upper](#mbs_mem_upper) | 0 |
| 0x0C | 4 | [mbs_bootdevice](#mbs_bootdevice) | 1 |
| 0x10 | 4 | [mbs_cmdline](#mbs_cmdline) | 2 |
| 0x14 | 4 | [mbs_mods_count](#mbs_mods_count) | 3 |
| 0x18 | 4 | [mbs_mods_addr](#mbs_mods_addr) | 3 |
| 0x1C | 16 | [mbs_syms](#mbs_syms) | 4 oder 5 |
| 0x2C | 4 | [mbs_mmap_length](#mbs_mmap_length) | 6 |
| 0x30 | 4 | [mbs_mmap_addr](#mbs_mmap_addr) | 6 |
| 0x34 | 4 | [mbs_drives_length](#mbs_drives_length) | 7 |
| 0x38 | 4 | [mbs_drives_addr](#mbs_drives_addr) | 7 |
| 0x3C | 4 | [mbs_config_table](#mbs_config_table) | 8 |
| 0x40 | 4 | [mbs_boot_loader_name](#mbs_boot_loader_name) | 9 |
| 0x44 | 4 | [mbs_apm_table](#mbs_apm_table) | 10 |
| 0x48 | 4 | mbs_vbe_control_info | 11 |
| 0x4C | 4 | mbs_vbe_mode_info | 11 |
| 0x50 | 2 | mbs_vbe_mode | 11 |
| 0x52 | 2 | mbs_vbe_interface_seg | 11 |
| 0x54 | 2 | mbs_vbe_interface_off | 11 |
| 0x56 | 2 | mbs_vbe_interface_len | 11 |

### mbs_flags

Gibt an welche Felder anwesend sind.

### mbs_mem_lower

Gibt die Größe des unteren Speichers in kB an.

### mbs_mem_upper

Gibt die Größe des höheren Speichers in kB an.

### mbs_bootdevice

Dieses Doubleword ist in 4 Bytes unterteilt. Das 1. Byte steht für die BIOS-Laufwerknummer. Byte 2-4 gibt die Partition und Subpartition an. Wenn ein Wert 0xFF ist, wird keine Partitionierung (auf diesem Level) benutzt.

### mbs_cmdline

Pointer zu einem 0-terminated ASCII-String, der die Kommandos enthält, die an den Kernel übergeben wurden.

### mbs_mods_count

Gibt an wie viele Module von GRUB geladen wurden

### mbs_mods_addr

Pointer auf die erste Modulstruktur, deren Einträge hintereinander im Speicher liegen. Eine Modulstruktur sieht folgendermaßen aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ----------- | ------------------------------------------------------------------------- |
| 0x00 | 4 | mod_start | Adresse an der das Modul liegt |
| 0x04 | 4 | mod_end | Adresse an der das Modul endet |
| 0x08 | 4 | string | Pointer zu einem 0-term. ASCII-String, der den Namen des Moduls enthält |
| 0x0C | 4 | reserved | Reserviert (0) |

### mbs_syms

Wenn Bit 4 in [mbs_flags](#mbs_flags) gesetzt ist, liegt diese Struktur am Offset 0x1C und enthält Informationen zur Sektionstabelle einer a.out-Datei.

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ---------- | ----------------------------- |
| 0x1C | 4 | tabsize |  |
| 0x20 | 4 | strsize |  |
| 0x24 | 4 | addr | Pointer zur Sektionstabelle |
| 0x28 | 4 | reserved | Reserviert (0) |

Wenn Bit 5 in [mbs_flags](#mbs_flags) gesetzt ist, liegt diese Struktur am Offset 0x1C und enthält Informationen zur Sektionstabelle einer [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")-Datei.

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ------- | ---------------------------------------------------- |
| 0x1C | 4 | num | Anzahl an Einträgen |
| 0x20 | 4 | size | Größe eines Eintrags |
| 0x24 | 4 | addr | Pointer zur Sektionstabelle |
| 0x28 | 4 | shndx | Stringtabelle für die Einträge der Sektionstabelle |

### mbs_mmap_length

Gibt die Länge der Memorymap an

### mbs_mmap_addr

Pointer zur Memorymap, deren Einträge hintereinander im Speicher liegen. Ein Eintrag in der Memorymap sieht folgendermaßen aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ---------- | ----------------------------------------------------- |
| 0x00 | 4 | size | Gibt die Größe des Eintrags -4 an |
| 0x04 | 8 | BaseAddr | Basisadresse des Speicherbereichs |
| 0x0C | 8 | Length | Länge des Speicherbereichs |
| 0x14 | 4 | Type | Typ des Speicherbereichs (1=frei, ansonsten belegt) |

Der Eintrag size sollte dazu verwendet werden zum nächsten Eintrag zu springen.

### mbs_drives_length

Länge der Drives-Liste

### mbs_drives_addr

Pointer zur ersten Drive-Struktur. Eine Drive-Struktur sieht folgendermaßen aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ----------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00 | 4 | size | Größe dieser Drive-Struktur |
| 0x04 | 4 | driver_number | BIOS-Driver-Number |
| 0x08 | 4 | drive_mode | 0 = [CHS](https://github.com/lowlevel-eu/wiki/wiki/Cylinder-Head-Sector "CHS")<br>1 = [LBA](https://github.com/lowlevel-eu/wiki/wiki/Logical-Block-Addressing "LBA") |
| 0x0C | 4 | drive_cylinders | Anzahl an Zylinder, die das Gerät hat |
| 0x0C | 4 | drive_heads | Anzahl an Köpfe, die das Gerät hat |
| 0x0C | 4 | drive_sectors | Anzahl an Sektoren pro Spur, die das Gerät hat |
| 0x10 | size-0x10 | drive_ports | [I/O-Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O-Ports"), die von diesem Gerät benutzt werden |

### mbs_config_table

Eine Tabelle, wie sie vom Get-Configuration-BIOS-Call zurück gegeben wird.

### mbs_boot_loader_name

Pointer zu einem 0-terminated ASCII-String, der den Namen des Bootloades darstellt.

### mbs_apm_table

Pointer zur APM-Tabelle. Die APM-Tabelle sieht so aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ------------- | ------------------------------- |
| 0x00 | 2 | version | Version |
| 0x02 | 2 | cseg | 32bit Codesegment |
| 0x04 | 4 | offset | Offset des Entrypoints |
| 0x08 | 2 | cseg_16 | 16bit Codesegment |
| 0x0A | 2 | dseg | 16bit Datensegment |
| 0x0C | 2 | flags | Flags |
| 0x0E | 2 | cseg_len | Länge des 32bit Codesegments |
| 0x10 | 2 | cseg_16_len | Länge des 16bit Codesegments |
| 0x12 | 2 | dseg_len | Länge des 16bit Datensegments |

## Weblinks

- <http://www.gnu.org/software/grub/manual/multiboot/multiboot.pdf>
- <http://www.uruk.org/orig-grub/boot-proposal.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9829/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1560/index.html)

<!-- MediaWiki page 1560; revision 9829; parent 9823; 2011-06-08T13:58:43Z -->
