---
title: "LaSalle linearizzazione e studio degli equilibri"
aliases:
  - "CA — LaSalle linearizzazione e studio degli equilibri"
tags:
  - controlli-automatici
  - lezione
source: "pdf/Controlli automatici riccia commentati.pdf"
pdf_pages: "245-269"
class_label: "12/05"
---

# LaSalle linearizzazione e studio degli equilibri

> [!abstract]
> Questa lezione sviluppa lasalle linearizzazione e studio degli equilibri seguendo il blocco delle pagine 245–269 della dispensa commentata. Percorso completo: [[MOC - Controlli Automatici]].

**Indicazione nel materiale:** 12/05. La numerazione CA è editoriale e non sostituisce quella del docente.

**Prima:** [[26 - CA - Metodo diretto di Lyapunov]]. **Dopo:** [[28 - CA - Stabilizzazione non lineare e linearizzazione esatta]].

## Derivata semidefinita e insieme invariante

Vedi [[CA - Principio di LaSalle]] · [[CA - Insieme invariante]] · [[CA - Massimo insieme invariante]].

Se $\dot V\le0$, $V(x(t))$ non cresce, ma può convergere a un valore positivo e non prova da sola che $x(t)\to0$. LaSalle consente di studiare ciò che accade nell'insieme $E=\{x:\dot V(x)=0\}$.

Sia $\Omega$ compatto e positivamente invariante e $V\in C^1$ con $\dot V\le0$ in $\Omega$. Ogni traiettoria in $\Omega$ tende al massimo insieme invariante $M$ contenuto in $E\cap\Omega$. Non basta risolvere $\dot V=0$: bisogna chiedersi quali soluzioni possono restare in quell'insieme per tutti i tempi.

> [!example] Pendolo con attrito
> Per $V=\omega^2/2+1-\cos\theta$, $\dot V=-b\omega^2$. In $E$ vale $\omega=0$, ma per restarvi serve anche $\dot\omega=-\sin\theta=0$. In una regione attorno alla configurazione bassa che esclude quella alta, $M$ contiene soltanto l'equilibrio basso, quindi si ottiene AS.

Per conclusioni globali si cercano sottolivelli compatti per ogni condizione iniziale, ad esempio con una $V$ radialmente illimitata, e si identifica l'insieme invariante su tutto lo spazio. Non affermare GAS di un equilibrio se esistono altri equilibri nello stesso spazio di stato.

_(Dispensa commentata, pagine PDF 245–253; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 245
> ![[CA-p245-1.jpg]]
> LaSalle affronta il caso in cui la derivata è solo semidefinita negativa: l'insieme invariante diventa il nuovo oggetto di studio.

> [!example]- Materiale originale — pagina PDF 246
> ![[CA-p246-1.jpg]]
> Il teorema locale afferma convergenza al massimo insieme invariante contenuto negli zeri della derivata, in un compatto positivamente invariante.

> [!example]- Materiale originale — pagina PDF 247
> ![[CA-p247-1.jpg]]
> L'applicazione al pendolo impone la compatibilità del vincolo di velocità nulla con le equazioni del moto, isolando l'equilibrio nella regione scelta.

> [!example]- Materiale originale — pagina PDF 248
> ![[CA-p248-1.jpg]]
> L'esercizio manoscritto distingue l'insieme dove la derivata si annulla dalle traiettorie che possono restarvi.

> [!example]- Materiale originale — pagina PDF 249
> ![[CA-p249-1.jpg]]
> Il corollario AS conclude la convergenza quando il massimo insieme invariante è il solo equilibrio considerato.

> [!example]- Materiale originale — pagina PDF 250
> ![[CA-p250-1.jpg]]
> I disegni chiariscono che LaSalle non richiede una singola curva invariante: cerca tutto l'insieme dinamicamente compatibile con gli zeri della derivata.

> [!example]- Materiale originale — pagina PDF 251
> ![[CA-p251-1.jpg]]
> La versione globale usa sottolivelli compatti per tutte le condizioni iniziali e la limitatezza radiale della candidata.

> [!example]- Materiale originale — pagina PDF 252
> ![[CA-p252-1.jpg]]
> Una famiglia meccanica con richiamo e attrito non lineari mostra come sfruttare energia e monotonia senza risolvere il moto.

> [!example]- Materiale originale — pagina PDF 253
> ![[CA-p253-1.jpg]]
> La derivata dell'energia individua gli zeri della dissipazione; le equazioni del sistema restringono l'insieme invariante fino all'equilibrio.

## Criterio indiretto e matrice Jacobiana

Vedi [[CA - Jacobiana]] · [[CA - Criterio indiretto di Lyapunov]] · [[CA - Caso critico della linearizzazione]].

Per $\dot x=f(x)$, $f(x_e)=0$ e $f$ sufficientemente regolare, si pone $z=x-x_e$ e si calcola $A=\partial f/\partial x|_{x_e}$. Il sistema linearizzato è $\dot z=Az$.

| Autovalori della Jacobiana | Conclusione sul non lineare |
|---|---|
| tutti con parte reale negativa | equilibrio localmente AS, anzi localmente esponenziale |
| almeno uno con parte reale positiva | equilibrio instabile |
| nessuno positivo e almeno uno con parte reale nulla | criterio non conclusivo |

Nel caso critico, anche una linearizzazione stabile non prova stabilità del non lineare; se la linearizzazione ha blocchi di Jordan sull'asse immaginario e risulta instabile, non basta comunque quel solo fatto per applicare la riga dell'instabilità, che richiede una parte reale positiva. Vanno studiati i termini non lineari con altri metodi.

> [!example] Stessa linearizzazione, risultati opposti
> $\dot x=-x^3$ e $\dot x=x^3$ hanno entrambi Jacobiana nulla all'origine. Il primo è AS, il secondo instabile. Il termine di ordine superiore decide.

_(Dispensa commentata, pagine PDF 254–260; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 254
> ![[CA-p254-1.jpg]]
> Il criterio indiretto linearizza il campo mediante la Jacobiana nell'equilibrio e separa il termine lineare dai residui superiori.

> [!example]- Materiale originale — pagina PDF 255
> ![[CA-p255-1.jpg]]
> La derivazione manoscritta esplicita la traslazione dell'equilibrio e la costruzione della matrice delle derivate parziali.

> [!example]- Materiale originale — pagina PDF 256
> ![[CA-p256-1.jpg]]
> Una Jacobiana non singolare implica isolamento locale dell'equilibrio; il contrario non è necessario, come mostrano esempi non lineari.

> [!example]- Materiale originale — pagina PDF 257
> ![[CA-p257-1.jpg]]
> Gli esempi confrontano equilibri isolati con Jacobiana singolare e casi in cui il nucleo del lineare non decide la struttura non lineare.

> [!example]- Materiale originale — pagina PDF 258
> ![[CA-p258-1.jpg]]
> Il teorema indiretto distingue Jacobiana Hurwitz, autovalori positivi e caso critico sull'asse immaginario.

> [!example]- Materiale originale — pagina PDF 259
> ![[CA-p259-1.jpg]]
> Il pendolo basso e quello alto forniscono un'applicazione diretta: la derivata del seno cambia segno nei due punti.

> [!example]- Materiale originale — pagina PDF 260
> ![[CA-p260-1.jpg]]
> Il sistema cubico con Jacobiana nulla mostra un caso critico da risolvere con V e non con il solo modello lineare.

## Procedura completa ed esercizi

Vedi [[CA - Studio di un equilibrio]] · [[CA - Analisi parametrica non lineare]] · [[CA - Stima locale e globale]].

La procedura riepilogata nelle dispense è: risolvere $f(x)=0$, elencare tutti gli equilibri, calcolare la Jacobiana in ciascuno, classificare i casi non critici, usare una candidata di Lyapunov nei casi critici, applicare LaSalle se la derivata è semidefinita, delimitare il dominio della conclusione.

Se il sistema contiene parametri, anche il numero degli equilibri può cambiare: non analizzare soltanto il segno della Jacobiana nell'origine senza verificare le altre soluzioni. Un candidato quadratico può dare solo una regione locale; un livello compatto contenuto nella zona di segno certo permette di formulare una stima rigorosa del bacino.

Gli algoritmi testuali inseriti nel PDF sono promemoria. Ogni ramo «non conclusivo» richiede un nuovo argomento matematico: non equivale né a stabilità né a instabilità. Le pagine con esercizi conservano esempi di cambio di equilibrio e curve di livello per la stima del dominio di attrazione.

_(Dispensa commentata, pagine PDF 261–269; numerazione fisica del file.)_

> [!example]- Materiale originale — pagina PDF 261
> ![[CA-p261-1.jpg]]
> L'esercizio cerca tutti gli equilibri e confronta le loro Jacobiane prima di passare al criterio diretto.

> [!example]- Materiale originale — pagina PDF 262
> ![[CA-p262-1.jpg]]
> La candidata scelta nell'esercizio controlla il segno della derivata e costruisce una regione certificata attorno al punto stabile.

> [!example]- Materiale originale — pagina PDF 263
> ![[CA-p263-1.jpg]]
> L'algoritmo riassume ricerca degli equilibri, Jacobiana e classificazione dei casi risolti dal metodo indiretto.

> [!example]- Materiale originale — pagina PDF 264
> ![[CA-p264-1.jpg]]
> La seconda pagina dell'algoritmo completa il ramo critico con scelta di V, insieme invariante di LaSalle e conclusione sul dominio.

> [!example]- Materiale originale — pagina PDF 265
> ![[CA-p265-1.jpg]]
> Il primo foglio di esercizi applica l'algoritmo con parametri e ricava condizioni diverse per gli equilibri trovati.

> [!example]- Materiale originale — pagina PDF 266
> ![[CA-p266-1.jpg]]
> Il calcolo della derivata verifica i pesi della candidata e il dominio in cui il segno è certo.

> [!example]- Materiale originale — pagina PDF 267
> ![[CA-p267-1.jpg]]
> Un secondo esempio distingue casi parametrici con diversa struttura degli equilibri e della Jacobiana.

> [!example]- Materiale originale — pagina PDF 268
> ![[CA-p268-1.jpg]]
> I conti costruiscono regioni locali e ne confrontano i confini con il piano delle fasi.

> [!example]- Materiale originale — pagina PDF 269
> ![[CA-p269-1.jpg]]
> Le curve di livello conclusive visualizzano una stima del bacino, lasciando distinta la regione provata da quella suggerita dalla simulazione.

## Esercizi collegati

[[E11 - CA - Prova finale 2021-2022]] · [[E13 - CA - Prova finale 2023-2024 e assegnazione canonica]] · [[E14 - CA - Prova completa del 12 luglio 2019]]
