# Versionsverwaltung

Versionsverwaltungen machen das Leben einfacher. Nicht nur für Betriebssystementwickler, sondern auch für jede andere Entwicklungsart. Nicht nur für Einzelpersonen, sondern auch und insbesondere für Gruppen. Doch wie?

# Hauptaufgaben

Eine Versionsverwaltung erfüllt eine handvoll nützliche Aufgaben, die Entwicklern das Leben leichter machen.

- Protokollierung der Änderung. Jede Änderung am Quelltext kann nachvollzogen werden, egal von wem, an was, oder wieso.
- Wiederherstellung und Archivierung von Entwicklungsständen. So ist es möglich, bestimmte Versionen von Dateien oder ganzen Verzeichnisbäumen wiederherzustellen, oder auf anhieb einem Namen einen bestimmten Zustand zuzuordnen (siehe [Tagging](https://github.com/lowlevel-eu/wiki/wiki/Versionsverwaltung "Versionsverwaltung")).
- Koordinieren von gemeinsamen Zugriffen. Gleichzeitige Änderungen von mehreren Entwicklern werden verhindert, oder erleichtert.
- Koordinieren von Entwicklungszweigen, z.B. wenn eine alte Funktionalität komplett ersetzt werden soll, aber der Hauptzweig während dieser Änderung weiterhin ungestört funktionieren soll.

# Mechanismen

Diese Aufgaben können auf verschiedene Arten umgesetzt werden. Dabei unterscheidet sich insbesondere, wie die Versionsverwaltung aufgebaut ist. Mögliche Varianten:

- **Lokale Versionsverwaltungen** laufen auf dem Entwicklerrechner. Fremdentwickler gibt es hierbei in der Regel nicht, eine Koordination zwischen Entwicklern ist nicht nötig.
- **Zentrale Versionsverwaltungen** setzen in der Regel einen Server voraus. Entwickler spiegeln sich einen Entwicklungsstand auf ihr System, um daran zu arbeiten (sog. checkout), der Server behält dabei keinerlei Informationen über lokale Kopien. Nach den Änderungen werden die neuen Versionen wieder auf den Server übertragen (sog. commit). Oft wird hierbei auch eine Rechtekontrolle vorgenommen, so dass nicht jeder seine Änderungen direkt eintragen kann, aber öffentliches Lesen möglich ist. Verbreitete Beispiele für diese Variante sind [Subversion](https://github.com/lowlevel-eu/wiki/wiki/Subversion "Subversion") und [CVS](https://github.com/lowlevel-eu/wiki/wiki/Concurrent-Versions-System "CVS").
- **Dezentralisierte Versionsverwaltungen** sind quasi die Hybriden. Jeder Entwickler hält eine komplette Kopie der gesamten Versionshistorie vorrätig, wie bei einer Lokalen Verwaltung. Aber im Gegensatz hierzu können Änderungen auch direkt in fremde Systeme übertragen werden. Populäres Beispiel ist [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git").

# Konzepte

Das arbeiten mit einer Versionsverwaltung basiert auf gewissen Konzepten, welche hier näher erläutert werden sollen.

## Lock-Modify-Write

Lock-Modify-Write ist quasi der ursprüngliche Arbeitsvorgang mit einer Versionsverwaltung unter mehreren Benutzern. Wenn ein Entwickler etwas ändern will, markiert er die Datei auf der zentralen Verwaltung als gesperrt (sog. lock). Dann kann er alle Änderungen nach seinen Wünschen durchführen, andere Entwickler bekommen während der Lock besteht keinen Schreibzugriff auf betroffene Objekte. Nach Abschluss der Arbeiten werden die Änderungen zurückübertragen und der Lock aufgehoben. Nun können wieder andere an der Datei arbeiten.

## Copy-Modify-Merge

Copy-Modify-Merge ist die Alternative zu Lock-Modify-Write. Jedem Entwickler wird direkt gestattet an seiner lokalen Kopie Änderungen durchzuführen. Beim zurückübertragen der Änderungen prüft die Verwaltung selbstständig ob es Kollisionen zwischen den Änderungen gibt. Ist dies der Fall wird dies dem späteren Entwickler zusammen mit den vorherigen Änderungen gemeldet dass der Vorgang abgebrochen werden muss. Der Entwickler hat dann die Gelegenheit seine und die fremden Änderungen in Einklang zu bringen (Merge), um eine neue Version übertragen zu können. Manche Versionsverwaltungen versuchen auch mehrere Änderungen alleine in Einklang zu bringen, was allerdings nicht immer funktioniert. Vorteil ist, das problemlos mehrere Entwickler auch den gleichen Quelltext bearbeiten können - solange jeder an einem anderen Teil arbeitet und es nicht zu Änderungen an der gleichen Codestelle kommt.

## Branching und Tagging

Branching und Tagging sind die Konzepte die sich mit der Koordinierung verschiedener Entwicklungszweige und spezifischen Versionen beschäftigen.

- **Branching** wird verwendet, um größere Änderungen einzuführen. Es wird ein neuer Branch gebildet, der den gesamten bisherigen Quelltext enthält. Hier können größere Bereiche rundumerneuert werden, ohne dass andere Entwickler im Hauptentwicklungszweig (trunk) mit Problemen zu rechnen haben. Sind die Änderungen abgeschlossen, wird der Branch in den Hauptzweig überführt, dabei auftretende Probleme (z.B. durch eine geänderte API) sollten dabei behoben werden (Merge).
- **Tagging** bezeichnet den Vorgang, einem bestimmten Entwicklungszustand einen gewählten Namen zu verleihen. Dies wird insbesondere bei Veröffentlichungen gemacht. Generell sollte ein Tag nicht nachträglich geändert werden, falls dies doch notwendig ist, sollten nur Bugfixes vorgenommen werden, keinesfalls aber neue Features hinzugefügt werden.

# Systeme

Momentan (Stand Anfang 2009)) sind die meistgenutzten Systeme im OpenSource-Bereich [git](https://github.com/lowlevel-eu/wiki/wiki/Git "Git") und [Subversion](https://github.com/lowlevel-eu/wiki/wiki/Subversion "Subversion"), selten trifft man auch noch auf das etwas ältere [CVS](https://github.com/lowlevel-eu/wiki/wiki/Concurrent-Versions-System "CVS"). Dabei sind sowohl Subversion als auch CVS für einen Zentralen Aufbau ausgelegt (können aber auch lokal gut verwendet werden), git hingegen folgt einem vollständig dezentralen Ansatz. Nähere Infos zu den einzelnen Systemen gibt es in den jeweiligen Artikeln.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3826/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1801/index.html)

<!-- MediaWiki page 1801; revision 3826; parent 0; 2009-01-03T18:48:53Z -->
