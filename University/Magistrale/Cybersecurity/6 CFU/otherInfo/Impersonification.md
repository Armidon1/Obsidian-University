# Impersonificazione e Attacchi Man-in-the-Middle (MITM)

**Tags:** #ingegneria #security #impersonation #mitm #pki #crittografia

## 1. Definizione e Contesto

L'**Impersonificazione** (o _Impersonation_) è un attacco in cui un avversario (Trudy) riesce a farsi passare per un'entità legittima (Alice) agli occhi di un verificatore (Bob).

Nel contesto della crittografia a chiave pubblica, questo problema nasce non dalla debolezza degli algoritmi crittografici, ma dalla mancanza di **Binding** (legame) certo tra l'identità di un utente e la sua chiave pubblica.

### Il Problema della "Falsa Chiave Pubblica"

Se Trudy riesce a convincere Bob che la chiave pubblica di Trudy ($K_{PT}$) è in realtà la chiave pubblica di Alice:

1. Bob userà $K_{PT}$ per cifrare i messaggi destinati ad Alice (o per verificare le firme).
    
2. Trudy potrà decifrare i messaggi (avendo la chiave privata corrispondente) o firmare documenti a nome di Alice.
    
3. **Risultato:** Autenticazione rotta, nonostante la matematica sia corretta.
    

> [!failure] Common Pitfall
> 
> Wrong Key = Wrong Identity. Il sistema crittografico verifica solo che la chiave privata corrisponda a quella pubblica. Non verifica "di chi" sia quella chiave pubblica.

---

## 2. Attacco Man-in-the-Middle (MITM)

L'impersonificazione è spesso il preludio a un attacco MITM completo, dove l'attaccante si interpone attivamente tra due vittime.

### Logica Tecnica (Esempio su Needham-Schroeder)

Un esempio classico di impersonificazione tramite MITM avviene nel protocollo Needham-Schroeder a chiave pubblica, dove l'attaccante $T$ sfrutta una sessione legittima con $A$ per impersonare $A$ verso $B$.

**The attack flow (Interleaved Sessions):**

$$\begin{align} 1. \ A \to T : \ & K_{PT}(N_A, A) \quad \text{(A inizia sessione con T)} \\ 2. \ T(A) \to B : \ & K_{PB}(N_A, A) \quad \text{(T inoltra a B fingendosi A)} \\ 3. \ B \to T(A) : \ & K_{PA}(N_A, N_B) \quad \text{(B risponde cifrando per A)} \\ 4. \ T \to A : \ & K_{PA}(N_A, N_B) \quad \text{(T usa A come oracolo per decifrare)} \\ 5. \ A \to T : \ & K_{PT}(N_B) \quad \text{(A decifra e risponde a T)} \\ 6. \ T(A) \to B : \ & K_{PB}(N_B) \quad \text{(T completa l'auth con B)} \end{align}$$

> [!abstract] Math Analysis
> 
> Il trucco:
> 
> - Al passo 3, $B$ invia un nonce $N_B$ cifrato per $A$. $T$ non può decifrarlo.
>     
> - Al passo 4, $T$ inoltra lo stesso messaggio ad $A$. Poiché $A$ sta aspettando una risposta da $T$, crede che sia legittima.
>     
> - Al passo 5, $A$ "aiuta" involontariamente $T$ decifrando $N_B$ e rispedendolo indietro (cifrato per $T$, che quindi può leggerlo).
>     
> - **Conclusione:** $T$ ha impersonato $A$ verso $B$ senza conoscere la chiave privata di $A$.
>     

---

## 3. Soluzione: Certificati e PKI

Per prevenire l'impersonificazione, dobbiamo garantire l'autenticità della chiave pubblica.

### Public Key Infrastructure (PKI)

È l'architettura che gestisce la fiducia. Si basa su Terze Parti Fidate (CA - Certification Authorities) che agiscono come "Trust Anchors".

### Certificati X.509

Un certificato è un documento firmato digitalmente che lega indissolubilmente un'identità a una chiave pubblica.

**The logical structure of a certificate verification is:**

$$\text{Verify}(Pk_{CA}, \text{Signature}_{CA}, \text{Identity}_A || Pk_A) \rightarrow \text{Valid/Invalid}$$

> [!abstract] Visual Analysis
> 
> Il verificatore non si fida ciecamente della chiave pubblica $Pk_A$. Invece:
> 
> 1. Legge il certificato fornito da $A$.
>     
> 2. Usa la chiave pubblica della CA ($Pk_{CA}$, che possiede a priori) per verificare la firma sul certificato.
>     
> 3. Se la firma è valida, accetta che $Pk_A$ appartiene davvero ad $A$.
>     

### Prevenzione negli Standard (Fix al MITM)

Per bloccare l'attacco MITM visto sopra (Needham-Schroeder), è necessario includere l'identità del mittente all'interno del messaggio cifrato.

**Corrected Step:**

$$B \to A : K_{PA}(B, N_A, N_B)$$

> [!tip] Exam Focus
> 
> Se $B$ include la propria identità ("Sono B") dentro il messaggio cifrato:
> 
> - Quando $A$ decifra il messaggio (che credeva provenire da $T$), legge "Sono B".
>     
> - $A$ rileva l'incongruenza ($T \neq B$) e interrompe il protocollo, sventando l'impersonificazione.
>