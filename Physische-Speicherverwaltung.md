# Physische Speicherverwaltung

Die **Physische Speicherverwaltung** bildet die unterste Ebene und ermöglicht das Allozieren und Freigeben von physischen Speicherbereichen. Meist sind diese Speicherbereiche gleich groß und richten sich nach der Seitengröße der jeweiligen Architektur. Die Seitengröße beträgt normalerweise bei der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- und [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Architektur 4kB. Es sind dort auch 4MB ([x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")) bzw. 2MB ([x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86") mit [PAE](https://github.com/lowlevel-eu/wiki/wiki/Physical-Address-Extension "PAE") oder [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")) möglich. Intern speichert die physische Speicherverwaltung welche Speicherbereiche im physischen Speicher frei sind.

Dies könnte folgendermaßen implementiert werden:

## Bitmap

Dabei wird eine Bitmap der Größe *Speichergröße / (Größe einer Speicherseite \* 8)* erstellt. Das x-te Bit dieser Bitmap gibt an ob die x-te Speicherseite (bzw. die Speicherseite an Adresse *Größe einer Speicherseite \* x*) frei oder belegt ist. Beispielsweise benötigt man bei 4GB RAM und 4kB großen Speicherseiten eine 128kB große Bitmap.

### Allokation & Freigabe von Speicherseiten

Um eine Speicherseite zu allozieren wird die Bitmap solange durchsucht, bis man ein Bit mit dem Wert 0 gefunden hat. Dieses Bit setzt man dann auf 1, um anzuzeigen, dass diese Speicherseite ab jetzt belegt ist. Dann errechnet man anhand der Position dieses Bits in der Bitmap die Adresse der Speicherseite. Anschließend kann man die Adresse an die aufrufende Funktion zurückgeben.

Zum Freigeben einer Speicherseite muss nur die Bitposition aus der physischen Adresse berechnet werden und anschließend das Bit an der errechneten Position auf 0 gesetzt werden.

### Implementierungsvorschläge

- Wenn man sich die Bitposition der zuletzt allozierten/freigegebenen Speicherseite merkt, kann man zumindest im Normalfall das Allozieren von Speicherseiten beschleunigen.
- Wenn man beim Allozieren gleich 32 bzw 64 Bit mit dem Wert 0xFFFFFFFF bzw. 0xFFFFFFFFFFFFFFFF vergleicht, kann man mit einem Vergleich gleich 32 bzw. 64 Speicherseiten ausschließen.

### Eigenschaften

\+ Das Allozieren physisch kontinuierlicher Speicherseiten ist möglich. (lineare Komplexität)  
o Die Bitmap ist relativ klein.  
o Das Freigeben einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
- Zum Allozieren einer Speicherseite muss im schlechtesten Fall die gesamte Bitmap durchsucht werden. (lineare Komplexität)  

## Stack

Die Adressen der Speicherseiten werden hierbei auf einen Stack gelegt.

### Allokation & Freigabe von Speicherseiten

Zum Allozieren einer Speicherseite wird einfach die Adresse, die ganz oben auf dem Stack liegt, genommen. Anschließend wird der Zeiger auf das Stackende angepasst. Das Freigeben einer Speicherseite exakt umgekehrt zur Allokation.

### Implementierungsvorschlag

Der Speicher, der für den Stack benutzt wird, wird aus den Speicherseiten, die auf den Stack gelegt werden sollen, erstellt. Dies kann folgendermaßen implementiert werden: Beim Start des Kernels ist der Stack erstmal leer. Desweiteren ist nur ein virtueller und kein physischer Speicherbereich für den Stack reserviert. Anschließend geht man die freien Speicherbereiche durch und legt jede freie Speicherseite auf den Stack. Da der Stack bei der ersten Speicherseite noch keinen Speicherbereich hat, nimmt man einfach diese Seite und blendet in den virtuellen Adressraum an der Adresse des Stacks ein. Anschließend können die Adressen einiger Speicherseiten auf den Stack gelegt werden, solange bis wieder kein Speicher vorhanden ist. Dann wird einfach die nächste Speicherseite, die auf den Stack gelegt werden soll, in den virtuellen Adressraum ein.

Das kann man beim Freigeben natürlich analog implementieren und Speicherseiten, die in den virtuellen Adressraum eingeblendet waren, wieder freigeben, falls dieser Speicherbereich nicht mehr vom Stack selbst benötigt wird. Somit verbraucht der Stack im Prinzip "keinen" Speicher.

### Eigenschaften

\+ Das Allozieren einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
+ Der Stack verbraucht keinen Speicher.  
o Das Freigeben einer Speicherseite ist in konstanter Zeit möglich. (konstante Komplexität)  
- Das Allozieren physisch kontinuierlicher Speicherseiten ist unmöglich.  

## verkette Liste

Die Elemente der Liste sind dabei (freie, physisch zusammenhängende) Speicherbereiche, d.h. Zeiger auf den Beginn des Speicherbereichs und Länge des Speicherbereichs. Diese Liste benötigt allerdings ein malloc/free, um Speicher für die Listenelemente zu allozieren, d.h. diese Art der Speicherverwaltung kann nur für einen Teil des Speichers genutzt werden.

### Allokation & Freigabe von Speicherseiten

Zum Allozieren von Speicherseiten wird die Liste solange durchsucht bis ein ausreichend großer Speicherbereich gefunden ist. Falls der zu allozierende Speicherbereich exakt so groß wie der gefundene ist wird das Listenelemente entfernt, andernfalls die Größe angepasst. Beim Freigeben wird - falls dies möglich ist - zuerst versucht der freizugebende Speicherplatz in eines der vorhandenen Listenelemente einzubauen, was natürlich nur geht, wenn das freizugebende physisch genau davor bzw. genau dahinter liegt. Andernfalls wird ein neues Listenelement erzeugt und passend initialisiert.

### Eigenschaften

\+ Das Allozieren von physisch kontinuierlichen Speicherseiten ist möglich.  
- Das Allozieren eines (physisch kontinuierlichen) Speicherbereichs oder einer Speicherseite ist in linearer Zeit möglich.  
- Freigeben eines Speicherbereichs oder einer Speicherseite ist in linearer Zeit möglich.  
- Es wird ein darunterliegendes malloc/free benötigt.  

Das sieht natürlich für die verkettete Liste erstmal schlecht aus, aber nach Erfahrung von [Bluecode](https://lowlevel-eu.github.io/wiki/pages/1489/index.html "Benutzer:Bluecode") eignet sie sich perfekt zum Verwalten eines Speicherbereichs für Allokationen von physisch kontinuierlichem Speicher, da solche Allokationen sehr selten und deswegen die Liste nicht sonderlich groß ist. Der Rest des Speichers könnte den über einen wie oben beschriebenen Stack verwaltet werden.

## Buddy

Beim Buddy Verfahren wird Speicher ausschließlich in verschiedenen festgelegten Größen allokiert, wobei diese Blöcke auf ein vielfaches ihrer Größe ausgerichtet sind. Für jede Größe existiert eine Menge mit freien Blöcken ("free list"), von denen einer gewählt wird, um die Anfrage zu erfüllen. Existiert kein freier Block der angeforderten Größe, wird ein Block der nächstgrößeren verfügbaren Größe gewählt und geteilt, wobei die ungenutzte Hälfte wieder in die entsprechende Freelist eingetragen wird. Jede Hälfte eines derartig geteilten Blocks ist der Buddy von der jeweils anderen Hälfte.

Gibt man Speicher wieder frei, so will man zwei direkt nebeneinander liegende freie Blöcke wieder zu einem großen freien Block zusammenfügen. Damit man dafür nicht die free list durchsuchen muss, was relativ aufwändig ist, verwaltet man für jede Blockgröße in einer Bitmap den Status eines Blocks. Ein Block wird nur mit seinem Buddy wieder zusammengefügt.

### Allokation & Freigabe von Speicherseiten

### Implementierungsvorschlag

- Für die Blockgrößen wählt man in der Regel Potenzen von 2 beginnend mit der Größe einer Seite (4 KiB), bis zu einem bestimmten sinnvollen Wert (z.B. 4 MiB).
- Da in jeder Menge nur gleich große Blöcke sind, kann man diese als verkettete Liste implementieren und beim Allokieren einfach immer das erste Listenelement nehmen. (First Fit -\> konstanter Zeitaufwand)

### Eigenschaften

\+ Schnelle Reservierung von Speicherseiten  
+ Schnelle Freigabe von Speicherseiten  
- Recht komplizierte Implementierung  
- Allokierbare Größen sind auf bestimmte Werte eingeschränkt, damit anfällig für interne Fragmentierung  

## Fazit

Zusammenfassend lässt sich festhalten, dass eine Kombination aus den oben erklärten Datenstrukturen das Beste sein wird. Die Bitmap hat den Vorteil, dass man physisch kontinuierlichen Speicher allozieren kann. Dies benötigt man vor allem für [DMA](https://github.com/lowlevel-eu/wiki/wiki/Direct-Memory-Access "DMA"). Das heißt es macht Sinn bei der [x86](https://github.com/lowlevel-eu/wiki/wiki/X86 "X86")- bzw. [x86-64](https://github.com/lowlevel-eu/wiki/wiki/X86-64 "X86-64")-Architektur die unteren 1/16MB mit einer Bitmap zu verwalten. Der Stack hingegen hat einen unschlagbaren Geschwindigkeits- und Speichervorteil und kann für den Rest des Speichers verwendet werden.

## Initialisierung

Unabhängig von der Wahl der Speicherstruktur muss diese relativ früh im Kernel initialisiert werden, d.h. alle beim Start verfügbaren Bereiche müssen als frei und alle anderen als besetzt markiert werden. Außerdem möchte man unter Umständen noch einen freien Platz für die Bitmap/den Stack suchen, bevor man die freien und reservierten Bereiche überhaupt eintragen kann. (Wenn man nicht so penibel ist, tut es im Allgemeinen aber auch ein fest vordefinierter Platz im Speicher.)

Die einfachste, intuitiv oft gewählte und falsche Methode zur Initialisierung ist, die Speichergröße (vom [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") oder der [Multiboot](https://github.com/lowlevel-eu/wiki/wiki/Multiboot "Multiboot")-Struktur) herzunehmen und genau soviel Speicher als frei zu markieren. Stattdessen sollte man die Informationen aus der Memory Map des BIOS bevorzugen, die unter anderem alle freien Speicherbereiche mit Startadresse und Länge aufzählt. Die Memory Map wird auch von [GRUB](https://github.com/lowlevel-eu/wiki/wiki/Grand-Unified-Bootloader "GRUB") in der Multiboot-Struktur übergeben, siehe dazu die Felder [mbs_mmap\_\*](https://github.com/lowlevel-eu/wiki/wiki/Multiboot#mbs_mmap_length "Multiboot").

Anschließend sollte man nicht vergessen, weitere Bereiche als reserviert zu markieren, die z.B. bereits vom Kernel selbst genutzt werden und nicht überschrieben werden sollten. Typischerweise sind das:

- Der Kernel
- Die Multiboot-Struktur
- Von GRUB geladene Kernelmodule und ihre Kommandozeile
- Die Speicherverwaltungsstrukturen selbst, also z.B. der Platz, den die Bitmap einnimmt

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9425/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1843/index.html)

<!-- MediaWiki page 1843; revision 9425; parent 6813; 2011-02-04T21:35:03Z -->
