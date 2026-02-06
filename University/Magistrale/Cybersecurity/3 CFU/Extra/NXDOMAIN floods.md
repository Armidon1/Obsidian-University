# DNS NXDOMAIN Floods

**Tags:** #CyberSecurity #DNS #DDoS #Availability #AttackVector 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Chiave

Il **NXDOMAIN Flood** (o attacco Water Torture) è una tipologia di attacco che mira a compromettere la **Disponibilità (Availability)** del servizio DNS.

L'attacco sfrutta la natura gerarchica del DNS per sovraccaricare i server ricorsivi e autoritativi, costringendoli a elaborare un numero massiccio di richieste per nomi di dominio inesistenti.

## ⚙️ Meccanismo di Attacco

Sebbene le slide descrivano questo meccanismo principalmente come fase preliminare del _Cache Poisoning_, la tecnica è identica per i flood:

1. **Generazione di Query:** L'attaccante invia migliaia di richieste DNS per sottodomini casuali e inesistenti (es. `q0001.bankofamerica.com`, `x123.attacker.com`).
2. **Cache Miss:** Poiché i sottodomini sono casuali e non esistono, il risolutore ricorsivo non ha la risposta in cache (Cache Miss).
3. **Carico sull'Autoritativo:** Il risolutore è costretto a inoltrare ogni singola richiesta al server autoritativo del dominio target per chiedere "Esiste questo nome?".
4. **Esaurimento Risorse:** Il server autoritativo viene inondato di richieste inutili, dovendo rispondere costantemente con messaggi di errore **NXDOMAIN** (Non-Existent Domain).

## ⚠️ Impatto di DNSSEC

L'utilizzo di **DNSSEC** può aggravare l'impatto di questi attacchi (aumentando il rischio DDoS).

Per garantire l'integrità, DNSSEC deve fornire una **"Authenticated Denial of Existence"** (prova autenticata che un nome non esiste).

- Invece di restituire un semplice errore NXDOMAIN leggero, il server deve restituire record **NSEC** o **NSEC3**.
- Questi record provano crittograficamente che non ci sono domini tra due nomi esistenti in ordine canonico (o hash order per NSEC3).
- **Risultato:** Il server vittima deve consumare più CPU e banda per inviare risposte firmate e più grandi, facilitando l'esaurimento delle risorse.

---

## 🔗 Collegamenti

- [[DNS Cache Poisoning]] (Usa una tecnica simile per forzare i cache miss)
- [[DDoS Amplification]]
- [[DNSSEC]]