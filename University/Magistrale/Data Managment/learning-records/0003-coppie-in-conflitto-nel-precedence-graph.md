# Coppie in conflitto: tutte, ma non read-read

Il 26 ottobre 2026 Simone ha risposto correttamente alle tre domande della lezione 03: due read non sono in conflitto, l'arco va da chi agisce prima a chi agisce dopo, e il seriale si ottiene da un ordine topologico. In chat ha ricostruito il senso del teorema: un ciclo impedisce un ordine topologico, quindi non esiste un seriale equivalente. Va ancora precisato che il conflitto è tra azioni e che la serializzabilità è una proprietà dello schedule, non delle transazioni. Le due cose sono state spiegate con l'esempio dei due intrecci delle stesse T1 e T2.

Nell'esercizio 04 (`r2(x) r1(x) w1(y) r3(y) w2(z) r4(z) w3(x) r4(y)`) ha fatto due errori di metodo:
1. ha messo archi per coppie read-read (r2·r1 su x, r3·r4 su y), nonostante avesse risposto correttamente alla domanda 01;
2. ha confrontato solo azioni adiacenti nella colonna di un elemento, perdendo r2·w3 (T2 → T3) e w1·r4 (T1 → T4).

Da qui il verdetto sbagliato (ciclo T1 ↔ T2 inesistente). Gli è stata data la regola «per ogni azione scorri fino in fondo alla colonna, salta read-read». Prossimo passo: verificare il trasferimento su uno schedule casuale, poi passare a 2PL (lezione 04).
