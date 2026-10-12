---
title: La Progettazione Logica
aliases:
  - BD — La Progettazione Logica
tags:
  - basi-di-dati
  - progettazione-logica
  - ristrutturazione
  - traduzione-diretta
  - normalizzazione
source: 6-progettazionelogica.pdf
---

# La Progettazione Logica

> [!abstract]
> La progettazione logica prende lo **schema concettuale** prodotto in [[05 - BD - Progettazione Concettuale]] (diagramma ER + dizionario dei dati + vincoli esterni) e lo traduce in uno **schema relazionale** con vincoli ([[02 - BD - Modello Relazionale]]), pronto per essere scritto in [[03 - BD - SQL|SQL]]. Si articola in tre fasi:
> 1. **ristrutturazione dello schema ER**: si eliminano i costrutti che il modello relazionale non ha (attributi multivalore e composti, ISA, generalizzazioni) e si scelgono gli identificatori principali;
> 2. **traduzione diretta**: un procedimento quasi automatico che trasforma entità e relazioni in tabelle, chiavi, foreign key e vincoli di inclusione;
> 3. **ristrutturazione dello schema logico**: decomposizioni e accorpamenti guidati dal **carico applicativo** per migliorare le prestazioni, fino alla **denormalizzazione**.
>
> Indice dei concetti: [[MOC - Basi di Dati]].

---

## 6.1 Introduzione alla progettazione logica

![[BD-L06-p003.png]]

Le fasi della progettazione: la concettuale riguarda il **"cosa"**, logica e fisica il **"come"**. Annotazione a penna sulla progettazione fisica: "non in questo corso → Data Management" (il corso magistrale).

**Obiettivo**: tradurre lo schema concettuale (ER con vincoli) in uno schema logico che rappresenti **correttamente** i dati del dominio:
- usando il **modello logico del DBMS** scelto (per noi il modello relazionale con vincoli);
- in maniera **corretta, completa ed efficiente**.

Annotazione: lo schema concettuale deve essere corretto; del livello "fisico" non si tiene conto qui.

**Analogia con la compilazione**: lo schema ER sta al modello relazionale come una specifica UML sta al programma in linguaggio macchina. La progettazione logica è la "compilazione" dello schema.

**Ingresso**: schema concettuale (diagramma ER e dizionario dei dati) e **informazioni sul carico applicativo**. **Uscita**: schema logico relazionale, vincoli aggiuntivi, documentazione.

La traduzione ha **due obiettivi**: **mantenere la semantica** dello schema concettuale e **ottimizzare le prestazioni** (annotazione: "ora si ottimizza!!"). Alcune scelte sono fisse, dettate dallo schema ER; altre sono fatte dal progettista per l'efficienza. La metodologia delimita chiaramente i momenti in cui si fanno scelte.

**Fasi della progettazione logica**:
1. **ristrutturazione dello schema ER**: eliminare (mantenendo la semantica) i costrutti non traducibili direttamente, e scegliere gli identificatori principali di entità e relazioni (annotazione: "il modello ER è più ricco: le IS-A non sono traducibili direttamente nel modello relazionale");
2. **traduzione diretta** nel modello relazionale: può essere eseguita in modo (quasi) automatico, tiene conto delle scelte concettuali, e produce uno schema **senza ridondanze**, se non quelle volute;
3. **ristrutturazione dello schema relazionale**: scelte del progettista in base al **carico applicativo** (ottimizzazione).

![[BD-L06-p009.png]]

L'analogia completa: schema concettuale → **schema concettuale ristrutturato** (fedele rappresentazione, come un programma Java rispetto alla specifica) → **schema logico da traduzione diretta** (come un programma in assembler) → **schema logico ristrutturato** (come il linguaggio macchina). Le frecce larghe indicano che ogni passo è una **fedele rappresentazione** del precedente.

---

## 6.2 Ristrutturazione dello schema ER

Vedi [[Ristrutturazione dello Schema ER]].

**Motivazioni**: semplificare la traduzione eliminando i costrutti non traducibili (mantenendo la semantica) e tenere conto dell'**efficienza**. Uno schema ER ristrutturato è uno schema ER **"degradato"** (monco di alcuni costrutti) per avvicinarsi al modello relazionale. Annotazioni: i vincoli esterni del modello ER rimangono e verranno trattati a parte; "noi dovremmo avere una tabella … perdo informazione … non così a caso" (lo schizzo di un'entità con ISA trasformata direttamente in tabella).

| # | Attività |
|---|---|
| 0 | preparazione iniziale dello schema ER |
| 1 | analisi delle ridondanze |
| 2 | eliminazione degli attributi multivalore |
| 3 | eliminazione degli attributi composti |
| 4 | eliminazione delle ISA e delle generalizzazioni |
| 5 | scelta degli identificatori principali di entità e relazioni |
| 6 | specifica degli ulteriori vincoli esterni |

### Attività 0 e 1, preparazione e ridondanze

**Preparazione**: si ridisegna il diagramma aggiungendo i vincoli **rilevanti** che, essendo implicati da altri, non erano indicati (identificatori derivati di entità e di relazioni, tranne quello implicito). Non è necessario riportarli tutti, ma tutti quelli che non si vuole rischiare di ignorare per errore.

**Analisi delle ridondanze**: le ridondanze **intensionali** vanno evitate; una ridondanza **estensionale** prefigura dati significativi ma derivabili da altri (attributi derivabili da altri della stessa entità o di altre entità; relazioni derivabili da cicli di relazioni). Si decide se mantenerle, eliminarle o introdurne di nuove:

| Mantenere una ridondanza | |
|---|---|
| **Vantaggi** | interrogazioni potenzialmente più efficienti |
| **Svantaggi** | gestione dei vincoli aggiuntivi, aggiornamenti più pesanti, più spazio |

La scelta dipende dal carico applicativo; se si mantiene va **documentata** con vincoli. Nel seguito si assume di eliminarle tutte.

### Attività 2, attributi multivalore

Un attributo multivalore (massima > 1) non si traduce in relazionale senza ridondanze inaccettabili: va eliminato.

![[BD-L06-p017.png]]

**Di entità**: si trasforma l'attributo in una **relazione** e il dominio in un'**entità** (la trasformazione a1 di [[05 - BD - Progettazione Concettuale#Trasformazioni dello schema|reificazione]]). `Persona` con `Telefono/Stringa` (1,n) diventa `Persona` (1,n) – `HaTelefono` – (1,n) `Telefono` (Numero). Annotazioni: "si stringe la cardinalità"; "a parte: difficile gestire i telefoni come un numero di persone, la parte schema complessa di telefono ma, poi nel modello si può gestire".

Se la massima è una **costante** $M > 1$ si potrebbe usare $M$ attributi (es. `NumeroDocumentoIdentità` (1,3) → tre attributi (1,1), (0,1), (0,1)), ma è poco usato: introduce attributi e molti valori nulli.

![[BD-L06-p019.png]]

**Di relazione**: qualunque sia la cardinalità $(s,t)$, si trasforma la relazione $R$ in **entità** e l'attributo in relazione verso una nuova entità $H$; anche le relazioni in ISA con $R$ (qui $Q$) diventano entità.

![[BD-L06-p020.png]]

Caso particolare: se l'attributo è $(1,n)$ e tutte le massime dei ruoli sono $n$, l'attributo diventa un'entità $H$ connessa **direttamente** a $R$, che aumenta di grado. Vincolo esterno: per ogni $\langle E{:}e, F{:}f \rangle$ in $Q$ esiste un $h$ con $\langle E{:}e, F{:}f, H{:}h \rangle$ in $R$.

### Attività 3, attributi composti

A questo punto un attributo composto ha cardinalità (1,1) o (0,1).

![[BD-L06-p022.png]]

**Alternativa 1**: si associano i componenti direttamente all'entità. `Indirizzo` (Via, Numero, CAP) diventa tre attributi di Persona. Se l'attributo è (0,1), come `DataMatr` (Giorno, Mese, Anno), diventano `GMatr`, `MMatr`, `AMatr` (0,1) con il **vincolo esterno**: ciascuno è definito se e solo se lo sono gli altri due.

![[BD-L06-p023.png]]

**Alternativa 2**: si trasforma l'attributo in una relazione binaria con una nuova entità: `Persona` (0,1) – `Sposato` – (1,n) `Data` (Giorno, Mese, Anno). Se l'attributo è di una relazione, la relazione va prima trasformata in entità.

### Attività 4, ISA tra entità

Vedi [[Eliminazione delle ISA]].

![[BD-L06-p024.png]]

$E$ ISA $F$ si sostituisce con una **relazione binaria** `ISA-E-F` a cui $E$ partecipa con **(1,1)** e $F$ con **(0,1)**; agli identificatori di $E$ si aggiunge un **identificatore esterno** dato dalla partecipazione a ISA-E-F. Studente ISA Persona diventa `Persona` (0,1) – `ISA-S-P` – (1,1) `Studente`, con Studente identificato tramite ISA-S-P. Annotazioni: "se diventano 2 enti… [le entità] 'alias'"; schizzo di TOP con Persona e Studente.

![[BD-L06-p025.png]]

Esempio di Simone di istanze: $I_1$ dello schema originale ha Persona = {p1, p2}, Studente = {p1}; $I_2$ dello schema ristrutturato ha Persona = {p1, p2}, Studente = {s1}, ISA-S-P = {⟨Studente: s1, Persona: p1⟩}. "p1 alias di s1: ora devo dire che p1 è alias di s1 con la relazione". Schemi completamente diversi **ma isomorfi**: da uno posso ricavare l'altro.

**A livello estensionale**: nello schema ristrutturato $S_r$ tutte le entità sono **disgiunte a coppie**. Nell'istanza $I$ di $S_o$, E = {f1, f2} ⊆ F = {f1, f2, f3}; nell'istanza $J$ di $S_r$, E = {e1, e2} sono oggetti nuovi e ISA-E-F = {(e1,f1), (e2,f2)}.

**Corrispondenza tra istanze**: esistono due funzioni totali $g : \text{istanze}(S_o) \to \text{istanze}(S_r)$ e $h : \text{istanze}(S_r) \to \text{istanze}(S_o)$ con $h(g(I_o)) = I_o$:
- $g$ copia F e A, crea per ogni $x \in E$ un nuovo oggetto $g_E(x)$, mette $(E{:}g_E(x), F{:}x)$ in ISA-E-F e sposta B su $g_E(x)$;
- $h$ ricostruisce E come gli $x \in F$ collegati a qualche $y$ tramite ISA-E-F, e B di conseguenza.

Così si concilia il fatto che in $S_r$ le entità sono disgiunte: e1 ed f1 corrispondono **allo stesso** oggetto f1 di $S_o$.

**Attributi in comune**: se due entità non disgiunte avevano lo stesso attributo A, dopo l'eliminazione delle ISA diventano due funzioni diverse; serve un **vincolo esterno** che imponga lo stesso valore per oggetti che corrispondono allo stesso oggetto originale.

![[BD-L06-p032.png]]

`Impiegato` e `Operaio` ISA `Persona`, entrambi con `Stipendio`. Vincolo esterno: per ogni $p$ in Persona, se esistono $i$ in Impiegato e $o$ in Operaio con $(i,p) \in$ ISA-I-P e $(o,p) \in$ ISA-O-P, allora esiste $s$ con $\langle i, s \rangle$ e $\langle o, s \rangle$ in Stipendio. Annotazione: "se io sono un impiegato e un operaio allora devo avere lo stesso stipendio".

### Attività 4, generalizzazioni

Una generalizzazione di $F$ in $E_1, \dots, E_n$ si tratta come $n$ ISA, con $n$ relazioni ISA-$E_i$-$F$, più i **vincoli di generalizzazione**:
- disgiunzione: ogni istanza di $F$ partecipa **al più a una** delle ISA-$E_i$-$F$;
- se **completa**: ogni istanza di $F$ partecipa **esattamente a una**.

![[BD-L06-p034.png]]

Studente/Docente (non completa): nessuna istanza di Persona partecipa sia a ISA-S-P sia a ISA-D-P. Annotazione: "la tratto come 2 IS-A + vincolo esterno".

![[BD-L06-p035.png]]

Uomo/Donna (completa): ogni istanza di Persona partecipa a ISA-U-P **oppure** a ISA-D-P, ma non a entrambe (annotazione: "disgiunte-completa").

### Attività 4, ISA e generalizzazioni tra relazioni

Si eliminano e si esprimono con **vincoli esterni**.

![[BD-L06-p037.png]]

Se le relazioni insistono sulle stesse entità, il vincolo è immediato: "ogni istanza di Dirige è anche un'istanza di Lavora". Se insistono su entità diverse (Direttore ISA Impiegato, eliminata in ISA-D-I), bisogna tener conto che le entità sono disgiunte: per ogni $(U{:}d, \text{Reparto}{:}r)$ in Dirige, detto $i$ l'impiegato con $(\text{Direttore}{:}d, \text{Impiegato}{:}i)$ in ISA-D-I (esiste ed è unico), $(U{:}i, \text{Reparto}{:}r)$ è in Lavora. Annotazione: "domanda d'esame: quali sono le condizioni per poter stabilire le IS-A tra le relazioni? Devono avere esattamente gli stessi ruoli".

### Attività 5, identificatori principali

Vedi [[Identificatore Principale]].

Si sceglie l'**identificatore principale** di ogni entità e di ogni relazione; deve essere **essenziale**. Annotazione: diventerà la primary key.

**Entità**: ognuna deve avere almeno un identificatore (altrimenti si concorda con gli esperti un **codice**). Criteri: essenzialità, **semplicità** (pochi elementi), uso nelle operazioni più frequenti, preferenza per gli identificatori **interni**, tra gli esterni quelli delle relazioni ISA; se nessuno va bene, si introduce un codice. Nel diagramma il principale si indica con un **cerchio** attorno al pallino.

**Cicli di identificazione esterna**: nel **grafo degli identificatori principali esterni** c'è un arco da $E$ a $F$ se $E$ partecipa a una relazione che fa parte dell'identificatore principale esterno di $F$. Non ci devono essere cicli.

![[BD-L06-p041.png]]

E1 è identificata tramite R1 da E2, E2 tramite R2 da E3/E4, E3 tramite R3 da E1: ciclo E1 → E3 → E2 → E1. Si spezza scegliendo per un'entità del ciclo un altro identificatore principale o, se non c'è, introducendo un **Codice** (qui per E1).

![[BD-L06-p042.png]]

Appunti di Simone: se c'è un ciclo di identificazione **principale** a livello concettuale non c'è alcun problema perché esistono gli object identifier, ma se non ci sono gli object identifier (e non ci saranno dopo) come faccio a identificare le entità? Per identificare E1 devo identificare E3, che a sua volta deve identificare E2, che è legato a E1: ciclo patologico → spezzare il ciclo. "In genere è difficile che succeda, ma ma impossibile". Come si spezza il ciclo? O scegliendo un identificatore principale diverso, oppure introducendo un nuovo modo: parlare con gli esperti di dominio (nella realtà è impossibile che succeda) e modificare lo schema concettuale, oppure inserire qualcosa io. "Spezza il ciclo inventandomi un attributo 'CODICE' e lo identifica come principale". "Se io non rompo il ciclo, non so poi tradurlo nel MR."

![[BD-L06-p043.png]]

Caso significativo: due entità che si identificano a vicenda, `Rettore` (Cognome) – `Di` (1,1)/(1,1) – `Università` (Nome). Si spezza ad esempio scegliendo `Nome` come principale per Università.

**Relazioni**: per ogni relazione che non partecipa a un identificatore principale di entità si sceglie un principale. Criteri: essenzialità, semplicità, uso frequente, per le relazioni da ISA quello sul ruolo dell'entità figlia.
1. Se $R$ partecipa all'identificatore principale esterno di un'entità $E$, l'identificatore di $E$ fa già da identificatore di $R$: nessuna scelta.
2. Se $R$ non partecipa ad alcun identificatore esterno e ha solo l'implicito, l'implicito è il principale (indicarlo è facoltativo).
3. Se $R$ ha identificatori espliciti diversi dall'implicito, se ne sceglie uno (eventualmente l'implicito, che allora va indicato).

![[BD-L06-p047.png]]

Esempio: le operazioni accedono ai direttori per codice, a Responsabilità per città, agli svolgimenti dei progetti per filiale e numero di progetto. Si scelgono Codice per Direttore, Città per Responsabilità, l'implicito per **Svolge** (indicato, altrimenti si interpreterebbe come principale l'unico esplicito, (Anno, Filiale)) e l'implicito per **Riguarda** (non serve indicarlo, non ci sono espliciti). Annotazioni (sulla slide precedente): "Responsabilità ha 1 cerchio Direttore, che ha 2 scelte; Codice è meglio".

### Attività 6, vincoli esterni

- Riformulare i vincoli esterni originari sullo schema ristrutturato, mettendo in evidenza quelli impliciti.
- Aggiungere quelli derivanti dalla ristrutturazione: attributi composti opzionali, attributi comuni di entità figlie, vincoli di generalizzazione (disgiunzione, completezza), identificatori non principali non più rappresentati.

### Esercizi di ristrutturazione

![[BD-L06-p050.png]]

Annotazione: **all'esame** non siamo obbligati a ridisegnare tutto lo schema: possiamo indicare quello che è cambiato.

![[BD-L06-p051.png]]

**Esercizio 3**: ristrutturare lo schema dei voli, con vincoli esterni (1) sull'ordine delle tappe e (2) "un numero di telefono è di una sola sede".

![[BD-L06-p052.png]]

Lo schizzo di Simone: Compagnia – ha – Sede – in – Città, con Sede – HaTelefono (1,n) – Telefono (numero) e Volo (0,1) – ISA-V-VC – (1,1) VoloCharter. Nota: gli identificatori principali li esplicito quando ci sono più identificatori; se è esplicito solamente 1, non faccio il cerchio intorno.

![[BD-L06-p053.png]]

Soluzione: VoloCharter collegato a Volo da ISA-VC-V (1,1)/(0,1); Volo identificato da Codice + Della (principale); l'attributo multivalore Telefono diventa l'entità **Telefono** (Numero) con **TelSede** (1,1) verso Sede (il vincolo 2 diventa interno: ogni telefono ha esattamente una sede); `Sede` diventa un'entità (C-S, S-C) identificata dalla compagnia. Annotazione della slide: l'identificatore di Sede tramite C-S è "non essenziale" (perché C-S con (1,1)/(1,1) già identifica). Rimane il vincolo esterno 1.

![[BD-L06-p054.png]]

**Esercizio 4**: ristrutturare lo schema delle officine.

![[BD-L06-p055.png]]

Lo svolgimento di Simone: Persona con ISA-Dr-P (Direttore: età, AnniAnz) e ISA-Dp-P (Dipendente: AnniAnz), Riparazione con ISA-T-R (Terminata), TelPer – Telefono. Vincoli esterni: riconsegna dopo accettazione; NumDip legato a Lavora; e in rosso il nuovo vincolo: data un'istanza $p$ di Persona che partecipa a ⟨Persona: p, Direttore: d⟩ in ISA-Dr-P e a ⟨Persona: p, Dipendente: dp⟩ in ISA-Dp-P, allora dato un valore $x$ di AnniAnz si ha che ⟨d, x⟩ e ⟨dp, x⟩ sono in istanze(I, AnniAnz).

![[BD-L06-p056.png]]

Soluzione ufficiale, uguale: Telefono diventa entità con TelPer, le ISA diventano ISA-Dr-P, ISA-Dp-P, ISA-T-R; vincoli esterni: riconsegna dopo accettazione, NumDip legato a Lavora, vincolo su AnniAnz derivante dall'eliminazione delle ISA.

### Esercitazione 9

![[BD-L06-p057.png]]

**Esercizio 1 (collaudi di veicoli)**: lo schema concettuale ufficiale e la ristrutturazione di Simone: Collaudo con ISA-P-C e ISA-B-C verso SuPista e SuBanco, Telefono come entità con HaTelefono verso Nazione. Nuovo vincolo esterno: ogni istanza di Collaudo partecipa o alla relazione ISA-P-C oppure ad ISA-B-C; e il vincolo esterno originale riformulato: per ogni istanza I, se ⟨SuPista: P, SuBanco: B⟩ è in Associato, dove ⟨SuPista: P, Collaudo: C1⟩ in ISA-P-C e ⟨SuBanco: B, Collaudo: C2⟩ in ISA-B-C, allora esiste un prototipo P tale che ⟨Collaudo: C1, Prototipo: P⟩ e ⟨Collaudo: C2, Prototipo: P⟩ sono in Relativo.

![[BD-L06-p058.png]]

**Esercizio 2 (permessi di soggiorno)**: lo schema concettuale di Simone (Cittadino con Italiano ed Extracomunitario, Domanda, LavoroOfferto, Città con Capoluogo, Provincia, StatoPresidenza…) con i vincoli esterni (una capoluogo di una provincia appartiene alla provincia; il numero di istanze di CittàResidenza deve essere uguale a NumRes) e la ristrutturazione (ISA-I-C, ISA-E-C, ISA-C-C), con il vincolo di generalizzazione "le istanze di Cittadino partecipano o a ISA-C-I oppure in ISA-E-C". Nota in verde: in Domanda poteva anche esprimersi come relazione tra Extracomunitario, Italiano, LavoroOfferto e Tipo (questa parte di Domanda non tanto: (1,1) legati alla stessa offerta di lavoro).

![[BD-L06-p059.png]]

**Esercizio 3 (vendita di giornali)**: edicole, comuni, province (con le autonome), distributori, quotidiani, contratti, proprietari per anno, persone; e la ristrutturazione di Comune/Provincia/Principale/Autonoma con il vincolo: data ⟨Principale: PR, Provincia: PA⟩ in Capoluogo e ⟨Principale: PR, Comune: C⟩ in ISA-P-C, deve esistere ⟨Comune: C, Provincia: PA⟩ in Appartiene.

---

## 6.3 Traduzione diretta nel modello relazionale

Vedi [[Traduzione Diretta]].

![[BD-L06-p061.png]]

Appunti di Simone: abbiamo visto che $S \to S'$ (ristrutturato) $\to S''$ (schema tradotto). Esistono $\phi_1, \phi_2$ tali che per ogni $I$ di $S$ si ha un $I'$ e viceversa (**isomorfismo**), e $\phi_3, \phi_4$ tra $I'$ e le istanze $I''$ di $S''$ (le "novità"). Per ogni $I''$ posso avere $I$ ma ho perso niente del modello. La base di dati $S''$ è già "buona", ma se la vogliamo ottimizzare: $S'' \to S'''$ (ristrutturata) con $\phi_5, \phi_6$: "magari $S''$ è inefficiente e serve $S'''$, ma corretta per isomorfismo". Ora ci concentriamo su $S' \to S''$.

Lo **schema ristrutturato** ha queste proprietà:
- **preserva la semantica** dell'originale (c'è una corrispondenza tra istanze);
- può contenere ridondanze, ma **volute** e documentate;
- **niente** attributi multivalore, attributi composti, ISA o generalizzazioni, quindi tutte le entità sono **disgiunte a coppie**;
- ogni entità e relazione ha **un unico identificatore principale**.

![[BD-L06-p063.png]]

Appunti: ora ci concentriamo su $S' \xrightarrow{\text{traduzione diretta}} S''$, che è un **algoritmo** (a differenza delle "scelte" di prima). Esempio: $F$ (B1 identificatore principale, B2, B3, B4, B5*) diventa `F(B1, B2, B3, B4, B5*)` con "chiave B3, B4", e poi in `create table` SQL. Punto fondamentale della traduzione: ogni istanza di questo schema concettuale diventa una **tupla di una tabella**. Definizione rigorosa: data una qualsiasi istanza $I$ di $S_2$, ogni oggetto che in $I$ è istanza di un'entità $E$ corrisponde a una tupla di una tabella nell'istanza di uno schema relazionale. Si inizia traducendo le entità e poi le relazioni; c'è il **grafo delle identità**: per tradurre E serve F e G, allora partiamo da F. Da un'istanza di F deve esistere una tupla di F → per ogni entità si ha 1 tabella. Siamo tornati al modello relazionale, dove la primary key è B1, e le chiavi B3, B4 (unique). Il tipo degli attributi viene dal dizionario dei dati; B5 può essere NULL.

![[BD-L06-p064.png]]

Seguito: lo schema ER ci dà una rappresentazione perfetta del mondo a differenza del modello relazionale, per questo partiamo da lui. Ora traduciamo G: `G(C1, C2)`. **Non posso fare E**: perché l'identificatore legato ad A1 è legato anche alla relazione R. Scriverei `E(A1, A2, A3)` con chiave A1, ma manca l'informazione inclusa nella primary key. Come facciamo? **Accorpiamo R ad E**: R non avrà una sua tabella, tutta R è dentro E, perché R contribuisce all'esistenza di E. Mi devo prendere la chiave primaria di G e prenderla come foreign key dentro E, e la chiamo con il nome del ruolo di G. Allora `E(A1, A2, A3, U1, U2, F, D)` con foreign key E[U1] ⊆ G[C1], E[U2] ⊆ G[C1], E[F] ⊆ F[B1], chiave A1 (rimane anche se non è PK); D è l'attributo di R. Nota che il formalismo E[U2] sarebbe la proiezione di E su U2, e che la chiave primaria ora è A3, U1, U2, F. Poi la variante con (1,1) su G (in basso, "supponiamo che"): la foreign key diventa E[U1, U2] ⊆ G[C1, C2]? No: ma dove R? Lo devo cercare dentro E. Com'è mai D non è chiave primaria? Perché D è un attributo ed è semplicemente una cazzo di funzione di R. Se ci fosse stata anche D allora sarebbe stata una superchiave.


![[BD-L06-p065.png]]

Seguito: supponiamo che G partecipi almeno una volta a R, (1,n) sul ruolo U1. Allora è sbagliato lo schema che non prevede questa informazione. Questa cosa è? Un **vincolo su G** che coinvolge E: ogni valore che c'è nell'attributo C1 di G deve essere presente in U1 di E, cioè `inclusione G[C1] ⊆ E[U1]`. **Vincolo di inclusione**: non è una foreign key, simile ma non lo è perché in E U1 non è una chiave. Come esercizio: considerare l'assenza del nuovo vincolo di inclusione e mostrare che esistono istanze del modello relazionale che non esistono in ER. Poi, se E partecipa (1,1) e si toglie l'identificatore che passa per A1: non esistono 2 istanze di E che partecipano ugualmente ad R (non c'è alcuna informazione rilevante su A1, devo ridurre qualcosa).

![[BD-L06-p066.png]]

**Novità**: se U2 di G ha (0,1), allora U2, U1, F è una superchiave; per definizione basta sapere già U2: dire che U2 è una chiave ⇒ ∄ e1, e2 di E t.c. U2 compare 2 volte, vincolo (0,1) violato. Altra novità: se è E ad avere (0,1) verso R e F (1,1)… dobbiamo scegliere tra 2 candidati (U2 e F) per la chiave primaria: si fa in base a quanto suggerito. Due casi: (1) chiave primaria U2 e `chiave F`; (2) chiave primaria F e `chiave U2`. Domanda off-topic: il fatto che io ho vincolo (0,1), non devo mettere l'asterisco? Vale solo se si ha a che fare con un attributo, perché R è una relazione, cioè una funzione. Se esiste una tupla nella tabella E allora esistono tutti i valori di R.

![[BD-L06-p067.png]]

**Ultima novità** (vincolo genuino molto tranquillo): se R ha un identificatore formato da F e dall'attributo D, si aggiunge `chiave F, D`. Abbiamo finito la traduzione delle entità. Facciamo un'applicazione semplice: Persona (CF) con generalizzazione **non completa** in Studente (crediti) e Impiegato (ore). $S'$: ISA-S-P e ISA-I-P; $S''$: `Persona(CF)`, `Studente(CF, Crediti)` foreign key Studente[CF] ⊆ Persona[CF], `Impiegato(CF, ore)` foreign key Impiegato[CF] ⊆ Persona[CF], più il **vincolo di disgiunzione**: Studente[CF] è disgiunto da Impiegato[CF] ("+ vincolo esterno di generalizzazione non completa: nessuna istanza di Persona partecipa sia in ISA-S-P che ISA-I-P"). Se fosse **stata completa**: in più il **vincolo completo**: le istanze di Persona partecipano o a Studente o a Impiegato (ogni istanza di Persona partecipa o in ISA-S-P o in ISA-I-P).

### Notazione

```
Partecipa(Cognome, DataN, Progetto, OreSett, Iva*)
    foreign key: Partecipa[Cognome,DataN] ⊆ Impiegato[Cognome,DataN]
    inclusione:  Partecipa[OreSett] ⊆ Orario[Ore]
    chiave:      Progetto
```

- La chiave primaria è **sottolineata** (qui Cognome, DataN, Progetto).
- `*` indica un attributo che **può essere NULL**; gli altri sono not null.
- Sotto la relazione si elencano i vincoli: **foreign key**, **inclusione** (non verso una chiave), **chiave** (non primaria).
- Il termine **ER-relazione** indica le relazioni dello schema ER, per distinguerle dalle relazioni (tabelle) dello schema logico.

La traduzione consiste di: (1) traduzione delle **entità**; (2) traduzione delle **ER-relazioni**; (3) traduzione dei **vincoli esterni**; (4) riformulazione di **operazioni e carico applicativo**.

### (1) Traduzione delle entità

Ogni entità $E$ diventa una relazione $R_E$ con:
- gli attributi di $E$ (not null, tranne quelli (0,1));
- per ogni ER-relazione $Q$ **accorpata** in $R_E$: le chiavi primarie delle altre entità di $Q$ e gli attributi di $Q$.

Una ER-relazione $Q$ si **accorpa** in $R_E$ quando uno o più suoi ruoli partecipano all'**identificatore principale (esterno)** di $E$ (allora $E$ partecipa a $Q$ con (1,1), ed è l'unica entità per cui ciò accade, per l'assenza di cicli). La chiave primaria di $R_E$ viene dall'identificatore principale di $E$; gli altri identificatori diventano **chiavi** non primarie; la partecipazione obbligatoria si esprime con foreign key o inclusioni.

![[BD-L06-p071.png]]

**Senza accorpamento**: gli attributi opzionali diventano attributi con `*`; l'identificatore principale diventa la chiave primaria, gli altri interni diventano chiavi; i vincoli esterni per attributi composti opzionali diventano **vincoli di tupla**. `E(A1, A2, A3, A4, A5*, A6*)`, chiave A2, A3, vincolo di tupla: A5 è NULL se e solo se A6 è NULL.

```
Impiegato(CodFis, Cognome, DataN, Stipendio, Bonus*)
    chiave: Cognome, DataN
```

![[BD-L06-p073.png]]

**Accorpamento, caso 1**: $R$ è **parte** dell'identificatore principale esterno di $E$ nel ruolo $U$, e negli altri ruoli la cardinalità è (0,n). $R$ si accorpa in $E$: attributi di $R$ e chiavi primarie delle altre entità diventano attributi di $R_E$ e contribuiscono alla sua chiave primaria. `E(A1, A2, A3, F, U1, U2, D)` con le foreign key verso F e (per i ruoli U1, U2) verso G; chiave A1.

![[BD-L06-p074.png]]

Esempio: `Ditta` identificata da Codice + città (`Di`), `Città` identificata da Nome + `In` verso `Nazione`:
```
Ditta(Codice, NomeCit, Nazione, AnnoFond)
    foreign key: Ditta[NomeCit,Nazione] ⊆ Città[Nome,Nazione]
Città(Nome, Nazione, NumAbitanti)
    foreign key: Città[Nazione] ⊆ Nazione[Nome]
Nazione(Nome, Fascia)
```

![[BD-L06-p075.png]]

**Caso 2**: come il caso 1, ma qualche altro ruolo ha cardinalità **(1,n)**: per ognuno si aggiunge un **vincolo di inclusione** dalla chiave dell'entità di quel ruolo verso gli attributi corrispondenti di $R_E$ (`inclusione: G[C1] ⊆ E[G]`). Nell'esempio con Città (1,n) in Di: `inclusione: Città[Nome,Nazione] ⊆ Ditta[NomeCit,Nazione]` (ogni città ha almeno una ditta).

**Caso 3**: $R$ è l'**intero** identificatore principale esterno di $E$ (non solo una parte), con ruoli (1,n): uguale, ma la chiave primaria di $E$ non comprende attributi di $E$.

![[BD-L06-p078.png]]

**Caso 4**: $R$ è identificatore principale di $E$ e in almeno un altro ruolo la massima è **1**: la chiave primaria si sceglie tra le chiavi primarie delle entità con massima 1. Scegliendo quella di F: `E(A1, A2, A3, F, U1, U2, D)` con chiave primaria F, chiave A1, chiave U1; e le foreign key inverse `F[B1] ⊆ E[F]`, `G[C1] ⊆ E[U1]` per le partecipazioni obbligatorie (1,1).

![[BD-L06-p079.png]]

```
Rettore(Cognome, DataN, Inizio, Università)
    foreign key: Rettore[Università] ⊆ Università[Nome]
    chiave: Cognome, DataN
Università(Nome, Città)
    foreign key: Università[Nome] ⊆ Rettore[Università]
```

**Caso 5**: $R$ è identificatore principale di $E$, altri ruoli (1,1), e $R$ ha identificatori propri (anche con attributi): si accorpa, si sceglie G come primaria, e gli identificatori di $R$ diventano chiavi in più (chiave F, D).

![[BD-L06-p081.png]]

**Accorpamento da ISA/generalizzazione**: ISA-E-F è l'identificatore principale esterno di $E$, quindi si accorpa: `E(A1, A2, B1)` con `foreign key: E[B1] ⊆ F[B1]`, chiave A1. In pratica si aggiunge a E la chiave primaria di F, che diventa anche chiave primaria di E: il vincolo ISA diventa una **foreign key**.

```
Studente(Cognome, DataN, Matricola, MediaVoti)
    foreign key: Studente[Cognome,DataN] ⊆ Persona[Cognome,DataN]
    chiave: Matricola
Persona(Cognome, DataN, Indirizzo)
```

![[BD-L06-p083.png]]

Generalizzazione **non completa**: `Persona(CodiceFiscale, Età)`, `Studente(CodiceFiscale, Matricola)` e `Docente(CodiceFiscale, Fascia)` con foreign key verso Persona; il vincolo diventa $\text{Studente}[\text{CodiceFiscale}] \cap \text{Docente}[\text{CodiceFiscale}] = \emptyset$.

![[BD-L06-p084.png]]

Generalizzazione **completa** (Uomo/Donna): in più $\text{Persona}[\text{CodFiscale}] \subseteq \text{Uomo}[\text{CodFiscale}] \cup \text{Donna}[\text{CodFiscale}]$.

### (2) Traduzione delle ER-relazioni

Una ER-relazione **accorpata** non ha una sua tabella: $R_E$ rappresenta sia $E$ sia $Q$ (es. la tabella `Ditta(Codice, Citta, AnnoFond)` rappresenta sia l'entità Ditta sia la ER-relazione Di).

![[BD-L06-p087.png]]

Appunti di Simone sulla traduzione delle relazioni non coinvolte nell'identità delle entità. **Primo caso**: E, F, G con R (ruoli U1, U2 su G, attributo D): R non deve essere accorpata ed ha un proprio identificatore principale, quello implicito. Allora F[B1, B2], E[A1, A2, A3], G[C1, C2], `R[EA1, EA2, F, U1, U2, D]` con le foreign key verso E, F, G (per U1 e U2). Abbiamo detto che R ha un proprio identificatore: quello implicito composto da tutte le chiavi primarie dei partecipanti. **Caso speciale** con G (1,n): G[C1, C2] con `inclusione: G[C1] ⊆ R[U2]`; "U2 NON è una chiave. Se fosse stata così: foreign key"; "almeno un valore U2 in R", "vincolo che insiste su G → vincolo di inclusione su G". **Altro caso**: F (1,1) e G (0,1): schema ristrutturato "+ corretto": "identificatori principali tendiamo a preferire sempre quelli locali"; "sempre prima non accorpa la relazione"; "visto già precedentemente: se esistono 2 istanze di G che partecipano con la stessa istanza di F → ∄ (1,1) vincolo" ; si sceglie in modo casuale; `F(B1, B2)` foreign key F[B1] ⊆ R[F], `R[EA1, EA2, F, U1, U2, D]` chiave F.

![[BD-L06-p088.png]]

**Ultimo caso**: F identificato da R (1,1), "invece qualcosa: ecco", "scelgo questo come prima", "supponiamo che le indicazioni ci dicono che è meglio questo": `F(B1, B2)` foreign key F[B1] ⊆ R[F], `R[EA1, EA2, F, U1, U2, D]` chiave F. Per la stessa motivazione di prima: supponiamo che esistono 2 F che hanno la stessa partecipazione ad R, vuol dire che tutte le altre componenti di R sono identiche, ma questo implica che ci sono 2 istanze di R che hanno stesso E, U1, U2 violando il vincolo di identità → non esistono 2 istanze di R che partecipano ugualmente ad R. Per dimostrarlo possiamo sfruttare la logica $\alpha \Rightarrow \beta \equiv \lnot\beta \Rightarrow \lnot\alpha$ (contronominale), dove $\alpha$ = non esistono 2 istanze di F con la stessa partecipazione ad R e $\beta$ = non esistono 2 istanze di R aventi la stessa combinazione U1, U2, E. Mostriamo $\lnot\alpha$: $\exists F_1, F_2$ in F t.c. ⟨F: F1, E: e1, U1: g1, U2: g2⟩, ⟨F: F2, E: e1, U1: g1, U2: g2⟩ sono istanze di R, ma questo implica $\lnot\beta$. Come volevasi dimostrare. Domanda per la lode: dov'è andato a finire il vincolo ⊕? Poiché in F c'è la foreign key, tutte le istanze di F partecipano ad R, ed in R non possono esserci la stessa combinazione di E, U1, U2 → è implicito.

Ogni ER-relazione $Q$ **non accorpata** diventa una relazione $R_Q$ con:
- gli attributi di $Q$;
- le chiavi primarie delle entità partecipanti (per ogni ruolo), che insieme formano la **superchiave implicita** di $R_Q$.

La chiave primaria viene dall'identificatore principale di $Q$; gli altri identificatori essenziali diventano chiavi; la tipizzazione dei ruoli diventa **foreign key di ruolo** verso le entità; la partecipazione obbligatoria e le ISA tra relazioni diventano foreign key o inclusioni.

![[BD-L06-p090.png]]

**Caso 1**: ER-relazione non accorpata con solo l'identificatore **implicito**: chiave primaria = superchiave implicita, più le foreign key di ruolo. `R(EA1, EA2, F, G, U, D)` con le foreign key verso E, F, G (due volte).

Conviene chiamare gli attributi con il **nome del ruolo**:
```
Impiegato(Cognome, DataN, Stipendio)
Progetto(Nome, Budget)
Partecipa(Cognome, DataN, Progetto, OreSett)
    foreign key: Partecipa[Cognome,DataN] ⊆ Impiegato[Cognome,DataN]
    foreign key: Partecipa[Progetto] ⊆ Progetto[Nome]
```

![[BD-L06-p092.png]]

**Cardinalità minima 1**: diventa un **vincolo di inclusione** dall'entità verso gli attributi del ruolo in $R$ (non una foreign key, perché quegli attributi non sono una chiave di $R$): `inclusione: E[A1,A2] ⊆ R[A1,A2]`, `inclusione: G[C1] ⊆ R[C1]`. Con Partecipa (1,n)/(1,n): `inclusione: Impiegato[Cognome,DataN] ⊆ Partecipa[Cognome,DataN]` e `inclusione: Progetto[Nome] ⊆ Partecipa[Progetto]`.

![[BD-L06-p094.png]]

**Caso 2**: l'identificatore principale **non è** quello implicito. Determina la chiave primaria; se è un solo ruolo e quell'entità ha minima 1, l'inclusione diventa una **foreign key** (perché ora punta a una chiave). Gli altri identificatori diventano chiavi. Nell'esempio F (1,1) identifica R: `chiave: F` e `foreign key: F[B1] ⊆ R[F]`; H (1,n) dà `inclusione: H[D1] ⊆ R[H]`.

Esempi:
```
-- Lavora: Impiegato (0,1), Progetto (1,n)
Lavora(Cognome, DataN, Progetto, Da)              -- chiave primaria: Cognome, DataN
    foreign key: Lavora[Cognome,DataN] ⊆ Impiegato[Cognome,DataN]
    foreign key: Lavora[Progetto] ⊆ Progetto[Nome]
Progetto(Nome, Budget)
    inclusione: Progetto[Nome] ⊆ Lavora[Progetto]
-- se Impiegato è (1,1): Impiegato[Cognome,DataN] ⊆ Lavora[Cognome,DataN] è una foreign key

-- Dirige: Direttore (1,1), Progetto (1,1)
Dirige(Cognome, DataN, Progetto, Da)              -- chiave primaria: Progetto
    chiave: Cognome, DataN
    foreign key: Dirige[Cognome,DataN] ⊆ Direttore[Cognome,DataN]
    foreign key: Dirige[Progetto] ⊆ Progetto[Nome]
Direttore(...)  foreign key: Direttore[Cognome,DataN] ⊆ Dirige[Cognome,DataN]
Progetto(...)   foreign key: Progetto[Nome] ⊆ Dirige[Progetto]
```

![[BD-L06-p098.png]]

Altro esempio di caso 2: il ruolo F identifica l'entità F, quindi gli altri ruoli formano un identificatore derivato di R, scelto come principale; la traduzione è la stessa, con chiave F.

![[BD-L06-p099.png]]

**ER-relazione da ISA non accorpata** (quando l'identificatore principale della figlia non è quello esterno):
```
ISA-S-P(Matricola, Cognome, DataN)
    foreign key: ISA-S-P[Cognome,DataN] ⊆ Persona[Cognome,DataN]
    foreign key: ISA-S-P[Matricola] ⊆ Studente[Matricola]
    chiave: Cognome, DataN
Studente(Matricola, MediaVoti)
    foreign key: Studente[Matricola] ⊆ ISA-S-P[Matricola]
Persona(Cognome, DataN, Indirizzo)
```

**Vincoli derivanti da ISA tra ER-relazioni**: il vincolo esterno "ogni istanza di Q è anche istanza di R" diventa una foreign key o un'inclusione tra le superchiavi implicite: `Q[F,G] ⊆ R[F,G]` (foreign key se ⟨F,G⟩ è chiave di R; inclusione se R ha un'altra chiave, es. con G (0,1) in R e (1,1) in Q, dove Q ha chiave G).

![[BD-L06-p102.png]]

Con le entità diverse (E ISA F eliminata): `Q(U, G)` con `foreign key: Q[U] ⊆ E[A1]` e `foreign key: Q[U,G] ⊆ R[U,C]`: grazie all'accorpamento, la chiave di E è la stessa di F, quindi il vincolo esterno diventa una semplice foreign key.

![[BD-L06-p103.png]]

Appunti: E (K identificatore, A) – R (0,1)/(1,1) – F. "Supponiamo che" E sia identificata da A + R (identificatore non principale): `E(K, A)` con ~~inclusione~~ **foreign key** E[K] ⊆ R[E] (questa perché in R(E), E è una chiave); `R(E, F)`. Manca qualcosa: ma come faccio? Vedo che A dipende solo da E, ma E dipende anche da R, ma non posso accorparli… quindi? **Vincolo esterno**: nel JOIN tra E ed R sulla condizione R.E = E.K, non esistono due tuple con lo stesso valore di A e lo stesso valore di F, cioè la combinazione di A e F forma una chiave nel JOIN.

![[BD-L06-p104.png]]

**Identificatore esterno non principale**: diventa un vincolo esterno **"di join"**. Studente (CodFis principale, Matricola + Iscritto identificatore esterno):
```
Iscritto(Studente, Università, Data)
    foreign key: Iscritto[Studente] ⊆ Studente[CodFis]
    foreign key: Iscritto[Università] ⊆ Università[Codice]
Studente(CodFis, Matricola)
    foreign key: Studente[CodFis] ⊆ Iscritto[Studente]
Università(Codice, AnnoFond)
Vincolo: nell'equi-join tra Studente e Iscritto su CodFis = Studente,
         gli attributi Matricola e Università formano una chiave
```

### (3) e (4) Vincoli e carico applicativo

| Vincolo concettuale | Diventa |
|---|---|
| attributo obbligatorio | `not null` |
| attributi composti opzionali | vincolo di tupla di interdipendenza dei nulli |
| identificatori | chiavi (primarie e non) |
| tipizzazione delle ER-relazioni (anche accorpate), ISA tra ER-relazioni | foreign key |
| generalizzazione | vincoli insiemistici (∩ = ∅, ⊆ ∪) |
| cardinalità minima 1 | inclusione o foreign key verso la relazione dell'ER-relazione |
| cardinalità massima 1 | chiave sulla relazione dell'ER-relazione |
| altre cardinalità, altri vincoli esterni | vincoli esterni (es. di join) |

Le **operazioni** e il **carico applicativo** si riformulano sullo schema logico, tenendo conto di come entità e relazioni sono state tradotte.

> [!summary] Riassunto della traduzione diretta
> 1. Ogni **entità** → una relazione con i suoi attributi, più (accorpando) gli attributi e le chiavi delle ER-relazioni del suo identificatore principale esterno.
> 2. Ogni **ER-relazione** non accorpata → una relazione con le chiavi delle entità partecipanti (con il nome del ruolo) e i suoi attributi.
> 3. **Vincoli**: not null, chiavi, foreign key / inclusioni, generalizzazione, cardinalità (minima 1 → inclusione, massima 1 → chiave), vincoli esterni (di join).
> 4. **Operazioni e carico applicativo** riformulati sullo schema logico.

### Esercizio 5, traduzione dei voli

![[BD-L06-p108.png]]

Lo schema ristrutturato dei voli (esercizio 3) da tradurre. Soluzione:

```
Volo(Codice, Comp, Durata)
    foreign key: Volo[Comp] ⊆ Compagnia[Nome]
    foreign key: Volo[Codice,Comp] ⊆ ArrPart[Codice,Comp]
ArrPart(Codice, Comp, Arrivo, Partenza)
    foreign key: ArrPart[Arrivo] ⊆ Aeroporto[Codice]
    foreign key: ArrPart[Partenza] ⊆ Aeroporto[Codice]
    foreign key: ArrPart[Codice,Comp] ⊆ Volo[Codice,Comp]
    chiave: Comp, Arrivo, Partenza
VoloCharter(Codice, Comp, TipoAereo)
    foreign key: VoloCharter[Codice,Comp] ⊆ Volo[Codice,Comp]
Aeroporto(Codice, Nome)
    foreign key: Aeroporto[Codice] ⊆ LuogoAeroporto[Aeroporto]
LuogoAeroporto(Aeroporto, NomeCittà, NazCittà)
    foreign key: LuogoAeroporto[Aeroporto] ⊆ Aeroporto[Codice]
    foreign key: LuogoAeroporto[NomeCittà,NazCittà] ⊆ Città[Nome,Nazione]
Città(Nome, Nazione, NumAbitanti)
Compagnia(Nome, AnnoFond)
    foreign key: Compagnia[Nome] ⊆ Sede[Comp]
Sede(Comp)
    foreign key: Sede[Comp] ⊆ Compagnia[Nome]
    foreign key: Sede[Comp] ⊆ CittàSede[Comp]
    inclusione: Sede[Comp] ⊆ TelefonoSede[Sede]
CittàSede(Comp, NomeCittà, NazCittà)
    foreign key: CittàSede[Comp] ⊆ Sede[Comp]
    foreign key: CittàSede[NomeCittà,NazCittà] ⊆ Città[Nome,Nazione]
TelefonoSede(Numero, Sede)
    foreign key: TelefonoSede[Sede] ⊆ Sede[Comp]
    foreign key: TelefonoSede[Numero] ⊆ Telefono[Numero]
Telefono(Numero)
    foreign key: Telefono[Numero] ⊆ TelefonoSede[Numero]
Tappa(CodVoloCharter, Comp, Aeroporto, Ordine)
    foreign key: Tappa[CodVoloCharter,Comp] ⊆ VoloCharter[Codice,Comp]
    foreign key: Tappa[Aeroporto] ⊆ Aeroporto[Codice]
Vincolo esterno: per ogni v in Tappa[CodVoloCharter], se o1,…,on sono i valori di Ordine
nelle tuple con v, per i = 1,…,n esiste uno e un solo oj = i.
```

La chiave (Comp, Arrivo, Partenza) di ArrPart viene dall'identificatore esterno non principale di Volo: qui non serve un vincolo di join, perché tutti gli attributi rilevanti sono in ArrPart.

> [!warning] Correzione
> Nella soluzione della slide compare in alcuni punti `TelefonoComp` (in `Sede` e `Telefono`) e in altri `TelefonoSede` per la stessa tabella. Il nome coerente con la relazione `TelSede` dello schema ristrutturato è `TelefonoSede`, usato sopra; nell'esercizio 8 (ristrutturazione dello schema logico) la tabella si chiama invece `TelefonoComp`.

### Esercizio 6, traduzione delle officine

![[BD-L06-p111.png]]

Lo schema ristrutturato delle officine da tradurre. Soluzione:

```
Officina(Nome, NumDip, Indirizzo)
    foreign key: Officina[Nome] ⊆ Dirige[Officina]
    inclusione: Officina[Nome] ⊆ Lavora[Officina]
Persona(CodFis, Indirizzo)
Direttore(CodFis, Età, AnniAnz)
    foreign key: Direttore[CodFis] ⊆ Persona[CodFis]
    foreign key: Direttore[CodFis] ⊆ Dirige[Direttore]
Dipendente(CodFis, AnniAnz)
    foreign key: Dipendente[CodFis] ⊆ Persona[CodFis]
    inclusione: Dipendente[CodFis] ⊆ Lavora[Dipendente]
Dirige(Officina, Direttore)
    foreign key: Dirige[Officina] ⊆ Officina[Nome]
    foreign key: Dirige[Direttore] ⊆ Direttore[CodFis]
    chiave: Direttore
Lavora(Officina, Dipendente, AnniServizio)
    foreign key: Lavora[Officina] ⊆ Officina[Nome]
    foreign key: Lavora[Dipendente] ⊆ Dipendente[CodFis]
TelPer(CodFis, Telefono)
    foreign key: TelPer[CodFis] ⊆ Persona[CodFis]
    foreign key: TelPer[Telefono] ⊆ Telefono[Numero]
Telefono(Numero)
    inclusione: Telefono[Numero] ⊆ TelPer[Telefono]
Veicolo(Targa, Modello, Tipo, AnnoImm)
    foreign key: Veicolo[Targa] ⊆ Possiede[Veicolo]
Possiede(Veicolo, Proprietario)
    foreign key: Possiede[Veicolo] ⊆ Veicolo[Targa]
    foreign key: Possiede[Proprietario] ⊆ Persona[CodFis]
Riparazione(Codice, Officina, OraAcc, DataAcc)
    foreign key: Riparazione[Officina] ⊆ Officina[Nome]
    foreign key: Riparazione[Codice,Officina] ⊆ Relativa[Codice,Officina]
Relativa(Codice, Officina, Veicolo)
    foreign key: Relativa[Codice,Officina] ⊆ Riparazione[Codice,Officina]
    foreign key: Relativa[Veicolo] ⊆ Veicolo[Targa]
Terminata(Codice, Officina, OraRic, DataRic)
    foreign key: Terminata[Codice,Officina] ⊆ Riparazione[Codice,Officina]
Vincoli esterni: riconsegna dopo accettazione; NumDip legato alle istanze in Lavora;
vincolo su AnniAnz di Direttore e Dipendente (dall'eliminazione delle ISA).
```

### Esercitazione 10

![[BD-L06-p114.png]]

**Esercizio 1** (ristrutturazione e traduzione): schema con E (C, B, A) – R (1,1) – F (G, H) – Q (1,1)/(1,n) – M (P, N), e L ISA E con T verso M; per accedere a E si usa prevalentemente C. Svolgimento: C diventa principale di E; ISA-L-E ("poi lui lo accorpiamo a C"); F identificato da H + Q ("invece parte la accorpiamo ad F"). Traduzione:
```
M[P, N]            inclusione M[P] ⊆ F[M]
F[H, M, D*, G]     foreign key F[M] ⊆ M[P]
E[C, B, A]         foreign key E[C] ⊆ R[E]
    vincolo esterno: nel JOIN con E.C = R.E non possono esistere tuple che coincidono
    negli attributi A, FH, FM, cioè {A, FH, FM} è una chiave di R
R[E, FH, FM]       foreign key R[E] ⊆ E[C], R[FH,FM] ⊆ F[H,M]
L[E, S*]           foreign key L[E] ⊆ E[C]
T[L, M, V]         foreign key T[L] ⊆ L[E], T[M] ⊆ M[P]
```

![[BD-L06-p115.png]]

**Esercizio 2 (prestiti bancari)**: la specifica, lo schema concettuale $S$ (Agenzia – Concede – Prestito con giorno/mese/anno, somma, tasso iniziale – Per – Cliente; Prestito – haStatoPrestito – StatoPrestito con data, codice dirigente, variazione), il dizionario dei domini (Ammontare: float ≠ 0), il vincolo esterno (la data di ogni variazione deve essere successiva alla data del prestito) e lo schema ristrutturato $S'$ (identica forma).

![[BD-L06-p116.png]]

Lo schema tradotto $S''$:
```
Agenzia[Codice, Capitale]
Cliente[CF, età, sesso]                  inclusione Cliente[CF] ⊆ Prestito[CF]
Prestito[Giorno, Mese, Anno, CF, Somma, TI]
    foreign key Prestito[Mese,Anno,CF] ⊆ Concede[PMese,PAnno,PCF]
    foreign key Prestito[CF] ⊆ Cliente[CF]
    vincolo di dominio: Giorno 1..31, Mese 1..12
Concede[ACodice, PMese, PAnno, PCF]
    foreign key Concede[ACodice] ⊆ Agenzia[Codice]
    foreign key Concede[PMese,PAnno,PCF] ⊆ Prestito[Mese,Anno,CF]
StatoPrestito[Data, PMese, PAnno, PCF, CodiceDirigente, Variazione]
    foreign key StatoPrestito[PMese,PAnno,PCF] ⊆ Prestito[Mese,Anno,CF]
    vincolo di dominio: Variazione float ≠ 0
Vincolo esterno: nel JOIN (Prestito.Mese = StatoPrestito.PMese AND …)
    ogni data di StatoPrestito deve essere successiva alla data del prestito.
```

![[BD-L06-p117.png]]

**Esercizio 3 (vendite e affitti immobili)**: la specifica, la soluzione ufficiale dello schema concettuale (Agenzia, Transazione con Vendita/Affitto, Città, Ente con Persona/Azienda, Immobile con Ristrutturato/Storico, Ristrutturazione…).

![[BD-L06-p118.png]]

Lo schema ristrutturato $S'$ di Simone (ISA-V-T, ISA-A-T, ISA-P-E, ISA-A-E, ISA-R-I, ISA-S-I…) con i vincoli di generalizzazione (ogni Ente partecipa a ISA-P-E oppure ISA-A-E; ogni Transazione a ISA-V-T oppure ISA-A-T) e l'inizio dello schema tradotto: `Città[Nome, Regione, NumAbitanti]`, `Agenzia[Numero]` con le inclusioni verso Transazione e Sede, `Sede[ANumero, CNome, CRegione]`, `Transazione[Codice, data, valore, ANumero]`, `Vendita[Codice, ANumero, DataPrevendita*]`, `Affitto[Codice, ANumero, Periodo]`, `Immobile[Codice, NumLocali, Indirizzo, mq]`, `Riguarda[TCodice, TANumero, ICodice]`.

![[BD-L06-p119.png]]

Seguito: `Ubicazione`, `Ristrutturato`, `Storico`, `Ente`, `Residenza`, `Persona`, `Nascita`, `Contratto`, `Ristrutturazione`, `Direzione`, `Azienda`, con le foreign key, e gli ulteriori vincoli: Affitto[Codice] ∩ Vendita[Codice] = ∅; Transazione[Codice] = Affitto[Codice] ∪ Vendita[Codice]; Persona[Codice] ∩ Azienda[Codice] = ∅; Ente[Codice] = Persona[Codice] ∪ Azienda[Codice].

![[BD-L06-p120.png]]

**Esercizio 4 (collaudi)**: la specifica, lo schema concettuale e quello ristrutturato ufficiali (con i vincoli: per Associato, l'istanza di ISA-P-C e quella di ISA-B-C si riferiscono a collaudi dello stesso prototipo; ogni Collaudo partecipa ad ISA-P-C oppure ad ISA-B-C ma non a entrambi), e la traduzione di Simone: `Prototipo[Codice, Costo, TempoSvil]`, `Collaudo[Codice, CodiceP, Data, Durata]` con chiave Data…, `SuPista`, `SuBanco`, `Associato[CodiceP, CodiceB]`, `BancoProva[Codice, Qualità]`, `Nazione[Nome]`, `Omologazione[Anno, CodiceB, NNome]`.

![[BD-L06-p121.png]]

Seguito dell'esercizio 4: `Telefono[Numero]` con inclusione verso `haTelefono`, `haTelefono[NNazione, Numero]`, `Intervento[Mese, Anno, CodiceB]`; vincoli esterni: Collaudo[Codice] = SuPista[Codice] ∪ SuBanco[Codice] e SuPista[Codice] ∩ SuBanco[Codice] = ∅, più i vincoli di prima. La ristrutturazione dello schema logico è segnata "DA FARE".

![[BD-L06-p122.png]]

**Esercizio 5 (permessi di soggiorno)**, traduzione diretta: lo schema concettuale ristrutturato ufficiale con i tre vincoli esterni (capoluogo di comune, capoluogo di provincia, generalizzazione completa dei cittadini) e la traduzione di Simone: `Cittadino[CodFis, nome, cognome, DataNascita]`, `Extracomunitario[CodFis, Stato]` (foreign key verso Cittadino, inclusione verso Domanda), `Domanda[Data, CodFis]`, `Italiano[CodFis]`, `Residenza[CodFis, Codice, Sigla]`, `CittàItaliana[Codice, Sigla, NumResidenti]`, `CapoComune[CodiceCittà, SiglaCittà, CodiceCapoluogo, SiglaCapoluogo]`, `TipoLavoro[Codice, Settore]`.

![[BD-L06-p123.png]]

Seguito: `LavoroOfferto[Data, CFExtracomunitario, CFItaliano, CodTipoLavoro, CodCittà, SiglaCittà]` con le foreign key, `Provincia[Sigla, AnnoFond]`, `CapoLuogoProvincia[Codice, Sigla]`, `Valutazione[Sigla, TipoLavoroCodice, Valore]`, `Presidenza[Data, Sigla]`, `Presiede[CodFis, Data, Sigla]`; vincoli esterni: nel join Provincia.Sigla = CapoLuogoProvincia.Sigla non esistono 2 tuple con la stessa CittàItaliana.Codice; se esiste una tupla in CapoComune allora ne esiste una corrispondente; Cittadino[CodFis] = Extracomunitario[CodFis] ∪ Italiano[CodFis] ed Extracomunitario[CodFis] ∩ Italiano[CodFis] = ∅.

![[BD-L06-p124.png]]

**Esercizio 6 (vendita di giornali)**, traduzione diretta: lo schema concettuale ristrutturato ufficiale (Persona, Comune con ComunePrincipale, Provincia con ProvinciaAutonoma, Edicola, Distributore, Quotidiano, Contratto, Proprietà…) con il vincolo esterno "ogni istanza di Capoluogo è anche istanza di Appartiene". Segnato "DA FARE".

---

## 6.4 Ristrutturazione dello schema logico

Vedi [[Ristrutturazione dello Schema Logico]].

Dopo la traduzione diretta:
- si è rispettata la **modularizzazione concettuale**;
- possono esserci problemi di **spazio**: valori nulli (degli attributi opzionali), coppie di relazioni con $R_1[K_1] \subseteq R_2[K_2]$ e viceversa, ridondanze lasciate;
- possono esserci problemi di **tempo** per query e update: ridondanze, numero e struttura delle relazioni.

Servono **buoni motivi di efficienza** per cambiare le scelte; se ci sono, si ristruttura in modo che la base di dati resti **equivalente** a quella della traduzione diretta e sia più efficiente.

![[BD-L06-p125.png]]

Appunti di Simone: **cosa ho bisogno per ottimizzare?** Ho bisogno di sapere come viene usata la base di dati, altrimenti è inutile mettersi ad ottimizzare cose che sono poi inutili (esperti di dominio). Se uno mi dice che una determinata query verrà usata 10 mila volte al secondo, allora dobbiamo ottimizzare qualcosa. All'esame: se per qualche ragione il prof non ci dà alcuna informazione → non facciamo un cazzo. **Prima di iniziare: parliamo del costo.** Il costo asintotico vale nella memoria centrale; per le basi di dati però non parliamo di questo perché i dati non sono nella memoria centrale: **le tabelle sono in memoria secondaria**. Memoria secondaria (disco): quando lavoro con le tabelle, ogni volta che faccio una query o delle istruzioni che modificano una pagina, non lavoro direttamente sulle tabelle ma dalla memoria di archiviazione ottengo prima l'indirizzo di una pagina, sposto una pagina nella memoria centrale, scrivo e sposto nella memoria secondaria questa pagina. Questo mi causa un **enorme tempo** considerando solo uno spostamento da memoria secondaria a principale. Quindi il mio concetto di **costo** non è più quale operazione faccio, **ma quante pagine accedo!** Devo allora ottimizzare le tabelle con **molte pagine**: una pagina contiene tranquillamente un numero piccolo di pagine (circa 300 o 500) [tuple]; devo ottimizzare tabelle con 1 000 000 pagine! Supponiamo di avere tabelle con un elevato numero di attributi (tipo 80) e tantissime tuple (300 mila): quante pagine mi servono? La parola è che servono troppe pagine. La grandissima maggioranza delle query usano o la prima metà degli attributi, o la seconda metà; è molto raro che le utilizzi tutti. Domanda: lascio allora la relazione così? Se non faccio niente io analizzo tutte le pagine. Allora **spezzo la tabella in 2**. Come la spezzo? Devo mantenere una correttezza: serve una relazione di **isomorfismo**. K le chiavi primarie: R (n+2 attributi) → R1 (K, n/2+1 attributi) e R2 (K, n/2+1 attributi), con foreign key R1[K] ⊆ R2[K] e R2[K] ⊆ R1[K]. Per non perdere la correttezza: isomorfismo.

![[BD-L06-p129.png]]

Seguito: l'isomorfismo è verificabile facendo il JOIN R1.K = R2.K ed ottengo R, mentre le proiezioni mi fanno ottenere R1, R2 da R. Attenzione: il lavoro del **data administrator** (un ingegnere informatico che gestisce una base di dati senza controllo con niente gestito e come stanno evolvendo le query nelle basi di dati): supponiamo che stanno diminuendo le query per R1 e R2 perché gli utenti fanno un sacco di R1 JOIN R2, ed allora decide di unirli nuovamente in R senza problemi. **Non introduciamo mai le ridondanze di attributi**: in R1 e R2 non si devono avere attributi in comune (a parte la chiave), altrimenti gli update sono un casino da gestire: aumenta l'overhead per il mantenimento delle tabelle.

### Modello di costo

Vedi [[Modello di Costo]].

- Una relazione occupa un certo numero di **pagine** di memoria secondaria.
- Il numero di **accessi alle pagine** domina sull'elaborazione in memoria centrale; un accesso legge/scrive una **pagina intera**.
- Il numero di pagine accedute dipende da: tipo di operazione, numero di tuple delle relazioni coinvolte, numero di tuple per pagina.

Notazione: $N_P(R)$ = numero di pagine di $R$; $N_{TP}(R)$ = numero di tuple per pagina (annotazione: "si fa a il più possibile").

| Operazione | Costo stimato |
|---|---|
| selezione su $R$ | $N_P(R)$ |
| proiezione su $R$ | $N_P(R)$ |
| join $R \bowtie Q$ senza indici (doppio ciclo sulle pagine) | $N_P(R) \times N_P(Q)$ |
| join se $Q$ ha un indice molto selettivo sull'attributo di join | $N_P(R) + N_P(R) \times N_{TP}(R)$ |

Il secondo caso del join: si leggono tutte le pagine di $R$, e per ogni tupla di $R$ (cioè $N_P(R) \times N_{TP}(R)$ tuple) si accede con l'indice a una pagina di $Q$.

**Criteri per individuare i problemi**:
- relazioni con **tante tuple** → molte pagine; con **tanti attributi** → poche tuple per pagina → molte pagine;
- attributi con **tanti nulli** → spreco di spazio;
- la proiezione è costosa (poche tuple per pagina, eliminazione dei duplicati); il **join** è quasi sempre costoso; la verifica dei vincoli è costosa.

**Conclusione**: per una relazione rilevante conviene tenere basso $N_P(R)$, al limite aumentando $N_{TP}(R)$, cioè **decomponendo** (annotazione: "spezzando la tabella avremo più tuple per pagina"). D'altra parte per evitare join costosi si può **accorpare**.

### Operazioni di ristrutturazione

| Tipo | Variante | Scopo |
|---|---|---|
| **Decomposizione** | verticale (sempre sulla chiave) | facilitare l'accesso (selezioni e proiezioni); normalizzazione |
| | orizzontale | facilitare l'accesso (selezioni) |
| | mista | evitare valori nulli |
| **Accorpamento** | per facilitare l'accesso | evitare join |
| | di relazioni inutili | eliminarle |
| | di attributi inutili | eliminarli |

In tutti i casi le relazioni originarie si ricostruiscono con **viste**. $K$ indica una chiave. Non si considerano operazioni che introducono ridondanze.

### Decomposizione verticale

![[BD-L06-p135.png]]

$R(K, \alpha, \beta) \Rightarrow R_1(K, \alpha), R_2(K, \beta)$ con foreign key reciproche $R_1[K] \subseteq R_2[K]$ e $R_2[K] \subseteq R_1[K]$; i vincoli da/verso $R$ si riformulano su $R_1$ (o $R_2$). Si applica quando $\alpha$ e $\beta$ sono acceduti **separatamente** (annotazione: "concettualmente α è indipendente da β", "lui dovrà essere 2 tabelle separate"). È vantaggiosa perché $N_P(R_1)$ e $N_P(R_2)$ sono minori di $N_P(R)$. $R$ si ricostruisce con il **join** su $K$ (che dovrebbe servire raramente).

> [!example] Immobile
> `Immobile(Codice, Particella, Zona, Indirizzo, Città, Mq, NumVani, Valore)`, con dati catastali e commerciali acceduti separatamente:
> ```
> ImmobileCatasto(Codice, Particella, Zona, Indirizzo, Città)
>     foreign key: ImmobileCatasto[Città] ⊆ Città[Cod]
>     foreign key: ImmobileCatasto[Codice] ⊆ ImmobileComm[Codice]
> ImmobileComm(Codice, Mq, NumVani, Valore)
>     foreign key: ImmobileComm[Codice] ⊆ ImmobileCatasto[Codice]
> Agenzia(CodiceAg, Immobile)
>     foreign key: Agenzia[Immobile] ⊆ ImmobileCatasto[Codice]
> ```
> Annotazione: "riformulata la vecchia foreign key".

### Decomposizione orizzontale

![[BD-L06-p137.png]]

Le tuple di $R$ si dividono in "fasce" $R_1$ e $R_2$ con lo stesso schema. Se le fasce sono disgiunte: $R_1[K_1] \cap R_2[K_1] = \emptyset$. Le inclusioni **da** $R$ diventano inclusioni da $R_1$ e da $R_2$; quelle **verso** $R$ diventano verso $R_1 \cup R_2$. Si applica quando le due fasce sono accedute separatamente. $R$ si ricostruisce con l'**unione**.

> [!example] Telefonate per fascia oraria
> `Telefonata(Codice, OrarioInizio, OrarioFine, UtenzaInvio, UtenzaDestinazione)` acceduta per fascia (giorno, sera, notte): due decomposizioni orizzontali in cascata danno `TelefonataGiorno`, `TelefonataSera`, `TelefonataNotte` (stesso schema e foreign key verso Utenza), e il vincolo esterno
> $$\text{Centrale}[\text{Telefonata}] \subseteq \text{TelefonataGiorno}[\text{Codice}] \cup \text{TelefonataSera}[\text{Codice}] \cup \text{TelefonataNotte}[\text{Codice}]$$

### Decomposizione mista

![[BD-L06-p139.png]]

Per eliminare i nulli in $A^*$: decomposizione verticale in $R_1(K, A)$ e $R_2(K, \beta)$, poi orizzontale su $R_1$ eliminando la parte con $A$ NULL, che diventa inutile. Vincoli: $R_1[K] \subseteq R_2[K]$; inclusioni da/verso $R$ diventano da/verso $R_2$. $R$ si ricostruisce con il **join esterno** tra $R_1$ e $R_2$ su $K$ (annotazione: "con il join esterno posso ritornare da R1 e R2 a R").

> [!example] Persona senza nulli
> `Persona(CodFiscale, CittàNascita, NumTel*, DataMatrimonio*)` diventa
> ```
> Persona(CodFiscale, CittàNascita)
> PersonaConTelefono(CodFiscale, NumTel)
>     foreign key: PersonaConTelefono[CodFiscale] ⊆ Persona[CodFiscale]
> PersonaSposata(CodFiscale, DataMatrimonio)
>     foreign key: PersonaSposata[CodFiscale] ⊆ Persona[CodFiscale]
> ```

### Accorpamento caso 1, tabelle fortemente accoppiate

$R_1(K_1, \alpha)$ e $R_2(K_2, \beta)$ con foreign key **reciproche** $R_1[K_1] \subseteq R_2[K_2]$ e $R_2[K_2] \subseteq R_1[K_1]$ (tabelle **fortemente accoppiate**) diventano $R(K, \alpha, \beta)$. È l'inverso della decomposizione verticale; si applica quando $R_1$ e $R_2$ sono accedute insieme, per **evitare il join**. Le originali si ricostruiscono con proiezioni; se manca $\beta$, serve a eliminare una relazione inutile.

![[BD-L06-p142.png]]

Appunti di Simone: osservazione. E (K identificatore principale) – (1,1) R – F (H): si traduce con l'accorpamento di R in E. Oppure E (K) – (1,1) R – F (H) senza che R sia nell'identificatore: il 99% dei testi di Basi di Dati prefigurano la traduzione di questo schema accorpando R ad E, facendolo solo per (1,1). Perché accorparla anche se non c'è alcun identificatore principale? Ad esempio in questo modo. Secondo molti testi: `E(K, A, F)` foreign key E[F] ⊆ F[H], `F(H, B)`: **sbagliato**. Secondo la nostra metodologia: `E[K, A]`, `F[H, B]`, `R[E, F]` con foreign key R[E] ⊆ E[K] e R[F] ⊆ F[H]: **OK**. Perché? Altri testi dicono così: tradireste il vostro professore per 4 soldi? MAI. Perché? Se io applicassi la metodologia degli altri testi ed avessi 80 relazioni (1-1) ⇒ mi esce una cazzo di tabella E colossale con 80 attributi. Inoltre, se io volessi eliminare una relazione qualsiasi di E, è un casino. Molto meglio così che sono **concettualmente separati**. "NOI TRADIAMO LA PROGETTAZIONE CONCETTUALE SOLO QUANDO C'È QUALCHE MOTIVO PER L'EFFICIENZA. ALLORA ACCORPO LE RELAZIONI CHE POSSONO MIGLIORARE L'EFFICIENZA (MA NON IN GENERALE TUTTE LE RELAZIONI COME DICONO I TESTI)." In generale allora uso la metodologia del prof e se si scopre che è necessaria qualche ottimizzazione, allora dopo accorpo qualche relazione.

![[BD-L06-p143.png]]

**Caso 1 (fortemente accoppiate)**: Persona (KP) – (1,1) Nascita – Città (KC, Regione). Le tabelle Persona, Nascita, Città: Persona e Nascita sono derivate dalla stessa chiave e si dicono **fortemente accoppiate**. In questo caso quasi sempre gli utenti fanno un cazzo di join tra queste tabelle: non ci piace! Spreco di prestazioni!! Accorpa Persona con Nascita → Persona(KP, …, Città) – Città. Così non ho più Nascita. Come faccio a recuperarla? Faccio la proiezione Persona[KP, Città]! Come faccio a sapere che non ho perso nessuna informazione con questo accorpamento? Mi creo una vista che rappresenta la vecchia tabella Nascita a partire da Persona: `Vista Nascita(KP, Città) as select KP, Città from Persona` (proiezione). È meglio questo schema? Dipende: se l'utente non fa più i JOIN ok, però anche che ha fatto un accorpamento tra Persona–Nascita e non Persona–Città! Mi perdo l'attributo Regione. **Caso 2 (debolmente accoppiate)**: Persona – Nascita – Città e Persona (0,1) – Lavora – Azienda (KA). "Ci interessa questo": tabelle Persona, Lavora(KP, KA), Azienda.

![[BD-L06-p144.png]]

Le tabelle **non** sono fortemente accoppiate: **debolmente accoppiate**. Non siamo nelle stesse condizioni di prima. Supponiamo che però l'utente voglia fare il Persona JOIN Lavora. Però mi perderei delle tuple di Persona perché non tutte le persone lavorano. Comunque possiamo pensare ad un accorpamento tra Persona e Lavora: Persona(KP, …, Città, KA*) — "persona esserci NULL". Qual è la vista che mi ricostruisce Lavora? Il join come prima: `Vista Lavora(KP, KA) as select KP, KA from Persona where KA is not NULL`. Supponiamo che Lavora abbia un attributo AnnoInizio: quando accorpo Persona e Lavora, AnnoInizio va a finire su Persona: Persona(KP, …, Città, KA*, AnnoInizio*) — "necessita di un vincolo di tupla" (domanda d'esame): **vincolo di tupla**: KA IS NULL se e solo se AnnoInizio IS NULL.

![[BD-L06-p147.png]]

**Esempio 1**: Persona (CFis, Età) – Residenza (1,1) – Città (Cod, Regione) (1,n). Se quando si accede a una persona si accede spesso anche alla città di residenza (annotazione: "indicazione importante"), si accorpano Persona e Residenza:
```
Persona(CFis, Età, Città)   foreign key: Persona[Città] ⊆ Città[Cod]
Città(Cod, Regione)         inclusione: Città[Cod] ⊆ Persona[Città]
```

![[BD-L06-p148.png]]

**Esempio 2**: Rettore – Di (1,1)/(1,1) – Università. Accedendo all'università si accede sempre al rettore: si accorpano Università e Di (`Università(Nome, Città, Rettore)`, chiave Rettore). Se accedendo al rettore si accede sempre ai dati della sua università, un ulteriore accorpamento dà `UniversitàRettore(NomeUniversità, CittàUniversità, CognomeRettore, EtàRettore)` con chiave CognomeRettore.

### Accorpamento caso 2, tabelle debolmente accoppiate

$R_1(K_1, \alpha)$ e $R_2(K_2, \beta^*)$ con una **sola** foreign key $R_2[K_2] \subseteq R_1[K_1]$ (**debolmente accoppiate**) diventano $R(K, \alpha, F, \beta^*)$, dove $F$ è un **flag** booleano che vale true per le tuple che erano in $R_2$. Se $\beta$ è not null in $R_2$, $F$ è ridondante ($F$ true ⇔ $\beta$ non null). Vincolo: se $F$ è false allora $\beta$ è NULL. Le originali si ricostruiscono con proiezioni (per $R_2$ solo le tuple con $F$ true).

![[BD-L06-p150.png]]

Persona (Codice, DataN) – ISA-S-P – Studente (mediavoti) – Iscrizione – CorsoLaurea. Accedendo a uno studente si vuole sapere la data di nascita, e accedendo a una persona la media se è studente: si accorpa Studente in Persona.
```
Persona(Codice, DataN, mediavoti*)
    inclusione: SEL_{mediavoti is not null} Persona[Codice] ⊆ Iscrizione[Studente]
Iscrizione(Studente, CorsoLaurea)
    inclusione: Iscrizione[Studente] ⊆ SEL_{mediavoti is not null} Persona[Codice]
```
Il flag non serve: basta la condizione "mediavoti is not null".

![[BD-L06-p151.png]]

Se `mediavoti` è **opzionale** anche per gli studenti, il flag serve: `Persona(Codice, DataN, flag, mediavoti*)`, vincolo di tupla "se flag = false allora mediavoti IS NULL", e le inclusioni con $\text{SEL}_{\text{flag} = \text{true}}$.

### Accorpamento casi 3 e 3a, accorpamento orizzontale

![[BD-L06-p152.png]]

$R(K, \alpha)$ con più tabelle debolmente accoppiate $R_1(K_1, \beta_1), \dots, R_n(K_n, \beta_n)$ (foreign key $R_i[K_i] \subseteq R[K]$) diventano $Q(K, \alpha, T, \beta_1^*, \dots, \beta_n^*)$: l'inverso della decomposizione orizzontale. $T$ (tipo) è un vettore di $n$ booleani o un enumerato con $2^n$ valori (uno per combinazione di appartenenza). Vincoli che legano $T$ ai nulli in $\beta_i$.

![[BD-L06-p153.png]]

**Caso 3a**: le $R_i[K_i]$ sono **disgiunte** a coppie: $T$ assume solo i valori $1, \dots, n$ (bastano $\log n$ bit).

![[BD-L06-p154.png]]

Esempio: Persona con Studente (mediavoti*) e Lavoratore (stipendio*), disgiunti. Accorpandoli: `Persona(Codice, DataN, Tipo, mediavoti*, stipendio*)` con vincolo di dominio "Tipo assume valori 'studente' o 'lavoratore'" e vincoli di tupla "se mediavoti is not null allora Tipo = 'studente'", "se stipendio is not null allora Tipo = 'lavoratore'".

> [!note] Nota
> Nello schema logico della traduzione diretta di questa slide c'è `foreign key: Lavoratore[Studente] ⊆ Persona[Codice]`: si intende `Lavoratore[Codice]`. Inoltre in questo esempio una persona può non essere né studente né lavoratore, quindi a rigore Tipo dovrebbe ammettere anche un terzo valore (o essere nullo).

![[BD-L06-p145.png]]

Appunti di Simone sul **caso 3** (debolmente accoppiate): Persona con ISA-S-P (Studente: AnnoCorso) e ISA-I-P (Impiegato: Salario), vincoli esterni per garantire la disgiunzione di impiegato e studente ("solo disjoint"); traduzione in Persona, Studente(KP, AnnoCorso), Impiegato(KP, Salario): sono 2 tabelle debolmente accoppiate. Supponiamo che il mio carico applicativo sia tale da dirmi che ogni volta che l'utente accede a Persona vuole sapere se è uno studente oppure un impiegato o nessuno dei due, e vuole sapere anche AnnoCorso o Salario. Allora facciamo 2 accorpamenti!! Persona(KP, …, TIPO, AnnoCorso*, Salario*), TIPO ∈ [0, 1, 2]: una casella mi dice se una tupla è uno studente, impiegato o nessuno dei due, con **vincolo di tupla**: se TIPO = 0 ⇒ Salario = NULL AND AnnoCorso = NULL; se TIPO = 1 ⇒ Salario ≠ NULL AND AnnoCorso = NULL; se TIPO = 2 ⇒ Salario = NULL AND AnnoCorso ≠ NULL. Se ho relazioni **disgiunte** ho che il tipo richiede $2^k$ valori possibili (cioè k bit), mentre se non sono disgiunte comunque ho $2^k$ possibilità. **Caso 4 (lascamente accoppiate)**: Persona (KP) – (1,1) Nascita – Città (KC, Regione). Supponiamo che abbiamo già accorpato Persona e Nascita: Persona(KP, …, Città) e Città(KC, Regione). Supponiamo che l'utente vuole sempre conoscere la Regione, ma Regione **non** è una proprietà di Persona: Regione è una proprietà di Città. 1) Le tabelle sono fortemente accoppiate? No (annota). 2) Debolmente? No. Attenzione!

> [!warning] Correzione
> Negli appunti, per il caso con TIPO, i casi 1 e 2 sono scambiati rispetto all'esempio (TIPO = 1 con Salario non nullo dovrebbe corrispondere all'impiegato), ma la logica è coerente se si fissa la convenzione. Più importante: con relazioni **disgiunte** bastano $k + 1$ valori (nessuno, oppure una delle $k$ tabelle), cioè circa $\log_2(k+1)$ bit, come dice la slide 3a ("bastano log n bits"); i $2^k$ valori servono solo se le tabelle **non** sono disgiunte.

![[BD-L06-p146.png]]

Seguito: perché no? Si dice che sono accoppiate quando entrano in gioco **solo le chiavi**. Città in Persona non è una chiave, ma viene richiesto di accoppiarle con un attributo non chiave. Come le chiamiamo? **LASCAMENTE ACCOPPIATE**. Questo ragionamento va bene anche con attributo città con asterisco. Mettiamo Regione dentro Persona: Persona(KP, …, Città, Regione) e Città(KC, Regione), con **foreign key** Persona[Città, Regione] ⊆ Città[KC, Regione]: **accorpamento per denormalizzazione**. Lo chiamo foreign key anziché inclusione perché in Città[KC, Regione] è una superchiave (annotazione: "va bene anche se è super"). Va detto che da una parte è costoso perché io devo considerare che il vincolo di foreign key non è gratis: se inserisco una persona devo inserire anche più informazioni → più costo per aggiornamenti. Favorisce le query a scapito degli aggiornamenti. Commento: nell'epoca del **machine learning** le relazioni sono spesso denormalizzate perché nell'applicazione del data mining ecc. estraggono dalla base di dati una stata della base di dati e fanno un'analisi su quella stata. Cioè spesso nel machine learning si lavora con basi di dati che non verranno più aggiornate. **Caso 5**: una tabella inutile → quando è fortemente accoppiata con una tabella, ed è anche piccola ⇒ si elimina (vedi slide 123).

### Accorpamento caso 4, per denormalizzazione

Vedi [[Normalizzazione e Denormalizzazione]].

![[BD-L06-p155.png]]

$R_1(K_1, A)$ e $R_2(K_2, \beta)$ con $R_1[A] \subseteq R_2[K_2]$, dove $A$ **non** è chiave di $R_1$ (tabelle **lascamente accoppiate**). Si aggiungono gli attributi $\beta$ a $R_1$ **senza eliminare** $R_2$: $R_1(K_1, A, \beta)$ con `foreign key: R1[A,β] ⊆ R2[K2,β]`. Si chiama **accorpamento per denormalizzazione**: $R_1$ contiene attributi che dipendono non dalla sua chiave ma da un attributo non chiave ($A$). Crea ridondanze; si usa quando l'accesso a $R_1$ richiede quasi sempre il join con $R_2$ su $A = K_2$, e in genere non è problematico se $\beta$ cambia **raramente**. $R_1$ originale si ricostruisce con la proiezione su $K_1, A$. Se nello schema originale c'è anche $R_2[K_2] \subseteq R_1[A]$, si può eliminare $R_2$, aggiungendo il vincolo che $\beta$ **dipende funzionalmente** da $A$.

![[BD-L06-p157.png]]

Persona (CF, Età) – Risiede (1,1) – Città (Nome, Regione). (1) accedendo a una persona si vuole la città di residenza → accorpamento di Persona e Risiede; (2) si vuole anche la regione → accorpamento per denormalizzazione:
```
Persona(CF, Età, Città, Regione)
    inclusione: Persona[Città, Regione] ⊆ Città[Nome, Regione]
Città(Nome, Regione)
```

Con Città (1,n) in Risiede si ha anche $\text{Città}[\text{Nome}, \text{Regione}] \subseteq \text{Persona}[\text{Città}, \text{Regione}]$, quindi si può eliminare Città: `Persona(CF, Età, Città, Regione)` con il vincolo esterno "non esistono due tuple in Persona con la stessa città e diversa regione".

> [!note] Nota
> Qui la slide usa "inclusione" per `Persona[Città, Regione] ⊆ Città[Nome, Regione]`, mentre nella slide generale del caso 4 lo stesso vincolo è chiamato "foreign key". Come osservano gli appunti, è corretto chiamarla foreign key perché (Nome, Regione) è una superchiave di Città.

### Accorpamento per eliminare relazioni e attributi inutili

- **Relazioni inutili**: $R_1(K_1, \alpha)$ e $R_2(B)$ con $R_1[\alpha] \subseteq R_2[B]$ e $R_2[B] \subseteq R_1[\alpha]$: $R_2$ non contiene niente che non sia già in $R_1$; si elimina (ricostruibile come proiezione di $R_1$ su $\alpha$). Si applica quando è raro che interessi solo $B$.
- **Attributi inutili**: se per ogni tupla $t[A] = t[B]$, uno dei due è inutile; lo stesso se un attributo è sempre NULL.

### Traduzione in SQL

| Vincolo | SQL |
|---|---|
| attributo obbligatorio | `not null` |
| chiave primaria | `primary key` |
| chiave | `unique` |
| foreign key | `foreign key` |
| interdipendenza nulli | `check ((A is null and B is null) or (A is not null and B is not null))` |
| inclusione | `check (A in (select B from R))` |
| disgiunzione | `check (A not in (select B from R))` |
| cardinalità (i,j) | `check ((i <= (select count(*) from R where ...)) and (j >= (select count(*) from R where ...)))` |
| vincoli esterni | `assertion` o controlli a livello applicativo |

Poiché i DBMS attuali non accettano `check` con sottoquery (vedi [[03 - BD - SQL#Vincoli di integrità generici, check e asserzioni|SQL]]), questi vincoli si realizzano con i **trigger** ([[04 - BD - Accesso ai Dati da Software#Trigger|trigger]]).

### Esercizio 7, progettazione logica completa

![[BD-L06-p162.png]]

Schema: `Persona` (CFis, DataN, Livello, Occupazione, Patrimonio) – `Residenza` (1,1), con `Indirizzo` – `Città` (Nome, Nazione); `Studente` (Matricola, Corso, Anno) ISA Persona. Requisiti: per le persone **non studenti**, ai dati anagrafici (DataN, Residenza) si accede spesso separatamente da quelli fiscali; agli **studenti** si accede per matricola, con i dati universitari insieme a data di nascita e dati fiscali.

![[BD-L06-p163.png]]

Ristrutturazione (ISA-S-P con identificatore principale Matricola per Studente) e traduzione diretta:
```
Persona(CFis, DataN, Livello, Occupazione, Patrimonio)
    foreign key: Persona[CFis] ⊆ Residenza[Persona]
Studente(Matricola, Corso, Anno)
    foreign key: Studente[Matricola] ⊆ ISA-S-P[Studente]
Città(Nome, Nazione)
ISA-S-P(Studente, Persona)
    foreign key: ISA-S-P[Studente] ⊆ Studente[Matricola]
    foreign key: ISA-S-P[Persona] ⊆ Persona[CFis]
    chiave: Persona
Residenza(Persona, Indirizzo, Città)
    foreign key: Residenza[Persona] ⊆ Persona[CFis]
    foreign key: Residenza[Città] ⊆ Città[Nome]
```

Ristrutturazioni dello schema logico:
1. **decomposizione orizzontale** di Persona in PersonaNonStudente e PersonaStudente, e di Residenza in ResidenzaNonStudente e ResidenzaStudente (criteri di accesso diversi), con il vincolo $\text{PersonaNonStudente}[\text{CFis}] \cap \text{PersonaStudente}[\text{CFis}] = \emptyset$;
2. **decomposizione verticale** di PersonaNonStudente in PersonaDatiAnagrafe(CFis, DataN) e PersonaDatiFisco(CFis, Livello, Occupazione, Patrimonio);
3. **accorpamento** di PersonaDatiAnagrafe e ResidenzaNonStudente;
4. **accorpamento** di Studente con ISA-S-P e poi con PersonaStudente.

Schema finale:
```
PersonaDatiAnagrafe(CFis, DataN, Indirizzo, Città)
    foreign key: PersonaDatiAnagrafe[CFis] ⊆ PersonaDatiFisco[CFis]
    foreign key: PersonaDatiAnagrafe[Città] ⊆ Città[Nome]
PersonaDatiFisco(CFis, Livello, Occupazione, Patrimonio)
    foreign key: PersonaDatiFisco[CFis] ⊆ PersonaDatiAnagrafe[CFis]
Studente(Matricola, Corso, Anno, CFis, DataN, Livello, Occupazione, Patrimonio)
    foreign key: Studente[CFis] ⊆ ResidenzaStudente[Studente]
    chiave: CFis
ResidenzaStudente(Studente, Indirizzo, Città)
    foreign key: ResidenzaStudente[Studente] ⊆ Studente[CFis]
    foreign key: ResidenzaStudente[Città] ⊆ Città[Nome]
Città(Nome, Nazione)
Vincolo: PersonaDatiAnagrafe[CFis] ∩ Studente[CFis] = ∅
```

### Esercizi 8 e 9, ristrutturazioni dello schema logico

**Esercizio 8 (voli)**: partendo dallo schema dell'esercizio 5, con le specifiche (si accede spesso ai voli charter separatamente dagli altri; accedendo a un volo si vogliono tutte le sue proprietà; accedendo a una compagnia anche la sua sede):
- **decomposizione orizzontale** di Volo (VoloNonCharter, DatiVoloCharter) e di ArrPart;
- **accorpamenti** di DatiVoloCharter con VoloCharter e poi con ArrPartVoloCharter, e di VoloNonCharter con ArrPartVoloNonCharter;
- **accorpamento** di Compagnia e CittàSede;
- eliminazione delle relazioni inutili Sede e Telefono.

```
VoloNonCharter(Codice, Comp, Durata, Arrivo, Partenza)   chiave: Comp, Arrivo, Partenza
VoloCharter(Codice, Comp, TipoAereo, Durata, Arrivo, Partenza)   chiave: Comp, Arrivo, Partenza
Aeroporto(Codice, Nome), LuogoAeroporto(Aeroporto, NomeCittà, NazCittà), Città(Nome, Nazione, NumAbitanti)
Compagnia(Nome, AnnoFond, NomeCittà, NazCittà)   inclusione: Compagnia[Nome] ⊆ TelefonoComp[Comp]
TelefonoComp(Numero, Comp)
Tappa(CodVoloCharter, Comp, Aeroporto, Ordine)
Vincoli: VoloNonCharter e VoloCharter disgiunti (su Codice,Comp e su Comp,Arrivo,Partenza); Ordine in Tappa.
Viste: Volo = PROJ_{Codice,Comp,Durata}(VoloNonCharter) ∪ PROJ_{Codice,Comp,Durata}(VoloCharter)
       ArrPart = PROJ_{Codice,Comp,Arrivo,Partenza}(VoloNonCharter) ∪ (lo stesso su VoloCharter)
       Sede = PROJ_Nome(Compagnia); CittàSede = PROJ_{Nome,NomeCittà,NazCittà}(Compagnia)
       Telefono = PROJ_Numero(TelefonoComp)
```

**Esercizio 9 (officine)**: con le specifiche (direttori e officine acceduti insieme in entrambe le direzioni; dipendenti acceduti separatamente dai direttori; con i dipendenti interessa l'indirizzo):
- **accorpamento** di Direttore e Dirige, poi con Officina → `OfficinaDirettore(Nome, NumDip, Indirizzo, Direttore, EtaDir, AnniAnzDir)` con chiave Direttore;
- **decomposizione orizzontale** di Persona in dipendenti e non (`PersonaNonDip(CodFis, Indirizzo)`);
- **accorpamento** di Dipendente con i suoi dati anagrafici → `Dipendente(CodFis, AnniAnz, Indirizzo)`;
- eliminazione della relazione inutile Telefono.

Vincoli: $\text{PersonaNonDip}[\text{CodFis}] \cap \text{Dipendente}[\text{CodFis}] = \emptyset$; le foreign key verso Persona diventano inclusioni verso $\text{PersonaNonDip}[\text{CodFis}] \cup \text{Dipendente}[\text{CodFis}]$; restano i vincoli esterni. Viste: `Persona = PersonaNonDip ∪ PROJ_{CodFis,Indirizzo}(Dipendente)`, `Direttore`, `Dirige`, `OfficinaOrig`, `Telefono` come proiezioni.

> [!warning] Correzione
> Nella soluzione dell'esercizio 9 le viste e i vincoli si riferiscono a `Officina[Direttore]` e `Veicolo[Proprietario]`, ma nello schema ristrutturato la tabella si chiama `OfficinaDirettore` e il proprietario sta in `Possiede[Proprietario]`, non in Veicolo. Inoltre `Riparazione(Codice, Officina, OraAcc, DataAcc,)` ha una virgola di troppo.

### Normalizzazione e denormalizzazione

Tabella di un'agenzia immobiliare: `Interesse(cliente, appartamento, valore)`, dove ⟨c, a, v⟩ significa che il cliente c è interessato all'appartamento a, il cui valore al metro quadro è v.

| Cliente | Appartamento | Valore |
|---|---|---|
| C1 | A1 | 1000 |
| C1 | A2 | 2000 |
| C1 | A3 | 1000 |
| C2 | A2 | 2000 |
| C2 | A4 | 4000 |
| C2 | A5 | 2000 |
| C2 | A6 | 2500 |
| C3 | A2 | 2000 |
| C3 | A6 | 2500 |

**Anomalie**:
- **aggiornamento**: se il valore di A2 passa da 2000 a 1800, bisogna cambiarlo in **tutte** le tuple con A2 (tre);
- **cancellazione**: se C2 abbandona l'agenzia si perdono i valori di A4 e A5;
- **inserimento**: non si può inserire il valore di un appartamento che non interessa a nessun cliente (cliente non può essere NULL, è nella chiave).

Quindi: **ridondanza** (il valore è ripetuto), **aggiornamenti costosi**, **rischio di perdere informazione**.

Una tabella è **normalizzata** se ogni suo attributo dipende funzionalmente dalla **chiave**: non ci sono "legami nascosti". In Interesse la chiave è ⟨cliente, appartamento⟩, ma `valore` dipende solo da `appartamento` (una **parte** della chiave): c'è un legame nascosto, la tabella è **denormalizzata**, e da qui vengono le anomalie.

![[BD-L06-p185.png]]

Appunti di Simone: catalogo di tabelle: se non sono normalizzate ⇒ fanno schifo. **Dipendenza funzionale**: data $R(A, B, C, D, E, F)$, non esistono 2 tuple con lo stesso valore di D e un diverso valore di E: $D \to E$. Vale anche con le superchiavi: dati $\alpha$ e $\beta$ dove $\alpha$ è una superchiave di R e $\beta$ sono tutti gli attributi di R, $\alpha \to \beta$. **Tutte le dipendenze funzionali che valgono coincidono ad una superchiave** (in una tabella normalizzata). Esempio precedente (accorpamento per denormalizzazione): Persona(KP, …, Città, Regione), dove Città → Regione, ma città è chiave di persona? No ⇒ questa tabella è **denormalizzata**. Allora l'accorpamento per denormalizzazione partorirebbe delle tabelle che fanno schifo secondo le slide, **ma noi le abbiamo volute**; se invece le otteniamo direttamente dallo schema ristrutturato ⇒ problema (vedi pagina successiva).

Approfondimento nel corso magistrale: [[Functional Dependency]], [[Third Normal Form 3NF]].

![[BD-L06-p194.png]]

La progettazione concettuale avrebbe prodotto `Cliente` (codice) – `Interesse` (1,n) – `Appartamento` (codice, valore), tradotto in tre tabelle **normalizzate**:
```
Cliente(codice)              inclusione Cliente[codice] ⊆ Interesse[cliente]
Interesse(cliente, appartamento)
    foreign key Interesse[cliente] ⊆ Cliente[codice]
    foreign key Interesse[appartamento] ⊆ Appartamento[codice]
Appartamento(codice, valore)
```

> [!important] Osservazione
> Le tabelle che provengono dalla traduzione diretta di uno schema concettuale **di qualità** sono **sempre normalizzate** (annotazione: "mai tabelle denormalizzate").

> [!warning] Correzione
> Nella slide la foreign key è scritta `Interesse[appartamento] ⊆ Appartamento[valore]`: deve puntare alla chiave, `Appartamento[codice]`.

Se però dalle indicazioni di progetto risulta che ogni accesso a Interesse richiede il valore degli appartamenti, e che il valore cambia **raramente**, si possono accorpare (accorpamento per denormalizzazione, "dopo lo schema accorpato") Interesse e Appartamento, e poi eliminare Cliente:
```
Interesse(cliente, appartamento, valore)
    foreign key Interesse[appartamento, valore] ⊆ Appartamento[codice, valore]
Appartamento(codice, valore)
```
Lo schema finale non è normalizzato, ma **voluto**: in fase di ristrutturazione dello schema logico si può denormalizzare, in particolare per evitare join in query frequenti e importanti.

---

## Progettazione completa ed esercizi

![[BD-L06-p197.png]]

**Esercizio 1, car pooling** (progettazione completa): la specifica (utenti registrati che pubblicano offerte di passaggi; assegnazione al primo che aderisce; automobili, modelli, persone, utenti, indirizzi, città, regioni con tassa; offerte speciali con servizi in più e voto del titolare) e le indicazioni per la progettazione logica: (1) accedendo a un'offerta si vuole sempre l'utente; (2) accedendo a una persona la città di nascita; (3) evitare i valori nulli.

![[BD-L06-p198.png]]

Lo schema concettuale di Simone (Persona/Utente, Offerta/Speciale, Assegnazione/AssegnazioneSpeciale con voto, Automobile, Modello, Città, Regione, Indirizzo, Giro), i vincoli esterni (data di pubblicazione precedente alla data del passaggio; anno di immatricolazione e anno di registrazione coerenti con le date), un frammento del dizionario dei dati e le differenze dello schema ristrutturato: (1) ISA-U-P e ISA-S-O con il vincolo esterno che il titolare di un'assegnazione speciale, utente, sia anche il titolare dell'assegnazione corrispondente; (2) le recensioni del modello come entità (multivalore).

![[BD-L06-p199.png]]

Lo schema tradotto $S''$: Persona, Utente (vincolo di tupla sull'anno di registrazione), Offerta (vincolo di tupla dataPubblicazione < dataPassaggio), Pubblica, Assegnazione, Speciale, AssegnazioneSpeciale (voto*), Indirizzo, Città, Regione, Nascita, Automobile, Modello, ModelloAuto, Recensione, con le foreign key.

![[BD-L06-p200.png]]

Seguito: Giro e i vincoli esterni di join (utente nato prima della registrazione, immatricolazione prima della pubblicazione, nessuna tupla con la stessa data di passaggio); poi la ristrutturazione dello schema logico secondo le indicazioni: (1) Offerta e Pubblica **fortemente accoppiate** → accorpamento (Offerta con CFUtente); (2) Persona e Nascita fortemente accoppiate → accorpamento; (3) **decomposizione mista** per levare il possibile attributo nullo voto in AssegnazioneSpeciale → AssegnazioneSpecialeVoto(Codice, dataPubblicazione, voto).

![[BD-L06-p201.png]]

**Altri esercizi, esercizio 2**: schema $S_1$ con A (A1, A2) – R – B (B1, B2), con C (1,1) in R e attributo R1; quando si accede a C non interessano le informazioni sulla partecipazione a R. Ristrutturazione: identificatore di R scelto anche se "prima"…; traduzione: `A[A1, A2]`, `B[B1, B2]`, `C[C1, C2]` con foreign key C[C1] ⊆ R[C], `R[A, B, C, R1]` con foreign key verso C, A, B e **chiave A, B**. Il vincolo esterno sul join (barrato) "non serve": non è un errore, ma non è necessario grazie alla chiave A, B.

![[BD-L06-p202.png]]

**Esercizio 3** (politiche di reazione): schema logico `R(A, B)` con default A = 1, foreign key R[B] ⊆ S[C] on delete set default, chiave B; `S(C, D)` con foreign key S[D] ⊆ R[A] on delete cascade (A e B chiavi di R). Esiste una base di dati in cui la cancellazione di una tupla di R provoca un errore? Spiegazione del prof: normalmente il valore di default è NULL. È molto utile fare dei grafi per esprimere le foreign key: A e C hanno il NOT NULL implicito, D possibile NULL. S[D] ha cascade, quindi se cancello una tupla $t_1$ a partire da R ⇒ si cancellano tutte le tuple che hanno quel valore in S (in D possono avere duplicati). Ora però che succede? Ogni B relativo al C cancellato verrà messo su default, cioè NULL. Io non ho violato alcun vincolo così. Esempio prima/durante/dopo: cancellando ⟨a2, b2⟩ si cancellano in S le tuple con D = a2, e i B di R che le riferivano diventano NULL. Se io avessi avuto che R[B] IS NOT NULL ⇒ avrei avuto errore. Ricorda che un NULL non viola mai una foreign key; le chiavi primarie invece implicano il NOT NULL.

> [!warning] Correzione
> Negli appunti si dice che "normalmente il valore di default è NULL" e che B viene messo a NULL. Ma il testo dell'esercizio dice che il default è definito **per A** (A = 1), non per B: per B il default è effettivamente NULL, quindi la conclusione degli appunti regge. Attenzione però: B è **chiave** di R, e due tuple con B = NULL non violano il vincolo `unique` (i NULL non sono mai uguali), quindi anche più tuple messe a NULL non danno errore.

![[BD-L06-p203.png]]

**Esercizio 4**: schema S con A – R (U, B (1,1)) e Q (U, C (2,n)), Q ISA R e C ISA B. (1) Esiste un'istanza in cui R ha almeno un'istanza? Sì: istanze(I,B) = {b1}, istanze(I,R) = {⟨A: a1, U: b1⟩}, istanze(I,A) = {a1}. (2) Esiste un'istanza in cui Q ha almeno un'istanza? Poiché Q è un sottoinsieme di R, il vincolo di cardinalità di C in Q è esplicitamente (1,1) AND (2,n) = (2,1), che è impossibile: istanze(I,Q) = ∅. Inoltre bisogna anche ricordarsi che se $c_1 \in C$ partecipasse 2 volte minimo a Q ed inoltre C è anche istanza di B, violerebbe il vincolo di cardinalità massima (1,1) di B in R.

![[BD-L06-p204.png]]

**Esercizio 5 (droni)**: la specifica (droni con codice e peso; alcuni con fotocamera — classe, costo, voli con chilometri e data, al massimo uno al giorno — altri con videocamera — codice internazionale, tipo di videocamera con numero di serie, marca se nota, anno di produzione) e le indicazioni sul carico applicativo (accesso per codice internazionale; con la videocamera si vuole sempre il tipo, l'anno e la marca; accedendo a un drone si vuole sapere se ha la fotocamera, e in tal caso costo, tipo e peso).

![[BD-L06-p205.png]]

Lo schema concettuale di Simone: Drone (codice, peso) con generalizzazione in Drone Fotocamera (classe, costo) e Drone Videocamera (codice internazionale), Volo (chilometri, data) come evento legato a Drone Fotocamera ("nota che un volo è nello stesso pattern degli eventi"), Tipo (numSerie, annoProd, marca (0,1)) legato a Drone Videocamera.
