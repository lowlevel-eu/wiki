# Real Mode

Als Real Mode wird der 16-Bit-Modus der x86-Prozessoren bezeichnet. Der Real Mode existiert seit dem 8086 (damals allerdings nicht unter diesem Namen, weil die CPU keinen anderen Modus hatte) und ist auch auf neuen x86-Prozessoren noch kompatibel zu diesem. Der 286 führte den 16-Bit- und der 386 schliesslich den 32-Bit-[Protected Mode](https://github.com/lowlevel-eu/wiki/wiki/Protected-Mode "Protected Mode") ein, die den Real Mode abgelöst haben.

## Speicheradressierung

Im Realmode wird eine Speicheraddresse über ein Paar von 16bit Werten adressiert. Die beiden Werte nennt man Segment und Offset. Dies wurde so implementiert, da man nur 16bit Register zur Verfügung hatte, aber 20bit Speicheradressen erzeugen wollte. Die CPU berechnet dann aus der Segment:Offset Kombination die "richtige" physische Adresse (die dann auf den Bus gelegt wird, um sie wirklich vom RAM auszulesen/zu schreiben). Dies macht die CPU anhand folgender Formel:

physische Adresse = (Segment \* 16) + Offset

Als Beispiel kann die Adresse des Video-RAM dienen: Die physische Adresse des Video-RAM ist 0xB8000. Das kann man beispielsweise in 0xB800:0x0000 zerlegen (Da dieses Zerlegen nicht eindeutig ist, gibt es natürlich noch einige andere Segment:Offset-Kombinationen, die auf die gleiche physische Adresse zeigen), d.h. 0xB800 ist nur das (Realmode-) Segment und nicht die eigentlich dahinter stehende physische Adresse.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2978/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1665/index.html)

<!-- MediaWiki page 1665; revision 2978; parent 0; 2008-06-09T16:17:16Z -->
