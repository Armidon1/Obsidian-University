È normale che questa definizione risulti un po' ostica a una prima lettura, ma nasconde un concetto geometrico affascinante e fondamentale per comprendere a fondo il comportamento delle reti neurali.

Proviamo a smontare il concetto pezzo per pezzo, visualizzandolo geometricamente.

### 1. La ReLU come "Interruttore"

Ogni neurone in uno strato calcola prima una somma pesata degli input, detta **pre-attivazione** (chiamiamola $z$):

$$z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b$$

Successivamente, applica l'attivazione $\text{ReLU}(z) = \max(0, z)$.

Questo crea due stati netti:

- Se $z \le 0$, il neurone restituisce $0$ (è **spento**).
    
- Se $z > 0$, il neurone fa passare il segnale inalterato restituendo $z$ (è **acceso**).
    

### 2. Il Confine (L'Iperpiano Critico)

Cosa succede nell'istante esatto in cui $z = 0$?

L'equazione $w_1x_1 + w_2x_2 + \dots + b = 0$ in geometria definisce una retta (se siamo in 2D), un piano (in 3D) o, più in generale, un **iperpiano** (in $n$ dimensioni).

Questo iperpiano è una vera e propria "frontiera" che taglia lo spazio degli input in due semispazi: da un lato della frontiera il neurone è acceso, dall'altro è spento. Questo è quello che il testo chiama **iperpiano critico**.

### 3. I Poliedri (Le "Stanze" dello Spazio)

Immagina ora una rete con centinaia o migliaia di neuroni. Ognuno di questi neuroni lancia il proprio iperpiano (la propria "lama") nello spazio degli input.

Tutti questi iperpiani si intersecano e "affettano" lo spazio, frammentandolo in tantissime regioni, come una stanza divisa da pareti di vetro. In geometria, queste regioni delimitate da facce piane prendono il nome di **poliedri** (o politopi).

### 4. La Funzione Affine (Cosa succede dentro una regione)

Prendiamo un punto di input $x$ e muoviamolo **esclusivamente all'interno di una singola regione** (un poliedro), senza mai fargli attraversare un confine.

Poiché non attraversiamo iperpiani, lo stato della rete è "congelato": i neuroni accesi restano accesi e quelli spenti restano spenti.

Dato che la ReLU si comporta semplicemente come $f(z) = z$ per i neuroni accesi (che è lineare) e annulla tutto il resto, l'intera architettura della rete neurale collassa matematicamente. Per tutti i punti all'interno di quello specifico poliedro, la complessa rete profonda si comporta esattamente come una singola operazione matriciale:

$$y = Wx + b$$

Questa è la **funzione affine** menzionata nel testo.

---

### In Sintesi (L'idea della "Piecewise Linear")

Invece di modellare i dati creando curve morbide e continue (come farebbero funzioni di attivazione quali Sigmoide o Tanh), una rete ReLU si comporta come un **mosaico 3D** composto da tante piastrelle rigide e piatte.

- Ogni **piastrella** è una regione (il poliedro), e sopra di essa la rete è solo una semplice equazione lineare (affine).
    
- Le **giunture** tra le piastrelle sono gli iperpiani critici: i punti in cui almeno un neurone fa "click" accendendosi o spegnendosi. Attraversare una giuntura significa cambiare piastrella, e quindi cambiare l'equazione lineare in uso, creando un "punto di rottura" nella pendenza complessiva.
    

L'insieme di tutte queste piastrelle incollate tra loro forma una funzione che è, per l'appunto, **lineare a tratti** (piecewise linear).

## Rappresentazione grafica

![[Pasted image 20260515111352.png]]
### 1. Un Singolo Neurone ReLU: L'Interruttore e il Confine

In alto a sinistra, vedi il meccanismo base.

- Il diagramma del neurone mostra come calcola la pre-attivazione $z$.
    
- Il grafico 2D mostra lo spazio degli input ($x_1, x_2$) diviso esattamente in due da una linea arancione. Questa linea è l'**iperpiano critico** ($z=0$). Da un lato, il neurone è acceso e la funzione cresce linearmente; dall'altro, è spento e la funzione è piatta (zero).
    

### 2. Molti Neuroni: La Frammentazione in Poliedri

In basso a sinistra, vedi cosa succede quando _molti_ neuroni ReLU lavorano insieme.

- Ogni neurone lancia la propria "lama" (il proprio iperpiano critico, qui mostrato come linee di colori diversi).
    
- Questi confini si incrociano, frantumando lo spazio degli input in tante regioni geometriche. Queste regioni piatte e chiuse sono i **poliedri** (o regioni poliedriche). L'ingrandimento mostra come i confini multipli si uniscano per definire queste forme complesse.
    

### 3. La Funzione Complessiva: Un Mosaico 3D di Piani

In alto a destra, vedi il risultato finale: l'intera funzione della rete neurale.

- Nota che la superficie non è una curva morbida, ma assomiglia a un mosaico geometrico 3D rigido (o a un paesaggio a bassa poligonalità).
    
- **Punto A:** Mostra l'interno di un poliedro. Sopra quella specifica "mattonella", la rete è una singola **funzione affine** (piatta, $y = Wx + b$), dove lo stato di tutti i neuroni è "congelato" (on o off).
    
- **Punto B:** Indica una piega nella superficie. Lì si trova l'**iperpiano critico** di almeno un neurone che sta cambiando stato. La piega unisce due mattonelle con diverse pendenze, creando l'effetto **linear a tratti** (piecewise linear).
    

### 4. Sintesi Visiva: Il Mosaico Geometrico

In basso a destra, una breve sintesi del processo: la rete ReLU prende l'input e frammenta lo spazio in un mosaico geometrico 3D rigido. Ogni pezzetto del mosaico è un piano lineare, e la rete li "incolla" insieme lungo i confini critici creati dai singoli neuroni.

---

La rete f(x(t)) lungo questa retta è una funzione piecewise-lineare in t: rettilinea a tratti, con "spigoli" dove qualche neurone cambia stato (si accende o si spegne).

In quei punti t* la prima derivata df/dt ha un kink — è continua ma non differenziabile. La seconda derivata d²f/dt² ha quindi una discontinuità (un picco impulsivo).

![[Pasted image 20260515111600.png]]