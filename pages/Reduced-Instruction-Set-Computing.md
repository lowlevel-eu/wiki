# Reduced Instruction Set Computing

Das **Reduced Instruction-Set Computing** (englisch, in etwa *Arbeiten mit reduziertem Befehlssatz*, kurz **RISC**) bezeichnet ein Prozessordesign, welches sich dadurch auszeichnet, mit reduziertem und einfacherem Befehlssatz zu arbeiten. Dem entgegen steht das [Complex Instruction-Set Computing](Complex-Instruction-Set-Computing "CISC").

  

## Idee

Die Idee hinter RISC steckt darin, mit einem reduzierten und somit optimierten Befehlssatz zu arbeiten, der weniger Anforderungen an CPU und Peripherie stellt und dennoch alle nötigen Aufgaben erfüllen kann sowie auf komplexe Befehle und Befehlsabfolgen zu verzichten. Somit sind einzelne Befehle bzw. Einzelbefehle einfacher und schneller ausführbar, was zu schnelleren Abläufen und einer allgemein schnelleren Abarbeitung führt und somit auch zu einer geringeren Stromaufnahme. Somit findet „der“ RISC (im Sinne vom reduzierten Befehlssatz, deshalb „der“) vor allem in Mikrocomputern und Kleinstelektrogeräte Verwendung. [ARM](ARM "ARM")-Prozessoren sind ein Beispiel für RISC-Prozessoren.

  

## Eigenschaften

RISC-Systeme zeichnen sich vor allem durch einen erhöhten Satz an *General-Purpose*-Registern (Allzweckregister) aus, da diese vermehrt für Zwischenergebnisse genutzt werden. Somit fällt auch das von der x86-Architektur bekannte *pushen/poppen* aus, da Werte einfach in Register zwischengespeichert werden können, anstatt auf den Stack zu verschieben. Der Zugriff auf Speicher erfolgt *ausschließlich* mit den Befehlen LOAD und STORE, alle anderen Befehle arbeiten auf Registeroperanden. Auch sind die Befehle von RISC-Prozessoren immer gleich breit und das „Basisset“ immer das Gleiche.

  

## Weblinks

- [RISC im Elektronik-Kompendium](http://www.elektronik-kompendium.de/sites/com/0501011.htm)
- [RISC OS – Betriebssystem auf RISC-Basis](http://www.operating-system.org/betriebssystem/_german/bs-riscos.htm)
- [RISC versus CISC](http://www.weblearn.hs-bremen.de/risse/RST/assign02/Intel/risccisc.html)

## Siehe auch

- [ARM](ARM "ARM")
- [x86](X86 "X86")
- [CISC](Complex-Instruction-Set-Computing "CISC")

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9386/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2108/index.html)

<!-- MediaWiki page 2108; revision 9386; parent 9384; 2011-01-25T00:33:03Z -->
