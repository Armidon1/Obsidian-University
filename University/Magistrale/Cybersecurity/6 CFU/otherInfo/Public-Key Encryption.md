# 🔑 Public Key Encryption (Crittografia a Chiave Pubblica)

La **Crittografia a Chiave Pubblica** (o _Public Key Cryptography_, PKC) è un **sistema crittografico** che utilizza una **coppia di chiavi** matematicamente correlate per garantire la [[Confidentiality]] e l'[[Authentication]]:

1. Una **Chiave Pubblica:** Può (e deve) essere distribuita liberamente. Viene usata per **cifrare** i dati e per **verificare le firme digitali**.
    
2. Una **Chiave Privata:** Deve essere mantenuta rigorosamente segreta dal proprietario. Viene usata per **decifrare** i dati e per **creare firme digitali**.
    

![Immagine di Public Key Encryption data flow](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcT2r23QmVsLMxQZm2sDUKYQklJYpXaPqcMSy0AYZrYciJJZ7xW4XQyikaiC2xmDSMEYeHcb6GQo7g6JBxs42afK9mMNtRhUE2CNCj0zMOP6eEj7eu4)


Per un ingegnere, la sua proprietà fondamentale è l'**asimmetria funzionale**: i dati cifrati con la chiave pubblica possono essere decifrati _solo_ dalla corrispondente chiave privata.

Il suo scopo principale è risolvere due problemi fondamentali:

1. **[[Confidentiality]] (Scambio Chiavi):** Permette a due parti (es. Alice e Bob) di stabilire un canale sicuro (di solito scambiandosi una chiave simmetrica) senza aver mai condiviso un segreto in precedenza. Alice cifra la chiave di sessione usando la chiave pubblica di Bob. Potrebbe pure garantire [[Confidentiality]] semplicemente cifrando ogni singolo pacchetto con la chiave pubblica del destinatario (per poi essere decifrato dalla chiave privata del destinatario) ma per larga scala di pacchetti non è efficiente.
    
2. **[[Authentication]] (Firme Digitali):** Permette ad Alice di _firmare_ un messaggio con la sua chiave privata. Chiunque può usare la chiave pubblica di Alice per verificare che il messaggio provenga da lei e non sia stato alterato. Ancora di più, questo garantisce una proprietà più forte: [[Non-Repudiation]].
    

---

### Spiegazione: Perché "Asimmetrico" non implica "a Chiave Pubblica"

Questa è una distinzione tecnica importante che spesso viene trascurata, poiché nel linguaggio comune i due termini sono usati come sinonimi.

1. Crittografia Asimmetrica ([[Asymmetric Encryption]]):
    
    Questa è la proprietà matematica di un algoritmo. Definisce qualsiasi sistema crittografico in cui la chiave usata per la cifratura ($K_E$) è diversa dalla chiave usata per la decifratura ($K_D$).
    
    > $K_E \neq K_D$
    
2. Crittografia a Chiave Pubblica (Public Key Encryption):
    
    Questa è la politica di gestione e l'implementazione di un sistema asimmetrico. È definita dal fatto che una delle due chiavi (la $K_E$) è intenzionalmente resa pubblica, cioè non è un segreto.
    

**Perché non sono la stessa cosa?**

La "Crittografia Asimmetrica" non implica la "Crittografia a Chiave Pubblica" perché si può teoricamente costruire un sistema in cui le chiavi $K_E$ e $K_D$ sono diverse (asimmetriche), ma **entrambe sono tenute segrete**.

#### Esempio Teorico

Immagina un sistema (non-PKC) in cui un'autorità centrale fidata (CA) genera una coppia di chiavi asimmetriche ($K_E, K_D$) per un server.

- La CA installa la chiave di decifratura ($K_D$) sul **Server B** e la mantiene segreta.
    
- La CA consegna la chiave di cifratura ($K_E$) al **Client A** e gli ordina di mantenerla segreta.
    

In questo scenario:

- Il sistema è **asimmetrico** (le chiavi $K_E$ e $K_D$ sono diverse).
    
- Il sistema **non è a chiave pubblica**, perché la chiave di cifratura ($K_E$) è un segreto, non è pubblica.
    

**In sintesi:**

- **Asimmetrico** descrive la _matematica_ (le chiavi sono diverse).
    
- **A Chiave Pubblica** descrive l'_architettura_ e la _gestione_ (una delle chiavi è nota a tutti).
    

Nella pratica quotidiana, l'unico uso diffuso della crittografia asimmetrica è la crittografia a chiave pubblica (come RSA o ECC), motivo per cui i termini sono usati in modo interscambiabile.