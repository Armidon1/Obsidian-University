---
aliases:
  - RSA-PSS
---
# RSA-PSS (Probabilistic Signature Scheme)

**Tags:** #ingegneria #crittografia #RSA #firma_digitale #sicurezza #PSS #PKCS1

## 1. Introduzione e Motivazione

**RSASSA-PSS** (Probabilistic Signature Scheme, detto anche **RSA-PSS**) è lo standard **moderno e raccomandato** per la Firma Digitale RSA, introdotto in **PKCS#1 v2.1** (RFC 8017).

Perché è stato introdotto per sostituire la versione precedente (v1.5)?

- **Problema della v1.5:** Era **deterministica**. Firmare lo stesso file due volte produceva la stessa identica firma. Questo poteva portare a vulnerabilità teoriche.
    
- **Soluzione PSS:** È **probabilistico**. Introduce la casualità (tramite un **Salt**). Ogni volta che firmi, la firma cambia bit per bit, pur rimanendo valida per lo stesso messaggio.
    
- **Sicurezza:** Offre una sicurezza "provabile" sotto assunzioni standard.
    

---

## 2. Costruzione della Firma (Signature Generation)

Il processo di creazione della firma è strutturato per garantire robustezza matematica.

### Parametri di Input

- $M$: Il messaggio da firmare.
    
- $H$: L'hash del messaggio, calcolato come $H = \text{Hash}(M)$ (es. SHA-256).
    
- **Salt**: Una stringa casuale generata sul momento (es. 32 byte).
    

### Algoritmo Passo-Passo

Ecco come viene costruito il blocco dati prima della firma matematica.

1. Hashing Iniziale ($H'$)

Si crea un nuovo hash che lega insieme il padding iniziale, l'hash del messaggio e il salt casuale.

$$H' = \text{Hash}(0x00 \dots 00 \ || \ H \ || \ \text{salt})$$

_(Dove $||$ indica la concatenazione e $0x00 \dots 00$ sono 8 byte di zeri)_.

2. Creazione del Data Block ($DB$)

Si costruisce un blocco contenente il padding di zeri ($PS$), un byte separatore ($0x01$) e il salt.

**Structure visualization:**

Plaintext

```
DB = PS || 0x01 || salt
```

> [!abstract] Component Analysis
> 
> - **PS:** Padding String di zeri. La sua lunghezza è calcolata per riempire il blocco fino alla dimensione del modulo RSA.
>     
> - **0x01:** Separatore obbligatorio.
>     
> - **salt:** La stringa casuale generata al passo 1.
>     

3. Mascheramento (Masking)

Qui avviene la magia di PSS. Si usa una MGF (Mask Generation Function) per "nascondere" il Data Block.

$$maskedDB = DB \oplus \text{MGF1}(H', \text{len}(DB))$$

_(Il simbolo $\oplus$ indica lo XOR)_.

4. Encoding Finale ($EM$)

Il blocco finale pronto per la firma ($EM$) è composto dal DB mascherato, l'hash $H'$ e un byte finale fisso.

Plaintext

```
EM = maskedDB || H' || 0xbc
```

> [!failure] Common Pitfall
> 
> Il byte finale 0xbc è fondamentale. Se manca o è diverso, la verifica fallisce immediatamente.

5. Firma Matematica ($S$)

Infine, si applica la chiave privata RSA ($d$) al blocco $EM$ (interpretato come numero).

$$S = EM^d \pmod n$$
![[Pasted image 20260114143607.png]]
---

## 3. Verifica della Firma

Il destinatario deve verificare che la firma sia valida e che il messaggio non sia stato alterato.

**Algoritmo di Verifica:**

1. Recupero: Si decifra la firma $S$ usando la chiave pubblica $e$ per ottenere $EM$.
    
    $$EM = S^e \pmod N$$
    
2. **Splitting:** Si divide $EM$ per separare il `maskedDB` e l'hash `H'`. Si controlla che l'ultimo byte sia `0xbc`.
    
3. Unmasking: Si rimuove la maschera per recuperare il $DB$ originale.
    
    $$DB = maskedDB \oplus \text{MGF1}(H', \text{len}(DB))$$
    
4. **Estrazione Salt:** Dal $DB$ pulito, si verifica il padding di zeri, il separatore `0x01` e si estrae il **Salt** originale.
    
5. **Verifica Finale:** Il ricevente ricalcola autonomamente $H'_{new}$ usando il messaggio originale $M$, l'hash $H$ e il **Salt** appena estratto.
    
6. **Confronto:** Se $H'_{new}$ è identico all'$H'$ trovato dentro la firma, allora la firma è valida.
    

---

## 4. Riepilogo Differenze: PSS vs v1.5

|**Caratteristica**|**PKCS#1 v1.5 (Legacy)**|**RSA-PSS (Moderno)**|
|---|---|---|
|**Natura**|Deterministico (firme identiche)|Probabilistico (firme diverse)|
|**Componente Chiave**|Padding statico (0xFF)|Salt Casuale + MGF1|
|**Sicurezza**|Vulnerabile a Padding Oracle|Provabilmente Sicuro|
|**Uso**|Retrocompatibilità (PDF, TLS < 1.3)|Nuovi Sistemi (TLS 1.3, FIPS)|

> [!tip] Exam Focus
> 
> Se ti viene chiesto come PSS raggiunge la sicurezza probabilistica, la risposta chiave è: "Attraverso l'uso di un Salt casuale e di una Mask Generation Function (MGF) che randomizzano l'input della firma RSA."