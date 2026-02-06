# DNS Cache Poisoning

**Tags:** #CyberSecurity #DNS #NetworkSecurity #Spoofing #AttackVector 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Chiave

Il **DNS Cache Poisoning** (o DNS Spoofing) è un attacco che mira a corrompere la memoria cache di un server DNS ricorsivo. L'obiettivo è inserire dati falsi (es. associare `www.bankofamerica.com` all'IP dell'attaccante) in modo che le future richieste degli utenti vengano reindirizzate verso server malevoli.

> [!danger] Problema di Fondo Il protocollo DNS standard **non include meccanismi di autenticazione**. Un resolver accetta una risposta come valida basandosi solo su tre parametri deboli:
> 
> 1. IP Sorgente corrisponde all'IP Destinazione della query.
> 2. Porta di Destinazione corrisponde alla Porta Sorgente.
> 3. **Transaction ID (TXID)** corrisponde.

---

## ⚙️ Meccanismo dell'Attacco

L'attacco si configura come una **Race Condition** (corsa contro il tempo). L'attaccante deve far arrivare la sua risposta falsa al resolver _prima_ che arrivi la risposta del server autoritativo legittimo.

### Il Flusso (Step-by-Step)

1. **Trigger:** L'attaccante forza il resolver a inviare una query chiedendo un sottodominio casuale e inesistente (es. `q0001.bankofamerica.com`). Questo causa un **Cache Miss** e costringe il resolver a contattare il server autoritativo.
2. **Flooding:** Mentre il resolver attende, l'attaccante invia migliaia di risposte false simulate.
3. **Guessing Game:** Ogni risposta falsa tenta di indovinare il **Transaction ID** e la **Porta Sorgente** usati dal resolver.
4. **Poisoning:** Se una delle risposte false "azzecca" i parametri e arriva prima della risposta vera, il resolver la accetta e la memorizza in cache.
5. **Payload:** La risposta falsa contiene record malevoli (es. "Il server per `bankofamerica.com` è `ns.evil.com`") che permettono il **Full Domain Hijack**.

---

## 🎲 L'Entropia e la Difesa

La difficoltà dell'attacco dipende da quante combinazioni l'attaccante deve indovinare:

- **Transaction ID (TXID):** È un campo di soli **16-bit** ($2^{16} = 65,536$ possibilità). I resolver vecchi usavano ID sequenziali (facilissimi da prevedere).
- **Porta Sorgente:**
    - _Senza randomizzazione:_ Facile da indovinare.
    - _Con randomizzazione:_ Aumenta l'entropia di altri 16 bit.
    - _Totale:_ $2^{16} \times 2^{16} \approx 4 \text{ miliardi di combinazioni}$.

---

## ⚠️ Fattori di Vulnerabilità

Le slide identificano condizioni specifiche che rendono il poisoning più facile:

- Assenza di randomizzazione della porta sorgente o del TXID.
- Presenza di **[[Open Resolvers]]** accessibili da Internet.
- **TTL Lunghi:** Se l'attacco riesce, l'effetto persiste per molto tempo.
- Resolver che accettano record _out-of-bailiwick_ (record per domini che non c'entrano con la query originale) nella sezione "Additional".

---

## 🛡️ Impatto e Mitigazione

- **Impatto:** Furto di credenziali (login bancari), Intercettazione dati (MITM), Reindirizzamento del traffico.
- **Soluzione Definitiva:** L'unica vera difesa contro lo spoofing è l'autenticazione crittografica fornita da **[[DNSSEC]]**.

---

## 🔗 Collegamenti

- [[DNSSEC]]
- [[Open Resolvers]]
- [[DDoS Amplification]]