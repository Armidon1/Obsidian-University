# La Coppia $(r, s)$: La Firma Vera e Propria

**Tags:** #ingegneria #ecdsa #matematica #crittografia #firma_digitale

## 1. Che cos'è?

Quando firmi digitalmente un documento con ECDSA, il risultato finale NON è un file cifrato o una stringa incomprensibile unica.

La firma digitale è composta esattamente da due numeri interi:

1. **$r$**
    
2. **$s$**
    

Questi due numeri, insieme, costituiscono la "ricevuta" matematica che prova che tu (e solo tu) hai approvato quel messaggio specifico.

---

## 2. Analisi del componente $r$ (La parte casuale)

La $r$ rappresenta la componente visiva del segreto casuale.

Deriva direttamente dal Nonce $k$ (il numero casuale segreto generato all'inizio).

**The mathematical definition of r is:**

$$\begin{align} 1. \ & \text{Calcola il punto } R = k \cdot G \\ 2. \ & r = \text{coordinata } x \text{ del punto } R \pmod n \end{align}$$

> [!abstract] Math Analysis
> 
> - **$G$:** È il punto generatore della curva (un parametro pubblico standard).
>     
> - **$R$:** È un punto sulla curva ellittica. Ha due coordinate $(x, y)$.
>     
> - **$r$:** È semplicemente la **coordinata X** di quel punto.
>     
> 
> **Significato:** $r$ dice al verificatore: "Ho usato un numero casuale per questa firma, ed ecco la sua 'impronta' sulla curva". Poiché il problema del logaritmo discreto è difficile, conoscere $r$ non permette di risalire al nonce $k$.

---

## 3. Analisi del componente $s$ (La parte di legame)

La $s$ è la "prova" vera e propria. È il numero che lega matematicamente insieme tutti gli elementi: la tua chiave privata, il messaggio e la componente casuale.

**The formula to calculate s is:**

$$s = k^{-1} (h + r \cdot d_A) \pmod n$$

> [!abstract] Math Analysis
> 
> Questa formula è il cuore della sicurezza. Vediamo i componenti:
> 
> - **$k^{-1}$:** L'inverso del nonce (serve a nascondere la chiave).
>     
> - **$h$:** L'hash del messaggio (lega la firma al contenuto).
>     
> - **$d_A$:** La tua **Chiave Privata** (prova che sei tu).
>     
> - **$r$:** La componente casuale vista prima.
>     
> 
> **Significato:** $s$ è il risultato di un'equazione che dice: "Ho preso il messaggio e la mia chiave privata, li ho mescolati con il numero casuale $r$, e questo è il risultato".

---

## 4. Sintesi per Immagini

Per visualizzare il concetto, immagina la firma come un sigillo di ceralacca su una busta.

|**Componente**|**Ruolo nell'analogia**|
|---|---|
|**$r$** (Random Point)|È la **forma** unica del timbro usato quella volta specifica. Serve a garantire che ogni firma sia diversa (anche per lo stesso messaggio).|
|**$s$** (Signature Proof)|È la **pressione** precisa applicata, che poteva essere fatta solo dalla mano del proprietario (la chiave privata) su quella specifica busta (il messaggio).|

> [!tip] Exam Focus
> 
> Se all'esame ti chiedono "Perché servono due numeri?", la risposta è:
> 
> - **$r$** serve come riferimento al valore casuale (nonce) senza rivelarlo.
>     
> - **$s$** serve a provare la conoscenza della chiave privata legandola al messaggio e ad $r$.
>     
> 
> Senza $r$, non potremmo verificare l'equazione della curva. Senza $s$, non ci sarebbe legame con la chiave privata.