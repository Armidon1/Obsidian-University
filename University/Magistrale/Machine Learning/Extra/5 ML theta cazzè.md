Nel contesto dei classificatori lineari come il Perceptron e le SVM, il vettore **$\theta$ (Theta)** è il cuore di tutto il modello.

Possiamo immaginare la sua funzione in tre modi diversi, dal più visivo al più tecnico:

### 1. Il Ruolo Geometrico: "La Freccia Direzionale"

![[Pasted image 20260216181001.png]]

Visivamente, $\theta$ è un vettore che **punta perpendicolarmente** rispetto alla tua decision boundary (il muro).

- **Definisce l'orientamento:** Se ruoti la freccia $\theta$, ruota anche tutto il muro (l'iperpiano $H_\theta$) perché i due rimangono sempre bloccati a 90° l'uno rispetto all'altro.
- **Definisce il lato "Positivo":** La direzione in cui punta la freccia $\theta$ indica quale lato del muro è considerato la "Classe +1". Il lato opposto, alle spalle della freccia, è la "Classe -1".

### 2. Il Ruolo Funzionale: "Il Giudice"

Quando arriva un nuovo punto dati $x$, è $\theta$ che decide a quale classe appartiene. Lo fa attraverso il **prodotto scalare** che abbiamo visto prima:

- Il modello calcola quanto $x$ è "d'accordo" con $\theta$ ($x^T \theta$).
- Se sono d'accordo (risultato positivo), $\theta$ assegna l'etichetta **+1**.
- Se sono in disaccordo (risultato negativo), $\theta$ assegna l'etichetta **-1**.

### 3. Il Ruolo nell'SVM: "Il Regolatore del Margine"

Nelle Support Vector Machines, $\theta$ ha un compito extra molto importante legato alla sua **lunghezza** (norma $|\theta|$).

- C'è una relazione inversa tra la lunghezza di $\theta$ e la larghezza della strada (il margine $\gamma$).
- Più il vettore $\theta$ è **corto** (norma piccola), più il margine di sicurezza è **ampio**.
- Ecco perché l'obiettivo dell'SVM è minimizzare $|\theta|^2$: vuole trovare il vettore più "piccolo" possibile che riesca comunque a separare i dati, garantendo così la strada più larga possibile.

> **In sintesi per la tua immagine mentale:** Se l'iperpiano è un **muro** che divide il campo, $\theta$ è il **pilastro** che lo sostiene e ne decide l'inclinazione. Nell'SVM, cerchiamo di rendere questo pilastro il più piccolo possibile per allargare lo spazio libero attorno al muro.