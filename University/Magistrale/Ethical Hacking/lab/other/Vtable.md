Nasce in C++. Quando hai una classe con [[metodi virtuali]], il compilatore non sa a compile time quale implementazione chiamare — dipende dal tipo reale dell'oggetto a runtime. Risolve così:

```
oggetto in memoria:
[ vptr (8B) ][ campi dati... ]
     ↓
vtable (array di puntatori a funzione):
[ metodo_A* ][ metodo_B* ][ metodo_C* ]
```

Ogni oggetto ha un `vptr` nei primi byte — punta alla vtable della sua classe. Quando chiami `obj->metodo_A()`, il programma fa `obj->vptr[0]()`.

## Perché è exploitabile

La vtable sta in memoria. Il `vptr` sta nell'oggetto heap. Se puoi scrivere sull'oggetto (overflow, fastbin dup, qualsiasi primitiva write) puoi:

- sovrascrivere `vptr` → fai puntare a una vtable falsa che controlli tu
- oppure sovrascrivere direttamente una entry nella vtable

La prossima chiamata a un metodo virtuale → esegui quello che vuoi.

## Differenza pratica rispetto a `__malloc_hook`

| |`__malloc_hook`|vtable|
|---|---|---|
|Linguaggio|C|C++|
|Trigger|qualsiasi `malloc()`|chiamata a metodo virtuale|
|Dove scrivi|variabile globale libc|heap (vptr nell'oggetto)|
|Controllo|un puntatore solo|puoi falsificare tutta la tabella|

## Perché non è nel tuo lab

Il binario del lab è C puro — nessun oggetto C++, nessuna vtable. È una tecnica che vedi nei CTF su binari C++ o in exploit di browser (V8, SpiderMonkey usano vtable ovunque).

Finisci fastbin-dup, poi se vuoi approfondiamo.