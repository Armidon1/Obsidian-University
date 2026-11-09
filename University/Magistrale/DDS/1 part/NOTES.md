# Preferenze e contesto didattico

## 5 novembre 2026

- Avviato con /teach durante la lezione 18: Simone vuole arrivare al masking quorum "un po' per volta".
- Preferenze riprese da `Data Managment/NOTES.md`: DSA, preferisce schemi ed esempi concreti; poca lettura, esercizi subito; domande brevi a testo in chat invece di quiz a scelta multipla; niente punteggi o contatori; feedback sul metodo, non sul rendimento.
- Percorso previsto: 1 N−f e sovrapposizione → 2 server bugiardi, regola f+1 → 3 masking quorum, N>4f → 4 `byzhighestval` e letture concorrenti → 5 regular con firme → 6 regular senza crittografia, pre-write.
- Build: `python3 -I assets/build-lesson.py lessons/X.html assets/quorum.js`. Incorpora CSS e JS: modificare solo gli asset. La pagina non invia risposte all'agente, quindi chiedere l'esito in chat.
- Widget `.qsim` e `form[data-num]` in `assets/quorum.js`. Per la lezione 2 aggiungere i server bizantini a `.qsim`.
