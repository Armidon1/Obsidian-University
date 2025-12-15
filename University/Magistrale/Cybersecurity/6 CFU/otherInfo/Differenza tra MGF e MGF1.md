# Differenza tra MGF e MGF1

## 1. Il Concetto in Breve (Analogy)

Per capire la differenza, pensa alla programmazione ad oggetti:

- **MGF (Mask Generation Function):** È l'**Interfaccia** (o la classe astratta). Definisce _cosa_ deve fare la funzione (input e output), ma non _come_.
    
- **MGF1:** È l'**Implementazione** concreta (la classe reale). È l'algoritmo specifico scritto nel codice che soddisfa i requisiti dell'interfaccia MGF.
    

> [!tip] In Pratica
> 
> Nello standard PKCS#1, ogni volta che si parla di schemi come [[RSA-OAEP]] o [[RSA-PSS]], si dice che richiedono una generica "MGF".
> 
> Tuttavia, al momento, MGF1 è l'unica funzione MGF definita ufficialmente dallo standard. Quindi, nel 99% dei casi reali, quando leggi MGF stai usando MGF1.

## 2. MGF (Il Ruolo Astratto)

Una **MGF** è una qualsiasi funzione crittografica che accetta un input di lunghezza variabile e produce un output di lunghezza arbitraria (spesso più lungo dell'input).

**Firma Funzionale:**

$$\text{MGF}(seed, maskLen) \to \text{mask}$$

- **Input:** Un _seed_ (i dati da espandere) e la lunghezza desiderata ($maskLen$).
    
- **Output:** Una stringa di bit pseudo-casuali (la _maschera_).
    
- **Requisito:** Deve essere deterministica (stesso seed = stessa maschera).
    

## 3. MGF1 (L'Algoritmo Standard)

**MGF1** è l'algoritmo specifico descritto nell'appendice di PKCS#1. È costruito sopra una **Funzione Hash** esistente (come SHA-1, SHA-256, ecc.).

Come funziona MGF1:

Per generare una maschera lunga, MGF1 esegue un ciclo:

1. Prende il $seed$.
    
2. Gli appende un contatore a 32 bit ($0, 1, 2 \dots$).
    
3. Calcola l'hash del risultato.
    
4. Concatena gli hash finché non raggiunge la lunghezza desiderata.
    

$$\text{Mask} = \text{Hash}(seed || 0) \ || \ \text{Hash}(seed || 1) \ || \ \text{Hash}(seed || 2) \dots$$

## 4. Tabella di Confronto

|**Caratteristica**|**MGF**|**MGF1**|
|---|---|---|
|**Natura**|Definizione astratta (Ruolo).|Algoritmo concreto.|
|**Dipendenza**|Nessuna.|Dipende da una Hash Function (es. MGF1-SHA256).|
|**Flessibilità**|Lo standard permette di inventare nuove MGF in futuro.|È "cablata" nel modo Hash+Contatore.|
|**Uso**|Parametro di OAEP/PSS.|Valore tipico di quel parametro.|

---

**Vedi anche:**

- [[Mask Generation Function (MGF)]] (Dettagli tecnici di MGF1)
    
- [[RSA-OAEP]]
    
- [[PKCS#1]]