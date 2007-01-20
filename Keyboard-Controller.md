# Keyboard Controller

Der Keyboard Controller (KBC) sitzt auf dem Mainboard und dient, wie der Name vermuten lässt, unter anderem der Tastaturansteuerung. Er hat jedoch noch viele weitere Funktionen.

Funktionen des KBC:

- Ansteuerung der Tastatur
- Ansteuerung des PSAUX-Ports (z.B. PS/2-Maus)
- ein-/ausschalten der 21-Adressleitung (a20-Gate)
- CPU-Reset auslösen
- ein-/ausschalten des Systemlautsprechers
- Information ob das System eine Monochrom- oder Farbgrafikkarte benutzt

Zur Komunikation mit dem KBC werden die Ports 0x60, 0x61 und 0x64 verwendet.  

![kbcnr6.png](http://img241.imageshack.us/img241/5692/kbcnr6.png)  
Statusregister  

|  |  |  |  |
| ----- | ----------------------------------------- | ------ | ------------------------------------------------------------------------- |
| BIT | Beschreibung | Wert | Beschreibung |
| 0 | Status des Ausgabepuffers (KBC -\> CPU) | 0 | Ausgabepuffer leer |
| 0 | Status des Ausgabepuffers (KBC -\> CPU) | 1 | Ausgabepuffer voll (es kann von Port 0x60 gelesen werden) |
| 1 | Status des Eingabepuffers (KBC \<- CPU) | 0 | Eingabepuffer leer (es kann auf Port 0x60 oder 0x64 geschrieben werden) |
| 1 | Status des Eingabepuffers (KBC \<- CPU) | 1 | Eingabepuffer voll |
| 2 | Systemstatus? | 0 | Reset/Selbsttest wird gerade ausgeführt |
| 2 | Systemstatus? | 1 | Selbsttest erfolgreich |
| 3 | zuletzt benutztes Port | 0 | 0x60 |
| 3 | zuletzt benutztes Port | 1 | 0x64? 0x61? |
| 4 | Tastatursperre | 0 | Tastatur gesperrt |
| 4 | Tastatursperre | 1 | Tastatur nicht gesperrt |
| 5 | PSAUX? | 0 | ? |
| 5 | PSAUX? | 1 | ? |
| 6 | Timeout | 0 | kein Timeout |
| 6 | Timeout | 1 | Tastatur oder PSAUX-Gerät ragiert nicht? |
| 7 | Paritätsfehler | 0 | kein Fehler |
| 7 | Paritätsfehler | 1 | Beim letzten Senden/Empfangen trat ein Paritätsfehler auf |

  
inputport

|  |  |  |  |
| ----- | ---------------------------------------- | ------ | ------------------------------- |
| BIT | Beschreibung | Wert | Beschreibung |
| 0 | Keyboard data in pin? | 0 | ? |
| 0 | Keyboard data in pin? | 1 | ? |
| 1 | PS/2 mouse in pin? | 0 | ? |
| 1 | PS/2 mouse in pin? | 1 | ? |
| 2 | Reserviert |  |  |
| 2 | Reserviert |  |  |
| 3 | Reserviert |  |  |
| 3 | Reserviert |  |  |
| 4 | Reserviert |  |  |
| 4 | Reserviert |  |  |
| 5 | Reserviert |  |  |
| 5 | Reserviert |  |  |
| 6 | Wether you have a color or mono screen | 0 | ? |
| 6 | Wether you have a color or mono screen | 1 | ? |
| 7 | Tastatursperre | 0 | Tastatursperre gesperrt |
| 7 | Tastatursperre | 1 | Tastatursperre nicht gesperrt |

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/1764/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1468/index.html)

<!-- MediaWiki page 1468; revision 1764; parent 1763; 2007-01-20T16:29:47Z -->
