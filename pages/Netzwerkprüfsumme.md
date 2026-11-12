# Netzwerkprüfsumme

Bei [Netzwerkprotokollen](Kategorie-Netzwerk.md "Kategorie:Netzwerk") wie [IP](Internet-Protocol.md "Internet Protocol"), TCP und UDP wird eine Checksumme benötigt. Die Berechnung dieser Prüfsumme erfolgt bei allen diesen Protokollen auf die gleiche Art und Weise, wobei sie bei unterschiedlichen Protokollen über unterschiedliche Daten berechnet wird (z. B. bei IP nur über den Header, bei hingegen TCP über die Daten, den TCP-Header und einen Pseudo-IP-Header)

## Schema

Zuerst wird das Prüfsummenfeld des Protokolls auf null (bzw. 0x0000) gesetzt. Danach wird die Prüfsumme folgendermaßen berechnet: Eine vorzeichenlose 32-Bit-Variable (uint32_t) wird für die Prüfsumme erstellt und auf null gesetzt. Immer zwei benachbarte Bytes der Daten werden zu 16-Bit-Blöcken zusammengefasst. Wenn der letzte Block weniger als 16 Bit hat (das heißt, wenn die Anzahl der Bytes ungerade ist), dann wird er in der Berechnung von hinten mit Nullen aufgefüllt, bis er 16 Bit hat (Das heißt, das niederwertige Byte wird praktisch auf null gesetzt – die Daten für die Prüfsumme werden dabei aber nicht angetastet). Nun werden alle 16-Bit-Blöcke mit Übertrag addiert und das 32-Bit-Ergebnis in der Prüfsummenvariable gespeichert. Anschließend werden die höherwertigen 16 Bits der Prüfsumme so lange zu den niederwertigen 16 Bits hinzuaddiert, bis die höherwertigen 16 Bits null sind (also bis kein Übertrag bei der Addition mehr entsteht). Die niederwertigen 16 Bits der Prüfsumme sind nun die eigentliche Prüfsumme, die im Prüfsummenfeld gespeichert werden kann.

Für das Einlesen der 16-Bit-Blöcke wird, wie bei Netzwerkprotokollen üblich, Big Endian verwendet.

## Code

\<c\>int calculate_network_checksum(void \*buffer, int size) {

     uint32_t sum = 0;
     int odd = 0, i;
     uint8_t *data = buffer;
     
     if (!buffer || (size < 2))
       return 0;
     if ((size>>1)*2 != size)
     {
       odd = 1;
       size--;
     }
     for (i = 0; i < size; i += 2)
       sum += ((data[i]<<8) & 0xFF00) + (data[i+1] & 0xFF);
     if (odd)
       sum += (data[i]<<8) & 0xFF00;
     while (sum >> 16)
       sum = (sum&0xFFFF) + (sum>>16);
     
     return (~sum)&0xFFFF;

}\</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/8047/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1974/index.html)

<!-- MediaWiki page 1974; revision 8047; parent 8046; 2010-08-10T15:45:48Z -->
