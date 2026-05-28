# Input Validation

> [!abstract] In una riga A livello **server**, input non validato → **buffer overflow** nel binario del server o nelle sue estensioni → esecuzione di codice.

## Cos'è (a livello server)

Quando il server (o una sua [[Server Extensions|estensione]]) **non controlla** dimensione o forma dell'input che riceve, un attaccante può inviare dati malformati che **sforano un buffer** in memoria e sovrascrivono il flusso di esecuzione → **remote code execution**.

> [!warning] Attenzione a non confondere i due livelli
> 
> - **Input validation a livello SERVER** = [[Buffer Overflow]] nel software del server (questa nota).
> - **Input validation a livello APPLICAZIONE** = [[XSS]], **[[SQL Injection]]**, [[Command Injection]] → quelli stanno in [[Web Application Hacking]]. Stesso nome, due mondi diversi.

## Esempi storici

- **Buffer overflow `.ida`** (IIS Indexing Service) → worm **Code Red**.
- **Chunked-encoding overflow** in Apache.
- In generale, gli overflow nelle [[Server Extensions]] ricadono qui.

## Difese

- **Patch** del server e delle estensioni.
- Esecuzione con **minimo privilegio** (limita il danno post-exploit).
- Mitigazioni di memoria della piattaforma: **DEP**, **ASLR**, stack canaries.
- **Filtraggio dell'input** a monte (vedi [[Canonicalization]] → URLScan).

## Collegamenti

- ⬆️ [[Web Server Hacking]]
- ↔️ [[Server Extensions]] · [[Canonicalization]] · [[Web Application Hacking]]