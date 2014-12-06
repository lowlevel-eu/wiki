# Maschinensprache

Maschinensprache sind die Befehle, die direkt vom Prozessor ausgefuehrt werden. Der Intel x86 Befehlssatz hat eine variable Laenge, z.B. bedeutet das Byte 90h "NOP" in [assembler](https://github.com/lowlevel-eu/wiki/wiki/Assembler "Assembler") und steht fuer "no operation". Es ist also moeglich, mit einem Hexeditor ausfuehrbaren Code zu schreiben.

Maschinensprache kann mehr als Assembler, z.B. springt der Befehl

    eb ff

Zum *zweiten* Byte, also zum *Parameter* des Kommandos. Das bedeutet, nach dem Byte "eb" wird das Byte "ff" ausgefuehrt, das "eigentlich" als Parameter gedacht war. Ein solches Konstrukt ist in assembler unmoeglich. Diese Konstrukte wurden jedoch zum Sparen von Speicherplatz eingesetzt.

Mit Linux ist es moeglich, assembler in Maschinensprache zu uebersetzen (kompilieren) und umgekehrt (disassemblieren). Ich mache es hier einmal vor. Folgendes Programm beschreibt eine Endlosschleife in Assembler:

**endless.asm**

    global _start
    _start:
       nop
    jmp _start

zum Uebersetzen in Maschinensprache starten wir:

    nasm -f elf64 endless.asm

um das Ganze zu einem unter Linux ausfuehrbaren Programm zu machen geben wir ein:

    ld -s -o endless endless.o

Zum disassemblieren geben wir ein:

    # objdump -M intel -d endless

    endless:     file format elf64-x86-64
     

    Disassembly of section .text:

    0000000000400080 <.text>:
      400080:       90                      nop   
      400081:       eb fc                   jmp    0x400080

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11226/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2654/index.html)

<!-- MediaWiki page 2654; revision 11226; parent 11225; 2014-12-06T12:43:15Z -->
