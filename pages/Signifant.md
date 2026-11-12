# Signifant

**Hinweis:**

Dieser Artikel ist ein Scherzartikel. Er beschreibt (noch) keinen realen Gegenstand.

Ein **signierter Elefant** (oder kurz und gebräuchlicher **Signifant**) ist ein speziell signierter Elefant, der so durch Fälschung geschützt werden soll. Signifanten sind außerdem das potenzielle inoffzielle Maskottchen des Community-Betriebssystems [týndur](T%C3%BDndur "Týndur").

  

## Entstehung

Elefanten wurde vor einigen Jahren als große, massive Tiere von indischen Entwicklern entwickelt. Sie dienten und dienen heute noch der Kommunikation und dem Transport, weshalb sie vor allem in Indien ein wichtiges Kommunikationsmittel sind. Genau genommen basieren Elefanten allerdings auf dem Quellcode von Mammuts. Nachdem diese allerdings nicht mehr von den Usern genutzt wurde, stellte die Natur den Quellcode unter die GNU GPL Version 1. Somit sind Elefanten quasi ein "Rewrite" von Mammuts.

In Zeiten immer größer werdenden Datenverkehrs wurde der Aspekt der Sicherheit größer geschrieben. Man begann, erste Elefanten auf einfachste Art und Weise zu signieren, um sie fälschungssicher zu machen. Cjreek kam dabei auf die Idee, Signifanten im Zusammenhang mit [Binären Datentypen](Bin%C3%A4re-Datentypen "Binäre Datentypen") zu nutzen. Eine erste Spezifikation wird zur Zeit von [Hartmut](https://lowlevel-eu.github.io/wiki/pages/1865/index.html "Benutzer:Hartmut"), [XanClic](https://lowlevel-eu.github.io/wiki/pages/1860/index.html "Benutzer:XanClic") und SHyx0rmz entwickelt.

## Erstellung und Anwendung

Unter Linux wie auch Windows gibt es Tools zur Erstellung und Signierung von Elefanten. Nachfolgend die Erstellung und Signierung eines Elefanten unter Linux:

Mit dem Tool "newelph" wird ein neuer Elefant erstellt. Hier soll der Elefant vier Beine, einen Rüssel haben und nicht mehr als 10 GB wiegen: ` $ newelph --name myelephant.elph --alllegs --longsnout --maxweight=10 `

Der neu erstellte Elefant muss nun signiert werden. Dazu wird zuerst ein Schlüssel mit Hilfe von "create-elph-key" erstellt: ` $ createelphkey --name myelphkey.elphkey --verycomplex=true `

Nach dem man eine Passphrase eingegeben hat, hat man nun den öffentlichen und privaten Schlüssel erstellt. Anschließend kann ein Elefant mit dem privaten Schlüssel signiert werden:

` $ sigelph --elph=myelephant.elph --pubkey=myelphkey.pub.elphkey `

Hierdurch wurde ein signierter Elefant erstellt:

    -----BEGIN PGP SIGNED ELEPHANT-----
    Hash: SHA1
     
                   _..--""-.                  .-""--.._
               _.-'         \ __...----...__ /         '-._
             .'      .:::...,'              ',...:::.      '.
            (     .'``'''::;      Týndur      ;::'''``'.     )
             \             '-)              (-'             /
              \             /                \             /
               \          .'.-.            .-.'.          /
                \         | \0|            |0/ |         /
                |          \  |   .-==-.   |  /          |
                 \          `/`;          ;`\`          /
                  '.._      (_ |  .-==-.  | _)      _..'
                      `"`"-`/ `/'        '\` \`-"`"`
                           / /`;   .==.   ;`\ \
                     .---./_/   \  .==.  /   \ \
                    / '.    `-.__)       |    `"
                   | =(`-.        '==.   ;
             jgs    \  '. `-.           /
                     \_:_)   `"--.....-'
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2.0.17 (GNU/Linux)
     
    iJwEAQECAAYFAk53XcwACgkQFCe/r9OXfcIlugP+KOIsgSRK+SLPEpn6XJdnQ4bK
    aobCz2Rc89+TCRR07Zk+t4YSJTmxdcCpp/mTVqQ7OpcuXsgmuksTaQBArhENrmIr
    PouSOVDQlSTyfO9aQJdslfVcAQiDC8vQnRGAPTwDgvF2fpZH7DnUZep97iDaEIef
    dAFs9kYCdjRG9Xv3ciQ=
    =f+O8
    -----END PGP SIGNATURE-----
    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v2.0.17 (GNU/Linux)
     
    mI0ETndcxgEEANIB5qaqgQstA3MP5QZzBno5pCQhCXGoz0/U0duyhJQTbEXwEQVC
    AeNFVAHyj8Z+h1BSPfPwXA8VsxKiV5nDUeNLf2/qNAnARaU2SUC/Ne3seHUpO6fH
    kKC0Aczu7aSf8Wa4/ZDW6iTzTUZxI0oqKWVJt8SYBiQ9gSr0VBoQGnh7ABEBAAG0
    N1NpZ25pZmFudCAoVOG7s25kdXIgTWFza290dGNoZW4pIDxzaWduaWZhbnRAdHlu
    ZHVyLm9yZz6IuAQTAQIAIgUCTndcxgIbAwYLCQgHAwIGFQgCCQoLBBYCAwECHgEC
    F4AACgkQFCe/r9OXfcJmkAQAxDLir+ez/XrssrFukvpTrXesPEL+V550iXY7WcdM
    iZET6xuWeDHnZFgo92iVjg6W7nUHJCy1PrdkbmcnPQNDGvwVAnXhr/Fwg2tSm7pD
    wz0AEdWLYhF/eqJlcm+L/1+YH0azbcMllJ0W5dJJi/cZ8lWUS0XwUYyYN8ExFOWb
    tP8=
    =NW7d
    -----END PGP PUBLIC KEY BLOCK----

## Signifanten in der Betriebssystementwicklung

Signifanten verrichten Ihren Dienst in der Betriebssystementwicklung vor allem auf Mailinglisten. Große Patches werden meist mit Signifanten ausgeliefert, damit selbige besonders schwer auf der Mailingliste liegen und beachtet werden. Allerdings ist, bedingt durch die Größe eines durchschnittlichen Signifanten, die E-Mail überdurchschnittlich groß, sodass das Verschicken, je nach Internetverbindung, eine Zeit lang dauern kann.

### Signifanten und týndur

Mit der Version 0.3.0 werden Signifanten offiziell auch von týndur unterstützt. Entsprechende Programme zur Erstellung signierter Elefanten werden zur Zeit entwickelt.

Der Signifant ist auch das inoffzielle Maskottchen von týndur.

## Weblinks

- [Blauer Signifant](http://images.google.de/imgres?imgurl=http://www.unser-kalle.de/shop/images/Pict0024_.jpg&imgrefurl=http://www.unser-kalle.com/shop/&usg=__9tEk2g_ddqWVK4ha9yrqX0oofow=&h=794&w=538&sz=208&hl=de&start=2&um=1&tbnid=1ADYtE-TcDQyEM:&tbnh=143&tbnw=97&prev=/images%3Fq%3DSignierter%2BElefant%26hl%3Dde%26sa%3DG%26um%3D1)
- [Speziell signierter Elefant](http://images.google.de/imgres?imgurl=http://www.glaskilian.de/typo3temp/pics/0d9af209a1.jpg&imgrefurl=http://www.glaskilian.de/Grosser-Elefant-signiert-Balza.1095%2BB6YmFja1BJRD0xMDk1JnByb2R1Y3RJRD0xMjk3OSZwaWRfcHJvZHVjdD0xMDk1JmRldGFpbD0_.0.html&usg=__goXzG_oaA4-M4Tm5_F9-GMdAzqY=&h=722&w=800&sz=62&hl=de&start=5&um=1&tbnid=0juXyWslJAgL3M:&tbnh=129&tbnw=143&prev=/images%3Fq%3DSignierter%2BElefant%26hl%3Dde%26sa%3DG%26um%3D1)

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/10157/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/2047/index.html)

<!-- MediaWiki page 2047; revision 10157; parent 10152; 2011-09-23T22:07:24Z -->
