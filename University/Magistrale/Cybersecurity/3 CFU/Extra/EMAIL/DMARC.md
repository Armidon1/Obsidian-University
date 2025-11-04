# 🛡️ DMARC

**DMARC (Domain-based Message Authentication, Reporting, and Conformance)** è uno standard tecnico (RFC 7489) che agisce come il **livello di policy** (politica) per l'autenticazione delle e-mail. Aiuta a proteggere i domini dall'essere utilizzati per spam, spoofing e attacchi di phishing.

DMARC, essenzialmente, **"mette insieme [[SPF]] e [[DKIM]]"**. Permette al proprietario di un dominio di:

- Pubblicare le proprie pratiche di autenticazione e-mail (ad esempio, "noi usiamo SPF e DKIM").
    
- Indicare ai server di posta riceventi quali azioni intraprendere se un messaggio fallisce questi controlli di autenticazione.
    
- Abilitare il reporting, consentendo ai riceventi di inviare dati al proprietario del dominio sui messaggi che dichiarano di provenire dal suo dominio.
    

---

### Come funziona DMARC?

#### 1. Pubblicare una Policy

Un amministratore di dominio pubblica una policy DMARC nei record DNS del proprio dominio.

- Si tratta di un **record TXT** nel DNS, formattato in modo speciale.
    
- Viene posizionato su un hostname specifico: `_dmarc.tuodominio.com`.
    

**Esempio di record DMARC:**

> `dig +noall +answer _dmarc.uniroma1.it txt`
> 
> `_dmarc.uniroma1.it. 21600 IN TXT "v=DMARC1; p=reject; pct=10; rua=mailto:lxoyu6mk@ag.eu.dmarcadvisor.com, mailto:dmarc-ar@uniroma1.it; ruf=mailto:lxoyu6mk@fr.eu.dmarcadvisor.com, mailto:dmarc-f@uniroma1.it;"`

**Tag chiave:**

- `v=DMARC1`: Specifica la versione di DMARC.
    
- `p=reject`: Specifica la **policy** (politica) da applicare ai messaggi che falliscono i controlli.
    
- `pct=10`: La **percentuale** di e-mail a cui la policy deve essere applicata. Questo `pct=10` è una misura di sicurezza che consente ai domini di implementare gradualmente una policy restrittiva (applicando `reject` solo al 10% dei fallimenti) mentre monitorano i report.
    
- `rua=mailto:...`: La casella di posta a cui inviare i **report aggregati**.
    
- `ruf=mailto:...`: La casella di posta a cui inviare i **report forensi**.
    

**Policy DMARC:**

- `p=none`: La policy di "monitoraggio". Il ricevente non intraprende azioni (consegna normalmente) ma invia comunque i report. È il primo passo per implementare DMARC.
    
- `p=quarantine`: Il ricevente dovrebbe accettare l'e-mail ma posizionarla in un luogo diverso dall'inbox (tipicamente la cartella spam).
    
- `p=reject`: Il ricevente dovrebbe rifiutare il messaggio completamente (non consegnarlo affatto).
    

#### 2. Controllare Autenticazione e Allineamento

Quando un server di posta in ingresso riceve un'e-mail, cerca la policy DMARC per il dominio che trova nell'intestazione **"From" (RFC 5322)** del messaggio. Questa è l'intestazione `From:` visibile all'utente.

Il server controlla quindi tre fattori chiave:

1. La **firma DKIM** del messaggio è valida?
    
2. Il messaggio proviene da un indirizzo IP consentito dai **record SPF** del dominio?
    
3. Le intestazioni mostrano un corretto **"allineamento di dominio"**?
    

Allineamento di Dominio (Domain Alignment):

Questo è il concetto più importante in DMARC. Risolve le limitazioni di SPF e DKIM abbinando il dominio nell'intestazione From: visibile con i domini utilizzati nei controlli SPF e DKIM.

- **Allineamento SPF:** Il dominio nel `From:` visibile deve corrispondere al dominio nel `Return-Path` (utilizzato per il controllo SPF).
    
- **Allineamento DKIM:** Il dominio nel `From:` visibile deve corrispondere al dominio `d=` nella firma DKIM.
    

Un messaggio supera DMARC se supera _o_ l'SPF allineato _o_ il DKIM allineato. Non è necessario che li superi entrambi. È questo meccanismo che blocca lo spoofing: un'e-mail fraudolenta potrebbe passare il controllo SPF o DKIM per un _altro_ dominio, ma fallirà il controllo DMARC perché quel dominio non è allineato con il dominio `From:` che l'utente vede.

#### 3. Applicare la Policy

Con i risultati dell'autenticazione e dell'allineamento, il server ricevente è pronto ad applicare la policy DMARC del dominio mittente (`none`, `quarantine`, o `reject`) per decidere il destino del messaggio.

#### 4. Inviare Report

Dopo aver determinato il da farsi, il server di posta ricevente segnalerà l'esito al proprietario del dominio mittente utilizzando gli indirizzi specificati nei tag `rua` e `ruf`.

**Report DMARC:**

- **Report aggregati (`rua`):** Sono documenti XML che contengono dati statistici sui messaggi che dichiarano di provenire da un dominio. Includono indirizzi IP, risultati di autenticazione (SPF, DKIM, DMARC) e il numero di messaggi. Sono leggibili automaticamente e sono essenziali per il monitoraggio.
    
- **Report forensi (`ruf`):** Sono copie individuali dei messaggi che hanno fallito l'autenticazione, allegati in un formato speciale. Sono utili per il troubleshooting e per identificare attacchi specifici. A causa di problemi di privacy (poiché contengono il contenuto del messaggio), molti server riceventi scelgono di non inviare report forensi.
    

---

### Esiti del Controllo DMARC

I risultati di questi controlli vengono spesso aggiunti alle intestazioni dell'e-mail nell'header `Authentication-Results`.

Esempio di intestazione:

Authentication-Results: mx.google.com;

dkim=pass header.i=@diag.uniromal.it header.s=google header.b=gx0VIcD5;

spf=pass (google.com: domain of querzoni@diag.uniromal.it designates 209.85.220.41 as permitted sender) smtp.mailfrom=querzoni@diag.uniroma1.it;

dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=diag.uniroma1.it;

Questa intestazione mostra che il messaggio ha superato DKIM (per `diag.uniromal.it`), ha superato SPF (per `diag.uniromal.it`) e quindi ha superato DMARC (grazie all'allineamento con `header.from=diag.uniroma1.it`).

---

### Limitazioni di DMARC
![[Pasted image 20251104175445.png]]

Il problema più grande con DMARC è che policy restrittive (`p=reject`) possono **bloccare messaggi legittimi** che passano attraverso flussi di posta indiretti, come **mailing list** o servizi di **inoltro (forwarding)**.

Questo accade perché gli intermediari spesso "rompono" sia SPF che DKIM:

- **L'inoltro rompe SPF:** L'intermediario (es. la mailing list) invia il messaggio da un **nuovo indirizzo IP** che non è presente nel record SPF del mittente originale, causando il fallimento di SPF.
    
- **L'inoltro rompe DKIM:** Gli intermediari spesso **alterano il contenuto del messaggio**, invalidando la firma DKIM. Le modifiche comuni includono:
    
    - Aggiunta di disclaimer o piè di pagina (es. "Messaggio scansionato da antivirus").
        
    - Aggiunta di tag all'oggetto (es. `Subject: [NomeLista] ...`).
        
    - Visualizzazione dei risultati della scansione antivirus.
        
    - Rimozione di allegati.
        

Questo problema ha portato allo sviluppo di [[ARC]] (Authenticated Received Chain) per tentare di preservare i risultati dell'autenticazione attraverso questi intermediari.