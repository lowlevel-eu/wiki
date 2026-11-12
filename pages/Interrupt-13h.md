# Interrupt 13h

Der BIOS Interrupt 13h dient dem einfachen Zugriff auf Festplatten und Diskettenlaufwerke. Diese sind nur im [Real Mode](Real-Mode "Real Mode") verfügbar und für den [Bootloader](Bootloader "Bootloader") da.

## Die wichtigsten Funktionen

| Funktion | Parameter | Rückgabe |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 02h Sektorweises Lesen | AH=02h<br>AL=Zahl der Auszulenden Sektoren<br>CH=Spur<br>CL=Nummer des Ersten Sektors<br>DH=Kopf<br>DL=Laufwerksnummer(0/1 erstes Zweites Floppy;<br>80h/81h/... Erste/Zweite/... Festplatte)<br>ES:BX=Addresse des Puffers | CF=Fehler<br>AL=Zahl der Sektoren<br>AH=Fehlercode |
| 03h Sektorweises Schreiben | AH=03h<br>AL=Zahl der zu schreibenden Sektoren<br>CH=Spur<br>CL=Erster Sektor<br>DH=kopf<br>DL=Laufwerksnummer<br>ES:BX=Adresse des Pufers | CF=Fehler<br>AL=Zahl der Sektoren<br>AH=Fehlercode |
| 04h Prüfen von Sektoren | AH=04h<br>AL=Zahl der zu prüfenden Sektoren<br>CH=Spur<br>CL=Erster Sektor<br>DH=Kopf<br>DL=Laufwerksnummer | CF=Fehler<br>AL=Zahl der Sektoren<br>AH=Fehlercode |
| 05h Spur Formatieren | AH=05h<br>AL=Anzahl Sektoren<br>CH=Spur<br>CL=erster Sektor<br>DH=Kopf(0/1)<br>DL=Laufwerksnummer<br>ES:BX=Adresse des Formatpuffers | CF=Fehler<br>AF=Fehlercode |
| 08h Format auslesen (Festplatte) | AH=08h<br>DL=Laufwerksnummer | CF=Fehler<br>AH=Fehlercode<br>DL=Zahl der Festplatten<br>DH=Zahl der Köpfe<br>CL=Zahl der Sektoren<br>CH=Zahl der Zylinder |
| 08h Format auslesen (Floppy) | AH=08h<br>DL=Laufwerksnummer | CF=Fehler<br>AH=Fehlercode<br>BL=Art des Laufwerks:<br>01h-5,25"\[360KB\]<br>02h-5,25"\[1,2MB\]<br>03h-3,5"\[720KB\]<br>04h-3,5"\[1,44MB\]<br>DH=1<br>CH=Zahl der Spuren-1<br>CL=Zahl der Sektoren-1<br>ES:DI=Zeiger auf die DDPT |
| 15h Auslesen des Laufwerktypes | AH=15h<br>DL=Laufwerksnummer | CF=Fehler<br>AH=Laufwerkstyp:<br>00h-Kein Laufwerk<br>01h-Diskettenlaufwerk<br>02h-Diskettenlaufwerk, Diskettenwechsel<br>03h-Festplatte:<br>DX/CX=Sektorenzahl(Bits 0-15/16-31) |

  
  
  

## Fehlercodes

| Fehlercode | Festplatte | Floppy |
| ------------ | --------------------------------------- | ------------------------------------- |
| 01h | Falsche Funktionsnummer oder Laufwerk | Falsche Funktionsnummer |
| 02h | Addressmarkierung nicht gefunden | Adressmarkierung nicht gefunden |
| 03h | \- | Schreibgeschützt |
| 04h | Sektor nicht gefunden | Sektor nicht gefunden |
| 05h | Reset-Fehler | \- |
| 06h | \- | Diskette wurde gewechselt |
| 07h | Falsche Initialisierung | \- |
| 08h | \- | DMA-Überlauf |
| 09h | Segmentgrenze überschritten \[DMA\] | Segmentgrenze überschritten \[DMA\] |
| 0Ah | Sektor Fehlerhaft | \- |
| 10h | Lesefehler | Lesefehler |
| 11h | Lesefehler mit EEC Korigiert | \- |
| 20h | Controller-Fehler | Controller-Fehler |
| 40h | Spur nicht gefunden | Spur nicht gefunden |
| 80h | Time-Out-Fehler | Tim-Out-Fehler |
| AAh | Laufwerk nicht bereit | \- |
| BBh | Fehler im BIOS | Fehler im BIOS |
| CCh | Schreibfehler | \- |
| FFh | Unbekannter Fehler | Unbekannter Fehler |

  
  

## Disk Drive Parameter Table \[DDPT\]

|  | Inhalt |
| ----- | --------------------------------- |
| 00h | Step-Rate/Head-Unload-Time |
| 01h | Head-Load-Time |
| 02h | Nachlaufzeit des Motors |
| 03h | Sektorgröße |
| 04h | Sektoren pro Spur |
| 05h | Länge von GAP3 |
| 06h | Data Length |
| 07h | Länge von GAP3 beim Formatieren |
| 08h | Füll-Byte für das Formatieren |
| 09h | Head-Settle-Time |
| 0Ah | Hochlaufzeit des Motors |

  
  

## Formatpuffer \[05h\]

|  | Festplatte | Floppy |
| ----- | -------------------------------------------------------- | -------------------------------------------------------- |
| 0 | Spur | Spur |
| 1 | Kopf | Diskettenseite<br>0 Oben/1 Unten |
| 2 | Sektornummer | Sektornummer |
| 3 | Bytes pro Sektor:<br>0=128<br>1=256<br>2=512<br>3=1024 | Bytes pro Sektor:<br>0=128<br>1=256<br>2=512<br>3=1024 |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4479/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1768/index.html)

<!-- MediaWiki page 1768; revision 4479; parent 4070; 2009-06-24T11:11:17Z -->
