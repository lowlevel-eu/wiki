# Real Mode

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Als Real Mode wird der 16-Bit-Modus der x86-Prozessoren bezeichnet. Der Real Mode existiert seit dem 8086 (damals allerdings nicht unter diesem Namen, weil die CPU keinen anderen Modus hatte) und ist auch auf neuen x86-Prozessoren noch kompatibel zu diesem. Der 286 führte den 16-Bit- und der 386 schliesslich den 32-Bit-[Protected Mode](Protected-Mode "Protected Mode") ein, die den Real Mode abgelöst haben.

## Eigenschaften

Der 8086 bzw. der Real Mode unterliegt im Gegensatz zum Protected Mode einigen Einschränkungen. Die wichtigsten sind:

- Der 8086 hatte einen 20 Bit breiten Adressbus, und kann demzufolge maximal 2^20 Bytes = 1 Megabyte Speicher adressieren. Von diesem Megabyte bleiben weniger als 640 Kilobytes übrig, die nicht vom BIOS und dem VGA-BIOS belegt sind. (Siehe [Speicherbereiche](Speicherbereiche "Speicherbereiche").)
- Es steht kein Speicherschutz und kein [virtueller Speicher](Paging "Paging") zur Verfügung.
- Indirekte Adressierung ist nur mittels der Register BX, BP, SI und DI möglich.
- Die 32-Bit-Register des 386ers und höher stehen zwar als Operanden zur Verfügung, es können trotzdem keine Offsets größer als 2^16 (64 Kilobytes) gebildet werden. (führt zu einer Exception.)

Ein weiterer Unterschied zum Protected Mode ist, dass [BIOS](Basic-Input-Output-System "BIOS")-Funktionen den Zugriff auf die Laufwerke, und die Abfrage der Tastatur ermöglichen. Außerdem stehen [VGA](Video-Graphics-Array "VGA")- und [VESA](Video-Electronics-Standards-Association "VESA")-Funktionen zur Verfügung, um die Grafikkarte in einen Grafikmodus wechseln zu lassen.

## Speicheradressierung

Im Real Mode wird eine Speicheraddresse über ein Paar von 16-Bit-Werten adressiert. Die beiden Werte nennt man Segment und Offset. Dies wurde so implementiert, da man nur 16-Bit-Register zur Verfügung hatte, aber 20-Bit-Speicheradressen erzeugen wollte. Die CPU berechnet dann aus der Segment:Offset Kombination die "richtige" physische Adresse (die dann auf den Bus gelegt wird, um sie wirklich vom RAM auszulesen/zu schreiben). Dies macht die CPU anhand folgender Formel:

physische Adresse = (Segment \* 16) + Offset

Als Beispiel kann die Adresse des Video-RAM dienen: Die physische Adresse des Video-RAM ist 0xB8000. Das kann man beispielsweise in 0xB800:0x0000 zerlegen (Da dieses Zerlegen nicht eindeutig ist, gibt es natürlich noch einige andere Segment:Offset-Kombinationen, die auf die gleiche physische Adresse zeigen), d.h. 0xB800 ist nur das (Real-Mode-) Segment und nicht die eigentlich dahinter stehende physische Adresse.

## OS-Dev im Real Mode

Die [Einschränkungen](#eigenschaften) des Real Modes erschweren die Entwicklung eines Betriebssystems erheblich. Viele Anfänger versuchen trotzdem ihre ersten Schritte im Real Mode, da das BIOS mit seinen Funktionen für Hardwarezugriffe die Nachteile auszugleichen scheint. Damit gibt man jedoch genau eine der Hauptaufgaben eines Betriebssystems nämlich Verwaltung von Ressourcen aus der Hand.

Der sinnvolle Einsatz des Real Modes im OS-Dev beschränkt sich darauf im Bootloader den Kernel zu laden, und dann in den Protected Mode zu springen. Diese scheinbar einfache Aufgabe ist jedoch keineswegs ohne Hürden und viele selbstgebaute Bootloader funktionieren nur auf einer handvoll PCs. Deswegen nehmen universelle Bootloader wie [GRUB](Grand-Unified-Bootloader "GRUB") dem Entwickler auch diese Last ab.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/5809/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1665/index.html)

<!-- MediaWiki page 1665; revision 5809; parent 5766; 2009-08-31T17:23:21Z -->
