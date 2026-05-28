# Canonicalization

> [!abstract] In una riga Una stessa risorsa ha **più nomi**; il controllo di sicurezza fatto sul nome "non canonico" viene aggirato, ma il filesystem risolve comunque il file.

## Cos'è

La **canonicalizzazione** è il processo con cui il sistema riduce le tante rappresentazioni di una risorsa a un unico nome standard (_canonico_). Esempi della stessa risorsa:

- `C:\text.txt`
- `..\text.txt`
- `\\computer\C$\text.txt`

Le applicazioni che prendono decisioni di sicurezza **sul nome** possono essere ingannate da una rappresentazione alternativa: è un **canonicalization attack**.

## Lo schema universale

> [!tip] Da ricordare **Due componenti interpretano lo STESSO nome in modo diverso, e l'attaccante sfrutta la discrepanza.**
> 
> Il controllo di sicurezza vede una stringa; l'accesso reale avviene **dopo** la canonicalizzazione → se un nome inganna il controllo ma viene comunque risolto nel file voluto, la protezione salta.

## Esempi storici

- **`ASP::$DATA` (IIS):** `file.asp` e `file.asp::$DATA` puntano agli stessi byte (flusso dati NTFS). Aggiungere `::$DATA` evita l'esecuzione → [[Source Code Disclosure]].
- **Case-sensitivity di Apache su Windows:** router Apache _case-sensitive_ vs filesystem Windows _case-insensitive_ → `/CGI-BIN/` aggira la regola ma il file viene comunque trovato.
- **Unicode / Double Decode (IIS):** caratteri percent-encoded (`%c0%af`, doppio `%252f`) che, decodificati, diventano `../` → **directory traversal** fino a `cmd.exe`. Sfruttato dal worm **Nimda**.

## Difese

- **Patch** costanti della piattaforma.
- **Filtraggio dell'input** a monte (es. **URLScan**, che strappa Unicode e doppio-esadecimale prima che arrivino al server).
- **Compartimentare** le cartelle (script fuori dalla document root).

## Collegamenti

- ⬆️ [[Web Server Hacking]]
- ↔️ [[Source Code Disclosure]] · [[Input Validation]]