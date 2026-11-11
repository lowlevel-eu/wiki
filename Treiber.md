# Treiber

Als **Treiber** wird der Teil eines [Betriebssystems](Betriebssystem "Betriebssystem") bezeichnet, der direkt mit der Hardware kommuniziert. Dies geschieht über [I/O Ports](I-O-Ports "I/O Port") oder Memory Mapped I/O unter Benutzung des [Hardware Abstraction Layer](Hardware-Abstraction-Layer "HAL"), der vom [Kernel](Kernel "Kernel") bereitgestellt wird. Nach außen hin bietet der Treiber ein abstrakteres Interface (wie beispielsweise Unixdateien), um es zu ermöglichen, Anwendungen von der konkreten Hardware unabhängig zu programmieren. Ob (ein Teil der) Treiber im User- oder im Kernelmode laufen, ergibt sich aus der Art des [Kernels](Kernel "Kernel") (siehe dort für eine ausführlichere Erklärung).

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/7455/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1669/index.html)

<!-- MediaWiki page 1669; revision 7455; parent 7453; 2010-03-30T13:39:55Z -->
