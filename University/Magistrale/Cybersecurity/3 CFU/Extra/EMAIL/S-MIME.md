# S/MIME

**S/MIME (Secure/Multipurpose Internet Mail Extensions)** è l'altro standard principale per la sicurezza e-mail end-to-end.

- È un'estensione dello standard MIME (il protocollo che permette di inviare allegati e HTML) specificamente progettata per aggiungere funzionalità di sicurezza.
    
- Fornisce le **stesse garanzie di PGP**: riservatezza (tramite crittografia), autenticazione del mittente, integrità del messaggio e non ripudio (tramite firme digitali).
    

---

### La Differenza Chiave: La PKI Centralizzata

Mentre PGP si basa su un modello decentralizzato (il "Web of Trust"), S/MIME utilizza un modello completamente diverso: una **Public Key Infrastructure (PKI)** centralizzata e gerarchica.

- Invece di una "rete di fiducia" gestita dagli utenti, S/MIME si affida a **certificati digitali X.509** (lo stesso standard usato per i siti web HTTPS).
    
- Questi certificati vengono emessi da **Certificate Authorities (CA)**, ovvero terze parti fidate (come DigiCert, Sectigo, IdenTrust). La CA ha il compito di verificare l'identità dell'utente (o dell'azienda) prima di emettere un certificato che lega indissolubilmente la sua chiave pubblica alla sua identità e al suo indirizzo e-mail.
    
- Questo modello offre **meno controllo all'utente** (che deve affidarsi a una CA), ma garantisce un'**interoperabilità molto maggiore**. È integrato nella maggior parte dei client e-mail aziendali (come Outlook, Apple Mail) e dei sistemi operativi, che si fidano "di default" delle principali CA mondiali. Questo permette a due utenti di due aziende diverse di scambiarsi e-mail crittografate senza dover prima scambiare e firmare manualmente le chiavi, come richiesto da PGP.
    

---