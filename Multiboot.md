# Multiboot

Multiboot ist ein Standard um Betriebssystemen eine einheitliche Startumgebung zu gewährleisten. Ein sehr bekannter Multiboot-Bootloader ist Grub.

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

### mbh_magic

Dient Grub zum Finden des Multiboot-Headers. Sollte immer 0x1BADB002 sein.

### mbh_flags

Bits 0-15 sind Flags die umbedingt benötigt werden. Wenn der Bootloader eines dieser Flags nicht kennt, bricht er den Bootvorgang ab. Bits 16-31 sind optionale Flags. Es gibt die folgenden Flags

| Bit | Auswirkung |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0 | Module werden 4k-aligned geladen |
| 1 | Ermittelt [mbs_mem_lower](#mbs_mem_lower) und [mbs_mem_upper](#mbs_mem_upper). Wenn möglich auch [mbs_mmap_length](#mbs_mmap_length) und [mbs_mmap_addr](#mbs_mmap_addr) |
| 16 | Informationen über das OS-Image werden aus den Feldern 0x0C-0x1C des Multiboot-Headers entnommen. |

### mbh_checksum

Ein u32-Wert der Zusammen mit [mbh_magic](#mbh_magic) und [mbh_flags](#mbh_flags) 0 ergeben soll. Man kann ihn so berechnen:

    -(mbh_magic + mbh_flags)

## Multiboot-Structure

Die Multiboot-Structure beinhaltet Informationen, die vom Bootloader verher ausgelesen wurden. Die Adresse der Multiboot-Structure ist unmittelbar nach dem Starten des Kernels in *EBX* gespeichert.

| Offset | Größe | Inhalt | Anwesend wenn mbs_flags\[X\] gesetzt |
| -------- | ------- | ------------------------------------- | -------------------------------------- |
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

Gibt an wie viele Module von Grub geladen wurden

### mbs_mods_addr

Pointer auf die erste Modulstruktur. Eine Modulstruktur sieht folgendermaßen aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ----------- | ------------------------------------------------------------------------- |
| 0x00 | 4 | mod_start | Adresse an der das Modul liegt |
| 0x04 | 4 | mod_end | Adresse an der das Modul endet |
| 0x08 | 4 | string | Pointer zu einem 0-term. ASCII-String, der den Namen des Moduls enthält |
| 0x0C | 4 | reserved | Reserviert (0) |

### mbs_syms

Wenn Bit 4 in [mbs_flags](#mbs_flags) gesetzt ist, liegt diese Struktur am Offset 0x1C und enthält Informationen zur Symboltabeööe einer a.out-Datei

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ---------- | --------------------------- |
| 0x1C | 4 | tabsize |  |
| 0x20 | 4 | strsize |  |
| 0x24 | 4 | addr | Pointer zur Symboltabelle |
| 0x28 | 4 | reserved | Reserviert (0) |

Wenn Bit 5 in [mbs_flags](#mbs_flags) gesetzt ist, liegt diese Struktur am Offset 0x1C und enthält Information zur Symboltabelle einer Elf-Datei

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ------- | --------------------------- |
| 0x1C | 4 | num | Anzahl an Einträgen |
| 0x20 | 4 | size | Größe eines Eintrags |
| 0x24 | 4 | addr | Pointer zur Symboltabelle |
| 0x28 | 4 | shndx |  |

### mbs_mmap_length

Gibt die Länge der Memorymap an

### mbs_mmap_addr

Pointer zur Memorymap. Ein Eintrag in der Memorymap sieht folgendermaßen aus:

| Offset | Größe | Name | Beschreibung |
| -------- | ------- | ---------- | ----------------------------------- |
| -0x04 | 4 | size | Gibt die Größe des Eintrags an |
| 0x00 | 8 | BaseAddr | Basisadresse des Speicherbereichs |
| 0x08 | 8 | Length | Länge des Speicherbereichs |
| 0x10 | 4 | Type | Typ des Speicherbereichs |

## Weblinks

- <http://www.gnu.org/software/grub/manual/multiboot/multiboot.pdf>
- <http://www.uruk.org/orig-grub/boot-proposal.html>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2462/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1560/index.html)

<!-- MediaWiki page 1560; revision 2462; parent 2460; 2007-12-21T15:26:17Z -->
