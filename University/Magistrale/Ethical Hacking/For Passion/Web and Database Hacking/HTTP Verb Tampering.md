# HTTP Verb Tampering

> Collegamenti: [[Centreon]] (bypass Basic Auth su Wall) Categoria: Web — Access Control / Authentication Bypass

---

## Definizione

**HTTP Verb Tampering** (o _Method Tampering_) è una classe di vulnerabilità in cui un controllo di accesso o di autenticazione è configurato per uno o pochi **metodi HTTP specifici** (tipicamente `GET` e `POST`), ma **non per tutti gli altri**. Un attaccante può quindi accedere alla stessa risorsa cambiando semplicemente il metodo HTTP della richiesta — `HEAD`, `PUT`, `DELETE`, `OPTIONS`, `TRACE`, o anche una stringa arbitraria — e bypassare il controllo.

Il problema di fondo è quasi sempre lo stesso: **una regola di sicurezza scritta come allowlist/denylist di metodi, applicata a livello sbagliato** (webserver, `.htaccess`, framework), che lascia "scoperti" tutti i metodi non elencati.

---

## I metodi HTTP — promemoria

|Metodo|Uso previsto|
|---|---|
|`GET`|richiesta dati, idempotente, nessun side-effect previsto|
|`POST`|invio dati, può modificare stato|
|`HEAD`|come GET ma senza body nella risposta — spesso trattato dai framework come "alias" di GET|
|`PUT`|crea/sostituisce una risorsa|
|`DELETE`|elimina una risorsa|
|`OPTIONS`|chiede al server quali metodi sono supportati|
|`TRACE`|echo della richiesta (quasi sempre da disabilitare — abusabile per XST)|
|metodo arbitrario (es. `FOO`)|molti server/framework, se non configurati esplicitamente, lo trattano come `GET` per il routing, ma **non applicano i controlli di auth pensati per GET/POST**|

Il punto chiave: **molti application server instradano una richiesta con metodo non riconosciuto verso lo stesso handler di `GET`**, ma il livello di autenticazione/autorizzazione — spesso configurato più "in alto" (webserver, filtro, `.htaccess`) — **non riconosce quel metodo e non applica la regola**.

---

## Esempio classico: Apache `.htaccess` con `<Limit>`

```apache
<Limit GET POST>
    Require valid-user
</Limit>
```

`<Limit>` applica la direttiva **solo** ai metodi elencati. Una richiesta `GET` o `POST` senza credenziali → `401`. Una richiesta con un metodo diverso (es. `HEAD`, o un metodo custom) → **la direttiva non si applica affatto**, la richiesta passa senza autenticazione.

**Fix corretto** — usare `<LimitExcept>`, che applica la direttiva a _tutto tranne_ i metodi elencati (quindi, invertendo la logica, protegge per default):

```apache
<LimitExcept GET POST>
    Require valid-user
</LimitExcept>
```

Anche questo non è perfetto se GET/POST stessi non dovrebbero essere protetti diversamente — il punto è che **`<LimitExcept>` non lascia "buchi" su metodi non previsti**, mentre `<Limit>` sì.

---

## Esempio Java EE (`web.xml`)

```xml
<security-constraint>
  <web-resource-collection>
    <url-pattern>/admin/*</url-pattern>
    <http-method>GET</http-method>
    <http-method>POST</http-method>
  </web-resource-collection>
  <auth-constraint>
    <role-name>admin</role-name>
  </auth-constraint>
</security-constraint>
```

Stessa logica: la regola si applica solo a `GET`/`POST` su `/admin/*`. Una richiesta `HEAD /admin/qualcosa` non matcha nessun `<http-method>` elencato → il `<security-constraint>` non si applica → **nessuna autenticazione richiesta**, e molti container Java instradano comunque `HEAD` allo stesso servlet di `GET`.

---

## Collegamento con Wall (HTB)

Su Wall, `/monitoring/` richiede **Basic Auth**, ma — come spesso accade — la regola è effettivamente applicata solo per `GET`:

```bash
curl -X GET http://<target>/monitoring/
# → 401 Unauthorized

curl -X POST http://<target>/monitoring/
# → 200/302, niente auth richiesta — risposta che rivela il path verso /centreon
```

È **esattamente** lo scenario `<Limit GET>` visto sopra: la regola di Basic Auth è scritta pensando solo al caso "utente apre la pagina nel browser" (sempre `GET`), e nessuno ha protetto `POST`. Un attaccante che prova metodi diversi su una risorsa protetta trova la falla in pochi secondi.

> [!tip] Lezione generale Ogni volta che incontri una risorsa protetta da Basic/Digest Auth a livello webserver (401 su accesso normale), prova **sistematicamente altri metodi HTTP** sulla stessa URL prima di passare ad altro — è un test a costo quasi zero.

---

## Metodologia di test

1. **Identifica l'endpoint protetto** — qualcosa che risponde `401`/`403` su `GET` normale.
2. **Prova metodi alternativi** con `curl -X`:
    
    ```bash
    for m in HEAD POST PUT DELETE OPTIONS TRACE FOO; do  echo "== $m =="  curl -s -o /dev/null -w "%{http_code}\n" -X $m http://<target>/pathdone
    ```
    
3. **Confronta i codici di risposta** — qualunque cosa diversa da `401`/`403` è un candidato. `200`/`301`/`302` indicano che la richiesta è passata oltre il controllo di auth.
4. **Verifica che l'handler esegua davvero l'azione** — non basta che risponda `200`: controlla che il contenuto/comportamento sia equivalente a una richiesta autenticata legittima (a volte `HEAD` ritorna solo gli header ma confermano l'accesso).
5. Se il server è dietro un **reverse proxy** (Nginx/Apache davanti a backend applicativo), prova anche **metodi case-variant** (`get`, `Get`) o con **case mismatch tra proxy e backend** — a volte solo uno dei due livelli normalizza il metodo.

---

## Perché esiste — la causa ricorrente

In quasi tutti i casi la causa è la stessa:

- il controllo di accesso è scritto come **allowlist di metodi "sicuri da controllare"** (`GET`, `POST`) invece che come **denylist/default-deny** ("blocca tutto tranne ciò che è esplicitamente permesso");
- il livello che applica il controllo (webserver/`.htaccess`/filtro) e il livello che **instrada e gestisce** la richiesta (application server/framework) hanno **vocabolari diversi** di metodi riconosciuti — il primo conosce solo GET/POST, il secondo accetta (e instrada) qualsiasi cosa.

---

## Mitigazioni

- Applicare i controlli di **autenticazione/autorizzazione a livello applicativo**, indipendentemente dal metodo HTTP — non delegare solo al webserver/`.htaccess`.
- Se si usa `.htaccess` con restrizioni di metodo, usare **`<LimitExcept>`**, non `<Limit>`.
- **Default deny**: disabilitare esplicitamente tutti i metodi non necessari (`TRACE`, `TRACK`, `CONNECT`, metodi custom) a livello webserver.
- Testare ogni endpoint protetto con l'intero set di metodi HTTP standard + alcuni custom, non solo GET/POST.
- Assicurarsi che proxy e backend **normalizzino i metodi nello stesso modo** (case, metodi non standard).

---
# beh è una banale misconfiguration perhcé non si sta usando una whitelistv di metodi HTTP

Quasi — ma c'è una distinzione che vale la pena fare, perché cambia anche la soluzione.

`<Limit GET>` **è già**, in un certo senso, una whitelist — ma è la whitelist sbagliata: è l'elenco dei metodi _per cui scatta il controllo_, non l'elenco dei metodi _permessi sulla risorsa_. Il pattern risultante è:

> "default: nessun controllo. Eccezione: se è GET, controlla."

È l'opposto di quello che servirebbe — un **default-deny indipendente dal metodo**: "controlla sempre, qualunque sia il metodo".

Il motivo per cui "facciamo una whitelist di metodi HTTP permessi" non è la soluzione giusta è che **l'insieme dei metodi HTTP è aperto**: oltre a `GET/POST/HEAD/PUT/DELETE/OPTIONS/TRACE` esistono i verbi WebDAV (`PROPFIND`, `MKCOL`, `COPY`...), e tecnicamente un client può inviare _qualsiasi stringa_ come metodo — il server deve decidere cosa farne. Enumerare "tutti i metodi possibili da bloccare" è una lista potenzialmente infinita e incompleta per costruzione.

La soluzione robusta non è "whitelist più completa dei metodi", ma **rendere il controllo di autenticazione completamente indipendente dal metodo** — niente `<Limit>` attorno a `Require valid-user`, così la regola si applica a _qualunque_ richiesta arrivi, qualunque sia il verbo, noto o non noto.

In altre parole: il bug non è "whitelist incompleta", è **"il controllo è stato condizionato su qualcosa su cui non avrebbe mai dovuto dipendere"** — stessa famiglia di bug di, ad esempio, un controllo di autorizzazione condizionato sull'User-Agent o sul Content-Type: nessuna whitelist di User-Agent sarebbe "la soluzione giusta", la soluzione è non condizionare l'auth su quel campo.

Ricostruiamo il meccanismo passo per passo, confrontando le due richieste fianco a fianco.![[Pasted image 20260613130156.png]]**Il punto cruciale**: `<Limit GET> ... Require valid-user` non significa _"solo GET e POST sono permessi"_ — significa _"se il metodo è GET, allora applica `Require valid-user`"_. È una **condizione**, non un filtro generale.

Quindi:

**Colonna sinistra (GET)** — il metodo è dentro l'elenco di `<Limit>` → la condizione è vera → Apache valuta `Require valid-user` → non c'è header `Authorization` → `401`.

**Colonna destra (POST)** — il metodo _non_ è dentro l'elenco → la condizione è falsa → Apache **salta interamente il blocco `<Limit>...</Limit>`**, come se non esistesse. Non c'è "nessuna regola che dice ok" — c'è semplicemente **l'assenza totale del controllo**, e Apache passa la richiesta al livello successivo (PHP/backend) esattamente come farebbe per qualsiasi richiesta non protetta.

Il backend, dal suo punto di vista, riceve una richiesta `POST /monitoring/` perfettamente legittima — non sa né gli interessa che dovrebbe essere protetta, perché quella decisione è (mal) delegata interamente al livello Apache/`.htaccess`, che qui ha applicato la regola sbagliata.

**Perché `<LimitExcept>` risolve il problema**: `<LimitExcept GET POST>` significa _"se il metodo NON è GET o POST, applica questa regola"_ — ma per coprire davvero tutti i casi, la soluzione robusta è applicare `Require valid-user` **senza alcun `<Limit>`/`<LimitExcept>`**, così la regola si applica a _ogni_ richiesta indipendentemente dal metodo.

---
# quindi mi stai dicendo questo: se ho limit get e dentro require valid user, dice semplicemtne: se arriva una request get, controlla le credenziali. se invece ho limitexcept get e dentro require valid user, dice: se arriva una richeista con metodi diversi da get allora fai il controllo?

Sì, esatto — hai capito perfettamente il meccanismo.

```apache
<Limit GET>
    Require valid-user
</Limit>
```

→ "se il metodo è `GET`, controlla le credenziali. Per ogni altro metodo, non fare nulla — passa libero."

```apache
<LimitExcept GET>
    Require valid-user
</LimitExcept>
```

→ "se il metodo _non_ è `GET`, controlla le credenziali. Se è `GET`, non fare nulla — passa libero."

Sono **complementari** — coprono insiemi opposti di metodi, e in entrambi i casi c'è un insieme di metodi che **non viene controllato affatto**, non un insieme che viene "controllato e respinto".

L'unico modo per non avere nessun metodo scoperto è **non usare `<Limit>`/`<LimitExcept>` per niente**:

```apache
Require valid-user
```

da solo, fuori da qualsiasi blocco `<Limit>`, si applica a **ogni** richiesta su quel path, indipendentemente dal metodo — questa è la configurazione "sicura per costruzione" di cui parlavamo.

---
# ma sucsa, se uso allora il metodo get può tranquillamente passare senza autenticazione se uso limitextept

Esatto, confermato.

```apache
<LimitExcept GET>
    Require valid-user
</LimitExcept>
```

`GET /risorsa` → nessuna richiesta di credenziali, `200` diretto. `POST /risorsa`, `DELETE /risorsa`, ecc. → `Require valid-user` si applica, serve login.

**Importante**: questo _non è automaticamente un bug_ — a volte è esattamente il comportamento voluto. Pensa a un'API REST: "tutti possono leggere (`GET`) i dati pubblici, ma solo utenti autenticati possono modificarli/eliminarli (`POST`/`PUT`/`DELETE`)". In quel caso `<LimitExcept GET>` è la configurazione _corretta_ e intenzionale.

**Diventa un bug** quando lo sviluppatore _non si è accorto_ che `GET` su quella risorsa specifica restituisce dati che dovrebbero essere protetti — es. `GET /admin/config` che ritorna informazioni sensibili, ma chi ha scritto la regola pensava solo a "le azioni di scrittura vanno protette" senza considerare che anche la _lettura_ di quell'endpoint doveva esserlo.

Quindi, da attaccante, quando trovi `<LimitExcept GET>` (o equivalenti), la domanda da farti è: _"questo `GET` esposto restituisce qualcosa che non dovrebbe essere pubblico?"_ — non è automaticamente exploitabile, dipende da cosa fa quel `GET`.

---
## Riferimenti

- OWASP Web Security Testing Guide — "Testing for HTTP Verb Tampering"
- Imperva — "HTTP Verb Tampering"
- Acunetix — "Method Tampering" / "HTTP verb tampering via POST"