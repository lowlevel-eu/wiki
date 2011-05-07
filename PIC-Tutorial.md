# PIC Tutorial

| PIC |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Schwierigkeit**: [<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif" width="16" height="16" alt="Stern gold.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/f49eb9cc36b09af043f1.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)[<img src="https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif" width="16" height="16" alt="Stern weiß.gif" />](https://raw.githubusercontent.com/wiki/lowlevel-eu/wiki/assets/e092c7d3c71af0daba80.gif)<br> |  |
| Benötigtes Vorwissen: | ([PIC](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC")), [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") |
| Sprache: | C |

Dieses Tutorial soll auf die wichtigsten Aspekte der Programmierung des PICs eingehen. Ich empfehle dennoch, auch [diesen Aritkel](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller "PIC") zu lesen, da dieser alle Aspekte erläutert.

## Vorüberlegungen

### Wofür benötige ich den PIC überhaupt?

Wann immer ein Bauteil (Hardware) Daten für die CPU bereithält, benötigt dieses eine Möglichkeit der CPU mitzuteilen, dass sie diese Daten auslesen soll. Dafür gibt es im Grunde zwei Möglichkeiten: Entweder du fragst in regelmäßigen Abständen bei jedem Port nach, ob er Daten für dich hat &#150; Polling genannt &#150; oder du lässt den PIC das machen. Es liegt auf der Hand, dass letzteres erheblich schneller ist, weswegen es kein modernes Betriebssystem gibt, das Polling verwendet, wenn auch Interrupts möglich sind.

### Wie funktioniert der PIC denn genau?

Wenn ein Bauteil die Aufmerksamkeit der CPU möchte, dann sendet es einen sogenannten **Interrupt Request** (IRQ) an den PIC. Dieser überprüft dann, ob die CPU diesen IRQ im Moment blockt, andernfalls leitet der diesen an die CPU weiter, was schließlich zum Aufruf der entsprechenden [Behandlungsroutine](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR") führt.

### Wieso muss ich den PIC denn dann umprogrammieren?

Im [Real Mode](https://github.com/lowlevel-eu/wiki/wiki/Real-Mode "Real Mode") hat das [BIOS](https://github.com/lowlevel-eu/wiki/wiki/Basic-Input-Output-System "BIOS") den PIC so programmiert, dass er auf Einträge in der [IVT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Vector-Table "IVT") zeigt. Da diese aber nun durch die [IDT](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Descriptor-Table "IDT") ersetzt wird, stimmen die Interrupt-Nummern, die der PIC an die CPU übermittelt nicht mehr. So würde z. B. jeder Tastendruck eine Debug-Exception auslösen. Deshalb muss die Zuordnung der IRQ Nummer zur Interrupt Nummer geändert werden.

## Programmierung

### Initialisierung

Zur Reinitialisierung müssen vier sogenannte ICWs (Initialization Control Words) geschickt werden, die ich nun im Einzelnen durchgehen werde. Beginnen wir mit den Portnummern: \<c\>

1.  define PIC_MASTER_COMMAND 0x20
2.  define PIC_MASTER_DATA 0x21
3.  define PIC_MASTER_IMR 0x21
4.  define PIC_SLAVE_COMMAND 0xA0
5.  define PIC_SLAVE_DATA 0xA1
6.  define PIC_SLAVE_IMR 0xA1

\</c\> Wie man sehen kann, gibt es zwei PICs, die üblicherweise über die IRQ-Leitung 2 miteinander kommunizieren, was man aber auch ändern kann (siehe unten). Befehle müssen allerdings zu jedem PIC gesendet werden. Das Bitmuster der Befehle kann [hier](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#initialisierung "PIC") hier noch einmal im Einzelnen nachvollzogen werden.

Kommen wir also zu ICW Nummer Eins:

\<c\> void pic_remap(int interrupt_num) {

        outb(PIC_MASTER_COMMAND, 0x11);
        outb(PIC_SLAVE_COMMAND, 0x11);

\</c\> 0x11 bedeutet: Wir senden auch ICW4, es gibt zwei PICs und wir wollen Initialisieren.

Das nächste ICW ist das wichtigste, denn hiermit wird angegeben, auf welchen Eintrag in der IDT der IRQ 0 (für den Master PIC) und IRQ 8 (für den Slave) zeigt. Dieser Wert wird der Funktion als Parameter übergeben. Üblicherweise verwendet man 32, um direkt an die Exceptions anzuschließen. Aber natürlich dürfen auch andere Werte verwendet werden, solange diese durch 8 teilbar sind.

\<c\>

       outb(PIC_MASTER_DATA, interrupt_num);
       outb(PIC_SLAVE_DATA, interrupt_num+8);

\</c\>

Die Hälfte ist geschafft. Kommen wir zu ICW3. Mit diesem gibt man an, über welchen IRQ die beiden PICs miteinander kommunizieren, das ist IRQ 2.

\<c\>

       outb(PIC_MASTER_DATA, 0x04);
       outb(PIC_SLAVE_DATA, 2);

\</c\> Merkwürdigerweise übergibt man an den Slave direkt die IRQ-Nummer, dem Master übergibt man eine Bitmaske, in dem das betreffende Bit gesetzt ist.

Fast fertig, nur noch ICW4 fehlt. Es wird 0x01 an beide gesendet, um anzuzeigen, dass wir uns im 8086-Mode befinden (was auch sonst...).

\<c\>

      outb(PIC_MASTER_DATA, 0x01);
      outb(PIC_SLAVE_DATA, 0x01);

} \</c\>

### IRQs maskieren

Wie bereits erwähnt, können die PICs auch bestimmte IRQs blockieren. Dazu dienen die Interrupt Mask Register (IMR). In diesen liegt eine Bitmaske. Ist ein Bit gesetzt, so ist der entsprechende IRQ blockiert. Die Nummern der IRQs sind [hier](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interrupt-Controller#irq-tabelle "PIC") zu finden. Schreiben wir uns eine Funktion dazu: \<c\> void pic_mask_irqs(uint16_t mask) {

      outb(PIC_MASTER_IMR, (uint8_t) mask);
      outb(PIC_SLAVE_IMR, (uint8_t) mask>>8);

} \</c\> Simpel, oder? Nebenbei: Wenn das Interruptflag gelöscht ist (-\>cli), dann kommen sowieso keine IRQs an. Außerdem werden alle IRQs des Slaves blockiert, wenn im Master der IRQ 2 maskiert wird.

### ISRs programmieren

Gut, wir haben also bisher folgendes:

1.  die IRQs auf die entsprechenden Einträge der IDT umgelenkt
2.  alle IRQs demaskiert
3.  das Interruptflag gesetzt (-\>sti)

Und beim nächsten Tick des [Timers](https://github.com/lowlevel-eu/wiki/wiki/Programmable-Interval-Timer "PIT") schmiert das System ab. Der Grund: wir benötigen Interrupt Service Routinen (ISRs). Wie das funktioniert, ist nicht Aufgabe dieses Tutorials. Schau einfach mal hier: [Interrupt](https://github.com/lowlevel-eu/wiki/wiki/Interrupt "Interrupt") und [ISR](https://github.com/lowlevel-eu/wiki/wiki/Interrupt-Service-Routine "ISR"). Bei ISRs, die IRQs behandeln, gibt es allerdings noch eine Besonderheit: Sie müssen ein End Of Interrupt (EOI) Signal an den PIC senden. Andernfalls arbeitet der PIC so, als wären alle IRQs im IMR maskiert. Mit anderen Worten: Kein IRQ kommt mehr bei der CPU an. Dabei ist zu beachten, dass bei IRQs über 7 an *beide* PICs ein EOI gesendet werden muss, da diese ja auch über einen IRQ kommunizieren: \<c\>

1.  define EOI 0x20

void pic_send_eoi(int irq_num) {

     outb(PIC_MASTER_COMMAND, EOI);
     if (irq_num>7)
       outb(PIC_SLAVE_COMMAND, EOI);

} \</c\> Es ist eine beliebte Fehlerquelle, das Senden des EOI zu vergessen!

## Der Code im Gesamten

\<c\>

1.  define PIC_MASTER_COMMAND 0x20
2.  define PIC_MASTER_DATA 0x21
3.  define PIC_MASTER_IMR 0x21
4.  define PIC_SLAVE_COMMAND 0xA0
5.  define PIC_SLAVE_DATA 0xA1
6.  define PIC_SLAVE_IMR 0xA1

<!-- -->

1.  define EOI 0x20

void pic_remap(int interrupt_num) {

       outb(PIC_MASTER_COMMAND, 0x11);
       outb(PIC_SLAVE_COMMAND, 0x11);
       outb(PIC_MASTER_DATA, interrupt_num);
       outb(PIC_SLAVE_DATA, interrupt_num+8);
       outb(PIC_MASTER_DATA, 0x04);
       outb(PIC_SLAVE_DATA, 2);
       outb(PIC_MASTER_DATA, 0x01);
       outb(PIC_SLAVE_DATA, 0x01);

}

void pic_mask_irqs(uint16_t mask) {

      outb(PIC_MASTER_IMR, (uint8_t) mask);
      outb(PIC_SLAVE_IMR, (uint8_t) mask>>8);

}

void pic_send_eoi(int irq_num) {

     outb(PIC_MASTER_COMMAND, EOI);
     if (irq_num>7)
       outb(PIC_SLAVE_COMMAND, EOI);

} \</c\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/9750/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2183/index.html)

<!-- MediaWiki page 2183; revision 9750; parent 9749; 2011-05-07T16:47:13Z -->
