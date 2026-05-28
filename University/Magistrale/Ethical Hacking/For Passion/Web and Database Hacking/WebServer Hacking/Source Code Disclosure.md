# Source Code Disclosure

> [!abstract] In una riga Ottenere il **codice sorgente** di uno script lato server invece di farlo eseguire.

## Cos'è

Normalmente uno script lato server (ASP, PHP, JSP) viene **eseguito** dal motore del server, che restituisce solo l'**output** (HTML). Un attacco di source code disclosure inganna il server facendogli restituire il **file grezzo** così com'è.

## Perché è grave

Il sorgente rivela:

- la **logica interna** dell'applicazione;
- **credenziali hardcoded** e **stringhe di connessione** al database;
- percorsi interni, chiavi, nomi di tabelle → munizioni per attacchi successivi.

## Meccanismo

Il trucco è far sì che il server **non instradi** il file al motore di esecuzione, così ricade sul comportamento di default (servire un file statico). Quasi sempre è una **conseguenza** di un problema di [[Canonicalization|canonicalizzazione]].

## Esempi storici

- **`ASP::$DATA`** (IIS): si aggiunge `::$DATA` al nome → IIS non vede più l'estensione `.asp`, non esegue, e NTFS restituisce il flusso dati grezzo del file.
- **Case-sensitivity di Apache su Windows:** richiesta `/CGI-BIN/foo` (maiuscolo) non combacia con la regola `ScriptAlias /cgi-bin/` → Apache serve lo script come file statico.
- **`+.htr`** e header **`Translate: f`** (WebDAV) su IIS.

## Difese

- **Patch** della piattaforma.
- Tenere gli script **fuori dalla document root**.
- Configurare correttamente gli **handler** per ogni estensione.

## Collegamenti

- ⬆️ [[Web Server Hacking]]
- ↔️ [[Canonicalization]] (causa frequente) · [[Sample Files]]