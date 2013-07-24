# Syscall/sysret

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

Mit ***syscall*** und ***sysret*** stehen im *Long Mode* zwei Instruktionen zur Verfügung mit deren Hilfe schnelle Wechsel in Ring 0 bzw. Ring 3 möglich sind.

## Anforderungen

Für die Verwendung von syscall und sysret müssen Code- und Stack-Segmente in einer ganz bestimmten Reihenfolge liegen.

Es muss das Segment für den Kernel Stack direkt hinter dem Kernel Code Segment liegen:

1.  Kernel Code
2.  Kernel Stack *(Daten)*

So dass *KERNEL_SS = KERNEL_CS + 8* gilt.

Für den User Mode muss ein eventuell vorhandenes 32 Bit Code Segment direkt vor dem Stack Segment und das 64 Bit Code Segment direkt dahinter liegen:

1.  User Code 32 Bit
2.  User Stack *(Daten)*
3.  User Code 64 Bit

So dass gilt *USER_SS = USER_32_CS + 8* bzw. *USER_64_CS = USER_32_CS + 16*.

## Initialisierung

**MSR.STAR** *(`0xc000 0081`)*

| 63 – 48 | 47 – 32 | 31 – 0 |
| ----------- | ------------ | -------- |
| SYSRET_CS | SYSCALL_CS |  |

**MSR.LSTAR** *(`0xc000 0082`)*

**63–0**

Ziel für 64 Bit Code

**MSR.CSTAR** *(`0xc000 0083`)*:

**63–0**

Ziel für 32 Bit Code

## syscall

Die *syscall* Instruktion veranlasst einen Wechsel in Ring 0. Dabei wird die Rücksprungadresse in *RCX* gesichert. Das *CS* Register wird mit *STAR.SYSCALL_CS* und *SS* mit *STAR.SYSCALL_CS + 8*.

Wird *syscall* aus dem 32 Bit-Modus heraus aufgerufen wird *RIP* mit *CSTAR* geladen, aus dem 64 Bit-Modus heraus mit *LSTAR*.

## sysret

Mit der *sysret* Instruktion wechselt die CPU in Ring 3 und lädt *RIP* bzw. *EIP* mit dem Wert aus *RCX*. Das *SS* Register wird mit *STAR.SYSRET_CS + 8* geladen und *CS* mit *STAR.SYSRET_CS* bzw. *STAR.SYSRET_CS* + 16.

Um in den 64 Bit User Mode (Ring 3) zu wechseln braucht es die Opcodes `48 0f 07`.

NASM:

    o64 sysret

GNU/As:

    sysretq

In den 32 Bit User Mode (Ring 3) wechselt man mit den Opcodes `0f 07`.

NASM und GNU/As:

    sysret

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/11124/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2647/index.html)

<!-- MediaWiki page 2647; revision 11124; parent 0; 2013-07-24T15:06:22Z -->
