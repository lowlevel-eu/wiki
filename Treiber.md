# Treiber

Als **Treiber** wird der Teil eines [Betriebssystems](https://github.com/lowlevel-eu/wiki/wiki/Betriebssystem "Betriebssystem") bezeichnet, der direkt mit der Hardware kommuniziert. Dies geschieht über [I/O Ports](https://github.com/lowlevel-eu/wiki/wiki/I-O-Ports "I/O Port") oder Memory Mapped I/O unter Benutzung des [Hardware Abstraction Layer](https://github.com/lowlevel-eu/wiki/wiki/Hardware-Abstraction-Layer "HAL"), der vom [Kernel](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") bereitgestellt wird. Nach Außen hin bietet der Treiber ein abstrakteres Interface (wie beispielsweise Unixdatein), um es zu ermöglichen Anwendungen von der konkreten Hardware unabhängig zu programmieren. Ob (ein Teil der) Treiber im User- oder im Kernelmode laufen, ergibt sich aus der Art des [Kernels](https://github.com/lowlevel-eu/wiki/wiki/Kernel "Kernel") (siehe dort für eine ausführlichere Erklärung).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7453/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1669/index.html)

<!-- MediaWiki page 1669; revision 7453; parent 4864; 2010-03-30T12:55:34Z -->
