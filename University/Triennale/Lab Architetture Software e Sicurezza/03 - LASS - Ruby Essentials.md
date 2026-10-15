---
title: Ruby Essentials
aliases:
  - LASS — Ruby Essentials
tags:
  - lab-architetture-software-sicurezza
  - ruby
  - linguaggi
source: 3 - Ruby Essentials.pdf
---

# Ruby Essentials

> [!abstract]
> Introduzione rapida a **Ruby**, il linguaggio su cui è costruito Rails: principi (interpretato, tipizzato dinamicamente, tutto è un oggetto), installazione e strumenti, tipi di dato, commenti, condizioni e valori *truthy/falsey*, i diversi tipi di variabile, classi e accessor, metodi con `!`, `?` e `=`, array, blocchi, range, cicli, hash, espressioni regolari e qualche zucchero sintattico.
>
> Serve come base per [[05 - LASS - Rails Parte 1]], [[06 - LASS - Rails Parte 2]] e [[07 - LASS - Rails Parte 3]]: molte "magie" di Rails (associazioni, `attr_accessor`, callback) sono semplicemente **metaprogrammazione Ruby**. Le espressioni regolari tornano nelle step definition di Cucumber ([[08 - LASS - Behavior-Driven Development#Step Definitions|lezione 8]]).
>
> Indice dei concetti: [[MOC - Lab Architetture Software e Sicurezza]]. Materiale basato sulle slide del prof. John Yang.

---

## Ruby in 100 secondi

![[LASS-L03-p02.png]]

La slide rimanda al video *"Ruby in 100 Seconds"* di Fireship (youtube.com/watch?v=UYm0kfnRTJk), una panoramica velocissima del linguaggio. Il rubino rosso è il logo di Ruby.

## Ruby: i principi

Vedi [[Ruby]].

Ruby è *"a minimalistic language with rich libraries and few mechanisms"*: un linguaggio con pochi meccanismi di base ma librerie ricche. I suoi principi:

1. **Interpretato**: non si compila, il codice viene eseguito da un interprete (`ruby file.rb`).
2. **Tipizzato dinamicamente** (*dynamically typed*): il tipo appartiene ai valori, non alle variabili; una variabile può contenere prima un numero e poi una stringa, e gli errori di tipo emergono solo a runtime.
3. **Object oriented: tutto è un oggetto**, anche i numeri e `nil`. Di conseguenza:
   - **ogni operazione è una chiamata di metodo** (`5 + 3` è in realtà `5.+(3)`, vedi [[#Extras|più avanti]]);
   - **ogni chiamata di metodo restituisce un valore**, cioè un oggetto;
   - **ogni istruzione è un'espressione** che restituisce un valore (anche `if`).
4. **L'accesso alle variabili d'istanza dall'esterno della classe avviene solo tramite metodi accessor**: le variabili d'istanza senza accessor pubblici sono di fatto **private**.

## Installazione e strumenti

- Installazione: ruby-lang.org/it/documentation/installation/
- **RVM** (Ruby Version Manager) per Linux e macOS: permette di avere più versioni di Ruby e passare dall'una all'altra (rvm.io).
- **RubyInstaller** per Windows (rubyinstaller.org).
- **WSL** (Windows Subsystem for Linux) per Windows: l'alternativa consigliata per lavorare in un ambiente Linux.
- Editor: **Visual Studio Code** con le estensioni Ruby, oppure l'IDE **RubyMine** di JetBrains.

## Primi passi

1. Controllare l'installazione: `ruby --version`
2. Eseguire un file con l'interprete: `ruby hello_world.rb`
3. Usare la console interattiva **irb** (*Interactive Ruby*): `irb`

```ruby
puts "Hello World by Ruby!"
```

`puts` (*put string*) stampa una stringa seguita da un a capo.

> [!warning] Correzione
> Nella slide il comando è scritto `ruby -–version`, con un trattino normale seguito da un trattino lungo (un effetto della correzione automatica dell'editor delle slide). Copiato così non funziona: il comando corretto è `ruby --version`, con due trattini normali.

## Tipi di dato

**Tutto è un oggetto**: numerici (`Integer`, `Float`), booleani (`true`, `false`), stringhe (`String`), e così via. Ogni valore ha una classe e dei metodi: `3.class` restituisce `Integer`, `"ciao".upcase` restituisce `"CIAO"`.

## Commenti

```ruby
# commento su una riga

=begin
  commento
  su più righe
=end
```

> [!note]
> `=begin` e `=end` **non possono essere indentati**: devono stare all'inizio della riga.

## Condizioni, truthy e falsey

Vedi [[Truthy e Falsey]].

```ruby
if conditional [then]
  code...
[elsif conditional [then]
  code...]...
[else
  code...]
end

puts "you are still young" if age < 105   # if in linea (modificatore)
```

Operatori logici: `&&` (and), `||` (or), `!` (not).

I valori booleani ammessi sono `true` e `false`. Ma in una condizione si può mettere **qualsiasi valore**:
- un valore non booleano che conta come vero si dice **truthy**; uno che conta come falso si dice **falsey**;
- **solo `nil` (e `false`) sono falsey**;
- **tutti gli altri valori sono truthy**, compresi il numero `0`, la stringa vuota `""` e l'array vuoto `[]`.

> [!important] Diverso da C e Python
> In C `0` è falso, in Python `0`, `""` e `[]` sono falsi. In Ruby **sono tutti veri**. `if 0 then puts "vero" end` stampa "vero".

`nil` può significare sia falsità booleana sia **una variabile che non si riferisce a nulla**. È usato come risultato di un'operazione che altrimenti non darebbe un valore significativo (es. cercare un elemento che non c'è). Questo tornerà nel [[06 - LASS - Rails Parte 2#Backtracing|debugging]]: l'errore `undefined method for nil:NilClass` nasce proprio da un `nil` inatteso.

## Tipi di variabili

Vedi [[Tipi di Variabili in Ruby]].

In Ruby il **tipo di variabile si capisce dal nome**:

| Forma | Tipo | Visibilità |
|---|---|---|
| `local_variable` | variabile locale | il blocco o metodo corrente |
| `@instance_variable` | variabile d'istanza | il singolo oggetto |
| `@@class_variable` | variabile di classe | condivisa da tutte le istanze della classe |
| `ClassName` | nome di classe | globale (è una costante) |
| `Constant` / `CONSTANT` | costante | inizia con la maiuscola |
| `$global_variable` | variabile globale | tutto il programma |

`foo`, `@foo`, `@@foo`, `FOO`, `Foo` e `$FOO` sono **tutte variabili distinte**.

## Classi

Vedi [[Classi Ruby e Accessor]].

```ruby
class ClassName
  @@class_variable_default = "something_default_shared"
  CONSTAT = '192.168.0.1'
  def initialize(first_arg, second_arg = 0, *other_args)
    @instance_var1 = first_arg
    @instance_var2 = sec_arg
  end
  # metaprogramming
  attr_accessor :instance_var1  # can read and write this attribute
  attr_reader :instance_var2    # can only read this attribute
end
```

Cosa mostra l'esempio:
- `@@class_variable_default` è una **variabile di classe**, condivisa da tutte le istanze;
- `CONSTAT` è una **costante** (il nome è un refuso per `CONSTANT`, ma funziona lo stesso: basta l'iniziale maiuscola);
- `initialize` è il **costruttore**, chiamato da `ClassName.new(...)`. I parametri mostrano tre casi: obbligatorio (`first_arg`), con **valore di default** (`second_arg = 0`) e **variadico** (`*other_args` raccoglie in un array tutti gli argomenti in più);
- `attr_accessor :instance_var1` genera **automaticamente** due metodi, il getter `instance_var1` e il setter `instance_var1=`; `attr_reader` genera solo il getter. È **metaprogrammazione**: codice che scrive codice (metodi) al momento della definizione della classe.

> [!warning] Correzione
> Nel costruttore della slide c'è `@instance_var2 = sec_arg`, ma il parametro si chiama `second_arg`. Così com'è, `ClassName.new(1)` solleva `NameError: undefined local variable or method 'sec_arg'`. La riga corretta è `@instance_var2 = second_arg`.

### Esempi di codice delle classi

Il repository github.com/dcdelia/lab-assi (cartella `ruby-intro/examples`) contiene sei esempi:
1. una classe simile a quella appena vista;
2. dichiarazione **verbosa vs concisa** di getter, setter e inizializzazione (scrivere `def name; @name; end` a mano oppure usare `attr_accessor`);
3. sottoclassi e getter/setter;
4. sottoclassi e **polimorfismo**;
5. **effetti collaterali** di un metodo;
6. liste di argomenti di **lunghezza variabile**.

### Controllare la classe di un'istanza

```ruby
oggetto.class            # restituisce la classe dell'oggetto
oggetto.is_a?(NomeClasse) # true se è un'istanza di NomeClasse o di una sua sottoclasse
```

## Metodi e convenzioni sui nomi

I nomi dei metodi possono terminare con `!`, `?` o `=`:

```ruby
def title=(new_title)   # metodo di assegnamento: si chiama con obj.title = "x"
def is_year_leap?()     # restituisce un booleano
def capitalize!()       # ha un effetto collaterale sull'oggetto su cui è chiamato
```

- `=`: metodo di **assegnamento** (setter). Nota della slide: restituisce **sempre il suo argomento**, qualunque cosa ci sia scritto dentro, perché `x = (obj.title = "y")` deve valere `"y"`.
- `?`: per convenzione restituisce un **booleano** (es. `empty?`, `include?`).
- `!`: per convenzione indica un metodo **"pericoloso"**, di solito perché **modifica l'oggetto** invece di restituirne una copia: `s.capitalize` restituisce una nuova stringa, `s.capitalize!` modifica `s`. In Rails si vedrà anche `save!`, che solleva un'eccezione invece di restituire `false`.

**Tutti i metodi restituiscono un valore.** Se manca un `return` esplicito, il valore restituito è quello **dell'ultima espressione valutata**.

## Array

- Documentazione: ruby-doc.org/core-3.1.1/Array.html
- L'indice parte da **0**.
- Si dichiarano con le **parentesi quadre** `[]`.
- Elementi separati da virgole; un array può contenere **tipi diversi** (`[1, "due", :tre, nil]`).

## Blocchi

Vedi [[Blocchi Ruby]].

Un **blocco** è letteralmente un "blocco" di codice che può essere **passato a un metodo e chiamato** da esso. Si definisce con le **graffe `{ }`** oppure con **`do ... end`**:

```ruby
[1, 2, 3].each { |n| puts "Current number is: #{n}" }

[1, 2, 3].each do |n|
  text = "Current number is: #{n}"
  puts text
end
```

- `each` è un metodo dell'array che chiama il blocco una volta per elemento; `|n|` è il **parametro del blocco**.
- `#{n}` è l'**interpolazione di stringhe**: inserisce il valore di `n` nella stringa (funziona solo con le virgolette doppie).
- Per convenzione si usano le graffe per i blocchi di una riga e `do...end` per quelli su più righe.

I blocchi sono ovunque in Ruby e in Rails: `ActiveRecord::Base.transaction do ... end`, `describe ... do ... end` in RSpec, `create_table ... do |t| ... end` nelle migration.

## Range

Vedi [[Range Ruby]].

Un **range** è una collezione dei valori compresi tra un inizio e una fine:

```ruby
(1..4).to_a        # => [1, 2, 3, 4]        due punti: estremo incluso
('a'..'d').to_a    # => ["a", "b", "c", "d"]
(1...4).to_a       # => [1, 2, 3]           tre punti: estremo escluso
r = (..4)          # => nil..4, beginless (senza inizio)
r = (1..)          # => 1.., endless (senza fine)
r.include?(-50)    # => true se r = (..4)
```

L'ultima riga si riferisce al range *beginless* `(..4)`: −50 è minore di 4, quindi è incluso.

Un range infinito si può iterare se si esce esplicitamente:

```ruby
a = []
r = (1..)
r.each do |i|
  a.push(i) if i.even?
  break if i > 10
end
# a => [2, 4, 6, 8, 10]
```

Il ciclo aggiunge i numeri pari e si ferma con `break` appena `i` supera 10 (a `i = 11`, che è dispari e non viene aggiunto).

## Cicli

```ruby
for i in 1...10        # da 1 a 9
  puts i
end

3.times do             # ripete il blocco 3 volte
  puts "Hello!"
end

a = ['gio', 'nick', 'ale']
for i in a             # itera sugli elementi dell'array
  puts i
end

i = 0; t = 3
while i < t do
  puts("Iteration i = #{i}")
  i += 1
  if i >= t; break; end
end
```

In Ruby idiomatico si preferiscono i metodi con blocco (`each`, `times`, `map`) al `for`. Nel `while` dell'esempio il `break` è ridondante (la condizione `i < t` basta già), serve solo a mostrare la sintassi.

## Hash

Vedi [[Hash e Simboli Ruby]].

Gli **hash** sono quelli che altri linguaggi chiamano **array associativi** o **hashmap** (dizionari in Python): coppie chiave → valore.

```ruby
h = {foo: 0, :bar => 1, 'baz': 2, '1':3}
h[:foo]          # => 0
h[:foo] = 2      # modifica il valore
h.delete(:foo)   # rimuove la coppia
h = {}           # hash vuoto
```

L'esempio mostra più sintassi equivalenti. `:foo` è un **simbolo**: una stringa immutabile e unica, usata tipicamente come chiave. `foo: 0` è la forma abbreviata di `:foo => 0`.

> [!note] Una sottigliezza
> Anche `'baz': 2` e `'1':3` creano chiavi **simbolo** (`:baz` e `:"1"`), non stringhe: la sintassi `'testo': valore` è un'altra forma abbreviata per i simboli. Quindi `h['baz']` restituisce `nil`, mentre `h[:baz]` restituisce 2. Per avere chiavi stringa serve la freccia: `'baz' => 2`.

## Espressioni regolari

- Documentazione: ruby-doc.org/core-3.1.1/Regexp.html

```ruby
'haystack' =~ /hay/      # => 0: posizione del (primo) match, nil se non c'è
/a+/.match('haystack')   # => MatchData, nil se non c'è
```

Le espressioni regolari si delimitano di solito con gli **slash** `/.../`. Se una stringa contiene il pattern si dice che **fa match**. Siccome `nil` è falsey e un numero è truthy, il risultato di `=~` si può usare direttamente in un `if`.

## Extras

Ruby permette di **omettere le parentesi** attorno agli argomenti quando non crea ambiguità (*"poetry mode"*): `puts "ciao"` invece di `puts("ciao")`.

Quando l'**ultimo argomento** di un metodo è un hash, si possono **omettere le graffe**: `foo(arg, key: val)` equivale a `foo(arg, {key: val})`. È lo stile di Rails: `validates :title, presence: true` è una chiamata di metodo con un simbolo e un hash.

![[LASS-L03-p20.png]]

La tabella mostra lo **zucchero sintattico** (*sugared*) accanto alla forma reale (*de-sugared*), e conferma che *ogni operazione è una chiamata di metodo*:

| Sugared | De-sugared |
|---|---|
| `10 % 3` | `10.modulo(3)` |
| `5+3` | `5.+(3)` |
| `x == y` | `x.==(y)` |
| `a * x + y` | `a.*(x).+(y)` |
| `a + x * y` | `a.+(x.*(y))` |
| `x[3]` | `x.[](3)` |
| `x[3] = 'a'` | `x.[]=(3,'a')` |

Le righe 4 e 5 mostrano anche la **precedenza degli operatori**: in `a + x * y` la moltiplicazione viene valutata per prima, quindi è l'argomento di `+`.

## Hands-on

Laboratorio tratto dal libro del corso (*Engineering Software as a Service*, Fox e Patterson): github.com/dcdelia/lab-assi, cartella `ruby-intro/book-lab`.
