---

tags:

- ingegneria
- sicurezza_informatica
- web_security
- cookies
- SOP type: nota

---
# Cookies

> [!abstract] In una riga Un piccolo `name=value` che il server piazza nel browser e che il browser **riallega automaticamente** a ogni richiesta verso quel sito. Semplice da definire, fragile da mettere in sicurezza: i suoi attributi vivono solo nel browser, e il server riceve quasi nessuna garanzia.

## 1. Infrastruttura

Il meccanismo base è uno scambio di due header:

- Il server imposta il cookie: `Set-Cookie: nome=valore; <attributi>`
- Il browser lo memorizza e lo rispedisce a ogni richiesta successiva: `Cookie: nome=valore`

Le slide li descrivono ironicamente come _"un fragile file di testo tenuto a mano"_ — ed è vero: sono il modo principale per dare **stato** a un protocollo (HTTP) che di suo è stateless, quindi ci poggiano sopra sessioni, autenticazione e CSRF-protection.

## 2. Attributi e Flag

Un cookie porta con sé **attributi** (`Domain`, `Path`, `Expires`, `Max-Age`, `SameSite`) e **flag** (`Secure`, `HttpOnly`).

|Attributo / Flag|Cosa fa|Nota di sicurezza|
|---|---|---|
|**Domain**|Quali host ricevono il cookie|Se impostato → tutti i sottodomini (rischio related-domain). Se assente → host-only|
|**Path**|Limita il cookie a un prefisso di percorso URL|Solo isolamento, **non** è una barriera di sicurezza vera|
|**Secure**|Inviato solo su HTTPS|Garantisce confidenzialità; i browser recenti vietano anche la sovrascrittura via HTTP (integrità)|
|**HttpOnly**|JavaScript non può leggerlo (`document.cookie`)|Limita il furto del session token via [[XSS]]. **Non** dà integrità (vedi jar overflow)|
|**Expires / Max-Age**|Quando scade|Entrambi assenti → cookie di sessione (muore alla chiusura). `Max-Age` ha precedenza su `Expires`|
|**SameSite**|Se allegarlo a richieste cross-site|Difesa chiave contro [[CSRF]] (vedi sotto)|

### Approfondimento: Domain

L'attributo `Domain` è il punto più insidioso.

![[cookie-domain-scope.svg]]

- **Non impostato (host-only):** il cookie torna **solo** al dominio esatto che l'ha creato.
- **Impostato:** il cookie va al dominio indicato **e a tutti i suoi sottodomini**. Il valore può essere un qualsiasi suffisso fino al **registrable domain**, ma non un _public suffix_ (es. `ac.at` è vietato).

Regole di validità (dalle slide):

|Dominio che imposta|Valore `Domain`|Permesso?|Perché|
|---|---|---|---|
|`a.b.example.com`|`example.com`|✅ Sì|è il registrable domain|
|`www.example.ac.at`|`ac.at`|❌ No|`ac.at` è un public suffix|
|`a.example.com`|`b.example.com`|❌ No|non è un suffisso di `a.example.com`|

## 3. Same-site vs Cross-site

Concetto distinto dalla SOP-origin. Una richiesta è **cross-site** se URL target e pagina che la innesca **non condividono lo stesso registrable domain** (eTLD+1):

- `a.example.com` → `b.example.com` = **same-site** (stesso `example.com`)
- `example.com` → `bank.com` = **cross-site**

> [!warning] Attenzione: "site" ≠ "origin" Per i cookie e per `SameSite`, "site" è il **registrable domain**, non la tripla `(protocollo, host, porta)` della [[SOP]]. Per questo due sottodomini diversi sono "same-site" pur essendo origini diverse — ed è esattamente la falla che i token CSRF coprono.

### Valori di SameSite

1. **Strict:** mai allegato a richieste cross-site.
2. **Lax:** allegato cross-site solo su **navigazione top-level** che l'utente avvia (es. clic su un link). _Default dal Feb. 2020._
3. **None:** sempre allegato. **Implica `Secure`**: un cookie `SameSite=None` senza `Secure` viene scartato.

## 4. La SOP per i cookie (quando viene allegato)

Un cookie è allegato a una richiesta verso un URL `u` se valgono **tutti** questi vincoli:

1. **Domain:** se impostato, dev'essere un suffisso dell'host di `u`; altrimenti l'host di `u` dev'essere identico a chi ha creato il cookie.
2. **Path:** dev'essere un prefisso del percorso di `u`.
3. **Secure:** se impostato, `u` dev'essere HTTPS.
4. **SameSite:** se la richiesta è cross-site, rispettare i requisiti dell'attributo.

## 5. Il limite fondamentale del protocollo

> [!important] La radice di quasi tutti gli attacchi sui cookie Quando il browser invia un cookie, manda **solo `name=value`**. Tutti gli attributi vengono **persi**. Quindi il server **NON sa**:
> 
> - se il cookie è stato impostato su una connessione sicura,
> - quale dominio l'ha impostato,
> - quale `Path` aveva,
> - se era `HttpOnly`.
> 
> Il server riceve un nome e un valore, e basta. Da qui nascono tossing, overwrite e overflow.

## Cookie Jar

Il **cookie jar** è semplicemente il "barattolo" dove il browser conserva tutti i cookie che ha ricevuto.

Funziona così, in breve:

Ogni cookie è memorizzato con una **chiave a tre parti**: la tripla `(name, domain, path)`. Questo vuol dire che possono coesistere due cookie con lo **stesso nome** purché differiscano per dominio o path — ed è proprio questa la radice del cookie tossing.

Quando fai una richiesta, il browser **pesca dal jar** tutti i cookie che soddisfano i vincoli (Domain è suffisso dell'host, Path è prefisso dell'URL, Secure rispettato, SameSite ok) e li mette nell'header `Cookie`. Se più cookie hanno lo stesso nome, li **ordina** — di norma quelli con **path più lungo prima** — e il server di solito prende la **prima occorrenza**.

Il jar ha dei **limiti di capienza** (numero massimo di cookie per dominio): quando si riempie, il browser **espelle i più vecchi** per fare spazio. È la leva del _cookie jar overflow_.

E ricorda il punto cruciale: nel passaggio dal jar alla richiesta, **gli attributi si perdono** — esce solo `name=value`. Il server non vede da quale dominio o path arrivasse il cookie, e quindi non può difendersi da solo dalle manipolazioni del jar.

**Concettualmente** il cookie jar è il barattolo che contiene tutti i cookie del browser. Ma il limite che il jar overflow sfrutta **non è globale**: è **per dominio** (per _apex / registrable domain_, come dicono le tue slide). Ogni dominio ha la sua "quota" di cookie nel jar.

Quindi un cookie jar overflow **non distrugge i cookie di altri domini**. Se l'attaccante inonda di cookie lo scope di `example.com`, vengono espulsi solo i cookie più vecchi **dentro la quota di `example.com`** (incluso il session token legittimo). I tuoi cookie di `bank.com`, `google.com`, ecc. stanno in quote separate e **restano intatti**.

Ed è proprio per questo che l'attacco richiede una posizione da **related-domain attacker**: l'attaccante deve poter creare cookie che "contano" nella stessa quota della vittima, e l'unico modo è stare nello stesso registrable domain — cioè controllare un sottodominio come `evil.example.com`. Da `evil.example.com` può creare centinaia di cookie con `Domain=example.com`, che vanno a riempire la quota di `example.com` e spingono fuori il cookie legittimo.

In sintesi:

- **Barattolo unico** → sì, ma con **scaffali separati per dominio**.
- L'overflow riempie **solo lo scaffale del dominio bersaglio** → espelle i cookie vecchi **di quel dominio**, non degli altri.
- Serve quindi un sottodominio del target; da un dominio totalmente estraneo (`evil.com`) non potresti toccare la quota di `example.com`.

### Esempio di cookie tossing attack

Eccone uno concreto di **cookie tossing**, che mostra bene il meccanismo del jar.

Punto di partenza: tu sei loggato su `example.com` e il sito ti ha dato il tuo cookie legittimo:

```
Set-Cookie: SESSID=legit_bob; Path=/
```

L'attaccante però controlla un sottodominio, `evil.example.com`, e da lì imposta un secondo cookie con lo **stesso nome**, ma con scope allargato e path più specifico:

```
Set-Cookie: SESSID=attacker_1337; Domain=example.com; Path=/profile
```

Ora il tuo cookie jar contiene **due** voci con chiave `(name, domain, path)` diversa, quindi convivono entrambe:

|name|domain|path|value|
|---|---|---|---|
|SESSID|example.com|`/`|legit_bob|
|SESSID|.example.com|`/profile`|attacker_1337|

Quando visiti `example.com/profile`, il browser pesca dal jar **tutti e due** (entrambi i path sono prefissi di `/profile`) e li ordina per **path più lungo prima** (`/profile` viene prima di `/`):

```http
GET /profile HTTP/2
Host: example.com
Cookie: SESSID=attacker_1337; SESSID=legit_bob
```

Il server riceve solo `name=value`, due volte, e per convenzione prende la **prima occorrenza** → `attacker_1337`. Risultato: ti ritrovi loggato nel contesto dell'attaccante (è il classico _"Welcome Attacker!"_).

Il bug nasce tutto dai punti che avevi visto: due cookie con lo stesso nome possono coesistere (chiave a tripla), l'ordine li mette in un certo modo, e il server — vedendo solo `name=value` — non ha idea che il primo SESSID arrivi da un sottodominio malevolo con path `/profile`.


## 6. Attacchi

### Cookie Tossing

Un sottodominio (`evil.example.com`) imposta un cookie con `Domain=.example.com`, così viene inviato anche agli altri sottodomini. La chiave nel cookie jar è la tripla `(name, domain, path)`, quindi possono coesistere due cookie con lo **stesso nome**. Sfruttando l'**ordine** con cui il browser li invia (di solito **path più lungo prima**) e il fatto che il server accetta la **prima occorrenza**, l'attaccante fa prevalere il proprio cookie.

- _Impatto:_ bypass delle protezioni [[CSRF]], login CSRF, session fixation.

### Cookie Overwrite

Variante: l'attaccante su `evil.example.com` **sovrascrive** il cookie di `example.com` impostandone uno con lo stesso nome ma scope più ampio (`Domain=.example.com`). Siccome il server vede solo `name=value`, se il cookie malevolo arriva per primo l'app autentica nel contesto dell'attaccante (_"Welcome Attacker!"_ invece di _"Welcome Bob!"_).

### Cookie Jar Overflow

I browser limitano il numero di cookie per apex domain; oltre il limite, i **più vecchi vengono espulsi**. L'attaccante:

1. parte da un `session=legit` legittimo e `HttpOnly`;
2. via JS crea centinaia di cookie spazzatura (`overflow_0`, `overflow_1`, …);
3. il cookie legittimo (più vecchio) viene **espulso**;
4. ne reimposta uno `session=1337` controllato da lui.

> [!note] Perché aggira HttpOnly `HttpOnly` impedisce a JS di **leggere** il cookie, ma **non dà integrità**: JS può comunque riempire il jar e farlo espellere, poi reinserirne uno proprio.

## 7. La difesa: Cookie Prefixes

I prefissi danno al server garanzie **basate sul nome** del cookie, perché l'**enforcement lo fa il browser** al momento del `Set-Cookie`.

- **`__Secure-`** → il browser lo accetta solo se marcato **Secure**. Integrità contro attaccanti di rete.
- **`__Host-`** → accettato solo se: **Secure**, **senza attributo `Domain`** (host-only), e con `Path=/`. Integrità contro **related-domain attacker**.

> [!tip] Perché l'attaccante non può falsificarli Il controllo non è lato server — è il **browser** a rifiutare di salvare un cookie con quei prefissi se le regole non sono rispettate. Quindi se `evil.example.com` prova `Set-Cookie: __Host-Session=falso; Domain=example.com`, il browser vede il `Domain` vietato dal prefisso `__Host-` e **scarta** il cookie: non entra mai nel jar.
> 
> Ragionamento deduttivo del server: _"vedo un cookie `__Host-Session`; so che il browser l'avrebbe rifiutato se non fosse host-only e Secure → posso fidarmi."_

## 8. Cookie e CSRF (il legame con SameSite)

`SameSite=Lax` di default blocca il [[CSRF]] **classico** (attaccante su un dominio esterno), ma **non** il **related-domain attacker**: se `studenti.uni.it` attacca `voti.uni.it`, per il browser è _same-site_ e il cookie `Lax` parte lo stesso. Per questo i **token anti-CSRF** restano necessari (difesa in profondità): non dipendono dal dominio DNS e l'attaccante non conosce il token segreto nel form.

## 9. Takeaway per l'esame

- Il server riceve **solo `name=value`** → non può fidarsi degli attributi → da qui tossing/overwrite/overflow.
- `Domain` impostato = scope esteso ai sottodomini = superficie related-domain.
- `HttpOnly` protegge dalla **lettura** (anti-[[XSS]]), non dà **integrità**.
- `SameSite=Lax` (default) ferma il CSRF esterno ma non il related-domain.
- `__Host-` è la garanzia più forte: host-only + Secure + Path=/, imposta dal **browser**.

## Esempio di come [[HTTPS]] ([[HTTP]] over [[TLS]]) protegge il payload e viene incapsulato

Ottima richiesta — qui il concetto è l'**incapsulamento**: il pacchetto è come una matrioska, e la cifratura TLS avviene su uno strato ben preciso. Ti faccio vedere esattamente cosa succede a un GET, strato per strato.

Partiamo dai dati che l'applicazione vuole mandare (in chiaro, come li vede il browser):

```http
GET /account HTTP/1.1
Host: bank.com
Cookie: SESSID=k7Fa9Zx2
```

Ora questo testo scende lungo lo stack di rete e a ogni livello viene "avvolto" in un nuovo strato. Il punto cruciale: **solo il contenuto HTTP viene cifrato (dal TLS Record); le intestazioni di TCP, IP ed Ethernet restano in chiaro**, perché servono ai router e alle schede di rete per consegnare il pacchetto.Ecco la matrioska del pacchetto: il GET parte in chiaro, il **TLS Record** lo cifra, e poi TCP, IP ed Ethernet aggiungono le loro intestazioni _intorno_ — ma quelle restano leggibili.Leggendo dall'interno verso l'esterno, ecco cosa succede passo per passo.

**Lato client (incapsulamento, si scende lo stack):**
![[https_packet_encapsulation.svg|618]]
Il browser produce il GET in chiaro. Lo strato **TLS** lo prende e lo cifra con la chiave di sessione simmetrica concordata nell'handshake, producendo un **TLS record**. Sul filo quel record inizia con qualcosa tipo:

```
17 03 03 00 4A   →  type=23 (application_data), versione, lunghezza
9f a3 c1 7e ...  →  byte cifrati (il GET + Cookie, illeggibili)
[auth tag]       →  tag di integrità (AES-GCM)
```

Da qui scende: **TCP** ci mette davanti la sua intestazione (porta sorgente → `:443`, sequence number), **IP** aggiunge gli indirizzi (es. `192.168.1.10 → 203.0.113.5`), **Ethernet** aggiunge i MAC del prossimo hop e un controllo finale (FCS). Il frame va sul cavo.

**Cosa vede un MITM / sniffer:** tutte le intestazioni esterne sono in chiaro, quindi vede _chi parla con chi_ — il tuo IP che contatta il server della banca sulla porta 443 (metadati). Ma il contenuto — path `/account`, header `Host`, **cookie di sessione**, body — è dentro il blob cifrato: vede solo byte casuali.

**Lato server (de-incapsulamento, si risale lo stack — l'ordine inverso):**

1. La scheda di rete riceve il frame, verifica l'**FCS** e toglie l'intestazione Ethernet → pacchetto IP.
2. Lo strato IP controlla che l'IP di destinazione sia suo, toglie l'intestazione IP → segmento TCP.
3. Lo strato TCP vede la porta `:443`, rimette in ordine i segmenti e toglie l'intestazione TCP → TLS record.
4. Lo strato **TLS** usa la **stessa chiave simmetrica** dell'handshake per **decifrare** il payload e verifica l'**auth tag**: se il tag non torna, il pacchetto è stato manomesso in transito → connessione chiusa. Altrimenti → HTTP in chiaro.
5. Il web server (es. nginx) riceve finalmente il `GET /account` in chiaro e lo elabora.

Il punto chiave: la cifratura vive **solo sullo strato TLS**, "in mezzo" tra applicazione e TCP. Gli strati sotto non sanno nemmeno cosa trasportano — vedono il TLS record come un payload opaco qualsiasi. Per questo un router instrada un pacchetto HTTPS esattamente come uno HTTP: gli serve solo l'intestazione IP, che è in chiaro.

Vuoi che trasformi questo schema in una nota `[[HTTPS]]` / `[[TLS]]` per il vault (con il diagramma dell'incapsulamento + quello dell'handshake che ti avevo proposto prima)? Così chiudi anche la parte "Network Protocol Issues" delle tue slide (SSL stripping, HSTS) con il pezzo che spiega _come_ funziona davvero la cifratura sotto.

## Collegamenti

- ↔️ [[CSRF]] · [[XSS]] · [[SOP]]


---
# informazioni che puoi trovare in [[5 - CS Application Level - Web Security Part II]]

## 2. Cookies: Infrastruttura e Attributi

Le slide presentano i cookie ironicamente come "un fragile file di testo mantenuto manualmente e copiato da qualche posizione casuale su internet", evidenziando la loro natura basilare ma critica.

![[Pasted image 20260131133904.png]]
### Struttura di un Cookie

Un cookie viene impostato dal server tramite l'header HTTP `Set-Cookie` e inviato dal client tramite l'header `Cookie`.

![[Pasted image 20260131133921.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo scambio HTTP tra client e server e la tabella degli attributi.
> 
> **Meaning:**
> 
> - Il server invia: `Set-Cookie: nome=valore`
>     
> - Il browser memorizza e invia nelle richieste successive: `Cookie: nome=valore`
>     
> - Un cookie possiede **Attributi** (`Expires`, `Max-Age`, `Domain`, `Path`, `SameSite`) e **Flags** (`Secure`, `HttpOnly`).
>     

---

## 3. Scope dei Cookies (Ambito)

Lo scope definisce chi può leggere o ricevere un cookie.

![[Pasted image 20260131133940.png]]
### Attributo Domain

![[Pasted image 20260131134003.png]]

L'attributo `Domain` determina quali host possono ricevere il cookie.

1. **Attributo NON impostato:** Il cookie è allegato solo alle richieste verso il dominio che lo ha impostato (host-only).
    
2. **Attributo impostato:** Il cookie è allegato alle richieste verso il dominio specificato e **tutti i suoi sottodomini**.
    
    - Il valore può essere qualsiasi suffisso del dominio della pagina che imposta il cookie, fino al **registrable domain**.
        
    - **Rischio:** Un attaccante su un dominio correlato ("related-domain attacker") può impostare cookie che vengono inviati al sito web target.
        

#### Regole di Validità del Domain Attribute

|**Domain setting the cookie**|**Value of the Domain attribute**|**Allowed?**|**Reason**|
|---|---|---|---|
|`a.b.example.com`|`example.com`|**Yes**|il valore dell'attributo è il registrable domain|
|`www.example.ac.at`|`ac.at`|**No**|`ac.at` è un public suffix|
|`a.example.com`|`b.example.com`|**No**|il valore dell'attributo non è un suffisso di `a.example.com`|


> [!abstract] Visual Analysis
> ![[Pasted image 20260131134035.png]]
> **What to look at:** La gerarchia dei domini (`example.com` sopra a `shop.example.com`, ecc.).
> 
> **Meaning:** Se `example.com` imposta un cookie con `domain=.example.com`, quel cookie sarà visibile a **tutti** i sottodomini (es. `myprofile.shop.example.com`, `evil.example.com`). Per restringere lo scope al solo dominio che lo ha creato, l'attributo `domain` **non deve essere specificato**.

---

## 4. Altri Attributi dei Cookie

### Path

- Usa per restringere lo scope del cookie a uno specifico percorso URL.
    
- Il cookie viene allegato solo se il suo `path` è un **prefisso** del path dell'URL della richiesta.
    
- _Esempio utile:_ `example.com/userA` vs `example.com/userB`.
    
- Se non impostato: il path è quello della pagina che imposta il cookie.
    
- Se impostato: non ci sono restrizioni sul suo valore.
    

### Secure

- Se impostato, il cookie viene allegato **solo a richieste HTTPS** (garantisce confidenzialità).
    
- Recentemente, i browser impediscono che i cookie `Secure` vengano impostati (o sovrascritti) da richieste HTTP (garantisce integrità).
    

### HttpOnly

- Se impostato, **JavaScript non può leggere** il valore del cookie tramite `document.cookie`.
    
- **Limitazione:** Non fornisce integrità. Uno script può sovrascrivere il "cookie jar" (vasiere dei cookie), cancellando i vecchi cookie e impostandone uno nuovo.
    
- **Utilità:** Previene il furto di cookie sensibili (es. identificatori di sessione) in caso di vulnerabilità XSS.
    

### Max-Age e Expires

Definiscono quando il cookie scade.

- **Entrambi non impostati:** Il cookie viene cancellato alla chiusura del browser (cookie di sessione).
    
- **Max-Age negativo o Expires nel passato:** Il cookie viene cancellato dal cookie jar.
    
- **Precedenza:** Se entrambi sono specificati, `Max-Age` ha la precedenza.
    

---

## 5. Attributo SameSite

![[Pasted image 20260131134138.png]]

Controlla se il cookie deve essere allegato alle richieste **cross-site**.

**Definizione di Cross-site:** Una richiesta è cross-site se il dominio dell'URL target e quello della pagina che innesca la richiesta non condividono lo stesso **registrable domain**.

- `a.example.com` -> `b.example.com`: **Same-site** (dominio registrabile `example.com`).
    
- `example.com` -> `bank.com`: **Cross-site**.
    

**Valori dell'attributo:**

1. **Strict:** Il cookie non è **mai** allegato a richieste cross-site.
    
2. **Lax:** Il cookie viene inviato anche in caso di richieste cross-domain, ma solo se c'è un cambiamento nella **navigazione top-level** (l'utente se ne accorge, es. cliccando un link).
    
3. **None:** Il cookie è **sempre** allegato a tutte le richieste cross-site.
    

### Cambiamenti recenti (Feb. 2020)

- **Default:** `SameSite = Lax`. I cookie senza attributo esplicito sono trattati come Lax.
    
- **Dipendenza Secure:** `SameSite = None` implica `Secure`. I cookie con `SameSite=None` vengono scartati se non hanno anche l'attributo `Secure`.
    

---

## 6. SOP per la Lettura dei Cookie

Un cookie viene allegato a una richiesta verso un URL `u` se sono soddisfatti i seguenti vincoli:

1. **Dominio:** Se l'attributo `Domain` è impostato, deve essere un suffisso del dominio dell'host di `u`. Altrimenti, l'hostname di `u` deve essere uguale al dominio della pagina che ha impostato il cookie.
    
2. **Path:** L'attributo `Path` deve essere un prefisso del percorso di `u`.
    
3. **Secure:** Se l'attributo `Secure` è impostato, il protocollo di `u` deve essere HTTPS.
    
4. **SameSite:** Se la richiesta è cross-site, devono essere rispettati i requisiti dell'attributo `SameSite`.
    

---

## 7. Problemi del Protocollo dei Cookie e Cookie Tossing

### Problemi di Protocollo

L'header `Cookie` inviato dal browser contiene solo le coppie **nome-valore**.

- Il server **non sa** se il cookie è stato impostato su una connessione sicura.
    
- Il server **non sa** quale dominio ha impostato il cookie ricevuto.
    
- Il server **non sa** il path del cookie.
    

### Cookie Tossing

Impostando l'attributo domain (es. `.domain.com`), i sottodomini possono forzare un cookie verso altri sottodomini, domini correlati o persino il dominio apice (apex domain).

- La chiave nel "cookie jar" è la tripla `(name, domain, path)`.
    
- Quando i cookie vengono inviati, gli attributi vengono persi.
    
- **Comportamento del Server:** La maggior parte accetta la **prima occorrenza** dei cookie con lo stesso nome.
    
- **Comportamento del Browser:** La maggior parte ordina i cookie:
    
    1. Quelli con **path più lunghi** prima di quelli con path più corti.
        
    2. Quelli creati prima (o in base all'implementazione).
        

**Impatto:** Bypass delle protezioni CSRF, Login CSRF, Session Fixation.

---

## 8. Vulnerabilità: Cookie Overwrite & Cookie Jar Overflow

### Cookie Overwrite

Un attaccante su un sottodominio (es. `evil.example.com`) può sovrascrivere i cookie di un dominio legittimo (es. `introsec.example.com` o `example.com`) impostando un cookie con lo stesso nome ma con scope più ampio (es. `domain=.example.com`).

![[Pasted image 20260131134156.png]]

> [!abstract] Visual Analysis
> ![[Pasted image 20260131134230.png]]![[Pasted image 20260131134240.png]]![[Pasted image 20260131134245.png]]
> **What to look at:** Il diagramma mostra `evil.example.com` che imposta `SESSID=1337` e `example.com` che vede questo cookie.
> 
> **Meaning:** Poiché il server riceve solo `name=value`, se l'attaccante riesce a far inviare il suo cookie prima di quello legittimo, il server autenticherà la richiesta nel contesto dell'attaccante ("Welcome Attacker!" invece di "Welcome Bob!").

### Cookie Jar Overflow

![[Pasted image 20260131135710.png]]
![[Pasted image 20260131135728.png]]![[Pasted image 20260131135738.png]]
I browser hanno un limite sul numero di cookie che un **apex domain** può avere.

- Quando non c'è più spazio, i cookie **più vecchi vengono cancellati**.
    
- **Attacco:** Gli attaccanti possono inondare ("overflow") il cookie jar per:
    
    1. Sovrascrivere cookie `HttpOnly`.
        
    2. Aggirare le protezioni contro il cookie tossing sui server che bloccano richieste con cookie duplicati.
        

**Esempio di attacco (Testato su Chrome):**

1. Esiste un cookie legittimo `session=legit` (HttpOnly).
    
2. L'attaccante esegue uno script che crea centinaia di cookie "spazzatura" (`overflow_0`, `overflow_1`...).
    
3. Il cookie legittimo (più vecchio) viene espulso per fare spazio.
    
4. L'attaccante imposta un nuovo cookie `session=1337` (non HttpOnly o controllato da lui).
    

---

## 9. Cookie Prefixes

Per mitigare le ambiguità, sono stati proposti i prefissi dei cookie, che forniscono al server garanzie di sicurezza basate sul nome del cookie.

1. `__Secure-`:
    
    - Se un cookie ha questo prefisso, viene accettato dal browser solo se marcato come **Secure**.
        
    - Garantisce integrità rispetto ad attaccanti di rete.
        
2. `__Host-`:
    
    - Se un cookie ha questo prefisso, viene accettato solo se:
        
        - È marcato **Secure**.
            
        - **NON** include l'attributo `Domain` (è host-only).
            
        - Ha l'attributo `Path` impostato a `/`.
            
    - Garantisce integrità rispetto ad attaccanti su domini correlati (related-domain attackers).

**Gli attaccanti non possono creare arbitrariamente questi cookie**.

Il motivo risiede nel fatto che il controllo di sicurezza non viene fatto dal server, ma dal **browser**. Ecco come funziona il meccanismo e perché protegge anche se il server è "cieco":

### 1. Il Browser come "Guardiano" (Enforcement Lato Client)

Le fonti specificano chiaramente che se un cookie ha un prefisso, "viene accettato dal **browser** solo se...". Questo significa che il browser applica regole rigide nel momento in cui un sito prova a **impostare** (`Set-Cookie`) il cookie.

Se un attaccante prova a creare un cookie malformato con quei prefissi, il browser **rifiuta di salvarlo**. Non entra mai nel "Cookie Jar" (il contenitore dei cookie), quindi non verrà mai inviato al server.

### 2. Perché l'attacco fallisce (Scenari Pratici)

Analizziamo i due casi in base alle tue fonti:

- **Caso `__Secure-` (Contro Attaccanti di Rete/Man-in-the-Middle):**
    
    - _L'attacco:_ Un attaccante sulla rete intercetta una connessione HTTP (non cifrata) e prova a iniettare: `Set-Cookie: __Secure-Session=falso; Path=/`
    - _La Difesa:_ Il browser vede il prefisso `__Secure-`. Controlla se è presente l'attributo `Secure`. Poiché la connessione è HTTP (o l'attributo manca), il browser dice: "Violazione delle regole del prefisso" e **scarta il cookie**.
    - _Risultato:_ Il server non riceverà mai questo cookie falso.
- **Caso `__Host-` (Contro Attaccanti da Sottodomini/Cookie Tossing):**
    
    - _L'attacco:_ Un attaccante controlla il sottodominio `evil.example.com`. Vuole sovrascrivere il cookie di sessione del sito principale `example.com`. Invia: `Set-Cookie: __Host-Session=falso; Domain=example.com; Secure; Path=/`
    - _La Difesa:_ Il browser vede il prefisso `__Host-`. Le regole dicono che questo cookie **NON deve avere l'attributo Domain** (deve essere _host-only_).
    - _Risultato:_ Poiché l'attaccante ha dovuto usare `Domain=example.com` per cercare di colpire il sito padre (vedi Cookie Tossing), il browser rileva la violazione e **rifiuta il cookie**.

### 3. La Garanzia per il Server

È vero che il server non può verificare gli attributi quando riceve il cookie. Ma, grazie a questo meccanismo, il server può fare questo ragionamento deduttivo:

> _"Vedo un cookie che si chiama `__Host-Session`. So che i browser moderni avrebbero **rifiutato di salvarlo** se non fosse stato impostato in modo sicuro (Secure, HTTPS) e proveniente esattamente dal mio host (senza attributo Domain). Quindi, posso fidarmi che sia legittimo."_

In sintesi: il server si fida del **nome** del cookie perché sa che il **browser** ha già bloccato qualsiasi tentativo di creazione illegittima di quel nome specifico.

