# Authentication Service (AS)

## 🧐 Che cos'è?
L'**Authentication Service (AS)** è il componente del [[KDC (Key Distribution Center)]] responsabile della verifica iniziale dell'identità dell'utente (login).

È la prima entità con cui un client comunica quando un utente inserisce username e password. Il suo unico scopo è rilasciare il [[TGT (Ticket-Granting Ticket)]] se le credenziali sono corrette.

> [!NOTE] Analogia
> L'AS è come il **controllo passaporti** o la biglietteria all'ingresso del parco.
> Tu dimostri chi sei (passaporto/carta d'identità) e loro ti danno il pass di ingresso (il TGT). Non ti danno ancora accesso alle giostre specifiche, ma ti permettono di entrare nell'area sicura.

---

## ⚙️ Il Workflow (Fase AS)

Questa fase è spesso chiamata **Initial Authentication**.

1. **Richiesta (AS_REQ):**
   Il client invia un messaggio al KDC in chiaro contenente l'username dell'utente.
   * *Importante:* Per evitare di inviare la password sulla rete, il client cifra un timestamp con l'hash della password dell'utente. Questa tecnica si chiama **Pre-Authentication**.

2. **Verifica:**
   L'AS riceve l'username e cerca la chiave corrispondente nel suo database (es. Active Directory).
   * Usa questa chiave per tentare di decifrare il timestamp.
   * Se il timestamp ha senso (è leggibile ed è recente), significa che l'utente conosce davvero la password.

3. **Risposta (AS_REP):**
   Se la verifica ha successo, l'AS invia due cose al client:
   * **Il [[TGT (Ticket-Granting Ticket)]]:** Cifrato con la chiave del KDC (`krbtgt`). Il client non può leggerlo.
   * **La Session Key (Logon Session Key):** Una chiave temporanea che servirà al client per cifrare le future comunicazioni con il [[TGS (Ticket-Granting Server)]]. Questa parte del messaggio è cifrata con la chiave (hash della password) dell'utente, così solo l'utente legittimo può estrarla.

---

## 🛡️ Sicurezza: La Pre-Authentication

La **[[Kerberos]] Pre-Authentication** è fondamentale.
Senza di essa, chiunque potrebbe chiedere all'AS un TGT per *qualsiasi* utente. Anche se l'attaccante non potrebbe usare quel TGT (perché non può decifrare la Session Key allegata), riceverebbe comunque un pacchetto cifrato con la password dell'utente. Potrebbe portare quel pacchetto offline e tentare un attacco Brute Force.
La Pre-Authentication impedisce al KDC di rispondere a chi non dimostra *a priori* di conoscere la password.