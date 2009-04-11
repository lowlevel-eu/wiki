# Entwicklungsumgebung

# Vorwort

Leider gibt es verschiedene Ansichten darüber, welche Plattform nun die bessere ist um eine Entwicklungsumgebung einzurichten. Jedoch soll keiner dieser Plattformen zwingend empfohlen werden, bzw. soll auch keine vernachlässigt werden. Daher wird in diesem Artikel zu jeder der in dieser Community verwendeten Plattform sehr nützliche Informationen preisgeben, wie man auf der jeweiligen Plattform am besten vorgeht.

  

# Unter Linux

Unter Linux stehen einige einfach zu benutzenden Tools zum Compilieren bereit, unter anderem gcc/g++ etc. für höhere Sprachen und nasm/gas für Assembler, gelinkt wird üblicherweise mit dem GNU ld, womit sowohl raw binaries als auch ELF-Programme sowie eine breite Auswahl an anderen Formaten erzeugt werden kann. Alle diese Programme sind einfach über den Paketmanager der meisten Distributionen verfügbar. Gleichzeitig gibt es eine sehr breite Auswahl an mächtigen Texteditoren mit Syntax-Highlighting (z.B. gedit, kate, vim, emacs) sowie eine Reihe gute Entwicklungsumgebungen (KDevelop, Anjuta, Code::Blocks(? lässt sich zumindest mit externen Makefiles benutzen)). Für die Entwicklung sowohl mit einem simplen Texteditor als auch mit einer IDE gibt es dabei eine große Anzahl an vorhandenen Build-Systemen, die (üblicherweise basierend auf Makefiles) das Compilieren des OS bei sehr hoher Flexibilität drastisch vereinfachen (Beispiel: CMake).

Das schwierigste ist wohl nun, aus dieser recht hohen Anzahl an Möglichkeiten vor allem bei Editor/Buildsystem die herrauszusuchen, mit der man am besten klar kommt. Für Source-Releases ist es jedoch zumindest sinnvoll, ein von der Kommandozeile aufrufbares Buildsystem bereitzustellen (Makefiles, CMake, autotools), da eine IDE wie Code::Blocks nicht unbedingt weit verbreitet ist, dazu kommen im Vergleich zu den genannten Tools größere Unterschiede zwischen Projektdateien verschiedener Versionen. Alternative: CMake selbst kann Projektdateien für Code::Blocks (noch nicht komplett implementiert) und MSVC erzeugen und kann direkt aus KDevelop eingebunden werden. Nachteil hierbei ist jedoch wieder, dass die CMake-Dateien normalerweise von Hand geschrieben werden müssen, was die Vorteile im Normalfall jedoch aufhebt (TODO: Es gibt eine Menge alternative Systeme zu CMake, ich kenne mich mit ihnen nur nicht aus. Wer sich damit auskennt, sollte diesen Absatz dann gleich auch etwas neutraler formulieren :D).

# Unter Windows

Unser Ziel in diesem Abschnitt ist es, eine Entwicklungsumgebung unter Windows (vorzugsweise XP, da ich auch kein Freund des UserControl von Vista bin) zu schaffen, in der wir unser OS entwickeln können. Abgesehen davon was wir an Tools (Editor, Assembler, Compiler, Linker und Co) benötigen, gibt es auch verschiedene Vorgehensweisen, besser gesagt verschiedene Entwicklungsumgebungen unter Windows.

Wofür wir diese Entwicklungsumgebung brauchen, sollte wohl dieses Wiki schon klar gestellt haben, nämlich die Entwicklung eines Betriebssystem. Um gleich zu Anfang nicht zu kleckern, schaffen wir uns eine Umgebung, mit der wir das gesamte OS von der ersten zeile Code bis zu einem fertigen CD-Image erstellen können.

Aber welche Umgebungen kann man sich nun unter Windows aufbauen?

- Singularity-Modell
- .NET-Framework-Modell
- Microsoft Visual Studio (IDE)
- [Eclipse (IDE)](http://de.wikipedia.org/wiki/Eclipse_(IDE))
- Sonstige, eine auf GCC-Basis

Nun gut, schauen wir mal was Windows da zu bieten hat. OK, die Reaktion war vorherzusehen, mir ging es nicht anders. Windows hinkt leider hinterher, was Entwicklungstools-OnBoard betrifft. Uns fehlt erstens ein guter Editor mit Highlighs, zweites das komplette Sortiment an Assembler, Comiler und Linker. Das alles soll aber kein Beinbruch sein, weshalb wir unser Taschentuch mal ganz schnell wieder beiseite legen. Welche Tools für welche Umgebung benötigt werden, wird in den nun gleich folgenden Unterpunkten genauer erklärt.

### Singularity-Modell

"In Bearbeitung!"

### .NET-Framework-Modell

"In Bearbeitung!"

### Microsoft Visual Studio (IDE)

### Eclipse (IDE)

### Sonstige, eine auf GCC-Basis

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4282/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1810/index.html)

<!-- MediaWiki page 1810; revision 4282; parent 4124; 2009-04-11T11:20:54Z -->
