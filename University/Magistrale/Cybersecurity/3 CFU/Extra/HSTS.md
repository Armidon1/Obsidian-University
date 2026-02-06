# HTTP Strict Transport Security (HSTS)

**Tag:** #security #web-security #HTTPS #hardening #HSTS #network-defense

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

**HSTS** è un meccanismo di sicurezza web che permette a un sito di dichiarare ai browser che tutte le interazioni future devono avvenire esclusivamente tramite una connessione sicura (HTTPS).

Serve a proteggere gli utenti da attacchi di _downgrade_ (come l'SSL Stripping) e dal dirottamento dei cookie.

---

## ⚙️ Funzionamento

Quando un server invia l'header HSTS (`Strict-Transport-Security`) in una risposta HTTPS valida:

1. **Upgrade Forzato:** Il browser memorizza questa direttiva per il dominio. Per tutta la durata specificata, convertirà automaticamente qualsiasi tentativo di connessione `http://` in `https://` _prima_ di inviare la richiesta alla rete.
    
2. **Stop-on-Error:** Se la connessione HTTPS fallisce (es. certificato scaduto, self-signed o nome non corrispondente), il browser **chiude la connessione** e mostra un errore bloccante.
    
    - _Differenza chiave:_ A differenza del normale HTTPS, l'utente **non ha l'opzione** di ignorare l'avviso di sicurezza e procedere comunque.
        
3. **Trust-On-First-Use (TOFU):** L'header viene elaborato solo se ricevuto su una connessione sicura e priva di errori. Se inviato via HTTP, il browser lo ignora (perché un attaccante potrebbe averlo iniettato o rimosso).
    

---

## 📋 Configurazione (The Header)

L'header `Strict-Transport-Security` supporta diverse direttive separate da punto e virgola:

HTTP

```
Strict-Transport-Security: max-age=6307200; includeSubDomains; preload
```

- **`max-age=<secondi>`**: (Obbligatorio) Il tempo in secondi per cui il browser deve ricordare di forzare HTTPS.
    
    - Esempio: `6307200` (circa 2 anni) è un valore comune raccomandato.
        
- **`includeSubDomains`**: (Opzionale) Estende la protezione a tutti i sottodomini del dominio corrente.
    
- **`preload`**: (Opzionale) Indica il consenso del proprietario del sito a essere incluso nella lista di precaricamento del browser (vedi sotto).
    

---

## 🚀 HSTS Preloading

Poiché l'HSTS standard protegge solo _dopo_ la prima visita riuscita (lasciando scoperta la primissima connessione), esiste il **Preloading**.

- **Concetto:** I produttori di browser (Google, Mozilla, Apple, ecc.) integrano direttamente nel codice sorgente del browser una lista statica di domini che devono essere **sempre** contattati via HTTPS.
    
- **Requisiti:** Per essere inclusi, i siti devono inviare un header HSTS valido con `max-age` lungo, `includeSubDomains` e la direttiva `preload`, per poi registrarsi su [hstspreload.org](https://hstspreload.org).
    

---

## ⚠️ Limitazioni e Attacchi

### NTP Attack (Bypass Temporale)

Poiché la policy HSTS ha una data di scadenza (basata su `max-age` + orario corrente), è vulnerabile alla manipolazione dell'orologio di sistema.

- **Vulnerabilità:** Molti sistemi operativi sincronizzano l'orario via **NTP (Network Time Protocol)** senza autenticazione.
    
- **Attacco:** Un attaccante Man-in-the-Middle può intercettare le richieste NTP e rispondere con un orario falso spostato nel futuro (oltre la scadenza del `max-age` salvato).
    
- **Effetto:** Il browser crede che la policy HSTS sia scaduta, permettendo nuovamente connessioni HTTP insicure e attacchi di SSL Stripping.