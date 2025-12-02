# Merkle Tree (Albero di Merkle)

> [!Abstract] Definizione
> Il Merkle Tree (o albero di hash) è una struttura dati matematica utilizzata per riassumere e verificare l'integrità di grandi set di dati in modo rapido ed efficiente.

In una blockchain, serve a raggruppare tutte le transazioni di un blocco in un unico codice alfanumerico finale, chiamato Merkle Root (Radice di Merkle).

## Struttura (Dal basso verso l'alto)

Immagina un albero rovesciato:

1. **Foglie (Leaf Nodes):** Alla base ci sono le transazioni vere e proprie (es. Tx A, Tx B, Tx C, Tx D). Ogni transazione viene convertita in un _Hash_.
    
2. **Rami (Branch Nodes):** Gli hash vengono accoppiati e "hashati" insieme (es. Hash(A) + Hash(B) = Hash(AB)).
    
3. **Radice (Merkle Root):** Il processo si ripete salendo fino a quando rimane un solo hash in cima. Questo è il _Merkle Root_.
    

## Perché è geniale? (L'Effetto Valanga)

Il Merkle Root è un'impronta digitale unica di tutte le transazioni nel blocco.

- Se modifichi anche solo una virgola nella transazione alla base dell'albero...
    
- Cambia il suo Hash...
    
- Cambia l'Hash del ramo superiore...
    
- Cambia l'Hash della radice.
    
    Risultato: Qualsiasi manomissione è immediatamente evidente perché il Root finale non corrisponderà più.
    

## **A cosa serve (Casi d'uso)**

### 1. Efficienza (Light Nodes & SPV)

Questo è il vantaggio principale. Immagina di avere Bitcoin sul cellulare (un "Light Node"). Il tuo telefono non ha spazio per scaricare la storia intera di Bitcoin (centinaia di GB).

- **Senza Merkle Tree:** Per verificare se hai ricevuto un pagamento, dovresti scaricare tutto il blocco e controllarlo riga per riga.
    
- **Con Merkle Tree (Merkle Proof):** Il tuo telefono scarica solo la **Merkle Root** (che è minuscola) e chiede ai nodi completi solo i pochi hash necessari per ricostruire il percorso dal tuo pagamento alla radice.
    
- _Analogia:_ Per sapere se una parola è in un libro, non devi leggere tutto il libro; ti basta guardare l'indice.
    

### 2. Integrità dei Dati

Garantisce che i dati ricevuti in una rete peer-to-peer non siano stati alterati o corrotti durante il download.

Esempio Pratico: Bitcoin

In un blocco Bitcoin:

- L'**Header del blocco** (l'intestazione) contiene la _Merkle Root_.
    
- Il corpo del blocco contiene migliaia di transazioni.
    
    Per collegare i blocchi tra loro (la "chain"), si usa l'hash dell'Header. Quindi, grazie al Merkle Root, sigillando l'header si sigillano automaticamente tutte le migliaia di transazioni sottostanti.
    

## **Concetti Correlati**

- **[[Hashing|Hash Function]]:** Il "motore" che permette di costruire l'albero.
    
- **SPV (Simple Payment Verification):** Il metodo usato dai wallet leggeri che si basa sui Merkle Trees.
    
- **State Trie ([[Ethereum]]):** Una versione più complessa del Merkle Tree usata da Ethereum per gestire non solo le transazioni, ma lo stato attuale dei conti (saldi).
    

---
