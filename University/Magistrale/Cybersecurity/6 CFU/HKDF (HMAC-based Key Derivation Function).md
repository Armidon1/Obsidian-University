# HKDF (HMAC-based Key Derivation Function)

**Tags:** #ingegneria #security #crittografia #tls #hkdf #rfc5869

## 1. Definizione e Scopo

**HKDF** è un meccanismo crittografico progettato per generare materiale crittografico forte (chiavi) partendo da un segreto iniziale che potrebbe non essere perfettamente uniforme (come il risultato di uno scambio Diffie-Hellman).

È definito nella **RFC 5869** ed è il cuore del sistema di gestione delle chiavi in **[[TLS]] 1.3**.

### Perché usare HKDF?

Non basta "tagliare a pezzi" una chiave lunga per ottenerne due corte. Se la fonte ha bassa entropia o pattern, le chiavi derivate saranno deboli. HKDF risolve questo problema usando **[[HMAC]]** (Hash-based Message Authentication Code) come primitiva di base per "distillare" ed espandere l'entropia.

---

## 2. L'Algoritmo "Extract-then-Expand"

HKDF opera rigorosamente in due fasi distinte. Questo paradigma (estrazione poi espansione) è considerato molto più robusto rispetto alle vecchie KDF ad-hoc.

### Fase 1: Extract (Estrazione)

L'obiettivo è prendere una sorgente di entropia "grezza" (IKM) e concentrarla in una chiave pseudocasuale uniforme e corta (PRK).

**The extraction logic is:**

$$\text{PRK} = \text{HMAC-Hash}(\text{salt}, \text{IKM})$$

> [!abstract] Math Analysis
> 
> - **IKM (Input Keying Material):** Il segreto iniziale (es. il risultato condiviso di ECDHE).
>     
> - **salt:** Un valore casuale non segreto (opzionale ma raccomandato). In TLS 1.3, se manca, si usa una stringa di zeri.
>     
> - **PRK (Pseudorandom Key):** Il risultato intermedio, una chiave ad alta entropia di lunghezza fissa (es. 256 bit per SHA-256).
>     

### Fase 2: Expand (Espansione)

L'obiettivo è usare la PRK per generare una o più chiavi di output (OKM) crittograficamente indipendenti e di lunghezza arbitraria.

**The expansion logic is:**

$$\text{OKM}_i = \text{HKDF-Expand}(\text{PRK}, \text{info}_i, L_i)$$

> [!abstract] Math Analysis
> 
> - **PRK:** La chiave "maestra" calcolata nella fase 1.
>     
> - **info:** Una stringa di contesto (Context String) che lega la chiave a uno scopo specifico (es. "tls13 client write key"). È cruciale per la separazione delle chiavi.
>     
> - **L:** La lunghezza desiderata in byte dell'output.
>     
> - **OKM (Output Keying Material):** La chiave finale utilizzabile (es. chiave AES, IV, chiave HMAC).
>     

---

## 3. Implementazione e Pseudo-Codice

Il calcolo iterativo nella fase di espansione funziona concatenando i risultati precedenti.

**Here is the algorithmic logic:**

Plaintext

```
HKDF-Expand(PRK, info, L)
   N = ceil(L / HashLen)
   T[0] = empty string
   T[1] = HMAC(PRK, T[0] | info | 0x01)
   T[2] = HMAC(PRK, T[1] | info | 0x02)
   ...
   T[N] = HMAC(PRK, T[N-1] | info | N)
   OKM = first L bytes of (T[1] | T[2] | ... | T[N])
```

> [!abstract] Code Analysis
> 
> Si nota come ogni blocco dipenda dal precedente (T[i-1]) e includa un contatore esadecimale (0x01, 0x02...). Questo impedisce che parti diverse della chiave siano correlate.

---

## 4. Ruolo in TLS 1.3

In TLS 1.3, HKDF sostituisce completamente la vecchia funzione PRF (Pseudo-Random Function) di TLS 1.2.

- **Key Separation:** Grazie al parametro `info`, da un singolo segreto ECDHE si derivano chiavi per scopi completamente diversi (cifratura traffico, cifratura handshake, ripresa sessione) senza che la compromissione di una indebolisca le altre.
    
- **Transcript Hash:** L'input `info` include spesso l'hash di tutti i messaggi scambiati fino a quel momento, legando crittograficamente le chiavi alla specifica sessione e prevenendo attacchi man-in-the-middle.
    

> [!tip] Exam Focus
> 
> Salt vs Info:
> 
> - Il **Salt** serve a _estrarre_ casualità (usato nella fase Extract).
>     
> - L'**Info** serve a _separare_ i domini di utilizzo (usato nella fase Expand).
>