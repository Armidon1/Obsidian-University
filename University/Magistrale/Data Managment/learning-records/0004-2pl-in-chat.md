# 2PL fatto in chat, una domanda alla volta

Il 26–27 ottobre 2026 Simone non riusciva a leggere per l'ansia, quindi il 2PL è stato fatto in chat con domande brevi. Ha risposto bene su: read-read con soli lock esclusivi forza un unlock; dopo l'unlock il lock su y deve essere già preso; `r1(x) r2(x) w2(y) r1(y)` è no con X e sì con S/X; esercizio 03, parte X (T2 deve cedere x a r3(x) e poi riprenderlo per w2(x)).

Due sviste ricorrenti: (1) pensa che il 2PL obblighi a prendere tutti i lock all'inizio (è il conservative 2PL); (2) ha visto un ciclo T1 ↔ T2 inesistente, contando read-read come conflitto. Ha chiesto il senso delle due fasi: spiegato con la «finestra» che crea un ciclo e con il lock point. Il ripasso è in `lessons/0004b-2pl-ripasso-dalla-chat.html`. Prossimo passo: esercizio 03 parte S/X (passi A–C), poi strict/rigorous.
