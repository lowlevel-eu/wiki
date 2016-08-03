# SurO

| SurO (ehemals SUR-Office) |  |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | [Sur3](https://lowlevel-eu.github.io/wiki/pages/2234/index.html "Benutzer:Sur3") |
| Akt. Version: | 3,5b |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | [by-nc-nd 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/de/) |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86"), geplant: [AMD64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "AMD64"), AVR und [ARM](https://github.com/lowlevel-eu/wiki/wiki/ARM "ARM") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybridkernel |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [ASM](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") |
| API: | \- |
| Binärformat: | .x (eigenes) oder .elf ([ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF")) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

(noch keine)

SurO ist ein HobbyOS, welches durch einen Programmierwettstreit entstanden ist. Version 0.1 war noch eine in QBasic geschriebene DOS-GUI. Version 3,5b ist momentan in Flat-Assembler geschrieben, soll aber dann in Version 3,5c einen eigenen (Meta-)Assemblerdialekt benutzen.

## Screenshot

Intern geschossener Screenshot mit diversen Programmen auf verschiedenen verschobenen Hyperebenen.

[![image.jpg](http://s18.postimg.org/xjxi14945/image.jpg)](http://postimg.org/image/xjxi14945/)

Sichtbare Programme: Datum, Uhrzeit, Tetris, Mandelbrot, Editor mit ASCII-Code des Mandelbrotprogrammes.

## Features

Im Moment sind die folgenden Features implementiert:

- Multitasking (+SMP)
- FAT32 Dateisystem
- Editor (Angucken und Editieren des Arbeitsspeichers oder von Dateien)
- HyperEbenenProjektionsTreiber (Sowas wie Grafikfenster für Programme)
- 1024x768x25 (8881 rgba) Grafik + süßer Fadenkreuzmauszeiger
- Spezielle C-Bibliothek \<surlib.c\> mit Syscalls über Interrupt 35h
- Standard C-Bibliothek mit crt0.c und Linker-Script surlink.lds, welche auf \<surlib.c\> aufbaut
- ElfLoader für Elf-Dateien mit niedriger virtueller Adresse und maximal je einem W- und X-Segment
- XLoader für eigenes .x-Binärformat (36 Byte Header) mit getrenntem Code, Daten und Stacksegment
- Uhr- und Datumsanzeige
- Screenshots im SVM-Format (abgewandeltes PPM-Format, kann in PPM umgewandelt werden)
- Segmentierung und rudimentäres Paging
- Debug-Ausgabe über COM1
- Primitive Audio-Ausgabe über den PC Speaker

## Ladbare Programme \[Programmiersprache - Interface\]

- Tetris \[fasm - int 0x35\]
- Mandelbrot \[C - surlib.h math.h\]
- Hallo Welt \[C - surlib.h oder stdlib.h stdio.h\]
- Schach \[C - stdlib.h stdio.h math.h string.h\]

Ausschnitt aus einer Partie gegen das Schachprogramm auf schwacher Stufe (Denktiefe: 1 fest + 1 adaptiv):

[![schach.png](https://s32.postimg.org/vti2u35tt/schach.png)](https://postimg.org/image/vti2u35tt/)

## Beispiel-Programm für die spezielle C-Bibliothek

\<c\>

1.  include "surlib.h"

void main(){

    sur_HE_erstelle_std();                   //Grafikfenster erstellen
    sur_HE_clear(0x00330011);               //mit aRGB-Wert Füllen
    sur_Eingabe_registriereTasten_AlifNum();        //Alphanumerische Tastatur anfordern
    char cha[2]; cha[1]=0;                  //Nullterminiertes Zeichen
    sur_HE_male_cstring("Hallo",0x4040,0x0000ffff); //schreibe "Hallo" in Türkis auf den Bildschirm
                                 //zweiter parameter ist die Position 0x400*y+x
     sur_Eingabe_warteTaste(cha);               //auf einen Tastendruck warten
     sur_wandle_deKey2ANSI(cha);                //deutschen Tastencode in Schriftzeichen umwandeln
    sur_HE_male_cstring("Welt!",0x4070,0x00ffff00); //schreibe "Welt!" in Gelb auf den Bildschirm
     sur_HE_male_cstring(cha,0x8040,0x0000ff00);        //Gib das Zeichen von der Tastatur in Grün aus
    sur_sys_prog_ende();                    //Beende das Programm

} \</c\> Kompiliert werden kann zum Beispiel in das ELF-Format mit:

    gcc sur_hallo_welt.c -o hallo.elf -m32 -nostdlib -O2 -emain -Wl,-Ttext,0 -Wl,-s -Wl,-N --std=gnu99

## Konzepte

Sogenannte BlockDaten \[BD\] bestehend aus Datenblock-Ketten, diese sollen Systemweit Verwendung finden und ermöglichen Sparse-Files und das schnelle Einfügen durch Zwischenblöcke.

Filter die z.B. zwischen BD und Flat Daten umwandeln können, aber auch Filter die ein Bild rotieren etc. Filter finden vor allem Verwendung in Treiberketten die von dem sogenannten TriebMeister \[TM\] (eine Art Treiberverwaltung nur weitgehender, da sie auch Userprogramme einbinden kann) aufgebaut werden sollen.

Der TriebMeister soll später vermutlich außerdem eine Kompatibilitätsschicht zur Benutzung von CDI erhalten, eventuell über einen einfachen Filter als Zwischenschicht.

AtomPlus-VM-Code der vor dem ausführen in AtomPlus-SemiMaschinen-Code umgewandelt wird, dieser AP-Semi-Code ist eine stark eingeschränke Maschinensprache der jeweiligen CPU, die Einschränkungen sollen garantieren, daß der Code in einer vorgegebenen Zeit terminiert und sicher ist, Sinn des AP-Codes ist es diesen z.B. in den Tastertur- oder Maustreiber zu injezieren um so einfache Aufgaben direkt im Interrupt für das entsprechende Gerät lösen zu können, so können zum Beispiel Buttons beim Hovern mit der Maus die Farbe ändern oder eine Kommandozeile eingegeben werden ohne daß das zugehörige Programm geweckt werden muß, und erst bei komplexeren Aktionen wie einem Klick auf den Button oder einer Autovervollständigung oder dem Drücken der Eingabetaste wird das zugehörige Programm geweckt.

## ToDo

Aktuell wird daran gearbeitet das [SMP](https://github.com/lowlevel-eu/wiki/wiki/Symmetrisches-Multiprozessorsystem "SMP")-Sheduling zu optimieren und das Bearbeiten von Dateien komfortabler zu machen indem BlockDaten und die Grundfunktionen des Texteditors vi implementiert werden.

Außerdem soll das virtuelle Dateisystem \[vDS\] erweitert werden, dieses hat bisher nur rudimentäre Funktionen zum Zugriff auf den [FAT32](https://github.com/lowlevel-eu/wiki/wiki/File-Allocation-Table "FAT")-Treiber.

Zudem sollen der TriebMeister (die Treiberverwaltung) und der [PCI](https://github.com/lowlevel-eu/wiki/wiki/Peripheral-Component-Interconnect "PCI")-Treiber erweitert werden um automatisch Treibermodule laden zu können, welche durch den PCI-Treiber erkannt wurden. Dies ermöglicht die anfolgende Implementation eines [RTL8139](https://github.com/lowlevel-eu/wiki/wiki/RTL8139 "RTL8139")- oder [AC97](https://github.com/lowlevel-eu/wiki/wiki/AC97 "AC97")-Treibers oder auch eines [Common Driver Interfaces](https://github.com/lowlevel-eu/wiki/wiki/Common-Driver-Interface "Common Driver Interface").

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11359/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2233/index.html)

<!-- MediaWiki page 2233; revision 11359; parent 11357; 2016-08-03T19:05:53Z -->
