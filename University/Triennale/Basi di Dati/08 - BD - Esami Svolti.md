---
title: Esami Svolti
aliases:
  - BD — Esami Svolti
tags:
  - basi-di-dati
  - esami
  - esercizi
source: Esami svolti - Basi Di Dati.pdf
---

# Esami Svolti

> [!abstract]
> Sei appelli d'esame (A.A. 2021/22 – 2023/24) con le soluzioni svolte a mano da Simone. Ogni compito ha la stessa struttura e copre tutto il corso:
> - **progettazione concettuale** di uno schema ER da una specifica → [[05 - BD - Progettazione Concettuale]];
> - **progettazione logica** con indicazioni sul carico applicativo → [[06 - BD - Progettazione Logica]];
> - **query** in SQL e in algebra relazionale → [[03 - BD - SQL]], [[02 - BD - Modello Relazionale#2.2 Algebra relazionale|algebra relazionale]];
> - domande di **teoria** su vincoli, superchiavi, istanze di schemi ER, trigger e politiche di reazione.
>
> Le soluzioni sono di Simone, non ufficiali: dove c'è un errore lo segnalo con un callout di correzione.
>
> Indice dei concetti: [[MOC - Basi di Dati]].

| Appello | Problemi | Temi |
|---|---|---|
| [[#Appello del 26/01/2024]] | 5 | crociere, accordi giornalistici, piano di studi, superchiavi e foreign key |
| [[#Appello del 20/01/2023]] | 5 | contratti tra aziende, trigger, superchiavi |
| [[#Appello del 15/02/2023]] | 5 | rete sociale, chiave primaria in algebra, istanze ER |
| [[#Appello del 23/02/2024]] | 5 | edifici, esami/università, istanze ER, logica in SQL |
| [[#Appello del 21/01/2022]] | 6 | mostre, finanziamenti, divisione in algebra, traduzione di ISA tra relazioni |
| [[#Appello del 07/02/2022]] | 6 | centro spaziale, contratti gemelli, politiche di reazione |

> [!tip] Come è fatto l'esame
> Si accede alla prova scritta solo dopo il **test SQL** ([[01 - BD - Introduzione#Informazioni generali|Introduzione]]). Lo schema concettuale da consegnare è **diagramma + dizionario dei dati + vincoli esterni**; nella progettazione logica si possono indicare solo le differenze rispetto allo schema precedente ([[06 - BD - Progettazione Logica#Esercizi di ristrutturazione|nota del professore]]).

---

## Appello del 26/01/2024

![[BD-ES-p001.png]]

**Testo.**
1. Schema ER sulle **crociere** offerte da compagnie navali (partita IVA, capitale sociale), con la somma investita da ogni compagnia; l'insieme dei porti toccati cambia al massimo una volta all'anno (da storicizzare); le crociere "adventure" hanno una compagnia **capofila** che assegna un extra-investimento.
2. Progettazione logica: alle crociere adventure si accede separatamente; accedendo a una adventure si vuole sempre categoria, capofila e numero di certificati.
3. Revisione di uno schema ER (Giornalista–Accordo–Testata–Garante): massimo 3 accordi per testata, gettone diverso per ogni articolo.
4. Su `Corso(codice, disciplina)` e `PianoDiStudi(studente, codcorso)`: (3.1) in algebra, le coppie $(s, d)$ tali che nel piano di $s$ non c'è alcun corso della disciplina $d$; (3.2) in SQL, gli studenti con almeno un corso di **ogni** disciplina.
5. Definizioni di vincolo di integrità e integrità referenziale; poi, per lo schema $R(\underline{A}, B, C)$ con foreign key $R[A,B,C] \subseteq Q[D,E,F]$ e $Q(D, \underline{E}, F^*)$ con "F not null implica F = E", dire se esiste una base di dati in cui (5.1) $\{B, C\}$ non è superchiave in R, (5.2) $\{D\}$ non è superchiave in Q, (5.3) $\{F\}$ non è superchiave in Q.

![[BD-ES-p002.png]]

**Problemi 1 e 2.** Schema: `CompagniaNavale` (IVA, CapitaleSociale) – `Offrono` (DenaroInvestito) – `Crociera` (Codice, Categoria), con `Capofila` (InvestimentoExtra) ISA `Offrono` verso `Adventure` (NumCertificati) ISA Crociera; i porti storicizzati con `InsiemePorti` (Anno, Mese, Giorno) legato a Crociera (1,n) e a `Porto` (Nome, Nazione) tramite `in`. Dizionario dei dati. Nella ristrutturazione Adventure diventa `ISA-A-C`, con il vincolo esterno che la capofila di un'adventure deve anche **offrire** la crociera (riformulazione dell'ISA tra `Capofila` e `Offrono`). Traduzione: `CompagniaNavale`, `Offrono` (foreign key verso compagnia e crociera), `Crociera` (inclusioni verso Offrono e InsiemePorti), `InsiemePorti`.

![[BD-ES-p003.png]]

Seguito della traduzione (`In`, `Porto`, `Adventure`, `Capofila` con foreign key verso Offrono) e **ristrutturazione dello schema logico**: (1) decomposizione orizzontale di Crociera in `CrocieraNonAdventure` e `Adventure` con il vincolo di disgiunzione e una vista `Crociera` come unione; (2) accorpamento di Capofila in Adventure. **Problema 3**: Accordo diventa un'entità (identificata da giornalista e testata), con Testata (0,3), `Garanzia` verso Garante e `Gettone` verso una nuova entità `Articolo` (valore del gettone per articolo).

![[BD-ES-p004.png]]

**Problema 4.**
$$\text{PROJ}_{\text{studente}, \text{disciplina}}(\text{Corso JOIN PianoDiStudi}) - \text{PROJ}_{\text{studente}, \text{disciplina}}(\text{Corso JOIN}_{\text{codice} = \text{codcorso}}\, \text{PianoDiStudi})$$
Il primo join non ha attributi comuni, quindi è il **prodotto cartesiano**: tutte le coppie (studente, disciplina); si tolgono quelle in cui lo studente ha un corso della disciplina ([[02 - BD - Modello Relazionale#Il problema della negazione|negazione con la differenza]]).

```sql
with Discipline as (select distinct disciplina from Corso)
select distinct studente
from PianoDiStudi
where studente not in (
    select distinct studente
    from PianoDiStudi, Discipline
    where (studente, disciplina) not in (select studente, disciplina
                                         from PianoDiStudi join Corso on codice = codcorso))
```
È lo schema del "per ogni": uno studente va bene se non esiste una disciplina che gli manca. A destra, le definizioni di vincolo di tupla, di chiave, foreign key e inclusione (estese per il ripasso).

![[BD-ES-p005.png]]

**Problema 5.** (5.1) **No**: C non è nullo in R, quindi la tupla di Q riferita ha F non nullo, quindi $F = E$, cioè $C = B$; B corrisponde a E, chiave primaria di Q, quindi due tuple di R con stessi B, C riferiscono la stessa tupla di Q, hanno lo stesso A e (A chiave primaria) sono la stessa tupla: $\{B, C\}$ è sempre superchiave. (5.2) **Sì**: basta che due tuple di Q abbiano lo stesso D (D non è chiave), come nell'istanza mostrata. (5.3) **No**: i valori non nulli di F coincidono con E, che sono tutti distinti, e i NULL non sono mai uguali tra loro: $\{F\}$ è sempre superchiave.

---

## Appello del 20/01/2023

![[BD-ES-p006.png]]

**Testo.** (1) Schema ER dei **contratti** tra aziende fornitrici e beneficiarie su un "servizio nativo", con revisioni mensili (incremento del costo, eventuale nuovo servizio); le **consulenze** sono servizi nativi di al massimo un contratto. (2) Progettazione logica con indicazioni di accesso. (3) Adattare lo schema logico (anche con SQL) a: cancellazione a cascata delle revisioni, divieto di modificare i contratti, vincolo sulle revisioni di contratti con consulenza. (4) Query SQL: per ogni contratto IVA del fornitore, codice del servizio, categoria e numero di revisioni che hanno cambiato servizio. (5) Definizioni (vincolo di integrità, di tupla, superchiave, chiave) e tutte le superchiavi di $R(\underline{A}, B, \underline{C}, D)$ con il vincolo "non esistono $t_1, t_2$ con $t_1[D] = t_2[D]$ e $t_1[C] \neq t_2[C]$".

![[BD-ES-p007.png]]

**Problemi 1 e 2.** Schema: `Azienda` (IVA, CapSociale) con `Fornisce` e `Beneficiaria` verso `Contratto` (Costo, Penale), identificato da fornitrice + servizio (`Riguarda`); `RevisioneContratto` (Anno, Mese, Giorno, Incremento) storicizzata con `haStato`, e `NuovoServizio`; `Consulenza` (CostoStandard (0,1)) ISA `Servizio` (Codice, Categoria). Vincolo di dominio: incremento > 0; vincolo esterno: ogni consulenza partecipa al massimo a un contratto. Ristrutturazione con ISA-C-S, traduzione in `Azienda`, `Servizio`, `Consulenza`, `Beneficiaria`…

![[BD-ES-p008.png]]

Seguito: `RevisioneContratto`, `NuovoServizio`, e la **ristrutturazione dello schema logico**: (1) accorpamento di Beneficiaria in Contratto e di NuovoServizio in RevisioneContratto (con un flag `HaNuovoServizio` e il vincolo di tupla sui nulli); (2) accorpamento di Consulenza in Servizio con un flag `Consulenza` e il vincolo che CostoStandard è nullo se non è una consulenza. Schema finale.

![[BD-ES-p009.png]]

Viste per ricostruire le tabelle originali. **Problema 3**: (1) foreign key con `on delete cascade`; (2) trigger `before update` su Contratto che restituisce `NULL` (come il [[04 - BD - Accesso ai Dati da Software#Trigger e transazioni, valore di ritorno|trigger "dontTouch"]]); (3) trigger `before insert` su RevisioneContratto che rifiuta la revisione se il servizio nativo è una consulenza e il nuovo servizio no. **Problema 4**: una `with` che conta le revisioni con nuovo servizio per contratto, più un'unione con i contratti senza revisioni (conteggio 0).

> [!note] Nota
> Nel trigger di (3) la condizione va scritta con `exists`/valori booleani: `IF (SELECT Consulenza FROM Servizio WHERE ...)` restituisce 0/1 secondo il flag scelto, non un booleano. È un dettaglio sintattico che l'esame dichiara di ignorare.

![[BD-ES-p010.png]]

**Problema 5**: definizioni scritte da Simone (vincolo di integrità, vincolo di tupla e di dominio, superchiave, chiave); il punto 5 è rimasto **vuoto**.

> [!example] Soluzione del punto 5 (non svolto)
> Il vincolo dice che **D determina C** ($D \to C$). La chiave primaria è $\{A, C\}$. Una superchiave deve contenere A (nessun vincolo determina A) e C, oppure A e D (perché D determina C, $\{A, D\}$ identifica come $\{A, C\}$). Quindi le superchiavi sono tutti gli insiemi che contengono $\{A, C\}$ o $\{A, D\}$: $\{A,C\}, \{A,D\}, \{A,B,C\}, \{A,B,D\}, \{A,C,D\}, \{A,B,C,D\}$. Gli altri insiemi non contengono A (due tuple possono differire solo in A) oppure contengono A ma né C né D (es. $\{A, B\}$: due tuple con stessi A, B e C diversi sono ammesse).

---

## Appello del 15/02/2023

![[BD-ES-p011.png]]

**Testo.** (1) Schema ER di una **rete sociale**: utenti, amicizie (proponente/accettante), aggiornamenti mensili dello stato dell'amicizia con classificazione **lasca** o **stretta**, utenti "gold" con bonus. (2) Progettazione logica (accesso agli utenti gold; stati lasche/strette acceduti separatamente). (3) Query SQL: per ogni amicizia, "l" o "s" secondo l'ultimo aggiornamento. (4) Definizione di "R soddisfa il vincolo di chiave primaria su A" e query in algebra che restituisce le tuple che lo violano. (5) Per uno schema con E (3,n) – R – F (0,3), G, attributo A ∈ {1,2,3} identificatore con F: istanze con $\text{istanze}(I,G) = \emptyset, \{g_1\}, \{g_1, g_2\}$.

![[BD-ES-p012.png]]

**Problemi 1 e 2.** `Utente` (Codice, Pseudonimo, LivelloSocialità) con `Proponente`/`Accettante` verso `Amicizia`; `StatoAmicizia` (NumContatti, Mese, Anno) con generalizzazione in `Lasca` (NumVolte) e `Stretta` (NumLikeProponente, NumLikeAccettante); `Gold` (età, compenso) con `haBonus`. Vincoli: nessuna amicizia di un utente con se stesso, NumContatti ≥ 0, ogni nuova amicizia nasce lasca, bonus quando l'amicizia di un gold diventa stretta. Ristrutturazione (ISA-G-U, ISA-L-S, ISA-S-S) e traduzione.

![[BD-ES-p013.png]]

Seguito della traduzione e ristrutturazione logica: accorpamento delle tabelle fortemente accoppiate (Proponente, Accettante in Amicizia), accorpamento di Gold in Utente con flag e vincoli di tupla, e decomposizione di `StatoAmicizia` in `StatoAmiciziaLasca` e `StatoAmiciziaStretta` (disgiunte).

![[BD-ES-p014.png]]

Vincoli esterni e viste. **Problema 3**: per le lasche e per le strette, gli stati con (anno, mese) maggiore di tutti gli altri stati della stessa amicizia, uniti.

> [!warning] Correzione
> La query confronta ogni stato solo con gli stati **della stessa tabella**: uno stato lasco viene preso come "ultimo" anche se esiste uno stato stretto più recente. Il confronto `> all` va fatto con l'unione dei due tipi di stato. Inoltre il confronto tra coppie deve escludere lo stato stesso (`>= all` oppure una condizione sulla data diversa), altrimenti `>` con se stesso è sempre falso e nessuna tupla viene selezionata.

**Problema 4**: definizione (nessuna coppia di tuple con lo stesso A e nessun A nullo) e query
$$\text{SEL}_{A \text{ IS NULL}}(R) \cup \text{PROJ}_{A,B,C}(R \text{ JOIN}_{A = A_1 \text{ AND } (B \neq B_1 \text{ OR } C \neq C_1)} \text{REN}_{A_1, B_1, C_1 \leftarrow A, B, C}(R))$$

> [!warning] Correzione
> Negli appunti è scritto $\text{SEL}_{A = \text{NULL}}$: nessuna condizione di uguaglianza è vera con NULL, serve `A IS NULL` ([[02 - BD - Modello Relazionale#Il valore nullo nell'algebra|valori nulli nell'algebra]]).

**Problema 5**: (1) **no**: ogni istanza di E partecipa ad almeno 3 tuple di R, che richiedono un'istanza di G; (2) **no**: le tuple di R devono essere almeno $2 \cdot 3 = 6$ (E ha minimo 3) e al massimo $2 \cdot 3 = 6$ (F ha massimo 3), ma con un solo $g$ le terne distinte possibili sono solo $2 \cdot 2 \cdot 1 = 4$.

![[BD-ES-p015.png]]

(3) **sì**: con $g_1, g_2$ ci sono 8 terne possibili; se ne scelgono 6, tre per ogni $f$, e per ciascun $f$ i valori di A sono 1, 2, 3 (così A con F identifica R).

---

## Appello del 23/02/2024

![[BD-ES-p016.png]]

**Testo.** (1) Schema ER sugli **edifici**: proposti → autorizzati → progettati → costruiti, con aziende diverse per progettazione e costruzione e collaudi (al massimo uno al mese per edificio, uno all'anno per azienda e edificio). (2) Progettazione logica con accesso all'edificio e al suo stato. (3) Su `Esame(studente, corso, voto)` e `Iscritto(studente, università)`: (3.1) gli studenti della Sapienza con media > 25; (3.2) le università senza alcun corso con media > 28. (4) Istanze di uno schema ER (Acquirente, Notaio, Accordo, Prodotto, Acquisto, Fornitore). (5) Progettazione logica fino a SQL di Merce/Veicolo, gestendo inserimenti, cancellazioni e aggiornamenti in modo da limitare i rifiuti.

![[BD-ES-p017.png]]

**Problemi 1 e 2.** Catena di ISA `EdificioCostruito` → `EdificioProgettato` (CostoProgettazione (0,1)) → `EdificioAutorizzato` (metriCubi) → `EdificioProposto` (Codice, ClasseEnergetica, Coordinate, Locazione); `Progettazione` e `Costruzione` verso `Azienda`; `Collaudo` (Esito, Giorno, Mese, Anno) con `haCollaudo` ed `EffettuatoDa`. Vincolo esterno: la stessa azienda non può progettare e costruire lo stesso edificio. Traduzione con foreign key lungo la catena e vincoli esterni di join.

![[BD-ES-p018.png]]

Seguito e ristrutturazione: accorpamento orizzontale dei tre livelli in un'unica tabella `Edificio` con un attributo **Stato** ∈ {0, 1, 2} ([[06 - BD - Progettazione Logica#Accorpamento casi 3 e 3a, accorpamento orizzontale|accorpamento caso 3a]]).

![[BD-ES-p019.png]]

`Edificio(Codice, ClasseEnergetica, Locazione, Coordinate, Stato, metriCubi*, Progettista*, Costo*, Costruttore*)` con vincolo di dominio sullo Stato e vincoli di tupla sui nulli per ogni stato; `Costruito`, `Azienda`, `Collaudo`, `Effettuato` e le viste `Proposto`, `Autorizzato`, `Progettato`.

![[BD-ES-p020.png]]

**Problema 3.**
```sql
-- 3.1
with StudenteMediaAlta as (
    select studente, avg(voto) as MediaVoto
    from Esame group by studente having avg(voto) > 25)
select studente from Iscritto i
where università = 'Sapienza' and i.studente in (select studente from StudenteMediaAlta)

-- 3.2
with MediaCorso as (
    select università, corso, avg(voto) as MediaVoto
    from Esame e join Iscritto i on i.studente = e.studente
    group by università, corso having avg(voto) > 28)
select distinct università from Iscritto
where università not in (select università from MediaCorso)
```

> [!warning] Correzione
> Negli appunti la `having` usa l'alias (`having MediaVoto > 25`): in PostgreSQL gli alias della target list non si possono usare nella `having`, serve ripetere l'aggregato `avg(voto)`. Nella 3.2 serve anche `distinct`.

**Problema 4**: (4.1) **sì**, con Notaio e Accordo vuoti, due prodotti e un acquirente che li acquista dallo stesso fornitore; (4.2) **no**: con Fornitore (2,2) in Accordo, ogni fornitore deve stare in due accordi con acquirenti diversi, ogni acquirente (0,1) in Accordo ma (2,2) in Acquisto, e il ragionamento richiede di aggiungere sempre nuovi acquirenti e fornitori senza fine (come negli [[06 - BD - Progettazione Logica#Progettazione completa ed esercizi|esercizi sulle cardinalità propagate]]). **Problema 5**: ristrutturazione con `ISA-V-M`.

![[BD-ES-p021.png]]

```sql
create table Merce (
    Codice varchar(n) constraint pkMerce primary key,
    Marca  varchar(n));
create table Veicolo (
    Codice varchar(n) constraint pkVeicolo primary key
           constraint fkVeicoloMerce references Merce on delete cascade on update cascade,
    Costo  integer not null);
```
Per limitare i rifiuti, un trigger `before insert` (e `before update`) su Veicolo inserisce in Merce il codice se manca (con marca NULL), invece di far fallire la foreign key; la cancellazione di una merce cancella a cascata il veicolo.

> [!note] Nota
> La sintassi corretta è `CREATE TRIGGER ... BEFORE INSERT ON Veicolo FOR EACH ROW EXECUTE PROCEDURE ...` (negli appunti c'è "into Veicolo" e manca `for each row`).

---

## Appello del 21/01/2022

![[BD-ES-p022.png]]

**Testo.** (1) Schema ER delle **mostre** (allestimenti in diverse città, una persona organizzatrice per città, contributo solo se l'organizzatore è un Premio Nobel; direttori nel tempo, al massimo uno all'anno). (2) Progettazione logica (accesso agli allestimenti con il contributo). (3) Query SQL: per ogni istituto e tipo di azienda, il totale finanziato. (4) In algebra: le aziende finanziate da **tutti** gli istituti. (5) Ristrutturazione di uno schema con relazione ternaria Fornitura (attributo multivalore DataConsegna). (6) Dire se uno schema logico $L$ è una corretta traduzione di uno schema ER con `Q` ISA `R`.

![[BD-ES-p023.png]]

**Problema 1.** `Mostra` (Nome, Costo, Argomento) – `Allestita` (identificatore con città) – `Città` (Codice, Regione), con l'organizzatore `Persona` (CF, data); `AllestitaNobel` (Contributo) ISA Allestita, con `Nobel` (AnnoTitolo) ISA Persona; `Direzione` storicizzata. Dizionario dei dati e vincolo esterno nello schema ristrutturato (l'organizzatore di AllestitaNobel è il Nobel corrispondente all'organizzatore dell'Allestita). Inizio della traduzione.

![[BD-ES-p024.png]]

Seguito e accorpamento di `AllestitaNobel` in `Allestita` con flag `Nobel` e vincoli. **Problema 3**: una `with` con il totale per (istituto, tipo), unita alle coppie senza finanziamenti con totale 0.

**Problema 4**:
$$\text{PROJ}_{\text{codice}}(\text{Azienda}) - \text{PROJ}_{\text{codice}}(\text{PROJ}_{\text{codice}, \text{istituto}}(\text{Azienda JOIN Finanziamento}) - \text{PROJ}_{\text{codice}, \text{istituto}}(\text{Finanziamento}))$$

> [!warning] Correzione
> In Finanziamento l'attributo si chiama `azienda`, non `codice`: il secondo termine va scritto $\text{REN}_{\text{codice} \leftarrow \text{azienda}}(\text{PROJ}_{\text{azienda}, \text{istituto}}(\text{Finanziamento}))$, altrimenti la differenza è tra relazioni con attributi diversi. Il ragionamento è corretto: il join senza attributi comuni è il prodotto cartesiano di tutte le coppie (azienda, istituto); si tolgono le coppie effettive, e le aziende che restano sono quelle a cui manca almeno un istituto.

![[BD-ES-p025.png]]

**Problema 5**: Fornitura reificata in entità con `A` (Farmacia), `Di` (CasaFarmaceutica), `Per` (Farmaco) e l'attributo multivalore DataConsegna trasformato nell'entità `DataConsegna` con `In` (1,n). **Problema 6**: $L$ **non** è corretta: lo schema logico accorpa R in E con $G^*$ nullable, ma un'istanza di R che non appartiene a Q e una che appartiene a Q senza valore di G (G è (0,1)) diventano indistinguibili (entrambe con G NULL). Esempio di istanza: e partecipa a R e a Q con G vuoto.

---

## Appello del 07/02/2022

![[BD-ES-p026.png]]

**Testo.** (1) Schema ER di un **centro spaziale**: astronauti (senior), missioni (speciali con un solo astronauta senior), ruoli nell'equipaggio, fasi della missione con fase finale. (2) Progettazione logica (accesso alle missioni speciali). (3) Query SQL: quanti contratti in `Contratto(codice, azienda, anno)` **non hanno un gemello** (un'altra tupla uguale). (4) In algebra: il codice delle persone con almeno un contratto dopo il 2000 e per cui, se non è nota la professione, è nota l'età. (5) Progettazione logica di uno schema A–R–B con C (1,1). (6) Politiche di reazione: $R(\underline{A}, B)$ default A = 1, foreign key $R[B] \subseteq S[C]$ on delete set default, chiave B; $S(\underline{C}, D)$ foreign key $S[D] \subseteq R[A]$ on delete cascade: esiste una base di dati in cui la cancellazione di una tupla di R provoca un errore?

![[BD-ES-p027.png]]

**Problemi 1 e 2.** `Astronauta` (Codice, Nome, Cognome, Sesso) – `Equipaggio` (Ruolo (1,n)) – `Missione` (Codice, Descrizione); `Senior` (NazioneNascita) ISA Astronauta; `Speciale` (BaseSpazialePartenza) ISA Missione con `EquipaggioSpeciale` ISA Equipaggio; `Fase` (Giorno, Mese, Anno, TipoAttività) con `Finale` (Valutazione). Vincoli esterni (date delle fasi precedenti a quella finale, equipaggio speciale coerente). Ristrutturazione con Ruolo come entità, ISA-S-A, ISA-S-M, ISA-F-F.

![[BD-ES-p028.png]]

Traduzione e accorpamento di Speciale in Missione (`MissioneSpecialeENon` con flag `Speciale` e `BaseSpazialePartenza*`), con la vista `Missione`.

![[BD-ES-p029.png]]

Vista `Speciale`. **Problema 3**, **Problema 4**, **Problema 5** (traduzione: `A`, `B`, `C` con inclusione verso R, `R(A, B, C, R1)` con chiave primaria C e chiave A, B) e **Problema 6**.

> [!warning] Correzione (Problema 3)
> Negli appunti: una `with` raggruppa per (codice, azienda, anno) con `having TOT > 1`, poi `select distinct codice from Contratto except select codice from miavista`. Due problemi: si chiede **quanti contratti** (serve un `count`), e lavorare solo su `codice` sbaglia, perché la stessa persona può avere contratti con gemello e contratti senza. Una soluzione:
> ```sql
> select count(*)
> from (select codice, azienda, anno
>       from Contratto
>       group by codice, azienda, anno
>       having count(*) = 1) as SenzaGemello
> ```
> (Le tabelle SQL sono [[03 - BD - SQL#SQL e modello relazionale|multiinsiemi]]: un "gemello" è proprio una tupla duplicata.)

> [!warning] Correzione (Problema 4)
> Negli appunti la condizione è $\text{professione} = \text{NULL OR età IS NOT NULL}$. "Se la professione non è nota, allora l'età è nota" è l'implicazione $\text{prof IS NULL} \Rightarrow \text{età IS NOT NULL}$, cioè $\text{prof IS NOT NULL OR età IS NOT NULL}$ ([[02 - BD - Modello Relazionale#Vincoli di tupla e di dominio|implicazione come $\lnot\alpha \lor \beta$]]). Inoltre `= NULL` non è mai vero: va usato `IS NULL`. Corretta:
> $$\text{PROJ}_{\text{codice}}(\text{SEL}_{\text{anno} > 2000 \text{ AND } (\text{professione IS NOT NULL OR età IS NOT NULL})}(\text{Persona JOIN Contratto}))$$

> [!warning] Correzione (Problema 6)
> Negli appunti la risposta è "esiste: … l'eventuale tupla $t_3$ di R modifica l'attributo $B = 1$". Ma il default 1 è definito per **A**, non per B: per B il default è NULL. Cancellando una tupla di R si cancellano a cascata le tuple di S con quel D; le tuple di R che riferivano quelle tuple di S ricevono B = NULL, che non viola né la foreign key né il vincolo `unique` su B (i NULL non sono mai uguali). È la stessa analisi fatta nell'[[06 - BD - Progettazione Logica#Progettazione completa ed esercizi|esercizio 3 della progettazione logica]]. Un errore si avrebbe solo se B fosse `not null`.
