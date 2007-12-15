# Speicherverwaltung

Memory Managment ist ein wichtiger Teil des Betriebssystem, um genau zu sein ist es ein Grundbestandteil eines Betriebssystem.

## Einleitung

Zuerst ist es wichtig zu wissen, was ein Memorymanager eigentlich machen soll. Generell ist der Memorymanager zuständig nachfragenden Prozessen freien Speicher zuzuteilen. Dafür muss natürlich gespeichert werden, welche Speicherbereiche belegt, bzw frei sind. Auch wichtig ist zu unterscheiden zwischen physikalischen Memorymanager und virtuellen Memorymanager. Der physikalische Memorymanager sucht freie Stellen im physikalischen Speicher. Der Virtuelle im virtuellen Speicher. Der physikalische Memorymanager liegt aber eine Schicht über dem virtuellen Memorymanager.

## physikalischer Memorymanager

Der physikalische Memorymanager muss Speicher allozieren und freigeben können. Dafür muss er immer bescheit wissen welcher Speicher schon belegt ist. Dafür gibt es zwei Möglichkeiten. Der physikalischer Memorymanager sollte aber immer so gestaltet sein, dass sich der Rest des OS keine Sorgen über Speicher machen muss.

### Bitmap-Methode

Bei der Bitmap-Methode wird, wie der Name schon sagt, eine Bitmap verwendet. Jedes Bit gibt an ob eine Page frei ist oder nicht. Bei 4GB RAM benötigt man dafür eine 1kB große Bitmap. Um eine freie Page zu finden muss man einfach die Bitmap durchgehen und nachschauen wo die erste leere Page ist.

Vorteile:

- Bitmap verbraucht nur 1kB
- Einfache Verwaltung von verschiedenen Speichertypen
- Es können auch aneinanderhängende Pages gesucht werden

Nachteile:

- Es muss jedes mal (theoretisch) die ganze Bitmap durchgeschaut werden

### Stack-Methode

Bei der Stack-Methode werden alle Adressen von freien Pages auf einen Stack gelegt. Wenn jetzt eine Page benötigt wird, muss man nur eine Adresse vom Stack nehmen. Umgekehrt, um eine Page freizugeben muss nur dessen Adresse wieder auf den Stack gelegt werden. Bei 4GB RAM benötigt man einen Stack von 4MB.

Vorteile:

- Schneller Zugriff

Nachteile:

- Es werden 4MB für den Stack benötigt
- Es können keine aneinanderhängende Pages gesucht werden
- Man kann nur mit Umständen z.B zwischen RAM über und unter 16MB trennen (Hier empfielt sich die benutzung zweier Stacks)

### Fazit

Die Bitmap-Methode sieht zwar auf den ersten Blick viel besser aus, aber den Geschwindigkeitsunterschied zur Stack-Methode sollte man nicht unterschätzen.

## virtueller Memorymanager

Der virtuelle Memorymanager ist dafür zuständig die einzelnen Speicherbereiche der Prozesse zu organisieren. Das wird im Grunde so gemacht: Jeder Prozess bekommt beim Erzeugen mindestens ein Pagedirectory und ein Pagetable. Pagedirectory und Pagetable sind jeweils 4kB größ, die Pages können mithilfe des physikalischen Memorymanagers leicht und dynamisch angefordert werden. Wann immer man ein neues Pagedirectory oder Pagetable braucht, muss man einfach nur eine physikalische Page vom physikalischen Memorymanager anfordern. Natürlich braucht der Prozess auch noch Speicher den er benutzen kann, dieser wird auch mithilfe des physikalischen Memorymanagers angefordert werden und dann leicht in die Pagetables eingetragen werden. Beim Prozesswechsel muss man nur noch CR3 mit dem richtigen Pagedir laden. Man sollte natürlich auf keinen Fall vergessen den Kernel in jeden der Pagedirectories/Pagetables der Prozesse einzutragen.

---

[Originalversion und Autorenschaft](https://lowlevel-eu.github.io/wiki/revisions/2398/index.html) · [MediaWiki-Versionsgeschichte](https://lowlevel-eu.github.io/wiki/history/1591/index.html)

<!-- MediaWiki page 1591; revision 2398; parent 2394; 2007-12-15T22:12:30Z -->
