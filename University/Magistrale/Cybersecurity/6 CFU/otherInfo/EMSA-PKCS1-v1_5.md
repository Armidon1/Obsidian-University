# EMSA-PKCS1-v1_5 (Encoding Method for Signature with Appendix)

**Tags:** #ingegneria #crittografia #RSA #firma_digitale #encoding #standard #legacy

## 1. Introduzione e Contesto

EMSA-PKCS1-v1_5 è lo schema di codifica (encoding) definito nello standard PKCS#1 v1.5.

Rappresenta il metodo di preprocessing utilizzato nel paradigma Hash-then-Sign per preparare un messaggio prima che venga firmato con la chiave privata RSA.

È importante notare che:

- **Stato:** È considerato **Legacy** (obsoleto per nuovi sviluppi), ma è ancora ampiamente supportato per retrocompatibilità.
    
- **Natura:** È un formato di padding **Deterministico**. Non introduce casualità: lo stesso messaggio produce sempre la stessa firma.
    

---

## 2. Struttura dell'Encoding (EM)

L'obiettivo dell'encoding è trasformare l'hash del messaggio in un blocco di dati ($EM$) della stessa lunghezza del modulo RSA ($|N|$).

### Logica di Costruzione

Il blocco $EM$ è costruito concatenando rigidamente diversi segmenti.

**La definizione matematica della struttura è:**

$$EM = 0\text{x}00 \ || \ 0\text{x}01 \ || \ PS \ || \ 0\text{x}00 \ || \ T$$

_(Dove $||$ indica la concatenazione)_.

### Dettaglio dei Componenti

**Here is the exact structure representation:**

```
EM = 0x00 || 0x01 || PS || 0x00 || T
```

> [!abstract] Component Analysis
> 
> - **0x00:** Byte iniziale fisso (garantisce che il valore intero di $EM$ sia minore del modulo $n$).
>     
> - **0x01:** Tipo di blocco (Block Type 1), specifico per le firme digitali (distingue dalla cifratura).
>     
> - **PS (Padding String):** Una sequenza di byte `0xFF`. Serve a riempire lo spazio vuoto per raggiungere la lunghezza del modulo.
>     
> - **0x00:** Separatore obbligatorio tra il padding e il digest.
>     
> - **T (DigestInfo):** Contiene l'OID dell'algoritmo di hash (es. SHA-256) e l'hash del messaggio stesso.
>     

---

## 3. Processo di Generazione della Firma

Il processo completo di firma (RSASSA-PKCS1-v1_5) integra l'encoding con la primitiva RSA.

**Passaggi Logici:**

1. Calcolo dell'hash: $H = \text{Hash}(M)$.
    
2. Costruzione di $T$ (codifica DER dell'algoritmo + $H$).
    
3. Costruzione di $EM$ aggiungendo il padding.
    
4. Calcolo della firma matematica.
    

**The signature equation is:**

$$S = EM^d \pmod n$$

_(Dove $d$ è la chiave privata)_.

---

## 4. Verifica della Firma

La verifica segue il percorso inverso e controlla se la struttura $EM$ decifrata corrisponde a quella attesa.

**Algoritmo di Verifica:**

1. Il ricevente calcola l'hash $H$ del messaggio originale.
    
2. Costruisce localmente il blocco atteso ($EM_{expected}$) usando EMSA-PKCS1-v1_5.
    
3. Decifra la firma ricevuta $S$ usando la chiave pubblica $e$:
    

$$EM' = S^e \pmod n$$

4. Confronta: Se $EM' == EM_{expected}$, la firma è valida.
    

> [!failure] Common Pitfall
> 
> Vulnerabilità: Poiché il formato è deterministico e il padding è semplice (solo byte 0xFF), questo schema è suscettibile ad attacchi di falsificazione (come l'attacco di Bleichenbacher) se la verifica non controlla rigorosamente ogni singolo byte del formato. Questo è il motivo principale per cui si preferisce RSA-PSS.