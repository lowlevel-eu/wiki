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
| Binärformat: | .x (eigenes) |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

(noch keine)

SurO ist ein HobbyOS, welches durch einen Programmierwettstreit entstanden ist. Version 0.1 war noch eine in QBasic geschriebene DOS-GUI. Version 3,5b ist momentan in Flat-Assembler geschrieben, soll aber dann in Version 3,5c einen eigenen (Meta-)Assemblerdialekt benutzen.

## Screenshot

Intern geschossener Screenshot mit diversen Programmen auf verschiedenen verschobenen Hyperebenen.

[![image.jpg](http://s18.postimg.org/xjxi14945/image.jpg)](http://postimg.org/image/xjxi14945/)

Von Oben nach Unten: Datum, Uhrzeit, Tetris, Mandelbrot, Editor mit ASCII-Code des Mandelbrotprogrammes.

## Features

Im Moment sind die folgenden Features implementiert:

- Multitasking (+SMP)
- FAT32 Dateisystem
- Editor (Angucken und Editieren des Arbeitsspeichers oder von Dateien)
- HyperEbenenProjektionsTreiber (Sowas wie Grafikfenster für Programme)
- 1024x768x25 (8881 rgba) Grafik + süßer Fadenkreuzmauszeiger
- kleine C-Bibliothek \<surlib.c\> über Interrupt 35h
- Uhr- und Datumsanzeige
- Screenshots im SVM-Format (abgewandeltes PPM-Format, kann in PPM umgewandelt werden)

## Ladbare Programme \[Programmiersprache\]

- Tetris \[fasm\]
- Mandelbrot \[C\]
- Hallo Welt \[C\]

## Beispiel-Programm für die zugehörige C-Bibliothek

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

} \</c\> Kompiliert wird in ein Binärformat mit:

    gcc sur_hello_world.c -o hello.x -m32 -nostdlib -O2 -emain -Wl,-Ttext,0 -Wl,--oformat,binary --std=gnu99

## ToDo

Aktuell wird daran gearbeitet das Sheduling zu optimieren und das Bearbeiten von Dateien komfortabler zu machen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11295/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2233/index.html)

<!-- MediaWiki page 2233; revision 11295; parent 11294; 2015-10-09T00:25:02Z -->
