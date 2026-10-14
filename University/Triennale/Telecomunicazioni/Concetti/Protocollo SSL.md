---
title: Protocollo SSL
tags:
  - telecomunicazioni
  - concetto
  - ssl
  - tls
  - sicurezza
---

# Protocollo SSL

> [!summary] In breve
> **SSL/TLS** aggiunge a TCP riservatezza, integrità e autenticazione. L'**handshake** negozia gli algoritmi, verifica il certificato del server e stabilisce un **master secret**, da cui si derivano 4 chiavi. I dati viaggiano in **record** cifrati con un MAC che include un numero di sequenza.

Handshake reale:
1. client: algoritmi + nonce;
2. server: scelte + certificato + nonce;
3. client: $K^+_{server}(PMS)$;
4. entrambi: MS da PMS + nonce → $E_B, M_B, E_A, M_A$ (+ IV);
5–6. MAC di tutti i messaggi di handshake (contro il downgrade).

- Record: tipo, versione, lunghezza (in chiaro), dati + MAC (cifrati).
- **Numeri di sequenza** nel MAC → contro riordino e sostituzione; **nonce** → contro la replica di intere connessioni.
- Chiusura con un record di tipo "chiusura" autenticato → contro il troncamento.
- Sta nel livello di applicazione, ma per lo sviluppatore è un "TCP sicuro" (https).

## Collegamenti

- **Concetti correlati**: [[Codice di Autenticazione del Messaggio]] · [[Certificazione della Chiave Pubblica]] · [[SSL]] · [[TLS]] · [[HTTPS]] · [[Gestione della Connessione TCP]]
- **Mappa**: [[MOC - Telecomunicazioni]]

> [!info] Approfondimento
> - [[08 - TLC - Sicurezza nelle reti#8.6 Rendere sicure le connessioni TCP: SSL|Capitolo 8 — 8.6 Rendere sicure le connessioni TCP: SSL]]
> - [[08 - TLC - Sicurezza nelle reti#Handshake|Capitolo 8 — Handshake]]
> - [[08 - TLC - Sicurezza nelle reti#Trasferimento dati|Capitolo 8 — Trasferimento dati]]
> - [[08 - TLC - Sicurezza nelle reti#Handshake SSL|Capitolo 8 — Handshake SSL]]
> - [[08 - TLC - Sicurezza nelle reti#Chiusura della connessione|Capitolo 8 — Chiusura della connessione]]
