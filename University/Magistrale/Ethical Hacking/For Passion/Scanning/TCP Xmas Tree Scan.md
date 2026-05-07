# Xmas Tree Scan 
## I flag TCP: FIN, URG, PUSH

Ogni pacchetto TCP ha un header con **6 flag** (bit) che dicono al destinatario cosa fare con il pacchetto:

| Flag    | Significato | Uso normale                                                |
| ------- | ----------- | ---------------------------------------------------------- |
| **SYN** | Synchronize | Aprire una connessione                                     |
| **ACK** | Acknowledge | Confermare ricezione                                       |
| **FIN** | Finish      | Chiudere una connessione ordinatamente                     |
| **RST** | Reset       | Chiudere di forza / rifiutare                              |
| **URG** | Urgent      | I dati sono urgenti, il ricevitore deve processarli subito |
| **PSH** | Push        | Non bufferizzare, inviare subito i dati all'applicazione   |

**FIN** viene usato quando vuoi chiudere una connessione già aperta — è una chiusura "gentile", al contrario del RST.

**URG** attiva il campo "urgent pointer" nell'header: dice al ricevitore di saltare la coda e processare subito questi dati. Usato rarissimamente in protocolli come Telnet.

**PSH** dice allo stack TCP di non accumulare i dati nel buffer ma di consegnarli immediatamente all'applicazione. Utile per comunicazioni interattive (es. SSH keystroke per keystroke).

---

## Xmas Tree Scan — perché si chiama così

Si chiama "albero di Natale" perché **accende tutti i flag contemporaneamente** — FIN + URG + PSH — come le luci su un albero. È un pacchetto assurdo e malformato, che nessuna connessione legittima manderebbe mai.

![[Pasted image 20260507182522.png]]

## Logica dello scan

Il trucco sfrutta una regola dell'**RFC 793** (lo standard TCP originale del 1981):

- **Porta chiusa** → il target risponde con **RST** (il comportamento "corretto" per un pacchetto inatteso)
- **Porta aperta** → il target **non sa cosa fare** con un pacchetto FIN+URG+PSH su una connessione che non esiste, e lo scarta silenziosamente

Nmap interpreta il silenzio come **porta aperta/filtrata**.

## Perché usarlo invece del SYN scan

| |SYN scan|Xmas scan|
|---|---|---|
|Completa l'handshake|No (half-open)|No|
|Appare nei log|Spesso sì|Meno probabile|
|Bypassa alcuni firewall stateless|No|Sì|
|Funziona su Windows|Sì|**No**|
|Funziona su Linux/BSD|Sì|Sì|

Lo Xmas scan è più **stealth** perché molti firewall e IDS degli anni '90-2000 filtravano i SYN ma non controllavam pacchetti con flag anomali. Oggi gli IDS moderni lo riconoscono comunque.

---

Vuoi che faccia anche la nota Obsidian su questo argomento?