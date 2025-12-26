# Ticket Granting Service (TGS)

## 🧐 Che cos'è?
Il **Ticket Granting Service (TGS)** è uno dei due componenti logici principali del [[KDC (Key Distribution Center)]] nel protocollo [[Kerberos]] (l'altro è l'Authentication Service o AS).

Il suo ruolo è fare da "sportello di smistamento": riceve un [[TGS (Ticket-Granting Server)]] valido e rilascia in cambio un [[Service Ticket]] (ST) specifico per accedere a una risorsa di rete (come un file server, un database SQL o una stampante).

> [!NOTE] In sintesi
> * **[[AS (Authentication Service)]]:** Scambia *Password* -> *TGT*
> * **TGS (Ticket Granting Service):** Scambia *TGT* -> *Service Ticket*

---

## ⚙️ Il Workflow (Fase TGS)

Questa fase avviene dopo che l'utente si è già autenticato e possiede un TGT.

1. **Richiesta (TGS_REQ):**
   Il client vuole accedere a un servizio (es. `CIFS/fileserver`). Invia al TGS:
   * Il proprio [[Ticket-Granting Ticket (TGT)]].
   * Un "Authenticator" (crittografato con la chiave di sessione) per provare che è il legittimo proprietario del TGT.
   * Il nome del servizio richiesto (SPN - Service Principal Name).

2. **Verifica:**
   Il TGS possiede la chiave segreta `krbtgt`, quindi può decifrare il TGT. Controlla:
   * Se il TGT è valido e non scaduto.
   * Se l'Authenticator corrisponde.
   * Se l'utente ha i permessi basilari per richiedere quel servizio.

3. **Risposta (TGS_REP):**
   Se tutto è corretto, il TGS genera il **[[Service Ticket]] (ST)** per quel servizio specifico.
   * Il Service Ticket è crittografato con la chiave segreta del *Servizio di destinazione* (che il TGS conosce).
   * Il client riceve questo ticket ma non può leggerlo; lo inoltrerà semplicemente al servizio finale.

---

## 🛡️ Sicurezza e Vantaggi

* **Minimizzazione dell'esposizione:** L'utente inserisce la password solo una volta (all'inizio, con l'AS). Il TGS gestisce tutte le richieste successive usando il TGT, senza che la password viaggi mai sulla rete.
* **Isolamento:** Ogni Service Ticket è valido solo per *quel* servizio specifico. Se un attaccante intercetta un Service Ticket per la stampante, non può usarlo per accedere al server di posta.

---

## ⚠️ Attacchi Correlati

Il TGS è coinvolto in un attacco molto diffuso in ambiente Active Directory chiamato **Kerberoasting**.

* **Kerberoasting:** Un attaccante (che ha già un account utente valido) può richiedere al TGS dei Service Ticket per altri servizi (es. SQL Server).
* Poiché il Service Ticket è crittografato con la chiave del servizio (derivata dalla password dell'account di servizio), l'attaccante può portare il ticket offline e tentare di "craccarlo" (Brute Force) per scoprire la password in chiaro di quell'account di servizio.

---

## 🔗 Collegamenti
- [[Kerberos]]
- [[Ticket-Granting Ticket (TGT)]] - Il biglietto necessario per parlare con il TGS.
- [[Service Ticket]] - Il prodotto finale rilasciato dal TGS.
- [[KDC]] - Il contenitore che ospita il TGS.