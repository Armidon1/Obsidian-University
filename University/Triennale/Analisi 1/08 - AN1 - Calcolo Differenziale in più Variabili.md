---
title: Calcolo Differenziale per Funzioni Reali di più Variabili
aliases:
  - AN1 — Calcolo Differenziale in più Variabili
tags:
  - analisi-1
  - più-variabili
  - derivate-parziali
  - gradiente
  - differenziabilità
  - hessiana
  - estremi-locali
source: Appunti di Analisi Matematica 1 di Camilli.pdf (cap. 8)
---

# Calcolo Differenziale per Funzioni Reali di più Variabili

> [!abstract]
> Il capitolo estende la [[05 - AN1 - Calcolo Differenziale|derivata]] alle funzioni di più variabili del [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità|cap. 7]]. A differenza di una variabile, qui i concetti di derivabilità sono **diversi** e non equivalenti: **derivate parziali** (e **gradiente**), **differenziabilità** (con il **piano tangente**) e **derivate direzionali**, collegate dal **teorema del gradiente**. Il gradiente ha due proprietà geometriche importanti: indica la direzione di **massima crescita** ed è **ortogonale alle curve di livello**.
> Seguono le **derivate di ordine superiore**, il **teorema di Schwarz** e la **matrice hessiana**, che servono per gli **estremi locali**: il **teorema di Fermat** in $\mathbb{R}^N$ dà i punti critici, e il segno della hessiana (tramite **autovalori** o il **criterio di Hurwitz**) li classifica in minimi, massimi e **punti di sella**.
> Mappa del corso: [[MOC - Analisi 1]].

---

## Intorni e insiemi aperti

Vedi [[Insiemi aperti e chiusi]].

Per $x_0 \in \mathbb{R}^N$ e $r > 0$ si definisce l'**intorno (circolare)** di raggio $r$:
$$B_r(x_0) := \{x \in \mathbb{R}^N : \|x - x_0\| < r\},$$
il luogo dei punti a distanza minore di $r$ da $x_0$ (la "palla" aperta). Per $N = 1$ è l'intervallo $(x_0 - r, x_0 + r)$; in $\mathbb{R}^2$ è il cerchio di centro $x_0$ e raggio $r$ esclusa la circonferenza; in $\mathbb{R}^3$ la sfera esclusa la superficie sferica.

> [!important] Definizione 8.1 — Punti interni, insiemi aperti e chiusi
> Dato $X \subseteq \mathbb{R}^N$, un punto $x_0$ si dice **interno** a $X$ se esiste $r > 0$ con $B_r(x_0) \subset X$. Inoltre $X$ si chiama
> - **aperto** se ogni $x_0 \in X$ è interno;
> - **chiuso** se il complemento $\mathbb{R}^N \setminus X$ è aperto.

Se un punto è interno al dominio di una funzione, ci si può avvicinare al punto **da ogni direzione** restando nel dominio: è ciò che serve per definire le derivate. Ad esempio il cerchio $\{x^2 + y^2 < 1\}$ è aperto, $\{x^2 + y^2 \le 1\}$ è chiuso (i punti della circonferenza non sono interni), e $\{x^2 + y^2 < 1\} \cup \{(1, 0)\}$ non è né aperto né chiuso. Gli insiemi aperti generalizzano gli intervalli aperti, quelli chiusi gli intervalli chiusi.

_(dispensa, p. 122)_

---

## I Concetti di Derivabilità in RN

Per le funzioni di una variabile c'è un solo concetto di derivabilità; per le funzioni di più variabili la situazione è più complicata.

### Derivate parziali

Vedi [[Derivate parziali]].

> [!important] Definizione 8.2 — Derivata parziale
> Sia $f : X \subseteq \mathbb{R}^N \to \mathbb{R}$ e $x_0 = (x_1^0, \dots, x_N^0)$ interno a $X$. Se, dato $i \in \{1, \dots, N\}$, converge
> $$\lim_{h\to0} \frac{f(x_1^0, \dots, x_{i-1}^0, x_i^0 + h, x_{i+1}^0, \dots, x_N^0) - f(x_1^0, \dots, x_N^0)}{h} =: \frac{\partial f}{\partial x_i}(x_0) \in \mathbb{R},$$
> $f$ si dice **derivabile parzialmente rispetto a $x_i$** in $x_0$, con **derivata parziale** $\frac{\partial f}{\partial x_i}(x_0)$. Altre notazioni: $f_{x_i}(x_0) = D_{x_i}f(x_0)$.

Si incrementa **solo** la coordinata $i$-esima, lasciando ferme le altre. Per $N = 2$:
$$f_x(x_0, y_0) := \lim_{h\to0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}, \qquad f_y(x_0, y_0) := \lim_{h\to0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}.$$

La derivata parziale rispetto a $x$ è la derivata ordinaria (in una variabile) della funzione $g(x) := f(x, y_0)$, la **restrizione** di $f$ alla retta $y = y_0$.

![[AN1-p129-1.png]]

*Figura 76 — Derivate parziali.* In alto la superficie $z = f(x, y)$ tagliata da due piani verticali passanti per $P = (x_0, y_0)$: il piano rosso $y = y_0$ e il piano giallo $x = x_0$. Ogni piano interseca la superficie in una curva. In basso le due curve viste "di fronte": a sinistra $g(x) = f(x, y_0)$, la cui tangente in $x_0$ ha pendenza $f_x(x_0, y_0) = g'(x_0) = \tan(\alpha)$; a destra $h(y) = f(x_0, y)$, con pendenza $f_y(x_0, y_0) = h'(y_0) = \tan(\beta)$ (qui negativa: la curva scende).

Quindi $f_x(x_0, y_0)$ dice se $f$ cresce o decresce lungo la retta $y = y_0$ vicino a $(x_0, y_0)$, e analogamente $f_y$ lungo $x = x_0$.

> [!tip] Come si calcolano
> Se le funzioni che compongono $f$ sono derivabili, basta derivare in modo ordinario **considerando le altre variabili come costanti**:
> - $f(x, y) = 2x^3y - y^2 + 3xy$: $f_x = 6x^2y + 3y$, $f_y = 2x^3 - 2y + 3x$;
> - $f(x, y) = e^{xy} + y^2$: $f_x = ye^{xy}$, $f_y = xe^{xy} + 2y$;
> - $f(x, y, z) = \cos(xyz)$: $f_x = -yz\sin(xyz)$, $f_y = -xz\sin(xyz)$, $f_z = -xy\sin(xyz)$.

Se le funzioni non sono derivabili, si torna alla definizione. Ad esempio per $f(x, y) = |x|y$ nei punti $(0, y)$:
$$f_x(0, y) = \lim_{h\to0} \frac{f(h, y) - f(0, y)}{h} = \lim_{h\to0} \frac{|h|y}{h} = \begin{cases} \nexists & y \neq 0, \\ 0 & y = 0. \end{cases}$$

### Gradiente

Vedi [[Gradiente]].

> [!important] Definizione 8.3 — Gradiente
> Se $f$ è derivabile parzialmente rispetto a ogni $x_i$ in $x_0$ (interno), $f$ si dice **derivabile (parzialmente)** in $x_0$ e si definisce il vettore delle derivate parziali
> $$Df(x_0) = \left(\frac{\partial f}{\partial x_1}(x_0), \dots, \frac{\partial f}{\partial x_N}(x_0)\right) \in \mathbb{R}^N,$$
> detto **gradiente** di $f$ in $x_0$. Altre notazioni: $Df(x) =: \operatorname{grad} f(x) =: \nabla f(x)$ ("nabla di $f$").

Esempio: per $f(x, y) = 2x^3y - y^2 + 3xy$, $Df(x, y) = (6x^2y + 3y,\ 2x^3 - 2y + 3x)$.

> [!warning] Derivabile non implica continua!
> Viene naturale chiedersi se questa derivabilità abbia le proprietà del caso unidimensionale. **Non è così!** La funzione
> $$f(x, y) = \begin{cases} \frac{xy}{x^2 + y^2} & (x, y) \neq (0, 0), \\ 0 & (x, y) = (0, 0) \end{cases}$$
> non ha limite in $(0, 0)$ ([[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Una condizione per la non esistenza del limite|cap. 7]]), quindi non è continua; eppure le derivate parziali esistono:
> $$\frac{\partial f}{\partial x}(0, 0) = \lim_{h\to0} \frac{f(h, 0) - f(0, 0)}{h} = \lim_{h\to0} \frac0h = 0, \qquad \frac{\partial f}{\partial y}(0, 0) = 0.$$
> Le derivate parziali "vedono" la funzione solo lungo gli assi, dove vale identicamente $0$, e non si accorgono di ciò che succede nelle altre direzioni.

D'altra parte la continuità non implica la derivabilità: $f(x, y) = \sqrt{x^2 + y^2} = \|(x, y)\|$ (un cono) è continua ma non derivabile in $(0, 0)$, come $|x|$ in una variabile.

Quindi la derivabilità parziale **non** è la giusta generalizzazione. Per trovarla si ricorda che in una variabile ([[05 - AN1 - Calcolo Differenziale#Il simbolo o-piccolo|Proposizione 5.13]]) sono equivalenti:
1. $f$ è derivabile in $x_0$, cioè il rapporto incrementale converge;
2. esiste $A \in \mathbb{R}$ con $f(x) = f(x_0) + A(x - x_0) + o(x - x_0)$ per $x \to x_0$ (e allora $A = f'(x_0)$).

Generalizzare la (1) non ha dato una proprietà soddisfacente; si segue la (2).

_(dispensa, pp. 122–124)_

### Differenziabilità

Vedi [[Differenziabilità]].

> [!important] Definizione 8.4 — Differenziabilità
> Sia $f : X \subset \mathbb{R}^N \to \mathbb{R}$ e $x_0$ interno a $X$. Se esiste un vettore $A \in \mathbb{R}^N$ con
> $$f(x) = f(x_0) + A \cdot (x - x_0) + o(\|x - x_0\|) \qquad \text{per } x \to x_0$$
> ($\cdot$ è il **prodotto scalare** in $\mathbb{R}^N$), $f$ si dice **differenziabile** in $x_0$.

Differenziabile significa: vicino a $x_0$, $f$ è approssimata da una funzione **lineare** (affine) con un errore che va a zero più velocemente della distanza da $x_0$, **in tutte le direzioni contemporaneamente**.

Osservazioni:
- se $f$ è differenziabile in $x_0$, allora è derivabile in $x_0$ e $A = Df(x_0)$:
$$f(x) = f(x_0) + Df(x_0) \cdot (x - x_0) + o(\|x - x_0\|) \qquad (x \to x_0);$$
- quindi **differenziabilità ⇒ derivabilità**, e come in $\mathbb{R}$ si dimostra che **differenziabilità ⇒ continuità**. Derivabilità e continuità sono condizioni necessarie ma non sufficienti per la differenziabilità;
- per la definizione di o-piccolo, la condizione si riscrive come un limite **in $\mathbb{R}$**:
$$\lim_{x\to x_0} \frac{f(x) - \big(f(x_0) + Df(x_0) \cdot (x - x_0)\big)}{\|x - x_0\|} = 0.$$

### Piano tangente

Il termine lineare fornisce l'equazione
$$z = p(x) = f(x_0) + Df(x_0) \cdot (x - x_0)$$
del **piano tangente** al grafico di $f$ in $x_0$: il piano (più propriamente l'iperpiano) che localmente ha un unico punto di contatto con il grafico. Per $N = 2$:
$$p(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0).$$
È l'analogo della [[05 - AN1 - Calcolo Differenziale#Derivata, definizione e prime proprietà|retta tangente]].

![[AN1-p131-1.png]]

*Figura 77 — Piano tangente.* La superficie $f(x, y)$ (a forma di cupola, sfumata dal giallo al blu) e il piano tangente $p(x, y)$ appoggiato sopra di essa nel punto sopra $(x_0, y_0)$. Vicino al punto di contatto la superficie e il piano quasi coincidono; allontanandosi la superficie si stacca, scendendo sotto il piano.

> [!important] Proposizione 8.5 — Condizione sufficiente per la differenziabilità
> Sia $x_0$ interno a $X$. Se esiste $r > 0$ tale che $f$ è **derivabile con continuità** in $B_r(x_0)$ (le derivate parziali esistono e sono continue in $B_r(x_0)$), allora $f$ è differenziabile in $x_0$.

È spesso più semplice da verificare della definizione: ad esempio tutti i polinomi, e le composizioni di funzioni elementari dove le derivate parziali sono continue, sono differenziabili.

> [!summary] Relazioni tra i concetti (per N > 1)
> ```mermaid
> flowchart LR
>     A["derivabile con continuità (C¹)"] -- "⇒ (non ⇐)" --> B["differenziabile"]
>     B -- "⇒ (non ⇐)" --> C["derivabile parzialmente"]
>     B -- "⇒ (non ⇐)" --> D["continua"]
>     C -. "né ⇒ né ⇐" .- D
> ```
> In una variabile, invece, derivabile = differenziabile.

_(dispensa, pp. 124–125)_

### Derivate direzionali

Vedi [[Derivata direzionale]].

> [!important] Definizione 8.6 — Derivata direzionale
> Siano $x_0$ interno a $X$ e $v \in \mathbb{R}^N$ un **versore** ($\|v\| = 1$). Se esiste
> $$\lim_{h\to0} \frac{f(x_0 + hv) - f(x_0)}{h} =: \frac{\partial f}{\partial v}(x_0) \in \mathbb{R},$$
> $f$ si dice **derivabile nella direzione $v$** in $x_0$, con **derivata direzionale** $\frac{\partial f}{\partial v}(x_0)$. Altre notazioni: $f_v(x_0) = D_v f(x_0)$.

La derivata direzionale è la derivata ordinaria di $F(t) := f(x_0 + tv)$, $t \in \mathbb{R}$, la restrizione di $f$ alla retta per $x_0$ in direzione $v$: dice se $f$ cresce o decresce muovendosi lungo $v$. Se $v = e_i = (0, \dots, 0, 1, 0, \dots, 0)$ (con l'$1$ al posto $i$, $i$-esimo vettore della base canonica), la derivata direzionale coincide con la derivata parziale $\frac{\partial f}{\partial x_i}$.

![[AN1-p132-1.png]]

*Figura 78 — Derivata direzionale.* A sinistra la superficie $z = f(x, y)$ tagliata dal piano verticale che contiene il punto $P_0 = (x_0, y_0)$ e la direzione $v = (v_1, v_2)$ (freccia blu sul piano $xy$), non più parallela a un asse. A destra la curva di taglio $F(t) = f(P_0 + tv)$ vista di fronte: la pendenza della tangente in $t = 0$ è $D_v f(x_0, y_0) = F'(0) = \tan(\varphi)$.

> [!important] Teorema 8.7 — Teorema del gradiente
> Siano $x_0$ interno a $X$ e $v$ un versore. Se $f$ è **differenziabile** in $x_0$,
> $$\frac{\partial f}{\partial v}(x_0) = Df(x_0) \cdot v.$$

In particolare, se $f$ è differenziabile in $x_0$, esistono le derivate direzionali in **ogni** direzione, e si calcolano con un semplice prodotto scalare.

> [!example] Esempio
> $f(x, y) = 2x^3y - y^2 + 3xy$, $v = \left(\frac{1}{\sqrt2}, \frac{1}{\sqrt2}\right)$, $(x, y) = (1, 1)$. Poiché $Df(1, 1) = (6 + 3,\ 2 - 2 + 3) = (9, 3)$:
> $$\frac{\partial f}{\partial v}(1, 1) = (9, 3) \cdot \left(\tfrac{1}{\sqrt2}, \tfrac{1}{\sqrt2}\right) = \frac{9}{\sqrt2} + \frac{3}{\sqrt2} = \frac{12}{\sqrt2} = 6\sqrt2.$$

### Proprietà geometriche del gradiente

**1) Direzione di massima crescita.** Per il teorema del gradiente e la disuguaglianza di Cauchy–Schwarz ($a \cdot v \le \|a\|\|v\|$, con uguaglianza se $v$ è parallelo e concorde ad $a$):
$$\max_{v : \|v\| = 1} \frac{\partial f}{\partial v}(x_0) = \max_{v : \|v\| = 1} Df(x_0) \cdot v = Df(x_0) \cdot \frac{Df(x_0)}{\|Df(x_0)\|} = \|Df(x_0)\|.$$
La derivata direzionale è massima nella direzione del gradiente: **il gradiente $Df$ punta nella direzione di massima crescita di $f$**, e $-Df$ in quella di **massima decrescita**. È l'idea alla base della **discesa del gradiente**, l'algoritmo con cui si addestrano le reti neurali: vedi [[Gradient Descent]] (Machine Learning).

**2) Ortogonalità alle curve di livello.** Si consideri la [[Curve di livello|curva di livello]] per $x_0$, $\Gamma_{f(x_0)} = \{x \in X : f(x) = f(x_0)\}$. Supponendo che sia una curva regolare (potrebbe non esserlo) e detto $\tau$ il versore tangente a $\Gamma_{f(x_0)}$ in $x_0$: $f$ è costante su $\Gamma_{f(x_0)}$, e muoversi lungo $\tau$ corrisponde, a meno di termini di ordine superiore, a muoversi lungo la curva, quindi euristicamente $\frac{\partial f}{\partial \tau}(x_0) = 0$. Per il teorema del gradiente
$$\frac{\partial f}{\partial \tau}(x_0) = Df(x_0) \cdot \tau = 0,$$
e poiché il prodotto scalare è nullo solo per vettori perpendicolari: **$Df(x_0)$ è ortogonale alla curva di livello di $f$ per $x_0$**.

![[AN1-p133-1.png]]

*Figura 79 — Grafico e linee di livello con gradiente.* A sinistra una superficie con una "collina" (rossa) e una "buca" (blu), con le curve di livello disegnate sopra. A destra le stesse curve di livello viste dall'alto, con il campo dei gradienti (frecce): attorno alla collina le frecce puntano verso la cima, attorno alla buca puntano verso l'esterno (in salita), e ogni freccia è perpendicolare alla curva di livello che attraversa. Su una carta topografica, il gradiente indica la direzione di massima pendenza, perpendicolare ai sentieri "in piano".

_(dispensa, pp. 125–127)_

---

## Derivate di Ordine Superiore

> [!important] Definizione 8.8 — Derivate seconde
> Se $f$ è derivabile parzialmente rispetto a $x_i$ e $\frac{\partial f}{\partial x_i}$ è a sua volta derivabile rispetto a $x_j$, si definisce
> $$\frac{\partial}{\partial x_j}\left(\frac{\partial f}{\partial x_i}\right) =: \frac{\partial^2 f}{\partial x_i \partial x_j} =: D^2_{x_i, x_j} f =: f_{x_i x_j}$$
> (**derivata seconda** di $f$ rispetto a $x_i$ e $x_j$), e si continua allo stesso modo con le derivate di ordine superiore.

> [!example] Esempio
> $f(x, y) = 2x^3y - y^2 + 3xy$ ($f_x = 6x^2y + 3y$, $f_y = 2x^3 - 2y + 3x$):
> $$f_{xx} = 12xy, \qquad f_{yy} = -2, \qquad f_{xy} = f_{yx} = 6x^2 + 3.$$

> [!warning] Correzione
> La dispensa scrive $f_{yy}(x, y) = 2$, e di conseguenza riporta $2$ nella hessiana dell'esempio successivo. Ma $f_y = 2x^3 - 2y + 3x$, quindi $f_{yy} = -2$ (deriva dal termine $-y^2$).

Le derivate miste $f_{xy}$ e $f_{yx}$ coincidono. Ci si chiede se l'**ordine** di derivazione conti.

> [!important] Teorema 8.9 — Teorema di Schwarz
> Sia $x_0$ interno a $X$. Se in $x_0$ esistono e sono **continue** entrambe le derivate $\frac{\partial^2 f}{\partial x_i \partial x_j}$ e $\frac{\partial^2 f}{\partial x_j \partial x_i}$, allora coincidono:
> $$\frac{\partial^2 f}{\partial x_i \partial x_j}(x_0) = \frac{\partial^2 f}{\partial x_j \partial x_i}(x_0).$$

Vedi [[Teorema di Schwarz]].

### Matrice hessiana

Vedi [[Matrice hessiana]].

Se $f$ ha in $x_0$ tutte le derivate seconde, si considera la matrice $N \times N$
$$Hf(x_0) = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1 \partial x_1}(x_0) & \frac{\partial^2 f}{\partial x_1 \partial x_2}(x_0) & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_N}(x_0) \\ \frac{\partial^2 f}{\partial x_2 \partial x_1}(x_0) & \frac{\partial^2 f}{\partial x_2 \partial x_2}(x_0) & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_N}(x_0) \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial^2 f}{\partial x_N \partial x_1}(x_0) & \frac{\partial^2 f}{\partial x_N \partial x_2}(x_0) & \cdots & \frac{\partial^2 f}{\partial x_N \partial x_N}(x_0) \end{pmatrix}$$
(nell'$i$-esima riga le derivate seconde fatte prima rispetto a $x_i$ e poi rispetto alle altre variabili, in ordine), detta **matrice di Hesse** o **hessiana** di $f$ in $x_0$. È l'analogo della derivata seconda.

Per il teorema di Schwarz la hessiana è **simmetrica** (se le derivate seconde sono continue): un fatto con conseguenze importanti nella ricerca degli estremi.

> [!example] Esempio
> Per $f(x, y) = 2x^3y - y^2 + 3xy$:
> $$Hf(x, y) = \begin{pmatrix} 12xy & 6x^2 + 3 \\ 6x^2 + 3 & -2 \end{pmatrix}$$
> (con $f_{yy} = -2$, vedi la correzione sopra).

_(dispensa, pp. 127–128)_

---

## Estremi in RN

Vedi [[Estremi in più variabili]].

Si cercano condizioni necessarie e sufficienti per i punti di massimo e minimo locale di $f : \mathbb{R}^N \to \mathbb{R}$, generalizzando il [[05 - AN1 - Calcolo Differenziale#Estremi Locali e il Teorema di Fermat|caso di una variabile]].

> [!important] Definizione 8.10 — Estremi locali
> Sia $f : X \subseteq \mathbb{R}^N \to \mathbb{R}$.
> - $x_0 \in X$ è un **punto di minimo locale** se esiste $r > 0$ con $f(x_0) \le f(x)$ per ogni $x \in X \cap B_r(x_0)$; $f(x_0)$ è un **minimo locale**.
> - $x_0 \in X$ è un **punto di massimo locale** se esiste $r > 0$ con $f(x_0) \ge f(x)$ per ogni $x \in X \cap B_r(x_0)$; $f(x_0)$ è un **massimo locale**.
> - In entrambi i casi $x_0$ è un **punto di estremo locale** e $f(x_0)$ un **estremo locale**.

### Condizioni necessarie

> [!important] Teorema 8.11 — Teorema di Fermat
> Sia $x_0 \in X$ un punto di estremo locale di $f$. Se $f$ è differenziabile in $x_0$ e $x_0$ è **interno** a $X$, allora $Df(x_0) = 0$, cioè
> $$\frac{\partial f}{\partial x_1}(x_0) = 0, \quad \dots, \quad \frac{\partial f}{\partial x_N}(x_0) = 0.$$

(Restringendo $f$ alla retta in direzione $e_i$ si ottiene una funzione di una variabile con un estremo in $0$: per il Fermat unidimensionale la sua derivata, cioè $f_{x_i}(x_0)$, è nulla.) Nel caso $N = 2$ significa che il piano tangente è **orizzontale**.

Osservazioni, simili al caso unidimensionale:
- Fermat vale **solo nei punti interni**: se $x_0$ è un estremo locale ma non è interno, non è detto che $Df(x_0) = 0$;
- se $Df(x_0) = 0$, $x_0$ si dice **punto critico** o **stazionario**;
- la condizione è **necessaria ma non sufficiente**. Ad esempio $f(x, y) = x^2 - y^2$ ha $Df(x, y) = (2x, -2y)$, quindi $(0, 0)$ è critico, ma non è un estremo: $f(x, 0) = x^2$ ha un minimo in $x = 0$, mentre $f(0, y) = -y^2$ ha un massimo in $y = 0$.

![[AN1-p135-1.png]]

*Figura 80 — Grafico di $f(x, y) = x^2 - y^2$.* La sella: lungo l'asse $x$ la superficie sale da entrambe le parti (come $x^2$), lungo l'asse $y$ scende da entrambe le parti (come $-y^2$). Nell'origine il piano tangente è orizzontale, ma il punto non è né un massimo né un minimo: è un **punto di sella** (come il punto più basso di una sella da cavallo nella direzione del cavallo, che è il più alto in quella trasversale).

> [!question] Problema
> Come si stabilisce se un punto critico di una funzione di più variabili è un estremo locale?

In una variabile si usano due metodi: il segno della derivata prima vicino al punto critico, e il segno della derivata seconda (o della prima derivata non nulla) nel punto critico. Si estende il secondo.

_(dispensa, pp. 128–129)_

### Matrici definite

Si indica con $x = \begin{pmatrix} x_1 \\ \vdots \\ x_N \end{pmatrix}$ un vettore colonna e con $x^T$ il suo trasposto (vettore riga).

> [!important] Definizione 8.12
> Una matrice simmetrica $A$ si dice
> - **definita positiva** (**negativa**) se $x^T A x > 0$ ($< 0$) per ogni $x \in \mathbb{R}^N$, $x \neq 0$;
> - **semi-definita positiva** (**negativa**) se $x^T A x \ge 0$ ($\le 0$) per ogni $x \in \mathbb{R}^N$;
> - **indefinita** se esistono $x_1, x_2$ con $x_1^T A x_1 > 0$ e $x_2^T A x_2 < 0$.

$x^T A x$ (la **forma quadratica** associata ad $A$) generalizza il numero $a x^2$: "definita positiva" è l'analogo di "$a > 0$".

> [!example] Esempi
> 1. La matrice **identità** $I$ è definita positiva: $x^T I x = x_1^2 + \ldots + x_N^2 > 0$ per $x \neq 0$. Analogamente $-I$ è definita negativa.
> 2. $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ è **indefinita**: $(1\ 0) A \begin{pmatrix} 1 \\ 0 \end{pmatrix} = 1 > 0$ e $(0\ 1) A \begin{pmatrix} 0 \\ 1 \end{pmatrix} = -1 < 0$. (È la hessiana di $\frac12(x^2 - y^2)$, la sella.)
> 3. $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ è **semi-definita positiva**: $x^T A x = x_1^2 \ge 0$ per ogni $x = (x_1, x_2)$, ma $x^T A x = 0$ per tutti i vettori $x = (0, x_2)$.

### Condizioni sufficienti

> [!important] Teorema 8.13 — Condizioni sufficienti per gli estremi locali
> Siano $f \in C^2(X)$, $x_0 \in X$ un punto critico interno e $Hf(x_0)$ la hessiana in $x_0$. Allora:
> 1. se $Hf(x_0)$ è **definita positiva**, $x_0$ è un punto di **minimo locale**;
> 2. se $Hf(x_0)$ è **definita negativa**, $x_0$ è un punto di **massimo locale**;
> 3. se $Hf(x_0)$ è **indefinita**, $x_0$ **non** è un estremo locale e si dice **punto di sella**.

**Dimostrazione.** Per la formula di Taylor del 2° ordine con resto di Peano, centrata in $x_0$:
$$f(x) = f(x_0) + Df(x_0) \cdot (x - x_0) + \frac12 (x - x_0)^T Hf(x_0)(x - x_0) + o(\|x - x_0\|^2) \qquad (x \to x_0).$$
Poiché $Df(x_0) = 0$:
$$f(x) - f(x_0) = \frac12(x - x_0)^T Hf(x_0)(x - x_0) + o(\|x - x_0\|^2).$$
Vicino a $x_0$ il resto è trascurabile rispetto al termine del 2° ordine, quindi il segno di $f(x) - f(x_0)$ è quello di $(x - x_0)^T Hf(x_0)(x - x_0)$:
1. hessiana definita positiva $\Rightarrow$ $f(x) \ge f(x_0)$ vicino a $x_0$: minimo locale;
2. definita negativa $\Rightarrow$ $f(x) \le f(x_0)$: massimo locale;
3. indefinita $\Rightarrow$ ci sono punti arbitrariamente vicini a $x_0$ in cui $f(x) - f(x_0)$ ha segni opposti: nessun estremo. $\square$

> [!note] Osservazioni
> - Se $Hf(x_0)$ è solo **semi-definita** non si può concludere nulla. Esempi: $f_1(x, y) = x^4 + y^4$ e $f_2(x, y) = -x^4 - y^4$ hanno entrambe un punto critico in $(0, 0)$ con hessiana **nulla** (quindi semi-definita), ma $f_1$ ha un minimo assoluto e $f_2$ un massimo assoluto.
> - Per $N = 1$ il teorema ritrova il [[05 - AN1 - Calcolo Differenziale#Criterio per estremi locali con le derivate successive|criterio della derivata seconda]]: la hessiana è la matrice $1 \times 1$ $(f''(x_0))$, definita positiva (negativa) se $f''(x_0) > 0$ ($< 0$), e semi-definita se $f''(x_0) = 0$; in quest'ultimo caso servono le derivate di ordine superiore. Una matrice $1 \times 1$ non può essere indefinita.

_(dispensa, pp. 129–130)_

### Autovalori e criterio di Hurwitz

Le condizioni della Definizione 8.12 non sono di verifica immediata (bisogna risolvere la disequazione $x^T A x \gtrless 0$ in $N$ variabili). Servono criteri più semplici.

Si ricordi che $\lambda \in \mathbb{C}$ è un **autovalore** di una matrice quadrata $A$ se $\det(A - \lambda I) = 0$. È un'equazione algebrica di grado $N$ in $\lambda$, quindi ha $N$ soluzioni contate con molteplicità. Un risultato importante della teoria delle matrici: una matrice **simmetrica** ha sempre **autovalori reali**.

> [!important] Teorema 8.14
> Sia $A$ simmetrica $N \times N$ con autovalori $\{\lambda_k\}_{k=1}^N$. Allora
> - $A$ è definita positiva $\iff$ $\lambda_k > 0$ per ogni $k$;
> - $A$ è definita negativa $\iff$ $\lambda_k < 0$ per ogni $k$;
> - $A$ è indefinita $\iff$ esistono un autovalore positivo e uno negativo.

Il motivo: in una base di autovettori (che per una matrice simmetrica esiste ed è ortonormale) la forma quadratica diventa $\sum \lambda_k y_k^2$, il cui segno dipende solo dai segni dei $\lambda_k$.

Calcolare gli autovalori richiede però di risolvere $\det(A - \lambda I) = 0$, difficile per $N \ge 3$. Un criterio che richiede solo **determinanti**:

> [!important] Definizione 8.15 — Minori principali
> Data una matrice $N \times N$ $A$, i **minori principali** sono le $N$ sottomatrici $A_k$ formate dalle prime $k$ righe e $k$ colonne:
> $$A_1 = (a_{11}), \quad A_2 = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}, \quad A_3 = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad \dots, \quad A_N = A.$$

> [!important] Proposizione 8.16 — Criterio di Hurwitz
> Sia $A$ simmetrica con minori principali $A_k$. Allora
> - $A$ è definita positiva $\iff$ $\det(A_k) > 0$ per ogni $k = 1, \dots, N$;
> - $A$ è definita negativa $\iff$ $(-1)^k \det(A_k) > 0$ per ogni $k$ (i determinanti alternano segno, partendo negativo).

(È noto anche come criterio di Sylvester.) Per $f : \mathbb{R}^2 \to \mathbb{R}$ si ottiene un metodo molto semplice:

> [!important] Proposizione 8.17 — Estremi di funzioni di 2 variabili
> Siano $f \in C^2(X)$, $X \subset \mathbb{R}^2$, $(x_0, y_0)$ un punto critico interno e $Hf(x_0, y_0)$ la hessiana. Allora
> 1. se $\det Hf(x_0, y_0) > 0$ e $f_{xx}(x_0, y_0) > 0$: **minimo locale**;
> 2. se $\det Hf(x_0, y_0) > 0$ e $f_{xx}(x_0, y_0) < 0$: **massimo locale**;
> 3. se $\det Hf(x_0, y_0) < 0$: **punto di sella**.

| $\det Hf$ | $f_{xx}$ | Natura |
|---|---|---|
| $> 0$ | $> 0$ | minimo locale |
| $> 0$ | $< 0$ | massimo locale |
| $< 0$ | — | sella |
| $= 0$ | — | non si conclude |

Se $\det Hf(x_0, y_0) = 0$ non si può concludere nulla sulla natura del punto critico, e servono altre tecniche.

> [!warning] Correzione
> Nell'osservazione su $\det Hf = 0$ la dispensa scrive che "la matrice hessiana è **indefinita**". Non è corretto: se $\det Hf = 0$ (in due variabili) almeno un autovalore è nullo, quindi la matrice è **semi-definita** (positiva o negativa), oppure nulla. Una matrice indefinita $2 \times 2$ ha invece $\det < 0$ (un autovalore positivo e uno negativo), che è proprio il caso (3). La conclusione ("non si può concludere nulla") è comunque giusta, come mostrano gli esempi $\pm(x^4 + y^4)$.

> [!example] Esempi
> - $f(x, y) = x^2 + y^2$: $Df = (2x, 2y)$, unico punto critico $(0, 0)$, $Hf(0, 0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$. $\det = 4 > 0$ e $f_{xx} = 2 > 0$: minimo locale (anzi assoluto, perché $f(0, 0) = 0 \le f(x, y)$ ovunque).
> - $f(x, y) = x^2 - y^2$: $Df = (2x, -2y)$, unico punto critico $(0, 0)$, $Hf(0, 0) = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, $\det = -4 < 0$: punto di sella.
> - $f(x, y) = 3x^2y + 4y^3 - 3x^2 - 12y^2 + 1$. Il gradiente è
> $$Df(x, y) = (6xy - 6x,\ 3x^2 + 12y^2 - 24y).$$
> Punti critici: dalla prima equazione $6x(y - 1) = 0$. Se $x = 0$, la seconda dà $12y^2 - 24y = 0$, cioè $y = 0$ o $y = 2$. Se $y = 1$, la seconda dà $3x^2 - 12 = 0$, cioè $x = \pm2$. Quindi $(0, 0)$, $(0, 2)$, $(2, 1)$, $(-2, 1)$. La hessiana è
> $$Hf(x, y) = \begin{pmatrix} 6(y - 1) & 6x \\ 6x & 24(y - 1) \end{pmatrix}.$$
>
> | Punto | $Hf$ | $\det$ | $f_{xx}$ | Natura |
> |---|---|---|---|---|
> | $(0, 0)$ | $\begin{pmatrix} -6 & 0 \\ 0 & -24 \end{pmatrix}$ | $144 > 0$ | $-6 < 0$ | massimo locale |
> | $(0, 2)$ | $\begin{pmatrix} 6 & 0 \\ 0 & 24 \end{pmatrix}$ | $144 > 0$ | $6 > 0$ | minimo locale |
> | $(2, 1)$ | $\begin{pmatrix} 0 & 12 \\ 12 & 0 \end{pmatrix}$ | $-144 < 0$ | — | sella |
> | $(-2, 1)$ | $\begin{pmatrix} 0 & -12 \\ -12 & 0 \end{pmatrix}$ | $-144 < 0$ | — | sella |

_(dispensa, pp. 130–132)_
