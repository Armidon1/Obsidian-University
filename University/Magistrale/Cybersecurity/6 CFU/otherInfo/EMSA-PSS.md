---
aliases:
  - PSS
---

# EMSA-PSS (Encoding Method for Signature with Appendix - PSS)

## 1. Definizione e Contesto

**[[EMSA]]-PSS** è lo schema di codifica definito in **PKCS#1 v2.1** (RFC 8017) utilizzato per trasformare un messaggio (o meglio, il suo hash) in un blocco dati strutturato ($EM$) pronto per essere firmato con RSA.

È il componente di Encoding dello schema di firma completo [[RSASSA-PSS]].

La sua caratteristica distintiva è essere Probabilistico: utilizza un numero casuale (Salt) per garantire che codificare lo stesso messaggio due volte produca due blocchi $EM$ completamente diversi.

## 2. Input e Parametri

Per eseguire la codifica, l'algoritmo necessita di:

1. **$M$**: Il messaggio da firmare.
    
2. **$Hash$**: Una funzione hash crittografica (es. [[SHA-256]]).
    
3. **$MGF$**: Una Mask Generation Function (solitamente [[Mask Generation Function (MGF)]]1 basata sullo stesso hash).
    
4. **$sLen$**: La lunghezza del Salt (tipicamente pari alla lunghezza dell'output dell'hash).
    

## 3. L'Algoritmo di Encoding (Passo dopo Passo)

L'obiettivo è creare un blocco $EM$ di lunghezza $emLen$ (bit del modulo RSA - 1).

### Fase 1: Hashing e Salting

Non si firma il messaggio nudo. Si calcola il suo hash ($mHash$) e lo si concatena con un **Salt** casuale e un padding di 8 byte di zeri (per evitare collisioni matematiche).

$$H' = \text{Hash}(0x0000000000000000 \ || \ mHash \ || \ salt)$$

### Fase 2: Costruzione del Data Block (DB)

Si crea un blocco dati ($DB$) che contiene il padding necessario per riempire la lunghezza, un byte separatore $0x01$ e il salt originale.

Plaintext

```
DB = PS || 0x01 || salt
```

_(Dove PS è una stringa di byte 0x00)_

### Fase 3: Mascheramento (Masking)

Qui avviene la protezione principale. Si usa la MGF per generare una maschera basata su $H'$ e si fa lo XOR con il $DB$.

$$maskedDB = DB \oplus \text{MGF}(H', \text{len}(DB))$$

### Fase 4: Assemblaggio Finale ($EM$)

Il messaggio codificato finale ($EM$) ha questa struttura precisa:

$$EM = maskedDB \ || \ H' \ || \ 0xbc$$

> [!abstract] Visual Analysis
> 
> Com'è fatto il blocco finale EM?
> 
> [ Dati Mascherati (Salt nascosto) ] [ Hash H' (in chiaro) ] [ 0xbc ]
> 
> - **Dati Mascherati:** Sembrano rumore casuale.
>     
> - **Hash H':** È il "perno" della verifica. Serve al destinatario per generare la stessa maschera e sbloccare i dati.
>     
> - **0xbc:** È il "magic byte" finale obbligatorio per PSS.
>     

## 4. Bit Clearing (Dettaglio Tecnico)

Poiché RSA lavora con numeri interi modulo $n$, il valore numerico di $EM$ deve essere sempre minore di $n$.

Per garantire questo in ogni caso:

- Il **bit più significativo** del primo byte di $maskedDB$ viene forzato a **0**.
    
- Questo assicura che $EM < n$ (assumendo che la lunghezza in bit sia corretta).
    

## 5. Differenze con EMSA-PKCS1-v1_5

|**Caratteristica**|**EMSA-PKCS1-v1_5**|**EMSA-PSS**|
|---|---|---|
|**Input Variabile**|Nessuno (Deterministico)|**Salt** (Probabilistico)|
|**Struttura**|`00 01 FF..FF 00 Hash`|`XOR-Mask|
|**Sicurezza**|Basata su euristiche|**Riduzione di Sicurezza** (Random Oracle)|
|**Recupero Salt**|Non applicabile|Il salt viene recuperato togliendo la maschera|

## 6. Verifica (Inversione)

La verifica dell'encoding (usata dopo `RSAVP1`) segue la logica inversa:

1. Controlla che l'ultimo byte sia $0xbc$.
    
2. Usa $H'$ (che è in chiaro nel blocco) per rigenerare la maschera con la MGF.
    
3. Esegue `maskedDB XOR Maschera` per riottenere il $DB$ pulito.
    
4. Estrae il salt e verifica che il padding $PS$ sia tutto zeri e finisca con $0x01$.
    
5. Se tutto coincide, ricalcola $H'$ e confronta.
    

> [!tip] Exam Focus
> 
> Ricorda che EMSA-PSS non cifra il messaggio per nasconderlo.
> 
> Maschera il salt e la struttura interna per rendere difficile per un attaccante manipolare la firma matematica, ma il contenuto informativo (l'hash del messaggio) è necessario per la verifica.

---

**Vedi anche:**

- [[RSASSA-PSS]] (Lo schema completo)
    
- [[Mask Generation Function (MGF)]]
    
- [[Salt (Crittografia)]]