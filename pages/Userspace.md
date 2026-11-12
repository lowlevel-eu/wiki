# Userspace

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Der Begriff "Userspace" wird für Prozesse verwendet, die im [Ring](Ring "Ring") 3 laufen. Sie können (bzw. sollten es nicht können) keine Steuerbefehle wie "in", "out", "cli", "popfd" oder "lgdt" ausführen. Außerdem können sie nicht auf die [Kontrollregister](Control-Register "Control Register") sowie auf den Speicher von anderen Prozessen zugreifen. Sie haben somit nur eingeschränken Zugriff auf das System, dies dient auch ihrem Selbstschutz.

Prozesse, die in Ring 0 laufen, befinden sich im Gegensatz dazu im sogenannten "Kernelspace". Sie haben vollen Zugriff auf das System.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5391/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2008/index.html)

<!-- MediaWiki page 2008; revision 5391; parent 0; 2009-08-06T20:23:28Z -->
