# Umschalten in Protected Mode

\<asm\>;;; Ein kleines Beispiel, wie man in den 32-Bit Protected Mode wechselt

Bei Fragen kann man sich einfach an stefan.marcik@web.de oder

an die ICQ-Nummer 338417614 wenden.

\[BITS 16\] cli ; Interrupts ausschalten lgdt \[gdtr\] ; GDT Pointer laden

mov eax,cr0 ; In PMode wechseln, indem das niedrigste or al,1 ; Steuerungsbit von cr0 geändert wird mov cr0,eax ; muss über Umweg über ein anderes Register gemacht werden

jmp codesel:PMode ; FarJump zu einer 32-Bit PMode Funktion

\[BITS 32\] PMode: mov ax,datasel ; Segmentregister laden mov ds,ax mov ss,ax mov esp,0x90000 ; Stack aufsetzen

  

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

gdt_end\</asm\> © by Stefan Marcik

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2026/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1537/index.html)

<!-- MediaWiki page 1537; revision 2026; parent 0; 2007-06-18T19:03:30Z -->
