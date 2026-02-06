# DNS Fast-Fluxing

**Tags:** #CyberSecurity #DNS #Botnet #Malware #NetworkSecurity #Evasion **Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Chiave

Il **DNS Fast-Fluxing** è una tecnica di evasione utilizzata dai criminali informatici per nascondere e proteggere le infrastrutture malevole (come server di Phishing o server [[Command-and-Control (C2)]]).

Sfrutta la natura dinamica del protocollo DNS per associare un singolo nome di dominio malevolo (es. `malicious-domain.com`) a un elenco di indirizzi IP che cambia a ritmi rapidissimi.

> [!abstract] Obiettivo Rendere l'infrastruttura "mobile" e resiliente. Se le forze dell'ordine bloccano un indirizzo IP, il dominio sta già puntando a un altro IP diverso, mantenendo il servizio attivo.

---

## ⚙️ Meccanismo Tecnico

Il funzionamento si basa su tre pilastri fondamentali descritti nelle fonti:

1. **Rotazione Rapida degli IP:**
    - I record DNS di tipo **A** (che mappano il nome all'IP) cambiano costantemente.
    - Ogni risposta DNS restituisce un sottoinsieme diverso di indirizzi IP presi da un pool molto più grande.
2. **TTL (Time-To-Live) Cortissimo:**
    - I valori TTL vengono impostati intenzionalmente molto bassi (es. **60 secondi** o meno).
    - Questo costringe i client e i resolver a non memorizzare la risposta in cache a lungo e a interrogare nuovamente il server DNS quasi subito, ricevendo nuovi IP.
3. **Botnet come Proxy:**
    - Gli indirizzi IP restituiti non appartengono al vero server dell'attaccante.
    - Appartengono a **host compromessi (bot)** che agiscono come _reverse proxies_.
    - Questi bot ricevono il traffico dalla vittima e lo inoltrano al vero "Backend Server" nascosto, proteggendolo dall'identificazione diretta.

---

## 🗂️ Varianti di Fast-Flux

Le slide identificano due livelli di complessità:

### 1. Single-Flux

- **Cosa cambia:** Ruotano solo i record **A** (l'indirizzo IP del server web finale).
- **Effetto:** Nasconde i nodi front-end (i proxy/bot), ma il server DNS autoritativo (NS) rimane statico e può essere individuato/bloccato.

### 2. Double-Flux

- **Cosa cambia:** Ruotano sia i record **A** che i record **NS** (Name Server).
- **Effetto:** Anche l'infrastruttura DNS che gestisce il dominio cambia continuamente indirizzo IP.
- **Impatto:** È molto più difficile da abbattere (takedown) perché non c'è un singolo punto fisso da colpire; l'intera infrastruttura è "fluida".

---

## 🔗 Collegamenti

- [[Botnet]] (L'infrastruttura fisica usata per fornire gli IP rotanti)
- [[Command-and-Control (C2)]] (Il servizio che il Fast-Fluxing protegge)
- [[Domain Generation Algorithm (DGA)]] (Spesso usato in combinazione per generare i nomi di dominio)
- [[DNS Security]]