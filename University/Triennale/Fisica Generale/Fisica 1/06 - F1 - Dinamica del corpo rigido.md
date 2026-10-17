---
title: "Dinamica del corpo rigido"
aliases:
  - "F1 — Dinamica del corpo rigido"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "150-193"
---

# Dinamica del corpo rigido

> [!abstract]
> Il corpo rigido è un modello in cui le distanze reciproche restano costanti. La sua dinamica combina traslazione del centro di massa e rotazione, descritta dal momento di inerzia.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Traslazione, rotazione ed equilibrio

Vedi [[F1 - Traslazione, rotazione ed equilibrio]].

Per un corpo rigido valgono le equazioni cardinali $\mathbf F_{\mathrm{ext}}=M\mathbf A_G$ e $\boldsymbol\tau_{G,\mathrm{ext}}=\dot{\mathbf L}_G$. In equilibrio statico sono nulli risultante e momento, e il corpo è inizialmente fermo. La prima condizione da sola non basta: due forze uguali e opposte su rette distinte fanno ruotare il corpo. Il polo per calcolare i momenti si può scegliere in modo da eliminare reazioni incognite, purché si usi la forma appropriata dell'equazione dinamica.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Momento di inerzia e teorema di Huygens-Steiner

Vedi [[F1 - Momento di inerzia e teorema di Huygens-Steiner]].

Rispetto a un asse, con distanza perpendicolare $r_\perp$,
$$I=\sum_i m_ir_{\perp i}^2=\int r_\perp^2dm.$$
Non dipende soltanto dalla massa ma da come è distribuita rispetto all'asse. Per assi paralleli, uno dei quali passa per il centro di massa, $I_O=I_G+Md^2$. Un anello sottile ha $I=MR^2$, un disco omogeneo $I=MR^2/2$ sull'asse centrale; una sbarra omogenea ha $I=ML^2/12$ sull'asse perpendicolare passante per il centro.

![[F1-p165-1.png]]

*Figura 6.22: ogni elemento di massa contribuisce con il quadrato della distanza perpendicolare dall’asse. Nel disegno il simbolo R rappresenta tale distanza locale, non un unico raggio caratteristico del corpo.* _(Libro, p. 156; PDF p. 165.)_

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Rotazione attorno a un asse fisso

Vedi [[F1 - Rotazione attorno a un asse fisso]].

Per un asse fisso la componente assiale soddisfa $\tau_{\mathrm{asse}}=I\alpha$, con $I$ costante. L'energia è $K_{\mathrm{rot}}=I\omega^2/2$, il lavoro $W=\int\tau_{\mathrm{asse}}d\theta$, la potenza $\mathcal P=\tau_{\mathrm{asse}}\omega$. La relazione vettoriale $\mathbf L=I\boldsymbol\omega$ richiede un asse principale: in generale il momento angolare non è parallelo alla velocità angolare. Per la componente lungo l'asse è invece sempre $L_{\mathrm{asse}}=I\omega$.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Rotolamento puro

Vedi [[F1 - Rotolamento puro]].

Nel rotolamento senza slittamento su un piano fermo il punto di contatto ha velocità istantanea nulla. Per una ruota $v_G=\omega R$ e
$$K=\tfrac12Mv_G^2+\tfrac12I_G\omega^2.$$
La direzione dell'attrito statico si ricava dalle equazioni, non si impone sempre contro il moto del centro di massa. In questo modello il suo lavoro totale sul corpo è nullo perché il punto di applicazione è istantaneamente fermo; può però redistribuire energia tra traslazione e rotazione. Va verificato $|F_s|\le\mu_sN$.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Pendolo composto, impulso angolare e precessione

Vedi [[F1 - Pendolo composto, impulso angolare e precessione]].

Per un corpo sospeso a distanza $d$ dal suo centro di massa, $I_O\ddot\theta=-Mgd\sin\theta$. Per piccoli angoli,
$$T=2\pi\sqrt{\frac{I_O}{Mgd}}.$$
Un impulso di momento dà $\Delta\mathbf L=\int\boldsymbol\tau dt$. Nel giroscopio un momento perpendicolare a $\mathbf L$ ne cambia la direzione: nel regime di precessione lenta di una trottola simmetrica $\Omega\simeq Mgd/(I_{\mathrm{spin}}\omega)$. Questa approssimazione non descrive da sola la nutazione generale.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Elasticità dei solidi reali

Vedi [[F1 - Elasticità dei solidi reali]].

La rigidità è un'approssimazione. Nel regime elastico lineare lo sforzo normale $\sigma=F/A$ è proporzionale alla deformazione relativa $\epsilon=\Delta\ell/\ell_0$: $\sigma=Y\epsilon$, con modulo di Young $Y$. Per una sbarra uniforme $\Delta\ell=F\ell_0/(YA)$: a parità di materiale e sezione una sbarra lunga si allunga di più. Il modulo di taglio lega sforzo tangenziale e deformazione angolare, quello di compressibilità lega pressione e variazione relativa di volume. Oltre il limite elastico possono comparire deformazioni permanenti: prolungare linearmente la legge di Hooke non descrive il cedimento.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Derivazione guidata

Per un corpo che rotola da fermo lungo un piano inclinato, scrivi $Ma=Mg\sin\theta-F_s$, $I_G\alpha=F_sR$ e $a=\alpha R$. Eliminando $F_s$ e $\alpha$ trovi $a=g\sin\theta/[1+I_G/(MR^2)]$. L'attrito richiesto è $F_s=I_Ga/R^2$ verso monte; devi infine controllare che non superi $\mu_sMg\cos\theta$. Il solo bilancio di energia dà la velocità in funzione del dislivello, ma non verifica da sé l'aderenza.

_(Libro, cap. 6; pagine stampate 141–184; PDF pp. 150–193.)_

## Esempio svolto

> [!example] Applicazione originale
> Un disco omogeneo rotola da fermo lungo un dislivello $h$ senza dissipazione. Con $I_G=MR^2/2$ e $\omega=v_G/R$, $Mgh=\tfrac34Mv_G^2$, quindi $v_G=\sqrt{4gh/3}$. Una massa che scivola senza attrito avrebbe invece $\sqrt{2gh}$: nel disco parte dell'energia alimenta la rotazione.

## Richiami matematici

[[10 - AN1 - Integrali Multipli]] · [[GEO - Teorema spettrale reale]].

## Verifica attiva

Perché non basta conservare l’energia per garantire il rotolamento puro?

> [!check]- Risposta ragionata
> Perché il vincolo di aderenza richiede un attrito statico disponibile sufficiente. Si calcola la forza richiesta e si verifica il limite $|F_s|\le\mu_sN$.

## Navigazione

Precedente: [[05 - F1 - Dinamica dei sistemi di punti materiali]] · Successivo: [[07 - F1 - Fenomeni di urto]].
