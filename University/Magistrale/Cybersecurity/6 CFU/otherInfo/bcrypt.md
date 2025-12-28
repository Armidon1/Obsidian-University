# bcrypt

## 1. Che cos'è?

bcrypt è una funzione di hashing delle password basata sul cifrario Blowfish.

Introdotto nel 1999, è stato per oltre due decenni lo standard de facto per l'archiviazione sicura delle password. Sebbene oggi [[Argon2]] sia preferibile per nuovi progetti, bcrypt rimane una scelta estremamente solida e diffusa.

## 2. Caratteristiche Fondamentali

A differenza di hash veloci (come SHA-256), bcrypt è progettato per essere **lento**.

1. **CPU-Bound:** Il suo calcolo dipende intensamente dalla potenza del processore.
    
2. **Salt Integrato:** Non richiede la gestione manuale del sale (come in PBKDF2); genera e include automaticamente un salt casuale nella stringa finale dell'hash.
    
3. **Fattore di Costo (Work Factor):** Possiede un parametro regolabile che determina quante iterazioni eseguire.
    

## 3. Il Meccanismo di Difesa

La sicurezza di bcrypt si basa sul rallentare l'attaccante.

> [!abstract] Logica del Work Factor
> 
> Il costo è logaritmico. Se aumenti il fattore di costo di +1, il tempo necessario per calcolare l'hash raddoppia.
> 
> Questo permette di mantenere il passo con la Legge di Moore: man mano che i computer degli attaccanti diventano più veloci, i difensori aumentano il costo per mantenere il tempo di verifica costante (es. 100ms).

## 4. Limiti e Confronto

Il limite principale di bcrypt è che è **solo CPU-bound** e non richiede molta memoria RAM.

- **Vulnerabilità:** Poiché usa poca memoria, è possibile costruire hardware dedicato (FPGA o GPU massive) per parallelizzare il cracking di bcrypt in modo efficiente.
    
- **Differenza con Argon2/scrypt:** Questi ultimi sono _Memory-Hard_ (riempiono la RAM), rendendo molto più costoso l'uso di hardware specializzato per l'attacco.
    

### Tabella Comparativa Rapida

|**Caratteristica**|**bcrypt**|**Argon2 (Moderno)**|**PBKDF2 (Obsoleto)**|
|---|---|---|---|
|**Tipo di Risorsa**|CPU|CPU + **Memoria (RAM)**|CPU|
|**Resistenza GPU/FPGA**|⚠️ Media|✅ **Alta**|❌ Bassa|
|**Salt Built-in**|✅ Sì|✅ Sì|❌ No (Manuale)|
|**Configurabilità**|Solo Tempo|Tempo, Memoria, Parallelismo|Solo Iterazioni|

## 5. Implementazione Sicura

Quando si utilizza bcrypt, la stringa salvata nel database contiene già tutte le informazioni necessarie per la verifica (algoritmo, costo, salt e hash).

**Esempio di struttura stringa (concettuale):**

Plaintext

```
$2b$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUX
```

> [!abstract] Code Analysis
> 
> - `$2b$`: Identificativo della versione dell'algoritmo.
>     
> - `$12$`: Il **Cost Factor**. Indica $2^{12}$ iterazioni (4096).
>     
> - `R9h...`: I primi 22 caratteri sono il **Salt**.
>     
> - `PST9...`: La parte finale è l'**Hash** vero e proprio.
>     

## 6. Best Practices di Manutenzione

- **Aggiornamento del Costo:** Poiché le CPU diventano più veloci, il "Cost Factor" deve essere aumentato periodicamente (es. ogni anno o due) per garantire che il tempo di verifica rimanga sufficientemente alto da scoraggiare il brute-force.
    
- **Migrazione:** Se possibile, per sistemi ad alta sicurezza, valutare la migrazione verso **[[Argon2]]** o **[[scrypt]]** per mitigare gli attacchi basati su GPU.