# Ada

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

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/3392/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1742/index.html)

<!-- MediaWiki page 1742; revision 3392; parent 0; 2008-10-07T15:17:51Z -->
