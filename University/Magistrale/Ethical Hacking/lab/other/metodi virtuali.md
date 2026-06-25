## Il problema che risolve

In C++ puoi avere una classe base e più classi derivate:

```cpp
class Animale {
    void parla() { printf("..."); }
};

class Cane : public Animale {
    void parla() { printf("Bau"); }
};

class Gatto : public Animale {
    void parla() { printf("Miao"); }
};
```

Se scrivi:

```cpp
Animale *a = new Cane();
a->parla();
```

Senza virtual, il compilatore guarda il tipo del puntatore (`Animale`) e chiama `Animale::parla()` — stampa `"..."`. Non sa che sotto c'è un `Cane`.

## Virtual risolve questo

```cpp
class Animale {
    virtual void parla() { printf("..."); }
};
```

Aggiungendo `virtual`, il compilatore dice "decidi a runtime quale implementazione chiamare, guardando il tipo reale dell'oggetto". Ora `a->parla()` stampa `"Bau"` perché l'oggetto reale è un `Cane`.

Questo meccanismo si chiama **dynamic dispatch** o **polimorfismo**.

## Come lo implementa il compilatore

Non può sapere a compile time quale funzione chiamare — quindi invece di scrivere direttamente l'indirizzo della funzione, scrive:

```
guarda vptr dell'oggetto → vai alla vtable → prendi il puntatore al metodo giusto → chiamalo
```

Ed è lì che entra l'exploitation: quella catena di puntatori sta in memoria heap, e se la controlli tu, controlli quale funzione viene chiamata.