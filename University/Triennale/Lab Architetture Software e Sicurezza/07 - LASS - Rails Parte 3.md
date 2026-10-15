---
title: Rails Parte 3
aliases:
  - LASS — Rails Parte 3
tags:
  - lab-architetture-software-sicurezza
  - rails
  - active-record
  - associazioni
  - transazioni
source: 7 - Rails (part 3).pdf
---

# Rails Parte 3

> [!abstract]
> Terza lezione su Rails: come far **riferire i model gli uni agli altri**. RottenPotatoes si arricchisce di `Moviegoer` e `Review`, e si introducono le **associazioni** Active Record (`belongs_to`, `has_many`, `has_many :through`), che traducono le **foreign key** del database in riferimenti diretti tra oggetti Ruby; le loro opzioni (validazioni, `dependent: :destroy`); le **route annidate** per esprimere RESTfully le risorse "dentro" altre risorse. Poi le **transazioni** e l'**ActiveRecord Query Interface** (`find`, `first`, `find_by`, `where`, `find_each`).
>
> Risponde alla seconda domanda lasciata aperta in [[05 - LASS - Rails Parte 1#Rails e RDBMS|lezione 5]] (come mediare le relazioni tra tabelle e oggetti) e usa i filtri di [[06 - LASS - Rails Parte 2#Controller Filters|lezione 6]]. Le stesse idee lato database sono in Basi di Dati: [[Foreign Key]], [[Join]], [[Transazione]].
>
> Indice dei concetti: [[MOC - Lab Architetture Software e Sicurezza]]. Materiale basato sulle slide del prof. Armando Fox.

---

## Moviegoers e Reviews per RottenPotatoes

Si aggiungono all'app gli utenti (*moviegoer*) e le loro recensioni:

```bash
rails generate model Moviegoer name:string
```

![[LASS-L07-p02.png]]

La migration per le recensioni (da generare con `rails generate migration create_reviews` e poi modificare):

```ruby
# Run 'rails generate migration create_reviews' and then
#   edit db/migrate/*_create_reviews.rb to look like this:
class CreateReviews < ActiveRecord::Migration
  def change
    create_table 'reviews' do |t|
      t.integer    'potatoes'
      t.text       'comments'
      t.references 'moviegoer'
      t.references 'movie'
    end
  end
end
```

Una recensione ha un voto in "patate" (`potatoes`, un intero), un commento e **due riferimenti**: al moviegoer che l'ha scritta e al film recensito. `t.references 'movie'` crea una colonna **`movie_id`**, cioè una **foreign key** verso la tabella `movies`. (Come in [[05 - LASS - Rails Parte 1#Creare il model e la migration|lezione 5]], con Rails ≥5 la classe va scritta `ActiveRecord::Migration[6.1]`.)

**Come facciamo a far riferire i tre model gli uni agli altri?** Ad esempio, come associamo una `Review` a un `Movie` e a un `Moviegoer`?

## Associations

Vedi [[Associazioni ActiveRecord]].

Un'**associazione** è una **relazione logica tra due tipi di entità** (model). Riferimenti: guides.rubyonrails.org/v6.1/association_basics.html e active_record_migrations.html.

Con le associazioni Active Record si **dichiara una connessione** tra due model. In un diagramma UML vorremmo queste relazioni:

![[LASS-L07-p03.png]]

Un **Moviegoer** (1) scrive **zero o più** (0..\*) **Review**; ogni **Review** riguarda **un** (1) **Movie**, e un film ha zero o più recensioni. La `Review` fa quindi da "ponte" tra moviegoer e film: è una relazione molti-a-molti tra `Moviegoer` e `Movie` realizzata con un'entità intermedia (come nel modello ER di [[05 - BD - Progettazione Concettuale|Basi di Dati]]).

### ActiveRecord Associations

Serve un modo per rappresentare le associazioni tra oggetti memorizzati. In un database relazionale si usano le **foreign key**. Ad esempio, per avere tutte le recensioni del film 41:

```sql
SELECT reviews.*
  FROM movies JOIN reviews ON movies.id = reviews.movie_id
  WHERE movies.id = 41
```

In Rails vorremmo invece che ogni oggetto avesse **"riferimenti diretti"** agli oggetti associati: scrivere `movie.reviews` e ottenere le recensioni, senza scrivere il join. Il modulo **`ActiveRecord::Associations`** supporta esattamente questo design.

- Un'associazione **`belongs_to`** crea una connessione con un altro model: **ogni istanza del model che la dichiara "appartiene a" un'istanza dell'altro model**. Rails mantiene la corrispondenza **chiave primaria – foreign key** tra le istanze dei due model. Va messa sul model che **contiene** la foreign key.
- Un'associazione **`has_many`** indica una connessione **uno-a-molti** con un altro model. Di solito si trova "dall'altra parte" di un `belongs_to`.
- In una migration si aggiunge alla tabella `t` una foreign key (un campo che è la chiave primaria di un'altra tabella) con **`t.references :altratabella`**.

```ruby
class Movie < ApplicationRecord
  has_many :reviews
end
class Moviegoer < ApplicationRecord
  has_many :reviews
end
```

![[LASS-L07-p06.png]]

```ruby
class Review < ActiveRecord::Base
  belongs_to :movie
  belongs_to :moviegoer
end
```

La `Review` contiene le colonne `movie_id` e `moviegoer_id`, quindi è lei ad avere i `belongs_to`. (`ApplicationRecord` è la classe base dei model nelle versioni recenti di Rails: eredita a sua volta da `ActiveRecord::Base`.)

| Model | Dichiarazione | Metodi generati (esempi) |
|---|---|---|
| `Movie` | `has_many :reviews` | `movie.reviews`, `movie.reviews <<`, `movie.reviews.build`, `movie.reviews=` |
| `Moviegoer` | `has_many :reviews` | `moviegoer.reviews`, … |
| `Review` | `belongs_to :movie`, `belongs_to :moviegoer` | `review.movie`, `review.moviegoer`, `review.movie=` |

### Più a fondo nelle associazioni

Il modulo `ActiveRecord::Associations` usa la **metaprogrammazione** Ruby per **creare metodi d'istanza** che "attraversano" le associazioni costruendo le query SQL appropriate.

- `has_many` implica una **collezione** degli oggetti posseduti (le `Review`). Si può quindi iterare con i metodi standard delle collezioni (`sort`, `map`, ecc.). Dietro le quinte `has_many` è una **chiamata di metodo** che aggiunge alla classe diversi metodi d'istanza per gestire l'associazione.
- I `belongs_to` in `review.rb` danno a un oggetto `Review` i metodi d'istanza **`movie`** e **`moviegoer`**, che cercano e restituiscono il film e il moviegoer a cui la recensione appartiene. Nota che in entrambi i casi il **nome è singolare**: restituiscono **un solo oggetto**, non una collezione.

![[LASS-L07-p08.png]]

```ruby
# association1.rb
inception = Movie.where(:title => 'Inception').first
# or also: Movie.find_by(:title => 'Inception')
alice,bob = Moviegoer.find(alice_id, bob_id)
# alice likes Inception, bob less so
alice_review = Review.new(:potatoes => 4)
bob_review   = Review.new(:potatoes => 3)
# a movie has many reviews:
inception.reviews = [alice_review, bob_review]
# a moviegoer has many reviews:
alice.reviews << alice_review
bob.reviews << bob_review
# can we find out who wrote each review?
inception.reviews.map { |r| r.moviegoer.name } # => ['alice','bob']
```

Cosa succede:
- si recupera il film *Inception* e i due moviegoer (`find` con due ID restituisce un array, che viene destrutturato in `alice, bob`);
- si creano due recensioni (in memoria);
- **`inception.reviews = [...]`** è una **chiamata di metodo** (il setter `reviews=` generato da `has_many`) che **imposta il campo `movie_id`** di entrambe le recensioni per collegarle a *Inception*;
- `alice.reviews << alice_review` aggiunge la recensione alla collezione di Alice, impostandone il `moviegoer_id`;
- l'ultima riga attraversa due associazioni: dalle recensioni del film al moviegoer di ciascuna, e ne prende il nome.

Nessuna riga di SQL scritta a mano: le foreign key vengono gestite dai metodi generati.

## Through-Associations

Vedi [[Through-Association]].

Siccome ogni `Review` è associata sia a un `Moviegoer` sia a un `Movie`, si può dire che c'è un'**associazione indiretta tra moviegoer e film** (i film che un utente ha recensito). Essendo un pattern ricorrente, Rails offre un'astrazione per semplificarlo: la **through-association**, espressa con l'opzione **`:through`**.

![[LASS-L07-p10.png]]

```ruby
# in moviegoer.rb:
class Moviegoer
  has_many :reviews
  has_many :movies, :through => :reviews
  # ...other moviegoer model code
end
```

Ora `alice.movies` restituisce direttamente i film recensiti da Alice, passando "attraverso" le recensioni.

![[LASS-L07-p11.png]]

Le tre tabelle con dati di esempio:

| movies | | |
|---|---|---|
| **id** | **title** | **rating** |
| 13 | Inception | PG-13 |
| 41 | Star Wars | PG |
| 43 | It's Complicated | R |

| reviews | | | |
|---|---|---|---|
| **id** | **movie_id** | **moviegoer_id** | **potatoes** |
| 21 | 41 | 1 | 5 |
| 22 | 13 | 2 | 3 |
| 23 | 13 | 1 | 4 |

| moviegoers | |
|---|---|
| **id** | **username** |
| 1 | alice |
| 2 | bob |
| 3 | carol |

Le frecce nella figura collegano ogni recensione al suo film (tramite `movie_id`) e al suo moviegoer (tramite `moviegoer_id`). Per trovare i moviegoer che hanno recensito il film 13 Rails genera un **doppio join**:

```sql
SELECT moviegoers.*
  FROM moviegoers JOIN reviews ON moviegoers.id = reviews.moviegoer_id
                  JOIN movies  ON movies.id = reviews.movie_id
  WHERE movies.id = 13
```

Con i dati della figura il risultato è **alice e bob**: le recensioni 22 e 23 riguardano *Inception* (13) e sono state scritte dai moviegoer 2 (bob) e 1 (alice). Carol non ha recensito nulla. Rails genera **query join efficienti** per attraversare le associazioni.

## Opzioni delle associazioni

- Le associazioni hanno **lifecycle hook** propri, che scattano quando un oggetto viene **aggiunto o rimosso** da un'associazione (distinti dagli hook del ciclo di vita degli oggetti stessi visti in [[06 - LASS - Rails Parte 2#Le lifecycle callback|lezione 6]]).
- Si possono dichiarare **validazioni anche sui model associati**.
- Altre opzioni controllano cosa succede agli oggetti **"posseduti"** quando l'oggetto **"proprietario"** viene distrutto. Ad esempio:

```ruby
has_many :reviews, dependent: :destroy
```

fa sì che le recensioni di un film vengano **cancellate dal database** quando il film viene distrutto. Senza questa opzione resterebbero recensioni "orfane", con un `movie_id` che punta a un film inesistente (una violazione dell'integrità referenziale).

> [!warning] Correzione
> Nella slide l'esempio è scritto `has_many: reviews, dependent: destroy`. Non è Ruby valido: il simbolo va scritto con i due punti **prima** del nome (`:reviews`, non `has_many:`), e il valore dell'opzione è anch'esso un simbolo (`:destroy`). Senza i due punti, `destroy` verrebbe interpretato come una chiamata di metodo. La forma corretta è quella riportata sopra.

![[LASS-L07-p13.png]]

```ruby
class Review < ActiveRecord::Base
  # review is valid only if it's associated with a movie:
  validates :movie_id, :presence => true
  # can ALSO require that the referenced movie itself be valid
  #  in order for the review to be valid:
  validates_associated :movie
end
```

Qui una recensione viene **salvata solo se è associata a un film** (`movie_id` presente). `validates_associated :movie` chiede in più che **il film stesso sia valido** secondo le sue validazioni.

> [!note]
> Da Rails 5 `belongs_to` rende già obbligatoria l'associazione per default (l'opzione contraria è `belongs_to :movie, optional: true`), quindi la prima validazione è spesso superflua nelle versioni recenti.

## RESTful Routes for Associations

Vedi [[Nested Routes]].

Come ci si riferisce ad **azioni che coinvolgono oggetti di più model**? Ad esempio, alla creazione o modifica di una recensione bisogna collegarla a un film e a un moviegoer.

Ricordare i dettagli con `session[]` o trucchi simili **non è RESTful** (la richiesta non sarebbe autosufficiente, vedi [[04 - LASS - SaaS Essentials#RESTful URI|lezione 4]]). Nel nostro caso si può fare in modo che le **route stesse riflettano l'"annidamento" logico** delle recensioni dentro i film:

![[LASS-L07-p14.png]]

```ruby
# in routes.rb, change the line 'resources :movies' to:
resources :movies do
  resources :reviews
end
```

![[LASS-L07-p15.png]]

Dopo la modifica, oltre alle route RESTful di base sui film viste nelle lezioni precedenti, compaiono queste:

| Helper | Route RESTful | Azione |
|---|---|---|
| `movie_reviews_path(m)` | `GET /movies/:movie_id/reviews` | index |
| `movie_review_path(m)` | `POST /movies/:movie_id/reviews` | create |
| `new_movie_review_path(m)` | `GET /movies/:movie_id/reviews/new` | new |
| `edit_movie_review_path(m,r)` | `GET /movies/:movie_id/reviews/:id/edit` | edit |
| `movie_review_path(m,r)` | `GET /movies/:movie_id/reviews/:id` | show |
| `movie_review_path(m,r)` | `PUT /movies/:movie_id/reviews/:id` | update |
| `movie_review_path(m,r)` | `DELETE /movies/:movie_id/reviews/:id` | destroy |

Rails usa il nome della risorsa **esterna** per fare in modo che **`:movie_id`** catturi l'ID della risorsa "proprietaria" (il film), mentre **`:id`** corrisponde all'ID della risorsa stessa (la recensione). Gli helper prendono quindi due argomenti: film e recensione.

> [!note]
> Nella tabella della slide (dal libro) l'helper di `create` è `movie_review_path(m)`; in realtà Rails genera `movie_reviews_path(m)` (plurale) sia per index sia per create, come per `movies_path` nella [[06 - LASS - Rails Parte 2#Routes and Controllers|tabella non annidata]].

Si definisce poi un **before-filter** per assicurarsi che `params[:movie_id]` esista nel database:

![[LASS-L07-p16.png]]

```ruby
class ReviewsController < ApplicationController
  before_filter :has_moviegoer_and_movie, :only => [:new, :create]
  protected
  def has_moviegoer_and_movie
    unless (@movie = Movie.where(:id => params[:movie_id]))
      flash[:warning] = 'Review must be for an existing movie.'
      redirect_to movies_path
    end
  end
  public
  def new
    @review = @movie.reviews.build
  end
  def create
    # since moviegoer_id is a protected attribute that won't get
    # assigned by the mass-assignment from params[:review], we set it
    # by using the << method on the association.  We could also
    # set it manually with review.moviegoer = @current_user.
    @current_user.reviews << @movie.reviews.build(params[:review])
    redirect_to movie_path(@movie)
  end
end
```

- il filtro vale solo per `new` e `create` (`:only`);
- se il film non esiste, mette un avviso in `flash` e fa il redirect all'elenco dei film;
- `new` prepara una recensione vuota **già collegata al film** (`@movie.reviews.build` imposta `movie_id`);
- `create` costruisce la recensione con i dati del form e la aggiunge alle recensioni dell'**utente corrente** (`@current_user`, impostato dal filtro di [[06 - LASS - Rails Parte 2#Controller Filters|lezione 6]]): così `moviegoer_id` viene preso dalla sessione e non dal form, e un utente non può firmare una recensione a nome di un altro.

> [!warning] Correzione
> Valgono gli stessi problemi del filtro della [[06 - LASS - Rails Parte 2#Controller Filters|lezione 6]]:
> 1. `before_filter` è stato rimosso in Rails 5.1: si usa **`before_action`**;
> 2. `Movie.where(:id => ...)` restituisce una relation, **sempre truthy** anche se vuota: la condizione dell'`unless` non è mai vera e il controllo "il film esiste?" **non scatta mai**. Inoltre `@movie` sarebbe una relation e non un film, quindi `@movie.reviews` fallirebbe. Si deve scrivere `@movie = Movie.find_by(id: params[:movie_id])`;
> 3. `build(params[:review])` con parametri non filtrati solleva `ForbiddenAttributesError` da Rails 4: servono le strong parameters (`params.require(:review).permit(:potatoes, :comments)`). Il commento sugli *protected attributes* si riferisce al vecchio meccanismo `attr_protected` di Rails 3.

## Transazioni con oggetti Active Record

Vedi [[Transazioni ActiveRecord]].

Le **transazioni** sono **blocchi protetti** in cui le modifiche al database diventano permanenti **solo se riescono tutte**, come se fossero un'unica **azione atomica** (la A di ACID, vedi [[Transazione]] in Basi di Dati).

Garantiscono l'**integrità del database** e proteggono i dati dagli errori di programma, soprattutto quando ci sono **più istruzioni che devono essere eseguite tutte insieme o per niente**. Esempio classico, un bonifico:

```ruby
ActiveRecord::Base.transaction do
  david.withdrawal(100)
  mary.deposit(100)
end
```

Se il versamento a Mary fallisce (eccezione), anche il prelievo da David viene annullato (*rollback*): i soldi non spariscono.

> [!warning] Attenzione
> Il rollback riguarda **il database**, non gli oggetti Ruby: dopo un rollback gli oggetti **non tornano** ai valori che avevano prima della transazione. `david.balance` in memoria potrebbe ancora mostrare il valore decrementato; per riallinearlo bisogna ricaricarlo (`david.reload`).

Anche se il metodo di classe `transaction` viene chiamato su una certa classe Active Record, gli oggetti dentro il blocco **non devono essere tutti istanze di quella classe**: le transazioni sono **per connessione al database**, non per model.

```ruby
Account.transaction do
  balance.save!
  account.save!
end
```

Si può usare anche come metodo d'istanza: `balance.transaction do ... end`. Riferimento: api.rubyonrails.org/v6.1/classes/ActiveRecord/Transactions/ClassMethods.html.

Una transazione agisce su **una sola connessione**. Se classi diverse usano **database diversi**, la transazione non protegge le interazioni tra di essi. Un rimedio è aprire una transazione su ogni classe i cui model vengono modificati:

```ruby
Student.transaction do
  Course.transaction do
    course.enroll(student)
    student.units += course.units
  end
end
```

Non è una grande soluzione (se il commit del database esterno riesce e quello interno no, la consistenza non è garantita)... ma Active Record **non è pensato per transazioni completamente distribuite** (per quelle servono protocolli come il *two-phase commit*).

Infine:
- **`save` e `destroy` sono già avvolti in una transazione**, che garantisce che tutto ciò che si fa nelle validazioni o nelle callback avvenga sotto la sua protezione. Si possono quindi usare le validazioni per controllare i valori da cui la transazione dipende, oppure **sollevare eccezioni nelle callback** (anche negli `after_*`) per fare **rollback**.
- Le **eccezioni sollevate dentro un blocco transazione vengono propagate dopo il rollback**: bisogna essere pronti a catturarle nel codice dell'applicazione (eccezioni in Ruby: docs.ruby-lang.org/en/2.7.0/syntax/exceptions_rdoc.html).

```ruby
begin
  ActiveRecord::Base.transaction do
    david.withdrawal(100)
    mary.deposit(100)
  end
rescue ActiveRecord::RecordInvalid => e
  flash[:alert] = "Transfer failed: #{e.message}"
end
```

## ActiveRecord Query Interface

Vedi [[ActiveRecord Query Interface]].

*"How to find records using a variety of methods and conditions"* (guides.rubyonrails.org/v6.1/active_record_querying.html).

L'interfaccia supporta le query al database in modo **indipendente dal DBMS sottostante** (lo stesso codice funziona con SQLite in sviluppo e PostgreSQL in produzione). I compiti di base sono recuperare **un singolo oggetto** o **più oggetti**, anche **a blocchi** (*in batches*). Le slide coprono i metodi più usati.

### find

Con `find` si recupera l'oggetto corrispondente alla **chiave primaria** indicata. Se non c'è nessun record corrispondente solleva l'eccezione **`ActiveRecord::RecordNotFound`**. Si possono cercare anche più oggetti passando un **array di chiavi primarie**: il metodo restituisce un array con tutti i record trovati.

![[LASS-L07-p22.png]]

```ruby
# Find the customer with primary key (id) 10.
irb> customer = Customer.find(10)
=> #<Customer id: 10, first_name: "Ryan">
```

### first

Trova il **primo record ordinato per chiave primaria**. Restituisce **`nil`** se non trova nulla (nessuna eccezione). Se chiamato su una collezione ordinata con `order`, restituisce il primo secondo quell'ordinamento.

![[LASS-L07-p23.png]]

```ruby
irb> customers = Customer.first(3)
=> [#<Customer id: 1, first_name: "Lifo">, #<Customer id: 2, first_name: "Fifo">, #<Customer id: 3, first_name: "Filo">]
```

Con un argomento numerico `first(n)` restituisce i **primi n** record (un array).

### find_by

Trova il **primo record che soddisfa una o più condizioni**. Restituisce `nil` se non trova nulla; la variante **`find_by!`** solleva invece `ActiveRecord::RecordNotFound`.

![[LASS-L07-p24.png]]

```ruby
irb> Customer.find_by first_name: 'Lifo'
=> #<Customer id: 1, first_name: "Lifo">
```

È il metodo giusto per i controlli "esiste?" dei filtri visti sopra.

### where

`where(*args)` restituisce una **nuova relation**, risultato del **filtraggio** della relation corrente secondo le condizioni negli argomenti.

![[LASS-L07-p25.png]]

```ruby
Customer.where(first_name: 'Lifo').take
```

Si comporta come l'esempio di `find_by`, ma attenzione: qui bisogna chiamare **`take`** sulla relation risultante per ottenere un record. Riferimento: apidock.com/rails/v6.1.3.1/ActiveRecord/QueryMethods/where.

> [!important] Relation, non oggetti
> `where` **non esegue subito la query** e **non restituisce mai `nil`**: restituisce una relation, a cui si possono concatenare altri metodi (`where(...).order(:title).limit(10)`). La query parte solo quando servono i dati (`take`, `first`, `each`, `to_a`). Ecco perché nei filtri delle lezioni 6 e 7 il controllo `unless Movie.where(...)` non funziona.

| Metodo | Restituisce | Se non trova nulla |
|---|---|---|
| `find(id)` | un oggetto | eccezione `RecordNotFound` |
| `find([id1, id2])` | array | eccezione se ne manca uno |
| `first` / `first(n)` | oggetto / array | `nil` / `[]` |
| `find_by(cond)` | un oggetto | `nil` |
| `find_by!(cond)` | un oggetto | eccezione `RecordNotFound` |
| `where(cond)` | relation (lazy) | relation vuota (truthy!) |

> [!tip] Query e sicurezza
> Le condizioni con l'hash (`where(first_name: nome)`) o con i segnaposto (`where("first_name = ?", nome)`) vengono passate al database come **parametri**, non concatenate alla stringa SQL: proteggono dalla [[17 - LASS - Sicurezza delle Web Application#A1 – Injection|SQL injection]]. Scrivere `where("first_name = '#{nome}'")` invece è vulnerabile.

### find_each

Il metodo recupera i record **a blocchi** (*batch*) e poi passa **ciascuno** al blocco. Accetta le opzioni `start`, `finish`, `batch_size` ed `error_on_ignore`.

![[LASS-L07-p26.png]]

```ruby
Customer.find_each(start: 2000, finish: 10000) do |customer|
  NewsMailer.weekly(customer).deliver_now
end
```

Manda la newsletter settimanale ai clienti con ID da 2000 a 10000, caricandoli **1000 alla volta** (la dimensione di default del batch) invece di caricarli tutti in memoria insieme. Riferimento: apidock.com/rails/v6.1.3.1/ActiveRecord/Batches/find_each.

**`find_in_batches`** invece passa al blocco **ogni batch** di record trovati, come array (utile per operazioni di gruppo).
