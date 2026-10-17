---
title: "Risposta armonica e diagrammi di Bode"
aliases:
  - "CA — Risposta armonica e diagrammi di Bode"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "10-16"
class_label: "01/03 (lezione 3 nel manoscritto)"
---

# Risposta armonica e diagrammi di Bode

> [!abstract]
> Questa lezione sviluppa risposta armonica e diagrammi di bode seguendo il blocco delle pagine 10–16 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 01/03 (lezione 3 nel manoscritto). La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[00 - CA - Richiami di Teoria dei Sistemi]]. **Dopo:** [[02 - CA - Interconnessioni e criterio di Nyquist]].

## Dal segnale sinusoidale alla risposta armonica

Vedi [[CA - Risposta armonica]].

Se $u(t)=a\sin(\omega t)$ e il sistema è AS, dopo l'esaurimento del transitorio vale
$$y_{\rm reg}(t)=a|W(j\omega)|\sin(\omega t+\arg W(j\omega)).$$
La frequenza rimane la stessa: il processo modifica ampiezza e fase. Il modulo e la fase come funzioni di $\omega$ costituiscono la risposta armonica. L'ipotesi di stabilità serve a far sparire i modi liberi; sostituire $s=j\omega$ in una FdT instabile non prova l'esistenza di un regime fisico attrattivo.

Si passa a coordinate logaritmiche perché prodotti e rapporti di fattori diventano somme e differenze: $L(\omega)=20\log_{10}|W(j\omega)|$ in decibel (dB). Un fattore 10 vale 20 dB; un fattore 2 vale circa 6.02 dB.

_(Dispensa commentata, pagine PDF 10–12; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 10
> ![[CA-p010-1.jpg]]
> La lezione 3 riparte dalla risposta a sinusoidi: il guadagno può amplificare o attenuare e la fase produce uno sfasamento.

> [!example]- Materiale originale — pagina PDF 11
> ![[CA-p011-1.jpg]]
> La forma di Bode normalizza i fattori; i disegni delle coppie complesse collegano pulsazione naturale, smorzamento e oscillazioni.

> [!example]- Materiale originale — pagina PDF 12
> ![[CA-p012-1.jpg]]
> Il fattore del secondo ordine mostra perché il picco effettivo non è rappresentato completamente dagli asintoti; le annotazioni richiamano il caso sottosmorzato.

## Fattori elementari e somma grafica

Vedi [[CA - Diagrammi di Bode]] · [[CA - Poli e zeri in frequenza]].

Si fattorizza la FdT in forma di Bode, isolando guadagno, integratori e fattori normalizzati. Per un polo reale stabile $1/(1+s/\omega_p)$ il modulo asintotico è 0 dB prima di $\omega_p$ e scende poi di 20 dB/decade; la fase esatta è $-\arctan(\omega/\omega_p)$. Uno zero stabile produce i contributi opposti. Un integratore ha pendenza $-20$ dB/decade e fase $-90^\circ$ a tutte le pulsazioni.

| Fattore | Pendenza dopo la rottura | Fase finale |
|---|---:|---:|
| $1+s/\omega_z$ | $+20$ dB/decade | $+90^\circ$ |
| $1/(1+s/\omega_p)$ | $-20$ dB/decade | $-90^\circ$ |
| coppia di poli stabili | $-40$ dB/decade | $-180^\circ$ |
| $K<0$ | 0 | $\pm180^\circ$ |

> [!example] Sommare i contributi
> Per $W(s)=10/[(1+s)(1+s/10)]$ il diagramma parte da 20 dB, cambia pendenza da 0 a $-20$ a 1 rad/s e a $-40$ a 10 rad/s. A 1 rad/s il modulo esatto è $20-10\log_{10}2-10\log_{10}1.01\simeq16.95$ dB: gli asintoti sono approssimazioni.

Un polo o zero nel semipiano destro ha lo stesso modulo del corrispondente fattore specchiato a sinistra, ma fase diversa. La stabilità non si legge dal solo modulo. Richiamo: [[TDS - Diagrammi di Bode]].

_(Dispensa commentata, pagine PDF 13–14; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 13
> ![[CA-p013-1.jpg]]
> La tabella introduce costante, integratori e fattori reali: sommare i contributi in dB equivale a moltiplicare i moduli.

> [!example]- Materiale originale — pagina PDF 14
> ![[CA-p014-1.jpg]]
> L'esempio somma i fattori sulla stessa scala logaritmica: ogni rottura cambia la pendenza e contribuisce gradualmente alla fase.

## Diagramma polare e fattori del secondo ordine

Vedi [[CA - Diagramma polare]] · [[CA - Risonanza del secondo ordine]].

Il diagramma polare è la curva complessa $W(j\omega)$: il modulo è la distanza dall'origine e la fase è l'angolo. Per coefficienti reali il ramo a frequenze negative è il coniugato del ramo positivo. La curva completa servirà per Nyquist.

Per $W(s)=\omega_n^2/(s^2+2\zeta\omega_ns+\omega_n^2)$, con $0<\zeta<1$, il modulo in $\omega_n$ è $1/(2\zeta)$. Il massimo di risonanza si presenta solo se $\zeta<1/\sqrt2$ e vale
$$\omega_r=\omega_n\sqrt{1-2\zeta^2},\qquad M_r=\frac1{2\zeta\sqrt{1-\zeta^2}}.$$
Il picco non coincide in generale con il valore alla pulsazione naturale. Una coppia poco smorzata può produrre un picco che il diagramma asintotico non mostra.

![[CA-Bode-promemoria.jpg]]
Il promemoria riunisce i fattori: va letto insieme alle formule esatte, soprattutto vicino alle rotture e per poli complessi.

> [!warning] Correzione del promemoria su Bode
> Nell'immagine le pendenze sono annotate come «20°/40°»: l'unità corretta del modulo è **dB/decade**, non gradi. La soglia $\zeta=1/2$ indicata nello schema non è la soglia esatta di esistenza della risonanza: quest'ultima è $1/\sqrt2$. La fase, invece, si misura in gradi o radianti.

_(Dispensa commentata, pagine PDF 15–16; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 15
> ![[CA-p015-1.jpg]]
> Il diagramma polare riunisce modulo e fase in una curva complessa; il ramo a frequenze negative si ricava per coniugio.

> [!example]- Materiale originale — pagina PDF 16
> ![[CA-p016-1.jpg]]
> Le tabelle completano i fattori con ritardo e coppie complesse: un modulo invariato non implica una fase invariata.
