# Týndur/Qemu

Diese Seite ist ein Artikel, welcher **mehr** haben könnte..  

Wenn du mehr darüber weißt oder recherchieren willst, bist **du** aufgerufen, dies zu tun. Wenn du dir in einer Sache nicht sicher bist, dann stell es auf die Diskussionsseite.

  

## Komplette Batch Datei

Mit dieser Batch-Datei sollte man [týndur](T%C3%BDndur.md "Týndur") unter [QEMU](QEMU.md "QEMU") zum Laufen bringen:

    REM Start qemu on windows.
    @ECHO OFF

    REM SDL_VIDEODRIVER=directx is faster than windib. But keyboard cannot work well.
    SET SDL_VIDEODRIVER=windib

    REM SDL_AUDIODRIVER=waveout or dsound can be used. Only if QEMU_AUDIO_DRV=sdl.
    SET SDL_AUDIODRIVER=dsound

    REM QEMU_AUDIO_DRV=dsound or fmod or sdl or none can be used. See qemu -audio-help.
    SET QEMU_AUDIO_DRV=dsound

    REM QEMU_AUDIO_LOG_TO_MONITOR=1 displays log messages in QEMU monitor.
    SET QEMU_AUDIO_LOG_TO_MONITOR=0

    REM PCI-based PC(default): -M pc 
    REM ISA-based PC         : -M isapc
    REM -M isapc is added for NE2000 ISA card.

    qemu.exe -L . -m 128 -fda tyndur.img -boot a -soundhw all -localtime -net nic,model=rtl8139 -net user

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10839/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1907/index.html)

<!-- MediaWiki page 1907; revision 10839; parent 5599; 2012-09-16T14:19:59Z -->
