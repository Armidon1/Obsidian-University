---
title: "Sistemi termodinamici e temperatura"
aliases:
  - "F1 — Sistemi termodinamici e temperatura"
tags:
  - fisica-1
  - capitolo
source: "pdf/Elementi di Fisica. Meccanica e Termodinamica (Paolo Mazzoldi, Massimo Nigro, Cesare Voci etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
source_pages: "284-309"
---

# Sistemi termodinamici e temperatura

> [!abstract]
> La termodinamica descrive sistemi macroscopici mediante poche variabili di stato. Prima di parlare di calore e lavoro occorre definire equilibrio, temperatura e percorsi fra stati.
> Percorso del corso: [[MOC - Fisica 1]]. Convenzioni e metodo: [[00 - F1 - Guida allo studio]].

## Sistema, ambiente ed equilibrio

Vedi [[F1 - Sistema, ambiente ed equilibrio]].

Un sistema chiuso scambia energia ma non materia; uno isolato non scambia né l'una né l'altra. L'equilibrio termodinamico richiede equilibrio termico, meccanico e chimico compatibili con i vincoli. Le variabili estensive, come volume ed energia, scalano con la quantità di materia; quelle intensive, come temperatura e pressione, no. Un'equazione di stato lega le variabili quando il sistema è all'equilibrio.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Principio zero e scale termometriche

Vedi [[F1 - Principio zero e scale termometriche]].

Il principio zero rende transitivo l'equilibrio termico: se A e B sono separatamente in equilibrio termico con C, sono in equilibrio fra loro. Permette di introdurre una temperatura misurabile con un termometro. Si usa la temperatura assoluta $T$ in kelvin; $T/\mathrm K=t/{}^\circ\mathrm C+273{,}15$. Le differenze di temperatura hanno uguale valore numerico in kelvin e gradi Celsius. La temperatura non misura la quantità totale di energia di un corpo.

![[F1-p290-1.png]]

*Figura 11.4: nel termometro a gas a volume costante si regola il livello del liquido manometrico per mantenere il volume del bulbo. La pressione del gas è la proprietà termometrica da confrontare con uno stato di riferimento.* _(Libro, p. 281; PDF p. 290.)_

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Gas ideale ed equazione di stato

Vedi [[F1 - Gas ideale ed equazione di stato]].

Per un gas diluito lontano dalla condensazione,
$$pV=nRT=Nk_BT.$$
$n$ è la quantità di sostanza, $N=nN_A$ il numero di particelle. Pressione, volume e temperatura non sono indipendenti. La scala assoluta si collega al comportamento limite dei termometri a gas. Le leggi a temperatura, pressione o volume costanti sono casi particolari dell'equazione di stato e non leggi per tutti i materiali.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Calorimetria e cambiamenti di fase

Vedi [[F1 - Calorimetria e cambiamenti di fase]].

Senza cambiamento di fase un piccolo scambio termico in condizioni specificate può scriversi $\delta Q=mc\,dT$; se $c$ è costante, $Q=mc\Delta T$. La capacità termica dipende anche dal processo imposto. In una transizione a pressione fissata si può scambiare calore senza cambiare temperatura: $Q=m\lambda$, con calore latente specifico $\lambda$. Per un calorimetro idealmente isolato si sommano gli scambi delle parti, includendo il calorimetro, e si pone $\sum_iQ_i=0$ se non intervengono altre forme di scambio energetico.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Trasmissione del calore e dilatazione

Vedi [[F1 - Trasmissione del calore e dilatazione]].

La conduzione segue la legge di Fourier $\mathbf j_Q=-\kappa\nabla T$: il flusso termico va verso temperature minori. Per una lastra uniforme in regime stazionario $\mathcal P=\kappa A(T_h-T_c)/\ell$. La convezione trasporta energia mediante moto del fluido; l'irraggiamento avviene anche nel vuoto. Per una superficie grigia ideale in un grande ambiente uniforme $\mathcal P_{\mathrm{netta}}=\epsilon\sigma_{\mathrm{SB}}A(T^4-T_{\mathrm{amb}}^4)$, usando kelvin. Il modello di scambio solido-fluido $\mathcal P=hA(T-T_{\mathrm{amb}})$ è fenomenologico.

Per piccoli intervalli termici $\Delta\ell=\alpha\ell_0\Delta T$; nei solidi isotropi il coefficiente volumico è circa $3\alpha$. Se la dilatazione è impedita nascono sforzi. I coefficienti dipendono dal materiale e dalla temperatura: l'acqua presenta anche intervalli di comportamento anomalo.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Trasformazioni e reversibilità

Vedi [[F1 - Trasformazioni e reversibilità]].

Una trasformazione quasistatica attraversa stati vicini all'equilibrio, così da poter rappresentare un percorso nel piano $p,V$. Per essere reversibile deve inoltre poter essere invertita senza lasciare modifiche nette in sistema e ambiente: attrito, dissipazione e salti finiti di temperatura la rendono irreversibile. Una trasformazione lenta non è per questo automaticamente reversibile. Nei processi rapidi gli stati iniziale e finale possono essere d'equilibrio anche se gli intermedi non ammettono una singola pressione o temperatura del sistema.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Derivazione guidata

Per due corpi senza cambiamenti di fase in un contenitore ideale isolato, il calore ceduto dal caldo deve essere quello assorbito dal freddo: $m_1c_1(T_f-T_1)+m_2c_2(T_f-T_2)=0$. Risolvi per $T_f$ e ottieni una media pesata con pesi dati dalle capacità termiche, non necessariamente dalle masse. Se il recipiente assorbe calore aggiungi $C_{\mathrm{rec}}(T_f-T_{\mathrm{rec},0})$. Se si fonde o evapora materia il bilancio richiede anche il calore latente e una verifica delle fasi finali.

_(Libro, cap. 11; pagine stampate 275–300; PDF pp. 284–309.)_

## Esempio svolto

> [!example] Applicazione originale
> Si mescolano in un recipiente ideale $0{,}20\,\mathrm{kg}$ di acqua a $80^\circ\mathrm C$ e $0{,}30\,\mathrm{kg}$ a $20^\circ\mathrm C$. Assumendo stesso calore specifico costante, nessuna evaporazione e capacità del recipiente trascurabile, $T_f=(0{,}20\cdot80+0{,}30\cdot20)/0{,}50=44^\circ\mathrm C$.

## Richiami matematici

[[03 - AN1 - Funzioni Reali di una Variabile Reale]] · [[06 - AN1 - Calcolo Integrale]].

## Verifica attiva

Scambiare calore implica sempre un cambiamento di temperatura?

> [!check]- Risposta ragionata
> No: durante una transizione di fase all’equilibrio a pressione fissata si può assorbire o cedere calore latente a temperatura costante.

## Navigazione

Precedente: [[10 - F1 - Proprietà meccaniche dei fluidi]] · Successivo: [[12 - F1 - Primo principio della termodinamica]].
