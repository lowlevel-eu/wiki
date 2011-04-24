# LF OS

| LF OS (LittleFox' Operating System oder Light & Fast Operating System) |  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
|  |  |
| Entwickler: | LittleFox |
| Akt. Version: | 1.0 Alpha 5 / Kernel2 |
| [Lizenz](https://github.com/lowlevel-eu/wiki/wiki/Lizenzen "Lizenzen"): | NewBSD |
| OS-Eigenschaften |  |
| Plattform: | [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") |
| [Kernelart](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel"): | Hybridkernel (Mikromonolith ;)) |
| [Sprache](https://lowlevel-eu.github.io/wiki/pages/1648/index.html "Kategorie:Programmiersprache"): | [C](https://github.com/lowlevel-eu/wiki/wiki/C "C"), [C++](https://github.com/lowlevel-eu/wiki/wiki/C%2B%2B "C++") |
| API: | Nativ, DarkblackAPI, evt. POSIX |
| Binärformat: | [ELF](https://github.com/lowlevel-eu/wiki/wiki/Executable-and-Linking-Format "ELF") |
| [IPC-Methode](https://github.com/lowlevel-eu/wiki/wiki/Interprozesskommunikation "IPC"): | \- |
| Homepage |  |

<http://www.lf-os.tk> (englisch)  
[http://littlefox.web-fuxx.de](http://littlefox.web-fuxx.de/newSite/lf_os.php) (deutsch)

  
LF OS ist ein weiteres Hobbybetriebssystem das in C und Assembler programmiert ist.

Folgende Features sind bereits implementiert:

- Basics (GDT, IDT, IRQ Handler, Speaker ...)
- Tastaturtreiber
- VESA Grafikmodus (von GRUB initialisiert)
- eine einfachste Shell (auch im VESA Modus, Schriftart vorhanden)
- Physische Speicherverwaltung
- ELF-Loader
- Multitasking im Usermode
- eine einfachste API
- Maustreiber (scheint zu funktionieren ... ;))
- Floppy Treiber

Folgende Features sind momentan in Arbeit:

- Paging
- FAT 12

Folgende Features fehlen noch:

- Dateizugriffe (Speichergeräte, Dateisysteme ...)
- Klickibunti-Oberfläche
- ein Treiberinterface (Planung bereits fertig)

Momentan wird LF OS (wiedereinmal) komplett neu geschrieben, womit ich dann bei Kernel 3 wäre. Als Sprache wird diesmal C++ verwendet. Außerdem versuch ich mich jetzt mal ein meine Roadmap zu halten ;). Alles was oben an Features steht, gilt nur für den Kernel 2.

Sollte es Fragen geben, können diese gerne im LF OS Forum gestellt werden. Die englische Version unter <http://www.lf-os.tk> ~~spinnt manchmal etwas~~ (sollte behoben sein ...), die deutsche unter <http://littlefox.web-fuxx.de> funktioniert in der Regel.

Falls mich jemand unterstützen möchte, kann er sich gerne per PM oder [E-Mail](mailto:littlefox@web-fuxx.de) bei mir melden. Ich werde wahrscheinlich nicht nein sagen, da ein wenig Unterstützung nicht schlecht wäre.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9717/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2267/index.html)

<!-- MediaWiki page 2267; revision 9717; parent 9716; 2011-04-24T14:53:05Z -->
