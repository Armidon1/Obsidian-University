# Network Time Protocol (NTP) & HSTS Bypass

**Tag:** #security #web-security #NTP #HSTS #bypass #network-attack #MITM

**Fonte:** [[5 - CS Application Level - Web Security Part II]]

---

## 📝 Definizione

Il **Network Time Protocol (NTP)** è il protocollo standard utilizzato per sincronizzare l'orologio di sistema tra diverse macchine attraverso una rete.

- **Vulnerabilità Architetturale:** Le slide evidenziano che la maggior parte dei sistemi operativi moderni utilizza NTP **senza autenticazione**. Questo rende il protocollo vulnerabile ad attacchi di rete, poiché il client non può verificare l'autenticità della sorgente temporale.
    

---

## ⚙️ HSTS Bypass Attack

L'attacco descritto non mira al protocollo NTP per sé, ma lo usa come vettore per disabilitare la protezione **HSTS (HTTP Strict Transport Security)**.

### Il Concetto

Le policy HSTS hanno una durata temporale definita dall'attributo `max-age` (es. 1 o 2 anni). Se un attaccante riesce a spostare l'orologio della vittima nel futuro, oltre la data di scadenza della policy, il browser considererà l'HSTS scaduto e permetterà nuovamente connessioni HTTP insicure.

### Flusso di Attacco

1. **Intercettazione:** L'attaccante si posiziona come Man-in-the-Middle (MITM).
    
2. **Forging NTP:** L'attaccante intercetta una richiesta di sincronizzazione oraria e invia una risposta NTP contraffatta contenente una data molto lontana nel futuro (es. anno 2030).
    
3. **System Update:** Il sistema operativo della vittima accetta l'orario falso e aggiorna l'orologio di sistema.
    
4. **HSTS Expiration:** Il browser verifica le policy HSTS salvate. Dato che l'orologio di sistema è ora successivo alla data di scadenza (`current_time > expiry_date`), la protezione HSTS viene rimossa.
    
5. **SSL Stripping:** L'attaccante può ora eseguire un attacco di SSL Stripping, poiché il browser non forzerà più l'HTTPS.
    

---

## 🖥️ Comportamento dei Sistemi Operativi

La riuscita di questo attacco dipende da come il Sistema Operativo gestisce aggiornamenti NTP drastici. Le slide notano differenze significative:

- **Sistemi Vulnerabili (es. Ubuntu, Fedora):** Tendono ad accettare qualsiasi orario contenuto nella risposta NTP, rendendo l'attacco immediato.
    
- **Windows:** Impone dei vincoli sulla differenza di tempo accettabile (solitamente permette uno scostamento massimo di circa 15-48 ore), rendendo l'attacco più difficile ma non impossibile (richiederebbe passi incrementali).
    
- **macOS:** Generalmente permette grandi differenze di orario (salti temporali) solo una volta o sotto certe condizioni.