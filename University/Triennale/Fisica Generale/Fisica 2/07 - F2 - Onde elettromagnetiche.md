---
title: "Onde elettromagnetiche"
aliases:
  - "F2 — Onde elettromagnetiche"
tags:
  - fisica-2
  - capitolo
source: "pdf/Fisica Generale - Elettromagnetismo ( etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "297-334"
---

# Onde elettromagnetiche

> [!abstract]
> Le equazioni di Maxwell prevedono onde che si propagano anche nel vuoto. La luce rientra in questa descrizione: campi trasversali trasportano energia e quantità di moto.
> Percorso del corso: [[MOC - Fisica 2]]. Convenzioni e metodo: [[00 - F2 - Guida allo studio]].

## Equazione delle onde e velocità nel vuoto

Vedi [[F2 - Equazione delle onde e velocità nel vuoto]].

In una regione vuota senza cariche né correnti, applicare il rotore alla legge di Faraday e usare Ampère-Maxwell dà
$$\nabla^2\mathbf E-\mu_0\varepsilon_0\partial_t^2\mathbf E=0,$$
e analogamente per $\mathbf B$. Si è usata l'identità $\nabla\times(\nabla\times\mathbf E)=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E$. La velocità è $c=1/\sqrt{\mu_0\varepsilon_0}\simeq3{,}00\cdot10^8\,\mathrm{m/s}$. Il risultato deriva dalle equazioni del campo e non richiede un mezzo materiale meccanico.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Onde piane e onde monocromatiche

Vedi [[F2 - Onde piane e onde monocromatiche]].

Per propagazione lungo $+x$, una soluzione è $\mathbf E=E_0\cos(kx-\omega t)\hat{\mathbf y}$ con $\omega=ck$. Il campo associato è $\mathbf B=(E_0/c)\cos(kx-\omega t)\hat{\mathbf z}$. In generale
$$\mathbf B=\frac1c\hat{\mathbf k}\times\mathbf E.$$
I campi sono in fase, perpendicolari fra loro e alla propagazione. Questa relazione puntuale vale per l'onda piana progressiva nel vuoto; non è una relazione universale fra campi statici, campi vicini alle sorgenti o sovrapposizioni arbitrarie. Un'onda piana può anche non essere monocromatica.

![[F2-p309-1.png]]

*Figura 7-8: in un’onda piana progressiva i campi elettrico e magnetico oscillano in fase su direzioni ortogonali. La direzione di propagazione è quella del prodotto vettoriale E×B; le curve rappresentano valori del campo, non traiettorie di materia.* _(Libro, p. 301; PDF p. 309.)_

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Polarizzazione

Vedi [[F2 - Polarizzazione]].

La polarizzazione descrive il moto della punta del vettore campo elettrico a posizione fissata. Se resta su una retta, è lineare. Due componenti ortogonali con la stessa frequenza e sfasamento generale producono un'ellisse; con uguale ampiezza e sfasamento $\pm\pi/2$ la polarizzazione è circolare. Componenti in fase o in opposizione danno una retta. Lo stato non si determina dalla sola ampiezza: servono anche fase relativa e orientazioni. Per una luce inizialmente polarizzata linearmente, un analizzatore ideale trasmette $I=I_0\cos^2\theta$.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Energia e vettore di Poynting

Vedi [[F2 - Energia e vettore di Poynting]].

Nel vuoto,
$$u=\tfrac12\varepsilon_0E^2+\frac{B^2}{2\mu_0},\qquad\mathbf S=\frac1{\mu_0}\mathbf E\times\mathbf B.$$
Il teorema di Poynting è $\partial_tu+\nabla\cdot\mathbf S=-\mathbf J\cdot\mathbf E$. L'energia del campo diminuisce per flusso uscente e lavoro sulla materia. Per un'onda piana i contributi elettrico e magnetico a $u$ sono uguali e $S=cu$. Per ampiezza di picco $E_0$, l'intensità media è $I=\tfrac12\varepsilon_0cE_0^2$. Non confondere ampiezza di picco e valore efficace.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Quantità di moto, pressione e spettro

Vedi [[F2 - Quantità di moto, pressione e spettro]].

Un'onda piana trasporta densità di quantità di moto $\mathbf g=\mathbf S/c^2$. A incidenza normale su una superficie ideale la pressione media vale $p=I/c$ per assorbimento totale e $p=2I/c$ per riflessione totale. Sono limiti ideali: angolo, trasmissione e assorbimento parziale modificano il risultato.

La radiazione è prodotta da cariche accelerate; lontano da una sorgente localizzata il campo radiativo decade come $1/r$ e l'intensità come $1/r^2$. Radio, microonde, infrarosso, visibile, ultravioletto, raggi X e gamma appartengono allo stesso spettro elettromagnetico, distinti per frequenza e lunghezza d'onda. La descrizione classica non esaurisce gli scambi quantizzati luce-materia.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Irraggiamento e onde in un mezzo

Vedi [[F2 - Irraggiamento e onde in un mezzo]].

Una carica accelerata genera un contributo radiativo; nel limite non relativistico nel vuoto la potenza di Larmor è $\mathcal P=q^2a^2/(6\pi\varepsilon_0c^3)$. Un dipolo elettrico oscillante irradia con distribuzione angolare proporzionale a $\sin^2\theta$: nessuna radiazione lungo l'asse del dipolo nel modello ideale. La zona radiativa lontana ha comportamento diverso dai campi quasi statici vicini.

In un mezzo omogeneo lineare isotropo non dissipativo e non dispersivo la velocità è $v=1/\sqrt{\mu\varepsilon}$; per mezzi ottici non magnetici $n\simeq\sqrt{\varepsilon_r}$. Se il mezzo è dispersivo, indice, velocità di fase e velocità di gruppo vanno distinti. Alla frontiera la frequenza si conserva per un'interfaccia ferma, mentre cambiano velocità e lunghezza d'onda. Le formule nel vuoto per $E/B$ e per la quantità di moto non si trasferiscono senza analizzare il mezzo.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Derivazione guidata

Per un'onda piana nel vuoto $B=E/c$ e $1/(\mu_0c^2)=\varepsilon_0$. I due contributi all'energia sono quindi uguali: $u=\varepsilon_0E^2$. Il flusso è $S=EB/\mu_0=\varepsilon_0cE^2=cu$. Per un segnale sinusoidale $\langle\cos^2\rangle=1/2$, quindi $I=\varepsilon_0cE_0^2/2$. Se usi $E_{\mathrm{rms}}=E_0/\sqrt2$, la stessa formula diventa $I=\varepsilon_0cE_{\mathrm{rms}}^2$ senza un secondo fattore $1/2$.

_(Libro, cap. 7; pagine stampate 289–326; PDF pp. 297–334.)_

## Esempio svolto

> [!example] Applicazione originale
> Un'onda nel vuoto ha intensità media $I=100\,\mathrm{W/m^2}$. L'ampiezza elettrica è $E_0=\sqrt{2I/(\varepsilon_0c)}\simeq274\,\mathrm{V/m}$; $B_0=E_0/c\simeq0{,}915\,\mathrm{\mu T}$. La pressione su un assorbitore ideale è $3{,}34\cdot10^{-7}\,\mathrm{Pa}$.

## Richiami matematici

[[09 - F1 - Onde meccaniche]] · [[11 - AN1 - Numeri Complessi]] · [[GEO - Prodotto scalare geometrico]].

## Verifica attiva

Se si raddoppia l’ampiezza elettrica di un’onda piana nel vuoto, come cambia l’intensità?

> [!check]- Risposta ragionata
> Si quadruplica, perché è proporzionale al quadrato dell’ampiezza. Raddoppia anche l’ampiezza magnetica, mentre la velocità di propagazione resta c.

## Navigazione

Precedente: [[06 - F2 - Induzione e campi elettromagnetici]] · Successivo: [[MOC - Fisica 2]].
