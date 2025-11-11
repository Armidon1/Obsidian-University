# 🔢 Piccolo Teorema di Fermat

Il **Piccolo Teorema di Fermat** è un teorema fondamentale della teoria dei numeri che descrive una proprietà cruciale dei numeri primi nelle congruenze modulari. È un **caso 
speciale del [[Euler's Theorem|Teorema di Eulero]]** quando il modulo è un numero primo.

>[!definizione]
>Se $p$ è un **numero primo**, allora per ogni numero intero $a$:
$$a^p \equiv a \pmod p$$

### Forma Comune in Crittografia

Nel contesto crittografico, si utilizza spesso una forma leggermente diversa. Se $p$ è un numero primo e $a$ è un intero **non divisibile** per $p$ (cioè $a$ e $p$ sono coprimi), allora:

$$a^{p-1} \equiv 1 \pmod p$$

_Nota: Questa è esattamente la stessa struttura del Teorema di Eulero ($a^{\phi(n)} \equiv 1 \pmod n$), dato che per un numero primo $p$, la funzione totiente è $\phi(p) = p-1$._

### Implicazioni e Usi per un Ingegnere

|**Applicazione**|**Descrizione Tecnica**|
|---|---|
|**Test di Primalità**|È la base per il **Test di primalità di Fermat**. Se vogliamo verificare se un numero $n$ è primo, scegliamo un $a$ casuale e calcoliamo $a^{n-1} \pmod n$. Se il risultato **non è 1**, allora $n$ è **sicuramente composto** (non primo).|
|**Pseudoprimi**|Il teorema è una condizione _necessaria_ ma non _sufficiente_ per la primalità. Esistono numeri composti che "ingannano" questo test per certi valori di $a$ (chiamati **pseudoprimi**) o per _tutti_ i valori di $a$ (numeri di **Carmichael**).|
|**Operazioni Modulari**|Permette di semplificare enormemente i calcoli di esponenti grandi in aritmetica modulare quando il modulo è primo. Esempio: calcolare $7^{222} \pmod{11}$ diventa banale sapendo che $7^{10} \equiv 1 \pmod{11}$.|

In sintesi, per un ingegnere informatico, il Piccolo Teorema di Fermat è uno strumento computazionale rapido per **escludere** che un numero sia primo (compositeness test) e per ottimizzare l'aritmetica modulare.