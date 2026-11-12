# Umschalten in Protected Mode

So einfach ist das! In der GDT wird ein Daten-, sowie Code-Deskriptor auf die ganzen 4 möglichen GByte Arbeitsspeicher eingerichtet. Heutzutage verwenden dank Paging alle OS ein solches, sogenanntes flaches Speichermodell. Das heißt, dass man von nun an nur noch mit 32-Bit Offsets hantieren und sich nicht mehr mit Segmenten herumschlagen muss.

Mehr [Infos](Protected-Mode.md "Protected Mode") und eine zweite Art in den Protected Mode umzuschalten findet man im Protected Mode Tutorial von Tee Jay, sowie dem, schon etwas älteren, [Tutorial der FH-Zwickau](http://www.fh-zwickau.de/doc/prmo/start.htm).

  
**Wichtig** bei diesem Code ist es, selbst noch die org-Anweisung auf die Startadresse des Codes anzupassen!! \<asm\>;;; Ein kleines Beispiel, wie man in den 32-Bit Protected Mode wechselt

Bei Fragen kann man sich einfach an die ICQ-Nummer 338-417-614 wenden.

\[BITS 16\] org 0x0000 ; Addiert zu allen Offsets die Start-Adresse dieses Codes

cli ; Interrupts ausschalten lgdt \[gdtr\] ; GDT Pointer laden

mov eax,cr0 ; In PMode wechseln, indem das niedrigste or al,1 ; Steuerungsbit von cr0 geändert wird mov cr0,eax ; muss über Umweg über ein anderes Register gemacht werden

jmp codesel:PMode ; FarJump zu einer 32-Bit PMode Funktion

\[BITS 32\] PMode: mov ax,datasel ; Segmentregister laden mov ds,ax mov ss,ax mov esp,0x90000 ; Stack aufsetzen

jmp \$ ; Endlosschleife, wird durch weiteren Code ersetzt

  

== GDT == ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

gdtr: ; Desktiptortabelle

      dw gdt_end-gdt-1       ; Limit
      dd gdt            ; Basisadresse

gdt:

      dd 0,0         ; Null-Deskriptor

codesel equ \$-gdt

      dw 0xFFFF          ; Segmentgrösse 0..15
      dw 0x0000         ; Segmentadresse 0..15
      db 0x00           ; Segmentadresse 16..23
      db 0x9A           ; Zugriffsberechtigung und Typ
      db 0xCF           ; Zusatzinformationen und Segmentgrösse 16...19
      db 0x00           ; Segmentadresse 24..31

datasel equ \$-gdt

      dw 0xFFFF          ; Segmentgrösse 0..15
      dw 0x0000         ; Segmentadresse 0..15
      db 0x00           ; Segmentadresse 16..23
      db 0x92           ; Zugriffsberechtigung und Typ
      db 0xCF           ; Zusatzinformationen und Segmentgrösse 16...19
      db 0x00           ; Segmentadresse 24..31

gdt_end:\</asm\>

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/4855/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1537/index.html)

<!-- MediaWiki page 1537; revision 4855; parent 3030; 2009-07-30T13:11:30Z -->
