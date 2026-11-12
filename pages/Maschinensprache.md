# Maschinensprache

Maschinensprache sind die Befehle, die direkt vom Prozessor ausgefuehrt werden. Schauen wir sie uns mal in Linux auf einem Intel-Rechner an. Zunächst schreiben wir ein "hello world" Programm in C:

    #include <stdio.h>
    int main()
    {
      printf("hello world");
    }

Dann wird die Datei compiliert:

    gcc hello.c

Und dann mit objdump -Mintel -d disassembliert, also in Assembler übersetzt. Die main Routine sieht dann so aus:

    0000000000001149 <main>:
        1149:   f3 0f 1e fa             endbr64 
        114d:   55                      push   rbp
        114e:   48 89 e5                mov    rbp,rsp
        1151:   48 8d 3d ac 0e 00 00    lea    rdi,[rip+0xeac]        # 2004 <_IO_stdin_used+0x4>
        1158:   b8 00 00 00 00          mov    eax,0x0
        115d:   e8 ee fe ff ff          call   1050 <printf@plt>
        1162:   b8 00 00 00 00          mov    eax,0x0
        1167:   5d                      pop    rbp
        1168:   c3                      ret    
        1169:   0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

Das Programm sichert zunächst mit dem Befehl **push** das Register rbp. Register sind die Variablen des Prozessors. Dann wird der Wert des Registers rdi auf den Wert des instruction pointers rip, vermehrt um den Hexadezimalwert eac, gesetzt. Dort steht die Zeichenkette "hello world" im Speicher. Dann wird das Register eax auf 0 gesetzt. Dann wird mittels **call** die Betriebssystemroutine **printf** aufgerufen. Diese wird die Speicherzelle, die vom Register rdi bezeichnet wird, auslesen, und den Inhalt von dort als Buchstabenkette ausgeben. Dann wird mit dem Befehl **pop** das Register rbp zurückgesichert, und mit dem Kommando **ret** zu dem aufrufenden Prozess zurück gekehrt.

Der Intel x86 Befehlssatz hat eine variable Laenge, z.B. bedeutet das Byte 90h "NOP" in [assembler](Assembler "Assembler") und steht fuer "no operation". Es ist also moeglich, mit einem Hexeditor ausfuehrbaren Code zu schreiben.

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

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11419/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2654/index.html)

<!-- MediaWiki page 2654; revision 11419; parent 11418; 2020-02-26T19:16:53Z -->
