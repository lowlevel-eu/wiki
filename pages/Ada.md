# Ada

| Allgemeines |  |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Name: | Ada |
| Inlineassembler: | Nein |
| Compiler: | GNAT (GNU Ada Compiler) |
| Spracheneigenschaften |  |
| Plattformen: | [Linux](Linux.md "Linux"), [Windows](Windows.md "Windows") |
| Beispielkernel in der Sprache: | siehe unten |
| Homepage |  |

[ISO-Norm](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=45001)

**Ada** ist eine nach Ada Lovelace, der ersten Programmiererin, benannte, in den 1970er Jahren von Jean Ichbiah entwickelte, strukturierte und stark typsierte [Programmiersprache](Kategorie-Programmiersprache.md "Kategorie:Programmiersprache"), deren Ziel die Entwicklung von und für eingebettete Systeme und Echtzeitanwendungen war. Ada war zudem die erste standardisierte Programmiersprache und wurde anfänglich vom US-Verteidigungsministerium gefördert.

  

## Ada als Sprache für ein [Betriebssystem](Betriebssystem.md "Betriebssystem")

Alle Vorteile von Ada, die Laufzeitüberwachung und die parallele Verarbeitung, können nicht ohne weiteres in einem Betriebssystem (genauer: In einem [Kernel](Kernel.md "Kernel")) benutzt werden, ohne im Kernel selbst eine Referenzimplementierung von Ada zu programmieren.

Dennoch ist es möglich, einen Kernel in Ada zu schreiben.

## Testkernel in Ada

### test.adb

    with System.Storage_Elements;

    procedure test is

        pragma Suppress (All_checks);

        multiboot: constant array (0..2) of integer
            := (16#1badb002#, 0, -16#1badb002#);

        v: Array (0 .. 80 * 25 * 2) of character;
        for v'Address use System.Storage_Elements.To_Address(16#B8000#);

        s: constant String := "Hello world!";
    begin
        for i in s'range loop
            v(2 * (i - 1)) := s(i);
        end loop;
    end test;

### build.sh

    #!/bin/bash
    gcc -c -m32 -x ada test.adb
    strip -dR .eh_frame test.o
    ld -melf_i386 -Ttext=0x100000 -e "_ada_test" -o test.krn test.o

  

## Weblinks

- [GNU Ada Compiler](https://libre2.adacore.com/)
- [ISO-Norm Ada 2005](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=45001)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10831/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1742/index.html)

<!-- MediaWiki page 1742; revision 10831; parent 9519; 2012-09-16T13:39:32Z -->
