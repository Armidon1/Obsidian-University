Ecco la **lista completa** basata sugli esempi e le tabelle presenti nelle slide che hai caricato. Memorizzare questi ti coprirà per la maggior parte degli esercizi d'esame.

### 📋 La Lista dei Porti e Protocolli (Dalle Slide)

|**Servizio / Protocollo**|**Porta (Port)**|**Trasporto**|**A cosa serve?**|**Fonte Slide**|
|---|---|---|---|---|
|**FTP (Data)**|**20**|TCP|Trasferimento dati file|111|
|**FTP (Control)**|**21**|TCP|Comandi di connessione FTP|222|
|**SSH**|**22**|TCP|Accesso remoto sicuro (terminale)|3|
|**Telnet**|**23**|TCP|Accesso remoto _non_ sicuro|4|
|**SMTP**|**25**|TCP|Invio di Email|555|
|**DNS**|**53**|UDP|Risoluzione nomi (es. https://www.google.com/search?q=google.com -> IP)|6|
|**Finger**|**79**|TCP|Info utenti (raro oggi, ma era negli esempi)|7|
|**HTTP (WWW)**|**80**|TCP|Navigazione web non sicura|8888|
|**HTTPS**|**443**|TCP|Navigazione web sicura (lucchetto)|9999|
|**Client Ports**|**> 1023**|TCP/UDP|Porte casuali usate dai client per uscire|10|

---

### 🧠 Trucchetti per ricordare (Memory Aids)

1. **FTP (20, 21):** Sono i primi, perché "File First". Il 21 comanda, il 20 lavora (porta i dati).
    
2. **SSH (22):** "Secure Shell". Due "S" = Due "2". Porta 22.
    
3. **Telnet (23):** Viene subito dopo SSH, ma è vecchio. (22 + 1).
    
4. **SMTP (25):** È a metà strada verso i 50. Ricorda: inviare mail costa "25 cents" (vecchio modo di dire).
    
5. **DNS (53):** Usa la porta **53** ed è tipicamente **UDP** (nelle slide è l'unico esempio esplicito di UDP 11).
    
6. **HTTP (80):** È la porta più famosa. Immagina il Web come un'autostrada a 80 corsie.
    
7. **HTTPS (443):** È l'HTTP (80) con più sicurezza (443 è un numero più grande e complesso).
    

---

### ⚠️ Attenzione: Client vs Server

Una distinzione fondamentale spiegata nelle slide (File `16 2.pdf`, slide 2) è questa:

- **Server Ports (Well-known ports):** Sono quelle < 1024 (come 21, 80, 25). Sono fisse e servono per _ricevere_ connessioni12.
    
- **Ephemeral Ports (Client ports):** Sono quelle > 1023. Sono dinamiche e vengono assegnate al tuo browser/client temporaneamente per ricevere la risposta dal server13.
    

Esempio:

Se tu (Client) navighi su un sito:

- La tua porta (Sorgente): **12345** (Random > 1023)
    
- La porta del sito (Destinazione): **80** o **443** (Fissa)
    
