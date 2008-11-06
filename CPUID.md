# CPUID

Der CPUID Befehl wird benutzt, um Informationen über die Fähigkeiten eines Prozessors zu erhalten. (Wie zum Beispiel den Herstellernamen, Modelnummer, die Größe des Cache ...)

## Wie man CPUID benutzt

Um den CPUID-Befehl auszuführen, schreibt man einfach den ASM-Befehl CPUID in den Code. Die Parameter werden dabei im Register EAX angegeben. Um z.B. den Vendor-ID-String (Herstellername) zu bekommen, ruft man CPUID mit dem Parameter 0x0 in EAX auf.

    mov eax, 0x0
    cpuid

Natürlich gibt der CPUID-Befehl auch ein Ergebnis zurück. In diesem Fall gibt er einen String zurück, dessen ASCII-Werte in EBX, EDX und ECX liegen. Wenn man den Inhalt dieser drei Register (in dieser Reihenfolge!) hintereinander in den Speicher schreibt, erhält man einen String. (Wenn der Prozessor von Intel hergestellt wurde, erhält man den String "GenuineIntel")  
**Achtung: Der String ist nicht nullterminiert !**

## Hinweise

Es gibt Befehle, die nur für Intel bzw. AMD Prozessoren verfügbar sind. Solche Befehle sollte man nicht ausführen, wenn man nicht weiß von welchem Hersteller die CPU ist! Z.B. sollten CPUID-Befehle, die nur für Intel-CPU´s gelten, nicht auf einer AMD-CPU ausgeführt werden.

## Siehe auch

[Englischer Artikel über den CPUID-Befehl](http://wiki.osdev.org/CPUID)

[Intels CPUID-Spezifikation](http://bochs.sourceforge.net/techspec/24161821.pdf)

[AMDs CPUID-Spezifikation](http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/25481.pdf)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3479/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1739/index.html)

<!-- MediaWiki page 1739; revision 3479; parent 3476; 2008-11-06T09:07:24Z -->
