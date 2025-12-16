# Generatore $g$ (Radice Primitiva)
	
## 1. Definizione Intuitiva

In crittografia (specialmente nei gruppi moltiplicativi modulo un numero primo $p$, indicati con $\mathbb{Z}_p^*$), un **Generatore** $g$ è un numero speciale che, se elevato a potenza ripetutamente, è capace di **generare tutti i numeri possibili** del gruppo (da $1$ a $p-1$) prima di ricominciare da capo.

In termini semplici: $g$ è un numero che, facendo $g^x \pmod p$, "tocca" ogni possibile risultato nel campo prima di ritornare a 1.

> [!abstract] Metafora dell'Orologio
> 
> Immagina un orologio con $p$ ore.
> 
> Un Generatore è una lancetta che, girando, tocca tutte le ore una per una senza saltarne nessuna, prima di tornare alle 12.
> 
> Un Non-Generatore è una lancetta che tocca solo poche ore (es. solo le ore pari) e entra in un ciclo corto ripetitivo.

## 2. Esempio Pratico (Piccoli Numeri)

Prendiamo un numero primo piccolo, $p = 7$.

Il gruppo $\mathbb{Z}_7^*$ contiene gli elementi $\{1, 2, 3, 4, 5, 6\}$.

Proviamo a vedere se **$g=2$** è un generatore:

1. $2^1 \pmod 7 = 2$
    
2. $2^2 \pmod 7 = 4$
    
3. $2^3 \pmod 7 = 8 \equiv \mathbf{1}$ _(Il ciclo si è chiuso!)_
    
4. $2^4 \pmod 7 = 2$ ...
    
    Sequenza generata: $\{2, 4, 1\}$.
    
    Risultato: Il 2 NON è un generatore. Ha generato solo 3 numeri su 6.
    

Proviamo a vedere se **$g=3$** è un generatore:

1. $3^1 \pmod 7 = \mathbf{3}$
    
2. $3^2 \pmod 7 = 9 \equiv \mathbf{2}$
    
3. $3^3 \pmod 7 = 27 \equiv \mathbf{6}$
    
4. $3^4 \pmod 7 = 81 \equiv \mathbf{4}$
    
5. $3^5 \pmod 7 = 243 \equiv \mathbf{5}$
    
6. $3^6 \pmod 7 = 729 \equiv \mathbf{1}$ (Ciclo chiuso)
    
    Sequenza generata: $\{3, 2, 6, 4, 5, 1\}$.
    
    Risultato: Il 3 È un generatore (o Radice Primitiva) modulo 7, perché ha coperto tutto l'insieme.
    

## 3. Perché è importante per la Sicurezza?

In protocolli come **Diffie-Hellman** o **ElGamal**, la sicurezza si basa sulla difficoltà del **Logaritmo Discreto**: dato $y = g^x \pmod p$, trovare $x$.

Se usassimo un $g$ sbagliato (non generatore) che genera un ciclo molto piccolo (es. sottogruppo di soli 1000 numeri invece di $10^{100}$):

1. Lo spazio delle chiavi possibili si ridurrebbe drasticamente.
    
2. Un attaccante potrebbe provare tutte le potenze possibili in pochi secondi (Brute Force sul sottogruppo piccolo).
    
3. L'algoritmo **Pohlig-Hellman** potrebbe rompere il sistema istantaneamente.
    

Per la massima sicurezza, vogliamo che il sottogruppo generato da $g$ abbia un **ordine primo molto grande**.

## 4. Come viene scelto $g$? (Algoritmo di Selezione)

Non si sceglie $g$ a caso sperando che vada bene. Esiste una procedura matematica rigorosa.

### Requisito Matematico

Un numero $g$ è un generatore modulo $p$ se e solo se:

$$g^{(p-1)/q} \not\equiv 1 \pmod p$$

Per tutti i fattori primi $q$ di $(p-1)$.

### Il Metodo dei "Safe Primes" (Primi Sicuri)

Per semplificare la vita agli ingegneri e rendere la verifica velocissima, si usano i **Primi di Sophie Germain**.

1. Si sceglie un primo $q$ grande.
    
2. Si calcola $p = 2q + 1$. Se anche $p$ è primo, allora $p$ è un **Safe Prime**.
    
    - _Esempio:_ $q=5 \to p=11$ ($11$ è safe prime).
        
3. In questo caso speciale, l'ordine del gruppo $p-1$ è $2q$. I fattori sono solo $\{2, q\}$.
    
4. **Test Semplificato:** Per verificare se $g$ è un generatore basta controllare che:
    
    - $g^2 \not\equiv 1 \pmod p$
        
    - $g^q \not\equiv 1 \pmod p$
        

Se supera questi due test, $g$ è un generatore sicuro.

> [!tip] Standard Reale
> 
> Nella pratica (es. nei gruppi Diffie-Hellman standard di Internet - RFC 3526), non si calcola $g$ ogni volta. Si usano valori standard fissi e sicuri.
> 
> Spesso si usa $g = 2$ (se il primo $p$ è scelto accuratamente per far sì che 2 sia un generatore) o $g = 5$.

---

**Vedi anche:**

- [[Criptosistema ElGamal]]
    
- [[Diffie-Hellman]]
    
- [[Logaritmo Discreto (DLP)]]
    
- [[Teoria dei Numeri]]