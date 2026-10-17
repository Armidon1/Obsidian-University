---
title: "Guida - Controlli Automatici"
tags:
  - controlli-automatici
  - fonti
source: "Materiale nella cartella pdf/"
---

# Guida - Controlli Automatici

> [!abstract]
> Gli appunti seguono l'ordine del materiale di classe, integrando richiami già presenti nei corsi di Teoria dei Sistemi e Geometria. L'accesso principale è [[MOC - Controlli Automatici]].

## Materiale e numerazione

| Fonte locale | Estensione | Uso |
|---|---:|---|
| `pdf/Controlli automatici riccia commentati.pdf` | 297 pagine | Fonte principale, ordine delle lezioni, schemi e annotazioni |
| `pdf/ES ERCIZI CONTROLLi_250609_213750.pdf` | 94 pagine | Tracce d'esame, svolgimenti e verifiche supplementari |
| `pdf/Bode for dummies .jpg` | 1 immagine | Promemoria dei fattori elementari, con precisazioni nella lezione su Bode |

I numeri di pagina citati sono quelli fisici del PDF, contando la copertina come pagina 1. Non coincidono necessariamente con la numerazione di una slide o con i numeri manoscritti.

La copertina specifica che le prime nove pagine costituiscono un richiamo di TDS e che dalla «lezione 3» seguono appunti commentati. Le nuove note usano 00 per i richiami e 01–28 per i successivi blocchi: sono numeri editoriali. Le intestazioni e le date leggibili sono riportate nelle note; dove non è chiaro un nuovo confine di lezione si usa la suddivisione per blocchi contigui del manoscritto, senza inventare un calendario o contenuti mancanti. L'eserciziario è distinto con E01–E15.

> [!example]- Copertina e indicazioni originali
> ![[CA-p001-1.jpg]]
> La copertina delimita il richiamo iniziale di TDS e segnala i successivi commenti aggiunti agli appunti delle lezioni.

## Come usare gli appunti

Leggere prima le sezioni riscritte e gli esempi. I callout richiudibili «Materiale originale» conservano tutte le pagine in ordine: servono per aprire grafici, schemi e annotazioni nel punto pertinente. Le scansioni sono renderizzate a 110 dpi e possono essere aperte singolarmente; per dettagli minuscoli rimane disponibile il PDF locale originale.

Le note atomiche in `Concetti/` sono sintesi autonome con collegamenti alle sezioni esatte. I richiami agli altri corsi sono wikilink a note esistenti, non riferimenti a libri o pagine non consultate. La teoria dei sistemi fornisce i prerequisiti dinamici; Geometria fornisce rango, coordinate e strumenti spettrali. Nessun capitolo estraneo al materiale di Controlli è stato aggiunto come nuova lezione.

## Convenzioni matematiche

- Retroazione unitaria: $F=GP$, $S=1/(1+F)$, $T=F/(1+F)$. Nella fonte $W$ indica spesso $T$.
- Feedback dello stato: $u=Kx+v$, matrice chiusa $A+BK$.
- Osservatore: $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x)$, errore $e=x-\hat x$, matrice $A-LC$.
- Coordinate lineari: $z=Tx$ salvo esplicita indicazione opposta.
- Nyquist: avvolgimenti orari positivi con contorno destro orario, $Z=P+N_{cw}$.
- AS significa asintoticamente stabile; GAS significa globalmente asintoticamente stabile.

## Correzioni e limiti di lettura

Le correzioni sono evidenziate nelle lezioni e nelle prove, conservando sempre lo svolgimento originale nella scansione. Riguardano unità e soglia esatta di risonanza nel promemoria, errore sulla rampa, stabilità del processo con integratore, confronto fra banda e attraversamento, equilibri dei sistemi lineari, un intervallo incompleto di guadagno e un passaggio sul massimo insieme invariante di LaSalle.

Le formule esplicitamente riscritte negli esempi sono state ricalcolate. L'eserciziario conserva integralmente gli svolgimenti manoscritti, ma le guide non dichiarano verificati tutti i coefficienti delle soluzioni numeriche lasciate soltanto nelle scansioni. Tratti minuti, sovrapposti o poco leggibili non sono stati trascritti con numeri inventati. Gli screenshot di spiegazioni aggiunti alla dispensa rimangono visibili come annotazioni della fonte: non sostituiscono le ipotesi dei teoremi.

Le pagine con gli stessi temi o con diagrammi ripetuti restano al loro posto, anche quando ridondanti: soprattutto simulazioni, esempi di Bode e ripassi delle forme canoniche. Non sono state eliminate annotazioni originali.

## Git e materiale locale

Il `.gitignore` di questo corso esclude tutta `pdf/`. Le note e le immagini renderizzate in `images/` sono incluse nel commit e rimangono quindi consultabili anche dopo un clone senza i PDF originali. Gli altri corsi non vengono modificati da questo lavoro.
