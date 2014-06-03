# Advanced Encryption Standard Befehlssatzerweiterung

**Advanced Encryption Standard Befehlssatzerweiterung** oder kurz **AESNI** ist eine Erweiterung der x86-Architektur. Die Befehlssatzerweiterung wurde von Intel im März 2008 entwickelt. Sie wurde entwickelt um AES-Verschlüsselungen und -entschlüsselungen zu beschleunigen.

## Unterstützung feststellen

Wenn AESNI von der CPU unterstützt wird, dann ist das Bit 25 im Register ECX gesetzt, nachdem die [CPUID Funktion 0x0000_0001](https://github.com/lowlevel-eu/wiki/wiki/CPUID#funktion-0x0000_0001 "CPUID") aufgerufen wurde.

## Befehle

| Befehl | Beschreibung |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| AESENC | Führt eine Runde in der AES-Verschlüsselung aus. |
| AESENCLAST | Führt die letzte Runde in der AES-Verschlüsselung aus. |
| AESDEC | Führt eine Runde in der AES-Entschlüsselung aus. |
| AESDECLAST | Führt die letzte Runde in der AES-Entschlüsselung aus. |
| AESKEYGENASSIST | Unterstützungsbefehl zur Erzeugung der AES-Rundenschlüssel |
| AESIMC | Unterstützungsbefehl zur AES-spezifischen Berechnung Vorlage:Lang |
| PCLMULQDQ | Übertragsloser Multiplikationsbefehl, welcher im Rahmen der AES-Verschlüsselung Anwendung findet.\<ref\>Vorlage:Cite web\</ref\> |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11208/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2651/index.html)

<!-- MediaWiki page 2651; revision 11208; parent 0; 2014-06-03T15:37:43Z -->
