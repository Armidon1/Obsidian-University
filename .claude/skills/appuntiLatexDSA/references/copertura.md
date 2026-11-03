# Matrice di copertura delle fonti

Usa `inventario/copertura.json`, indipendente dalla numerazione dei capitoli. Un contenuto può provenire da più fonti e avere più destinazioni; due spiegazioni ripetute possono confluire nella stessa destinazione. Scegli una granularità che permetta di verificare separatamente condizioni, esempi ed eccezioni importanti, evitando sia una voce per ogni parola sia un'unica voce per tutta la lezione.

```json
{
  "version": 1,
  "items": [
    {
      "id": "C001",
      "content": "Distinzione fra capacità suggerita dagli import e comportamento osservato; includere il caso della chiamata non raggiunta.",
      "sources": ["Lezione 3, sezione Imports", "Lezione 4, sezione sui limiti"],
      "destinations": [
        {"file": "capitoli/02-metodo.tex", "label": "sec:capacita-osservazione"}
      ],
      "review": {
        "status": "pending",
        "note": "Da confrontare con le fonti dopo la stesura."
      },
      "literals": ["GetProcAddress"]
    }
  ]
}
```

- `id`: stabile e univoco, anche dopo uno spostamento del capitolo.
- `content`: ciò che deve essere spiegato e preservato; una descrizione precisa, non necessariamente la frase da usare nel libro.
- `sources`: riferimenti non vuoti e rintracciabili ai materiali, con pagina, sezione o altro localizzatore quando disponibile. Lo script non verifica il contenuto delle fonti.
- `destinations`: percorsi `.tex` relativi al volume e inclusi da `main.tex`, con etichette della spiegazione. Preferisci etichette di sezione o sottosezione. Il controllo dei letterali parte dopo l'etichetta e termina alla successiva intestazione dello stesso livello o superiore.
- `review`: dopo aver confrontato fonte e spiegazione, imposta `status` a `verified` e scrivi una nota concreta: passaggi ed eccezioni controllati, accorpamenti effettuati, eventuale dubbio conservato. `pending` fa fallire il controllo finale. Un dubbio esplicitamente conservato può essere coperto: verificare la fedeltà non significa risolverlo inventando una risposta.
- `literals`: facoltativo, per nomi API, identificatori, valori, citazioni o notazioni che devono apparire con precisione. Il confronto distingue maiuscole e minuscole, normalizza parte del markup LaTeX e gli spazi, ed esclude diagrammi e indici. Una presenza letterale non dimostra una spiegazione corretta. Non richiedere una corrispondenza letterale per concetti parafrasabili.

Prima di marcare una voce come verificata, controlla che i passaggi richiesti siano nella prosa e non soltanto in un disegno. Registra una motivazione reale; non autocompilare `verified` perché un termine è stato trovato.

```bash
python3 -I <skill>/scripts/check_coverage.py <corso>/appunti
```

Lo script segnala voci senza fonti o destinazioni, etichette mancanti, file non inclusi, revisioni pendenti, letterali assenti e capitoli di contenuto senza destinazioni nella matrice. `problems: 0` prova la coerenza dei registri e dei riscontri automatici; il giudizio di completezza resta editoriale. I nomi `00-*`, `98-*` e `99-*` sono riservati alle parti comuni e non richiedono una voce autonoma per ogni capitolo.

Per i volumi precedenti, in assenza di `copertura.json`, lo script legge soltanto gli inventari `NN.txt` di due cifre, con una voce letterale per riga e commenti `#`. Se è presente la matrice, questa è il riferimento e i vecchi `.txt` non vengono usati. Non occorre riscrivere un volume esistente solo per migrare il registro.
