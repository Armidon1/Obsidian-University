# 🧮 Teorema di Eulero (Crittografia/Teoria dei Numeri)

Il **Teorema di Eulero** è un risultato fondamentale della teoria dei numeri. Il _[[Fermat's Little Theorem|Piccolo Teorema di Fermat]]_ è un  caso specifico del Teorema di Eulero.                

>[!Definizione]
>Se due numeri interi positivi $a$ e $n$ sono **[[Coprime|coprimi]]** (cioè, il loro massimo comun divisore è 1, $\gcd(a, n) = 1$), allora:
>$$a^{\phi(n)} \equiv 1 \pmod n$$

Dove:

- $n$ è il modulo.
    
- $a$ è un numero intero coprimo con $n$.
    
- $\phi(n)$ è la **[[Euler's totient function|Funzione Totiente di Eulero]]**.
    
- $\equiv$ indica la congruenza (il resto della divisione per $n$ è uguale a 1).
    

È la spina dorsale matematica su cui si basa il funzionamento dell'algoritmo di crittografia asimmetrica **[[RSA]]**.
### Componenti Chiave per un Ingegnere

|**Componente**|**Descrizione Tecnica**|
|---|---|
|**Funzione Totiente $\phi(n)$**|Conta quanti numeri interi positivi minori di $n$ sono coprimi con $n$.<br><br>  <br><br>• Se $p$ è primo, $\phi(p) = p - 1$.<br><br>  <br><br>• Se $n = p \times q$ (prodotto di due primi, come in RSA), $\phi(n) = (p-1)(q-1)$.|
|**Coprimalità ($\gcd(a, n) = 1$)**|Il teorema funziona _solo_ se $a$ e $n$ non condividono fattori comuni oltre a 1. In crittografia, $n$ è spesso il prodotto di grandi numeri primi, quindi quasi tutti gli interi $a < n$ soddisfano questa condizione.|
|**Relazione con Fermat**|Il Piccolo Teorema di Fermat è un caso speciale di questo teorema dove $n$ è un numero primo ($p$). In quel caso, $\phi(p) = p-1$, quindi $a^{p-1} \equiv 1 \pmod p$.|

### Implicazione in Crittografia (RSA)

Per un ingegnere informatico, questo teorema è cruciale perché permette di "annullare" un'esponenziazione modulare.

In RSA, cifrare significa calcolare $C = M^e \pmod n$.

Per decifrare, calcoliamo $M = C^d \pmod n$.

Questo funziona perché le chiavi $e$ (pubblica) e $d$ (privata) sono scelte in modo tale che $e \times d \equiv 1 \pmod{\phi(n)}$.

Sostituendo, la decifratura diventa $M^{e \times d} \pmod n$. Grazie al teorema di Eulero, sappiamo che questa operazione restituirà il messaggio originale $M$.