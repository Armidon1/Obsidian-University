# Path Traversal

> [!abstract] In una frase Il **path traversal** (o _directory traversal_) consiste nel manipolare un input che l'app usa per costruire un percorso di file, inserendo sequenze come `../`, per **uscire dalla directory prevista** e leggere (o a volte scrivere/eseguire) file arbitrari del filesystem.

> [!info] Dove sta nei due lab
> 
> - **[[Ethl 0x03 web security p1]]** lo presenta dentro **A01:2025 Broken Access Control**: crafting di input malevolo per accedere a file/directory non autorizzati, con la tabella dei **bypass via encoding** e la demo che legge `/proc/self/environ`.
> - **[[Ethl 0x04 web security p2]]** lo inquadra come **tipo di LFI** (Local File Inclusion): la path traversal _legge_ un file; l'LFI lo fa _includere/eseguire_ dall'app, aprendo la strada alla **RCE via log poisoning**.
> 
> In sintesi: **path traversal ⊂ LFI ⊂ Broken Access Control**. Stesso difetto di base, gravità crescente a seconda di cosa l'app fa col file.

---

## 1. Perché funziona

> [!info] Il difetto L'app prende un nome file **dall'utente** e lo concatena a una directory base, **senza sanificarlo**:
> 
> ```php
> $file = "/var/www/images/" . $_GET['filename'];
> readfile($file);
> ```
> 
> Con `filename=flowers.png` legge `/var/www/images/flowers.png` (legittimo). Ma `filename=../../../etc/passwd` produce:
> 
> ```
> /var/www/images/../../../etc/passwd  →  /etc/passwd
> ```
> 
> La sequenza `../` significa "directory genitore": ogni `../` **risale** di un livello nell'albero del filesystem. Concatenandone abbastanza si esce dalla cartella prevista e si raggiunge la radice, poi qualsiasi file di sistema.

> [!note] È lo stesso peccato originale del resto del corso Come injection e XSS (vedi [[Ethl 0x04 web security p2]]), il problema è **dati controllati dall'utente trattati come "percorso fidato"**. L'app non separa "la parte che decido io" (la directory base) da "la parte che decide l'utente" (il nome file).

---

## 2. Esempi base (slide lab 0x03)

```
https://insecure-website.com/loadImage?filename=../../../etc/passwd
https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini
```

|Target tipico|Sistema|Cosa rivela|
|---|---|---|
|`/etc/passwd`|Linux|utenti del sistema|
|`/etc/shadow`|Linux|hash delle password (se leggibile)|
|`/proc/self/environ`|Linux|**variabili d'ambiente del processo** (path, segreti, stack)|
|`..\..\..\windows\win.ini`|Windows|file di configurazione classico (prova di concetto)|

> [!info] Linux vs Windows Linux usa `/` come separatore, Windows `\`. Per questo i payload variano: `../` su Linux, `..\` su Windows. Molti web server Windows accettano **entrambi**.

> [!example] La demo del lab — `/proc/self/environ` Richiedendo `?filename=..%2f..%2f..%2fproc/self/environ` si legge l'ambiente del processo del web server (`HOME`, `USER`, `PATH`, e a volte segreti/token). È un classico **information disclosure** che alimenta la fase di recon: scopri lo stack, gli utenti, i percorsi.

---

## 3. Bypass dei filtri tramite encoding (cuore del lab 0x03)

> [!warning] "Not always that easy" Se l'app filtra `../`, si **codificano** i caratteri così che il filtro non li riconosca ma il filesystem (dopo la decodifica) sì. È un gioco di **mismatch tra dove si filtra e dove si decodifica**.

|Payload|Decodifica|Tipo|
|---|---|---|
|`%2e%2e%2f`|`../`|URL encoding pieno|
|`%2e%2e/`|`../`|URL encoding parziale|
|`..%2f`|`../`|solo lo slash|
|`%2e%2e%5c`|`..\`|variante Windows|
|`%2e%2e\`|`..\`|parziale Windows|
|`..%5c`|`..\`|solo il backslash|
|`%252e%252e%255c`|`..\`|**double encoding**|
|`..%255c`|`..\`|**double encoding**|
|`..//`|`../`|può ingannare filtri che rimuovono `../` una sola volta|
|`..%c0%af`|`../`|**UTF-8 overlong** (solo sistemi che la accettano)|
|`..%c1%9c`|`..\`|UTF-8 overlong|

### 3.1 Double encoding — la trappola d'esame

> [!info] Perché il double encoding aggira i filtri `%2f` è la codifica URL di `/`. Ma il `%` stesso si può codificare come `%25`. Quindi `%252f` decodifica **una prima volta** in `%2f`, e **una seconda volta** in `/`. Se l'architettura decodifica due volte (es. una il web server, una il framework applicativo) ma **filtra solo dopo la prima decodifica**, il payload supera il controllo (il filtro vede `%2f`, non `/`) e arriva al filesystem già trasformato in `/`. Il filtro e il consumatore guardano due "versioni" diverse della stessa stringa.

### 3.2 `..//` e la rimozione ingenua

> [!info] Perché `..//` può funzionare Alcuni filtri "puliscono" l'input rimuovendo `../` **una sola volta**, non ricorsivamente. Con `....//` o `..//`, dopo la rimozione di una sequenza interna resta comunque un `../` valido. È il motivo per cui la sanificazione _per sottrazione_ (blacklist) è fragile.

---

## 4. Escalation: da lettura a RCE (collegamento al lab 0x04)

> [!danger] Path traversal → LFI → RCE via log poisoning Finché si _legge_ un file, l'impatto è information disclosure. Ma se l'app **include ed esegue** il file (LFI), la stessa primitiva diventa RCE:
> 
> 1. L'attaccante invia una richiesta con un campo controllato (es. header **`User-Agent`**) contenente codice: `<?php system($_GET['c']); ?>`.
> 2. Il web server **scrive l'header nel log** (`/var/log/apache2/access.log`). Log "avvelenato".
> 3. Via path traversal/LFI si **include il log**: `?page=../../../var/log/apache2/access.log`.
> 4. L'inclusione tratta il contenuto come PHP → il payload **viene eseguito** → RCE.
> 
> Dettagli completi della catena in [[Ethl 0x04 web security p2]]. Il punto: _path traversal e LFI sono la stessa vulnerabilità a gravità diversa_ — dipende da cosa l'app fa col file che le dai.

---

## 5. Difese

> [!success]
> 
> - **Allowlist**, non blacklist: mappa input → file ammessi (`it → italian.json`), invece di concatenare il path e filtrare i caratteri cattivi.
> - **Canonicalizzazione + verifica del contenimento**: risolvi il path reale (es. `realpath()`) e verifica che resti _dentro_ la directory base consentita.
> - **Decodifica una sola volta** e rifiuta sequenze sospette _dopo_ la canonicalizzazione (chiude il double encoding).
> - Far servire i file statici dal **web server**, non dalla logica applicativa.
> - In PHP, `allow_url_include=Off` e `open_basedir` per confinare l'accesso.
> - Privilegi minimi: il processo non deve poter leggere `/etc/shadow` ecc.

> [!info] Perché allowlist batte blacklist Filtrare i caratteri cattivi è una corsa agli armamenti: per ogni filtro c'è un encoding che lo aggira (la tabella sopra lo dimostra). Una **allowlist** ribalta la logica: invece di elencare ciò che è vietato (infinito), elenchi ciò che è permesso (finito). L'attaccante non ha sequenze da inventare perché qualunque valore fuori lista è rifiutato a priori.

---

## 6. Trappole d'esame

> [!danger] Domande "spiega questo / perché funziona"
> 
> 1. **Path traversal vs LFI vs Broken Access Control** → path traversal è un caso di LFI (sorgente locale), che è una forma di Broken Access Control (A01). Gravità crescente: lettura → inclusione → esecuzione.
> 2. **Perché `../` permette di uscire dalla cartella** → `../` = directory genitore; concatenandone abbastanza si risale fino alla radice e poi a qualunque file.
> 3. **Cos'è il double encoding e perché aggira i filtri** → `%252f` → `%2f` → `/`; mismatch tra dove si filtra (dopo 1 decodifica) e dove si consuma (dopo 2 decodifiche).
> 4. **Perché `..//` o `....//` funzionano** → filtri che rimuovono `../` una sola volta lasciano residui validi.
> 5. **Cosa rivela `/proc/self/environ`** → variabili d'ambiente del processo: path, utente, talvolta segreti → recon.
> 6. **Come si arriva da path traversal a RCE** → log poisoning: payload nel User-Agent → finisce nel log → log incluso via LFI → eseguito.
> 7. **Allowlist vs blacklist: quale e perché** → allowlist; la blacklist è aggirabile all'infinito via encoding, l'allowlist rifiuta tutto ciò che non è esplicitamente permesso.

> [!todo] Homework/challenge (lab 0x03, slide 47) _Trova una path traversal in Juice Shop._ Suggerimento concettuale: cerca endpoint che servono file **per nome** (es. la sezione FTP/`/ftp` del sito) e prova le varianti di encoding della tabella sopra per uscire dalla cartella servita. Verifica _quale_ encoding passa e ragiona sul _perché_ (che filtro c'era).

---

## 7. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Spiega in una frase il difetto di codice che rende possibile il path traversal.
> 2. Cosa fa `../` e perché ripeterlo permette di leggere `/etc/passwd`?
> 3. Decodifica `%252e%252e%255c` passo per passo e di' perché può aggirare un filtro.
> 4. Perché un filtro che rimuove `../` una sola volta è insufficiente?
> 5. Qual è la relazione tra path traversal, LFI e Broken Access Control?
> 6. Descrivi la catena path traversal → RCE via log poisoning.
> 7. Perché l'allowlist è una difesa più solida del filtraggio dei caratteri?
> 8. Cosa contiene `/proc/self/environ` e perché interessa a un attaccante?

---

> [!quote] Idea da portare a casa Il path traversal è la versione "filesystem" del tema del corso: **input dell'utente trattato come istruzione fidata**. Letto da solo → information disclosure; incluso ed eseguito → RCE. La difesa non è inseguire gli encoding cattivi (perdi sempre), ma **decidere a priori cosa è permesso** (allowlist) e **verificare che il path risolto resti dentro i confini**.