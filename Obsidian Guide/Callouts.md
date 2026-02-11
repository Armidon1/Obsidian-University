In Obsidian, quelli che stai usando si chiamano **Callouts** (o "Admonitions"). `[!Abstract]` è solo uno dei tanti tipi disponibili di default.

Ce ne sono decine, ognuno con un colore e un'icona specifica. Ecco la lista completa divisa per "vibe" e colore, così puoi scegliere quello giusto per le tue note.

### 1. I "Blu/Azzurri" (Informazioni Generali)

Sono i più neutri, ottimi per note a margine o riassunti.

- `[!note]` (Il classico, blu con la matita).
    
- `[!info]` (Blu, icona "i").
    
- `[!todo]` (Azzurro, per le cose da fare).
    
- `[!abstract]` / `[!summary]` / `[!tldr]` (Quello che usi tu: verde acqua, icona lista).
    

### 2. I "Verdi" (Cose positive o Suggerimenti)

Perfetti per evidenziare soluzioni o consigli.

- `[!tip]` / `[!hint]` / `[!important]` (Verde/Ciano, icona fiammella o stella).
    
- `[!success]` / `[!check]` / `[!done]` (Verde acceso, spunta di verifica).
    

### 3. I "Gialli/Arancioni" (Attenzione e Domande)

Saltano subito all'occhio.

- `[!question]` / `[!help]` / `[!faq]` (Arancione, punto di domanda).
    
- `[!warning]` / `[!caution]` / `[!attention]` (Arancione scuro, triangolo di pericolo).
    

### 4. I "Rossi" (Pericolo e Errori)

Da usare per cose critiche o bug.

- `[!failure]` / `[!fail]` / `[!missing]` (Rosso, icona X).
    
- `[!danger]` / `[!error]` / `[!bug]` (Rosso scuro, fulmine o insetto).
    

### 5. Gli "Speciali" (Grigi o Viola)

- `[!example]` (Viola, per fare esempi pratici).
    
- `[!quote]` / `[!cite]` (Grigio, per le citazioni, simile al blockquote standard ma con lo stile del box).
    

---

### Due trucchi "Pro" per i Callouts

Oltre a cambiare il tipo, puoi fare due cose utilissime che non tutti sanno:

#### 1. Cambiare il Titolo

Di default, se scrivi `[!info]`, il titolo del box sarà "Info". Puoi scriverci quello che vuoi subito dopo la parentesi quadra.

Markdown

```
> [!info] Grammatica Inglese
> Ricordati la differenza tra Who e Whom!
```

#### 2. Renderli "Richiudibili" (Collapsible)

Questa è la funzione migliore per tenere le note pulite. Se aggiungi un **meno (-)** o un **più (+)** subito dopo la chiusura della parentesi quadra, il box diventa un menu a tendina.

- `[-]`: Il box parte **chiuso** (ottimo per spoiler o soluzioni di esercizi).
    
- `[+]`: Il box parte **aperto** ma si può chiudere cliccando.
    

**Esempio pratico:**

Markdown

```
> [!question]- Clicca qui per vedere la soluzione
> La risposta corretta è "To Whom".
```

Ne conoscevi già qualcuno di questi o usavi solo Abstract?