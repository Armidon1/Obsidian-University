# SPF – Sender Policy Framework

SPF è un meccanismo di autenticazione e-mail che consente al proprietario di un dominio di specificare quali server di posta (identificati dai loro indirizzi IP) sono autorizzati a inviare e-mail per conto di quel dominio.

- Definisce i server di posta autorizzati tramite **record TXT nel DNS**.
    
- Il suo scopo è validare l'**indirizzo IP del server mittente**.
    
- Risponde alla domanda: "Questo server IP è autorizzato a inviare e-mail per conto di questo dominio?"
    

### Esempio di Record

```
example.net TXT "v=spf1 mx a:pluto.example.net include:aspmx.googlemail.com -all"
```

![[Pasted image 20251028162915.png]]

Analizziamo questo record:

- `v=spf1`: Indica che si tratta di un record SPF versione 1.
    
- `mx`: Autorizza tutti i server elencati nei record MX (Mail Exchange) del dominio `example.net`.
    
- `a:pluto.example.net`: Autorizza l'indirizzo IP che risulta dalla risoluzione DNS (record A) di `pluto.example.net`.
    
- `include:aspmx.googlemail.com`: Include (e autorizza) tutti gli IP definiti nel record SPF di Google. Questo è il meccanismo usato per delegare l'invio a provider terzi (es. Google Workspace, SendGrid, Mailchimp).
    
- `-all`: Questo è il qualificatore. Il trattino (`-`) significa **Hard Fail**. Dice al server ricevente: "Se l'IP mittente non corrisponde a nessuna delle regole precedenti, _rifiuta_ il messaggio".
    
    - Alternative comuni sono `~all` (Soft Fail: "accetta ma marca come sospetto") o `?all` (Neutral: "non ho un'opinione").
        

### Come funziona

Quando un server di posta riceve un'e-mail, esegue i seguenti passaggi:

1. **Identifica il dominio mittente:** Legge il dominio dall'indirizzo **`MAIL FROM:`** (il mittente della _busta_ SMTP), non dall'intestazione `From:` (quella visibile all'utente).
    
2. **Query DNS:** Il server ricevente interroga il DNS per ottenere il record TXT (SPF) di quel dominio.
    
3. **Verifica IP:** Confronta l'indirizzo IP del server che ha inviato il messaggio con l'elenco di IP e regole presenti nel record SPF.
    

**Risultati:**

- **Pass (Superato):** Se l'IP del server mittente è presente nell'elenco, l'e-mail supera il controllo SPF.
    
- **Fail (Fallito):** Se l'IP non è presente, il controllo SPF fallisce. Il server ricevente può quindi decidere di rifiutare il messaggio (come nell'esempio seguente), contrassegnarlo come spam o accettarlo (in base alla policy locale e al qualificatore `-all` o `~all`).
    

### Esempio di Errore (Bounce SMTP)

```
<XXXX.YYYY@gmail.com>: host gmail-smtp-in.l.google.com[173.194.78.26]
said: 550-5.7.1 [aa.bb.cc.dd] The IP you're using to send mail is not
authorized to 550-5.7.1 send email directly to our servers. Please use the SMTP relay at your 550-5.7.1 service provider instead. Learn more at 550 5.7.1 http://support.google.com/mail/bin/answer.py?answer=10336 fl4si3665795wib.12 - gsmtp (in reply to end of DATA command)
```

Questo è un classico messaggio di rifiuto (codice 550). Il server di Google sta dicendo al server all'IP `aa.bb.cc.dd` che il suo IP non è autorizzato dal record SPF del dominio per cui sta cercando di inviare e-mail.

### Esempi di controllo (dig/nslookup)

Queste immagini mostrano come appaiono i record SPF quando vengono interrogati tramite strumenti a riga di comando.

![[Pasted image 20251028163320.png]]

![[Pasted image 20251028163346.png]]

---

### Limitazioni di SPF

- **Si rompe con l'inoltro (forwarding) e le mailing list:** Questa è la limitazione più grande. Se un utente inoltra un'email, o se l'email passa attraverso una mailing list, l'IP che il destinatario finale vedrà è quello del server di inoltro (o della mailing list), non quello del mittente originale. Questo IP quasi certamente non sarà nel record SPF del mittente originale, causando un fallimento (Fail) di SPF.
    
- **Nessuna protezione del `From:` visibile:** SPF controlla solo il mittente della _busta_ (`MAIL FROM:`). Un utente malintenzionato può inviare un'email con `MAIL FROM:<attacker@evil.com>` (che supera il controllo SPF di `evil.com`) ma con l'intestazione visibile `From: "CEO" <ceo@azienda-vittima.com>`. L'e-mail supera SPF ma è comunque un tentativo di spoofing.
    
- **Nessuna integrità del contenuto / Protezione del corpo:** SPF non si occupa minimamente del contenuto del messaggio. Non firma l'e-mail e non garantisce che il corpo o l'oggetto non siano stati modificati durante il transito.
    
- **Rischi di errata configurazione:** Un record SPF complesso, specialmente con molti `include`, può essere difficile da gestire. Dimenticare di autorizzare un servizio legittimo (es. una piattaforma di newsletter) può causare il blocco di e-mail valide.
    

---
# Example
vediamo passo per passo **come un server ricevente esegue il controllo SPF** quando riceve una mail.
## 🧠 Scenario di partenza

Immagina che arriva una mail così:

```
Return-Path: <user@example.com>
From: user@example.com
To: mario@azienda.it
Received from: 203.0.113.5
```

Il server ricevente è quello di `azienda.it`.

---

## 🧩 Passo 1 – Estrae il dominio da verificare

SPF si basa **sul dominio nel Return-Path (MAIL FROM)**, non su quello visibile nel campo “From:” che vedi nel client.

👉 Qui il dominio da verificare è `example.com`.

---

## 🧩 Passo 2 – Interroga il DNS del dominio

Il server chiede al DNS di `example.com` il record TXT per SPF:

```
example.com.  IN  TXT  "v=spf1 ip4:203.0.113.5 include:_spf.google.com -all"
```

---

## 🧩 Passo 3 – Analizza il record SPF

Regole elencate:

1. `ip4:203.0.113.5` → server con questo IP è autorizzato
    
2. `include:_spf.google.com` → anche i server nei record di Google sono autorizzati
    
3. `-all` → tutti gli altri _non lo sono_ (fail forte)
    

---

## 🧩 Passo 4 – Confronta l’IP mittente

Il server ricevente confronta l’IP del mittente (in questo caso `203.0.113.5`) con quelli elencati nel record SPF.

- ✅ **Match trovato** → `SPF PASS`
    
- ❌ **Nessuna corrispondenza** → `SPF FAIL`
    
- ⚠️ **Regola “~all”** → `SPF SOFTFAIL`
    
- ❓ **Regola “?all”** → `SPF NEUTRAL`
    
- 💤 **Assenza di record SPF** → `SPF NONE`
    
- ⚙️ **Errore DNS o troppi include (>10)** → `SPF TEMPERROR` o `PERMERROR`
    

---

## 🧩 Passo 5 – Aggiunge l’header di autenticazione

Il server ricevente aggiunge un’intestazione nel messaggio, tipo:

```
Received-SPF: pass (google.com: domain of user@example.com designates 203.0.113.5 as permitted sender)
```

Oppure:

```
Received-SPF: fail (example.com: domain does not designate 185.22.55.10 as permitted sender)
```

Queste righe puoi vederle nelle **intestazioni complete (“Show original”)** di una mail.

---

## 🧩 Passo 6 – Decisione finale (policy antispam)

Il risultato SPF viene poi combinato con:

- DKIM (firma digitale del contenuto)
    
- DMARC (policy del dominio: cosa fare se SPF/DKIM falliscono)
    
- altri segnali (reputazione IP, contenuto, allegati, ecc.)
    

💡 Ad esempio:  
DMARC può dire “se SPF o DKIM falliscono → rifiuta la mail”.

---

## 🧭 Riassunto finale

|Stato SPF|Significato|Azione tipica|
|---|---|---|
|**pass**|Server autorizzato|Accetta la mail|
|**fail (-all)**|Server non autorizzato|Rifiuta / spam|
|**softfail (~all)**|Non autorizzato ma tollerato|Accetta ma segna sospetto|
|**neutral (?all)**|Nessuna info certa|Nessuna azione speciale|
|**none**|Nessun record SPF|Nessuna protezione|
|**permerror/tempError**|Errore DNS o sintassi|Trattato come fail o ignorato|

---

# quindi semplicemente il DNS deve contenere, per ogni dominio, una lista di server che possono inviare le email per conto del dominio stesso?

Esatto ✅ — è proprio così!

In parole semplici:

> Il **record SPF** è una **regola pubblicata nel DNS del dominio** che **elenca i server autorizzati** a inviare email _per conto_ di quel dominio.

---

### 🧩 In pratica

Nel DNS del dominio (es. `miodominio.it`) ci sarà una voce come:

```
miodominio.it.  IN  TXT  "v=spf1 ip4:203.0.113.5 include:_spf.google.com -all"
```

Significa:

- `ip4:203.0.113.5` → il server con quell’IP può inviare email per `@miodominio.it`
    
- `include:_spf.google.com` → anche i server che Google usa per Gmail/Workspace possono farlo
    
- `-all` → **tutti gli altri sono _non autorizzati_**
    

---

### 🔐 In sintesi

|Elemento|Funzione|
|---|---|
|**DNS record TXT (SPF)**|Elenco pubblico dei server autorizzati|
|**Server mittente**|Deve comparire nella lista o in un record “include”|
|**Server ricevente**|Controlla che l’IP sia autorizzato prima di fidarsi|
|**Scopo**|Impedire che altri mandino email fingendosi il tuo dominio (spoofing)|

---

### 💡 Quindi:

- **SPF è dichiarativo** → “Questi server possono parlare a nome mio.”
    
- **Il controllo lo fa chi riceve la mail**, non chi la invia.
    

---

# però potrebbe essere manomesso per inserire il server di un adversary che può fare finta di essere qualcun'altro

Domanda **molto intelligente 🔥** — e sì, hai centrato un punto **cruciale di sicurezza DNS e autenticazione email**.

Vediamolo con precisione 👇

---

## 🧩 1. È vero: se qualcuno _manomette il DNS_, può falsificare l’SPF

Il record SPF è **pubblicato nel DNS del dominio**, quindi:

> chiunque abbia il **controllo (o accesso amministrativo)** al DNS del dominio  
> può modificare il record SPF e **autorizzare server arbitrari**, anche malevoli.

Esempio di manomissione:

```
v=spf1 ip4:203.0.113.5 -all
```

→ modificato in

```
v=spf1 ip4:203.0.113.5 ip4:10.10.10.10 -all
```

Ora anche `10.10.10.10` (server dell’attaccante) risulterebbe “autorizzato” ad inviare mail per il dominio 😬

---

## 🔒 2. Ma questo richiede il **controllo del DNS del dominio**

Quindi, l’attaccante dovrebbe:

- ottenere l’accesso al **pannello DNS** (es. del registrar o del provider cloud), oppure
    
- **compromettere il dominio** tramite _DNS hijacking_, _DNS cache poisoning_ o un attacco supply chain sul provider.
    

👉 In pratica: non può farlo “da fuori” senza violare qualcosa.

---

## 🛡️ 3. Come si protegge un dominio da questo rischio

Ecco le contromisure principali:

|Protezione|Descrizione|
|---|---|
|**DNSSEC**|Firma crittografica dei record DNS per impedirne la manomissione o falsificazione in transito. Il server ricevente può così verificare l’autenticità del record SPF.|
|**Access control forte sul DNS**|Limitare chi può modificare i record (autenticazione MFA sul pannello DNS).|
|**Logging e monitoraggio DNS**|Tenere traccia di tutte le modifiche ai record TXT.|
|**DMARC**|Anche se SPF viene manomesso, DMARC impone una _policy del dominio_ (reject/quarantine) basata su SPF e DKIM, e invia report agli amministratori.|
|**DKIM**|Firma crittografica del contenuto della mail — anche se SPF viene falsificato, DKIM rimane una prova crittografica valida che non può essere falsificata senza la chiave privata.|

---

## 🧠 4. Quindi, in sintesi:

- SPF **non è sicuro da solo**, perché si basa su DNS (che può essere compromesso).
    
- Serve **insieme a DKIM e DMARC** per ottenere una protezione completa:  
    → SPF dice _“chi può inviare”_,  
    → DKIM dice _“questa mail non è stata modificata”_,  
    → DMARC dice _“cosa fare se le verifiche falliscono”_.
    

---

# i server di google inseriti nell'include, servono per fare forwarding dell'email nel dominio interno di gmail?

Domanda **eccellente 🔥** — è chiaro che stai andando davvero in profondità nel funzionamento dell’email authentication.

La risposta breve è:

> ❌ No, i server di Google inclusi nell’`include:_spf.google.com` **non servono per il forwarding interno**,  
> ✅ ma per **autorizzare i server di Google a inviare email “verso l’esterno” per conto del tuo dominio.**

Ora vediamo **esattamente cosa succede** 👇

---

## 🧩 1. Cosa fa `include:_spf.google.com`

Quando scrivi nel tuo record SPF qualcosa come:

```
v=spf1 include:_spf.google.com -all
```

stai dicendo:

> “Tutti i server che Google utilizza per inviare posta (SMTP) sono autorizzati a spedire email a nome mio.”

Quindi se usi **Google Workspace** (ex G Suite) e mandi una mail da `utente@miodominio.it`,  
Google la invierà da uno dei suoi IP — e grazie a quell’`include`, il server ricevente saprà che è **autorizzato**.

---

## 🧩 2. Non è per il _forwarding interno_

Il “forwarding interno” (cioè lo spostamento della posta tra server interni a Gmail) **non coinvolge SPF**:

- Google gestisce tutto **all’interno della sua infrastruttura**, senza verifiche SPF tra server interni.
    
- SPF è usato **solo nei controlli esterni**, cioè **quando una mail entra o esce da Gmail**.
    

In altre parole:

> SPF è una _policy pubblica DNS_ per dire “chi può spedire verso Internet a nome mio”,  
> non una regola di routing interna.

---

## 🧩 3. Perché Google usa gli _include_

I record SPF di Google sono molto complessi e modulari:  
`_spf.google.com` include a sua volta altri record (`_netblocks.google.com`, `_netblocks2`, `_netblocks3`, ecc.) che elencano **centinaia di IP** usati da:

- Gmail (smtp.gmail.com)
    
- Google Workspace
    
- i server di mailing list e relay di Google
    

👉 In questo modo tu non devi scrivere tutti quegli IP nel tuo SPF — basta l’`include`.

---

## 🧩 4. Esempio di flusso reale

1. `utente@miodominio.it` (ospitato su Google Workspace) invia una mail.
    
2. Gmail la spedisce da un IP di Google (es. `209.85.220.65`).
    
3. Il destinatario (`outlook.com`) riceve la mail e vede:
    
    - MAIL FROM: `miodominio.it`
        
    - IP mittente: `209.85.220.65`
        
4. Outlook controlla nel DNS di `miodominio.it` → trova `include:_spf.google.com`.
    
5. Va a leggere `_spf.google.com` e scopre che `209.85.220.65` è incluso.  
    → **SPF PASS ✅**
    

---

## 🧩 5. Forwarding e SPF: dove nasce il problema

Il forwarding (inoltro automatico di email tra domini diversi) può **rompere SPF**, perché:

- il server che inoltra diventa il “mittente effettivo”,
    
- ma il suo IP **non è nel record SPF originale**.
    

👉 Per risolvere, si usa **SRS (Sender Rewriting Scheme)**, oppure si affida la protezione a **DKIM**, che non dipende dall’IP.

---

## ✅ In sintesi

|Cosa|Serve a cosa|Coinvolge SPF?|
|---|---|---|
|`include:_spf.google.com`|Autorizza i server Google a inviare mail per il tuo dominio|✅ Sì|
|Forwarding interno Gmail → Gmail|Consegna interna|❌ No|
|Forwarding esterno (tra domini)|Può rompere SPF|⚠️ Sì (serve SRS o DKIM)|

---

# In che modo le mailing list rompono SPF?

Ottima domanda — le mailing list sono uno dei casi tipici dove SPF “si rompe” nella pratica. Ti spiego **perché succede**, **quando succede**, e **come si può mitigare** (con esempi concreti e consigli pratici).

---

## Perché le mailing list rompono SPF (concetto chiave)

SPF controlla l’IP **che invia fisicamente** il messaggio (envelope MAIL FROM / Return-Path) rispetto al dominio presente in quel MAIL FROM.  
Le mailing list **ricevono** un messaggio e poi **lo ritrasmettono** ai propri iscritti **da loro stessi** (i server della lista), quindi l’IP mittente finale sarà quello della mailing list — **non** l’IP del server originale che ha inviato l’email.  
Se il dominio nel `MAIL FROM` originale è `utente@dominioA.com`, ma la mail viene inviata ai destinatari da `list-server@lista.org`, il controllo SPF fatto dal destinatario **verificherà dominioA rispetto all’IP di lista.org** → quasi sempre **mismatch → SPF fail**.

---

## Due comportamenti delle liste a confronto (decisivo)

1. **Resend (resend/rewrite)** — la mailing list crea un _nuovo_ messaggio e lo invia ai membri come se fosse la lista (sostituisce l’envelope, spesso aggiunge footer/subject).  
    → **SPF fallisce** per il dominio originale (perché l’IP non è autorizzato).
    
2. **Redirect (forward senza cambiare envelope)** — la lista inoltra il messaggio mantenendo il `MAIL FROM` originale (idealmente).  
    → **SPF può ancora passare**, perché il MAIL FROM rimane dominioA e il mittente effettivo è ancora il server originale — _ma_ pochi MTA usano questo comportamento; inoltre è meno sicuro / complicato per la lista.
    

La maggior parte delle moderne mailing list fa **resend** / rewrite → quindi SPF si rompe.

---

## Altri fattori che peggiorano il problema

- **La lista modifica il messaggio** (aggiunge footer, modifica subject): questo invalida DKIM se la mail originale era firmata, quindi perdi anche la protezione DKIM.
    
- **DMARC** può richiedere allineamento tra From: (visibile) e SPF/DKIM. Anche se DKIM passa ma non è allineato, DMARC potrebbe fallire se il dominio non è allineato.
    
- **Forwarding semplice** (es. inoltri personali) ha lo stesso problema se il forwarder non applica SRS.
    

---

## Come si mitiga (soluzioni pratiche)

### Per le **mailing list / amministratori**

- **Usare SRS (Sender Rewriting Scheme)** per i forward: rewrite del Return-Path in modo che l’envelope appartenga al dominio della lista e sia verificabile; questo evita bounce a indirizzi originali e aiuta SPF (ma non è sempre implementato).
    
- **Firmare i messaggi con DKIM** usando la chiave della lista: la firma sulla versione che la lista invia permette al destinatario di verificare che la lista è l’autore di quella "resend".
    
- **Implementare ARC (Authenticated Received Chain)**: ARC permette di trasferire i risultati di autenticazione (SPF/DKIM) dalla lista al destinatario in modo che il destinatario possa fidarsi delle verifiche fatte prima che la lista modificasse il messaggio.
    
- **Evitare modifiche non necessarie** al corpo/subject quando possibile (per preservare DKIM originale).
    
- **Documentare nei header** chi ha inviato/ritrasmesso (List-Id, List-Post, Received) — aiuta l’analisi.
    

### Per i **proprietari di domini che usano liste**

- **Firmare con DKIM** i messaggi dal tuo dominio: una firma valida **prima** che la lista modifichi il messaggio può essere trasferita tramite ARC (se la lista lo supporta).
    
- **Non fare affidamento solo su SPF**: usa DKIM+DMARC correttamente per gestire i casi di inoltro/lista.
    

### Per i **destinatari / provider di posta**

- **Supportare ARC**: permette di accettare mail inoltrate attraverso mailing list che hanno validato il messaggio originario.
    
- **Combinare segnali**: usare DKIM, SPF, ARC e il contenuto per decidere se consegnare/spam/rifiutare.
    

---

## Esempio pratico di cosa succede (intestazioni semplificate)

Mittente originale invia:

```
MAIL FROM: <alice@dominioA.com>
From: alice@dominioA.com
DKIM-signature: (firma di dominioA)
```

La lista riceve, modifica e rispedisce:

```
MAIL FROM: <list@lista.org>         ← envelope rewritten dalla lista
From: alice@dominioA.com            ← visibile in From: (spesso rimane originale)
[footer della lista aggiunto]       ← modifica che rompe DKIM originale
```

Al destinatario:

- SPF controlla `dominioA.com` vs IP di `lista.org` → **fail**
    
- DKIM originale è rotto → **fail**
    
- Se la lista ha applicato firma DKIM propria o ARC, il destinatario può comunque decidere di fidarsi.
    

---

## Raccomandazioni rapide (checklist)

- Se gestisci una lista: abilita **[[DKIM]]** per la lista, implementa **[[ARC]]** e considera **SRS** per i forward.
    
- Se sei mittente che usa liste: **fai DKIM-sign** dei messaggi e avvisa gli admin della lista se devi preservare autenticazione.
    
- Se sei provider/recipient: **supporta ARC** e non affidarti solo a SPF.
    

---
