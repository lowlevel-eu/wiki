# LILO

LILO, der **Li**nux **Lo**ader, ist ein englischsprachiger [Bootloader](https://github.com/lowlevel-eu/wiki/wiki/Bootloader "Bootloader") für [Linux](https://github.com/lowlevel-eu/wiki/wiki/Linux "Linux"), der jedoch auch andere Betriebssysteme starten kann. Er war lange der Standard-Bootloader unter Linux, ehe er allmählich von [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") abgelöst wurde.

## Technik

LILO ermittelt die zu ladenen Blöcke eines Kernels und lädt genau diese darauf beim Booten in den Arbeitsspeicher.

## Vorteile

Der Vorteil von LILO ist genau das ermitteln der benötigten Blöcke: Es werden keine Dateisystemtreiber oder Sonstiges benötigt, sodass der Bootloader einfach und klein gehalten werden kann.

## Nachteile

Nach dem Erstellen eines neuen Linux-Kernels muss zuerst der Befehl *lilo* ausgeführt werden, da LILO erst die zu ladenden Blöcke ermitteln muss.

  

## Weblinks

- [LILO-Homepage](http://lilo.alioth.debian.org/)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10676/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1776/index.html)

<!-- MediaWiki page 1776; revision 10676; parent 10004; 2012-08-15T17:00:38Z -->
