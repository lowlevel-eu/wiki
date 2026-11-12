# Entwicklungsumgebung

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

## Vorwort

Leider gibt es verschiedene Ansichten darüber, welche Plattform nun die bessere ist um eine Entwicklungsumgebung einzurichten. Jedoch soll keiner dieser Plattformen zwingend empfohlen werden, bzw. soll auch keine vernachlässigt werden. Daher wird in diesem Artikel zu jeder der in dieser Community verwendeten Plattform sehr nützliche Informationen preisgeben, wie man auf der jeweiligen Plattform am besten vorgeht.

  

## Unter Linux

Unter [Linux](Linux.md "Linux") stehen einige einfach zu benutzenden Tools zum Compilieren bereit, unter anderem [gcc](GNU-Compiler-Collection.md "GNU Compiler Collection")/g++ etc. für höhere Sprachen und [nasm](Netwide-Assembler.md "Netwide Assembler")/gas für [Assembler](Assembler.md "Assembler"), [gelinkt](Linker.md "Linker") wird üblicherweise mit dem GNU ld, womit sowohl raw binaries als auch ELF-Programme sowie eine breite Auswahl an anderen Formaten erzeugt werden kann. Alle diese Programme sind einfach über den Paketmanager der meisten Distributionen verfügbar. Gleichzeitig gibt es eine sehr breite Auswahl an mächtigen [Texteditoren](Editor.md "Editor") mit Syntax-Highlighting (z.B. gedit, kate, vim, emacs) sowie eine Reihe gute Entwicklungsumgebungen (KDevelop, Anjuta, Code::Blocks(? lässt sich zumindest mit externen [Makefiles](Makefile.md "Makefile") benutzen)). Für die Entwicklung sowohl mit einem simplen Texteditor als auch mit einer IDE gibt es dabei eine große Anzahl an vorhandenen Build-Systemen, die (üblicherweise basierend auf Makefiles) das Compilieren des OS bei sehr hoher Flexibilität drastisch vereinfachen (Beispiel: CMake).

Das schwierigste ist wohl nun, aus dieser recht hohen Anzahl an Möglichkeiten vor allem bei Editor/Buildsystem die herrauszusuchen, mit der man am besten klar kommt. Für Source-Releases ist es jedoch zumindest sinnvoll, ein von der [Kommandozeile](Shell.md "Kommandozeile") aufrufbares Buildsystem bereitzustellen (Makefiles, CMake, autotools), da eine IDE wie Code::Blocks nicht unbedingt weit verbreitet ist, dazu kommen im Vergleich zu den genannten Tools größere Unterschiede zwischen Projektdateien verschiedener Versionen. Alternative: CMake selbst kann Projektdateien für Code::Blocks (noch nicht komplett implementiert) und MSVC erzeugen und kann direkt aus KDevelop eingebunden werden. Nachteil hierbei ist jedoch wieder, dass die CMake-Dateien normalerweise von Hand geschrieben werden müssen, was die Vorteile im Normalfall jedoch aufhebt (TODO: Es gibt eine Menge alternative Systeme zu CMake, ich kenne mich mit ihnen nur nicht aus. Wer sich damit auskennt, sollte diesen Absatz dann gleich auch etwas neutraler formulieren :D).

## Unter Windows

Auch [Windows](Windows.md "Windows") bietet eine Fülle an Entwicklungsumgebungen, mit denen sich hervorragend entwickeln lässt

Eine Auswahl:

- Microsoft Visual Studio (IDE)
- [Eclipse (IDE)](http://de.wikipedia.org/wiki/Eclipse_(IDE))
- Code::Blocks
- DevCpp

Da das Hauptklientiel von Windows nicht der Programmierer, sondern der "Otto-Normal-User" ist, bietet Windows dementsprechend keine bzw. nur wenige Entwicklungstools von sich aus mit. Dem neuen OS-Developer stehen am Anfang nichts weiter als der gute alte Notepad zur Verfügung. Zum Glück sieht die Situation heute besser aus als vor Jahren: Viele wichtige Tools wurden portiert oder für Windows neu entwickelt:

- [DJGPP](http://delorie.com) (Windows-Port von gcc)
- MinGw
- Cygwin

Mitsamt den Tools hat man fast die gleichen Voraussetzungen wie unter Linux.

## Singularity-Modell

Eine Umgebung wie diese macht nur Sinn, wenn mein sein OS wie Singularity mit Managed-Code (wie C#) entwickeln möchte. Hierfür ist Singularity ein gutes Modell, an dem man sich gut orientieren kann, sofern man einmal richtig durchgeblickt hat. Sich die Dokus von Singularity anzuschauen kann keineswegs verkehrt sein. Doch wenn man sich Singularity mal genauer anschaut, ist das eher ein Sprachenwirrwarr, Assembler, C (glaube auch C++), C# und Sing#/Spec#.

Lassen wir uns nicht davon beirren, was wir brauchen sind eher die Build-Tools. Ja ja, hab ich auch gesehen, kein Editor. Naja, ein echter Hardcore-Freak kommt auch mit einem Highlight-losen Editor zurecht ... ich eher weniger. Aber hier kann man ja entweder auf Microsoft Visual Studio Express oder auf Notepad++ setzen, beiden natürlich kostenlos. Notepad++ wird zwar von vielen empfohlen, wer aber zu denen gehört, die gerne ihr Listing ausdrucken, dem empfehle ich die Visual Studio IDE, da Notepad++ meinen Geschmack nach zu verschwenderisch mit Papier um geht. Aber es soll jeder selbst entscheiden, welchen Editor er nutzen möchte.

Auf die Frage, ob wir noch einen Assembler, Compiler oder Linker benötigen ... nöööö, ist alles in den Build-Tools von Singularity zu finden, egal ob 16, 32 oder 64 Bit. Was uns aber fehlt, ist die eigentliche .NET-Framework Build-Umgebung, welche aber Bestandteil des .NET-Frameworks ist. Aktuell ist derzeit die Version 3.5 SP1, welche zwar schon bei Windows 7 mit bei ist, jedoch bei den Vorgängerversionen nachinstalliert werden müsste. Version 2.0 würde zwar auch ausreichen, da wir ja eigentlich ja nur den Builder (MSBuild.exe) brauchen.

OK, was benötigen wir nun alles. Die folgende Liste enthält alle nützlichen Links:

- [Microsoft Singularity RDK 2.0](http://www.codeplex.com/singularity/)
- [Microsoft .NET-Framework v3.5](http://www.microsoft.com/downloads/details.aspx?FamilyID=333325fd-ae52-4e35-b531-508d977d32a6&DisplayLang=de)
- [Microsoft Visual Studio 2008 Express](http://www.microsoft.com/germany/express/)
- [Notepad++](http://notepad-plus.sourceforge.net/de/site.htm)
- [Microsoft Windows-Debugger x86/x64 für Kernel-Debug](http://www.microsoft.com/whdc/devtools/debugging/default.mspx)
- [Microsoft Virtual PC 2007 inkl. SP 1](http://www.microsoft.com/downloads/details.aspx?FamilyID=28c97d22-6eb8-4a09-a7f7-f6c7a1f000b5&DisplayLang=de)

### .NET-Framework-Modell

"In Bearbeitung!"

### Microsoft Visual Studio (IDE)

### Eclipse (IDE)

### Sonstige, eine auf GCC-Basis

## Code::Blocks

[Code::Blocks](http://www.codeblocks.org) ist eine Entwicklungsumgebung für die Sprachen [C](C.md "C") und [C++](C%2B%2B.md "C++"). Die Syntaxhervorhebung beherrscht jedoch auch zahlreiche weitere Sprachen, etwa [Assembler](Assembler.md "Assembler"), [D](D.md "D"), [Ada](Ada.md "Ada"), Haskell und viele weitere. Code::Blocks bringt standartmäßig keinen Compiler mit, es wird jedoch so gut wie jeder aktuelle Compiler unterstützt:

- GNU Compiler Collection
- Digital Mars D Compiler
- Tiny C Compiler
- Intel C/C++ Compiler
- ...

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10865/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1810/index.html)

<!-- MediaWiki page 1810; revision 10865; parent 5184; 2012-09-22T16:09:14Z -->
