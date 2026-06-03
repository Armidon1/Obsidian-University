# Log Poisoning (LFI → RCE)

> [!abstract] In una frase Il **log poisoning** trasforma una **Local File Inclusion** da semplice lettura di file in **esecuzione di codice (RCE)**: l'attaccante fa scrivere codice (es. PHP) dentro un **file di log** controllando un campo della richiesta HTTP, poi usa la LFI per **includere quel log**, che viene così interpretato ed eseguito.

> [!info] Dove sta nei lab È la demo centrale di **[[Ethl 0x04 web security p2]]** (slide 6: _"LFI 2 RCE via Log Poisoning (User Agent)"_). Si appoggia sui concetti di **LFI** e **[[Path Traversal]]**: la path traversal _legge_ un file, la LFI lo _include/esegue_; il log poisoning sfrutta proprio l'inclusione per ottenere RCE.

> [!note] La gerarchia da tenere a mente `path traversal` (leggo un file) → `LFI` (lo includo/eseguo) → `log poisoning` (faccio in modo che il file incluso contenga **mio** codice). Stessa primitiva, impatto crescente.

---

## 1. Il prerequisito: LFI che _include_, non solo _legge_

> [!info] La differenza che abilita tutto
> 
> - Una path traversal che fa `readfile($path)` → ti **mostra** il contenuto del file (information disclosure).
> - Una LFI che fa `include($path)` (PHP) → **interpreta ed esegue** il contenuto del file.
> 
> Il log poisoning richiede il **secondo** caso: deve esserci un punto in cui un file scelto dall'attaccante viene **incluso ed eseguito** dal motore (tipicamente PHP `include`/`require`).

```php
// vulnerabile: il file viene INCLUSO (eseguito), non solo letto
include($_GET['page'] . ".php");
```

---

## 2. La catena completa (punto d'esame)

> [!danger] I quattro passi
> 
> 1. **Iniezione** — L'attaccante invia una richiesta HTTP in cui un campo **che controlla** (classicamente l'header **`User-Agent`**) contiene codice:
>     
>     ```
>     User-Agent: <?php system($_GET['c']); ?>
>     ```
>     
> 2. **Avvelenamento del log** — Il web server **scrive l'header nel log** (`/var/log/apache2/access.log`). Il log ora contiene il payload come **testo inerte**.
> 3. **Inclusione** — Via LFI/path traversal l'attaccante **include il file di log**:
>     
>     ```
>     ?page=../../../var/log/apache2/access.log
>     ```
>     
> 4. **Esecuzione** — Il motore PHP interpreta il contenuto del log: il `<?php … ?>` prima inerte **viene eseguito** → **RCE**. Da qui in poi `?c=id`, `?c=cat /etc/passwd`, ecc.

> [!info] Perché funziona — la frase da dire all'esame L'app si fida di un file _"locale e legittimo"_ (il log di sistema), ma quel file contiene **dati scelti dall'attaccante**, e l'inclusione li tratta come **codice**. È di nuovo il peccato originale del corso: **dati che diventano codice** perché l'interprete (PHP `include`) non distingue tra "log da leggere" e "script da eseguire". Il log è solo il _veicolo_ per portare il payload dentro un contesto di esecuzione.

---

## 3. Vettori di iniezione comuni

> [!info] Dove l'attaccante può "scrivere" nel log Qualunque campo della richiesta che (a) l'attaccante controlla e (b) finisce verbatim in un log.

|Vettore|Finisce in|Note|
|---|---|---|
|**`User-Agent`**|`access.log`|il più comune — header arbitrario, controllabile con `curl -A`, Burp|
|**`Referer`**|`access.log`|altro header libero|
|**URL/path** della richiesta|`access.log`|a volte filtrato/encoded dal server|
|**Username** di login fallito|`auth.log` (SSH)|scenario "SSH log poisoning"|
|**`X-Forwarded-For`** ecc.|log applicativi|dipende da cosa logga l'app|

> [!tip] Perché il `User-Agent` è il preferito È un header HTTP **completamente sotto controllo dell'attaccante** (basta `curl -A '<?php …?>'`), viene scritto **verbatim** nei log d'accesso, e non subisce le sanificazioni che a volte colpiscono l'URL. Massima affidabilità con minimo sforzo.

---

## 4. Percorsi di log tipici (da conoscere)

> [!info] Bersagli comuni dell'inclusione
> 
> |Path|Server / contesto|
> |---|---|
> |`/var/log/apache2/access.log`|Apache (Debian/Ubuntu)|
> |`/var/log/apache2/error.log`|Apache, errori|
> |`/var/log/httpd/access_log`|Apache (RHEL/CentOS)|
> |`/var/log/nginx/access.log`|Nginx|
> |`/var/log/auth.log`|SSH/auth (Debian/Ubuntu)|
> |`/proc/self/environ`|non un log, ma incudibile: contiene variabili d'ambiente, a volte iniettabili via header|
> 
> Il path esatto va spesso **indovinato/enumerato** (vedi enumeration in [[Ethl 0x03 web security p1]]) e il file deve essere **leggibile** dal processo del web server.

---

## 5. Prerequisiti perché l'attacco riesca

> [!warning] Tutte queste condizioni devono valere
> 
> 1. Esiste una LFI che **include/esegue** (non solo legge) un file scelto dall'utente.
> 2. Il motore **interpreta** il contenuto incluso (es. PHP `include`).
> 3. L'attaccante **conosce/indovina** il path del log.
> 4. Il file di log è **leggibile** dal processo web.
> 5. Il payload nel log **non viene neutralizzato** (encoding, sanitizzazione del log).
> 
> Se anche una sola salta, si ripiega su altri vettori (altro file controllabile, file upload — vedi sotto).

---

## 6. Alternative al log poisoning per arrivare a RCE

> [!info] Stesso obiettivo, veicoli diversi Il log è solo _un modo_ per portare codice dentro un contesto includibile. Altri:
> 
> - **File upload** (vedi [[Ethl 0x03 web security p1]]) — carichi direttamente uno script e lo includi/richiami: più diretto se l'upload è permesso.
> - **`/proc/self/environ`** — iniezione via header (es. User-Agent) poi inclusione dell'environ.
> - **Session file PHP** (`/var/lib/php/sessions/sess_<id>`) — se controlli un valore salvato in sessione.
> - **Wrapper PHP** (`php://filter`, `data://`, `expect://`) — quando la configurazione li consente.
> 
> Concetto unificante: trova **qualunque file che (a) contiene dati controllati da te e (b) può essere incluso/eseguito**.

---

## 7. Difese

> [!success]
> 
> - **Non includere mai path influenzati dall'utente.** Usare una **allowlist** di pagine includibili (come per [[Path Traversal]]): è la difesa che chiude la LFI alla radice, e senza LFI il log poisoning non parte.
> - **Niente esecuzione di contenuti non fidati**: in PHP, `allow_url_include=Off`, disabilitare funzioni pericolose, `open_basedir` per confinare l'accesso ai file.
> - **Log fuori dalla web root** e in formato **non interpretabile** (structured/JSON logging riduce il rischio di payload eseguibili "puliti").
> - **Sanificare/encodare** i campi controllabili prima di loggarli (es. neutralizzare `<?php`).
> - **Privilegi minimi**: il processo web non dovrebbe poter leggere i log di sistema arbitrari.

> [!info] Perché l'allowlist è la difesa-chiave Il log poisoning è un _secondo stadio_: senza la LFI iniziale non esiste. Chiudere la LFI con un'allowlist di file includibili (mappa `home → home.php`, `about → about.php`) elimina il primo stadio, e quindi tutta la catena. Inseguire i payload nei log (filtrare `<?php`) è fragile come ogni blacklist.

---

## 8. Trappole d'esame

> [!danger] Domande "spiega questo / perché funziona"
> 
> 1. **La catena completa** → payload in un campo controllato (User-Agent) → scritto nel log → log incluso via LFI → eseguito come codice → RCE. Saper dire _dove entra_ il payload e _quando_ diventa codice.
> 2. **Perché serve una LFI che _include_, non che legge** → solo l'inclusione (`include`) interpreta ed esegue il contenuto; il semplice `readfile` lo mostra soltanto.
> 3. **Perché il `User-Agent`** → header HTTP completamente controllabile, scritto verbatim nel log, raramente sanificato.
> 4. **Path traversal vs LFI vs log poisoning** → leggere → includere/eseguire → far sì che il file incluso contenga il tuo codice. Gravità crescente.
> 5. **Quali prerequisiti** → LFI con inclusione, motore che interpreta, path del log noto, log leggibile, payload non neutralizzato.
> 6. **Difesa-chiave e perché** → allowlist dei file includibili: elimina la LFI (primo stadio), quindi tutta la catena.
> 7. **Alternative al log** → file upload, `/proc/self/environ`, session file, wrapper PHP — qualunque file controllabile e includibile.

> [!todo] Collega all'homework La path traversal in Juice Shop (challenge di [[Ethl 0x03 web security p1]]) è il _primo_ mattone. Ragiona su cosa servirebbe in più perché diventi una LFI con esecuzione, e quindi un potenziale log poisoning — anche se in Juice Shop (Node.js, non PHP) il vettore di RCE è diverso (vedi SSTi/LoTL in [[Ethl 0x04 web security p2]]).

---

## 9. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Descrivi i quattro passi del log poisoning, dicendo a ogni passo dove sta il payload e se è codice o dato.
> 2. Perché una LFI che fa `readfile` non basta per il log poisoning?
> 3. Perché il `User-Agent` è il vettore di iniezione preferito?
> 4. Elenca tre file/path che un attaccante potrebbe includere e perché.
> 5. Quali condizioni devono valere tutte insieme perché l'attacco riesca?
> 6. Perché l'allowlist dei file includibili è la difesa più solida, e a quale stadio agisce?
> 7. Nomina due alternative al log come veicolo per la RCE.

---

> [!quote] Idea da portare a casa Il log poisoning è la dimostrazione che **"leggere un file" e "eseguire codice" sono separati da un solo passo**: basta che un file _controllabile dall'attaccante_ finisca in un contesto di _inclusione/esecuzione_. Il log è solo il veicolo più comodo. La difesa non è ripulire i log (fragile), ma **non includere mai path scelti dall'utente** — chiudendo la LFI si chiude tutta la catena.