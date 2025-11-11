# **CBC-MAC (Cipher Block Chaining – Message Authentication Code)**

> È un **meccanismo di autenticazione dei messaggi ([[MAC]])** basato sulla **modalità [[CBC]]** di un algoritmo di cifratura a blocchi (come [[AES]] o [[3DES]]).  
> Serve a garantire **l’[[Integrity]]** e **l’[[Authenticity]]** dei dati, ma **non la [[Confidentiality]]**.

---

**Come funziona (in sintesi):**
![[Pasted image 20251103112510.png]]

1. Il messaggio è diviso in blocchi ( $P_1, P_2, …, P_n$ ).
    
2. Ogni blocco viene elaborato come in **[[CBC]] encryption**, ma **solo l’ultimo blocco cifrato** viene usato come **[[MAC]]**:  $$C_i = E_k(P_i \oplus C_{i-1})  $$
    con ( $C_0 = IV$ ) (di solito impostato a zero).
    
3. Il **MAC finale** = ( $C_n$ ).
    
4. Il destinatario ricalcola il CBC-MAC sul messaggio ricevuto e confronta il risultato.
    

---

**Garantisce:**

- ✅ **Integrity** – rileva modifiche non autorizzate al messaggio.
    
- ✅ **Authenticity** – solo chi conosce la chiave segreta può produrre un MAC valido.
    

**Non garantisce:**

- ❌ **[[Confidentiality]]** – i dati non sono cifrati.
    
- ❌ **Sicurezza per messaggi di lunghezza variabile**, se non correttamente implementato (può essere manipolato).
    

---

**Varianti più sicure:**

- **[[CMAC]] (Cipher-based MAC):** versione migliorata e standardizzata di CBC-MAC (NIST SP 800-38B).
    
- **XCBC-MAC:** altra estensione sicura per messaggi di lunghezza variabile.
    

---

**Esempi d’uso:**

- Autenticazione in protocolli crittografici simmetrici.
    
- Validazione di dati cifrati o trasmessi in ambienti controllati.
    

---

**In breve:**

> **CBC-MAC** usa la struttura di **CBC** per creare un codice di autenticazione dei messaggi.  
> Garantisce **integrità e autenticità**, ma **non confidenzialità**,  
> e deve essere usato con attenzione — preferibilmente sostituito da **CMAC** o **[[HMAC]]** nelle implementazioni moderne.
> 

## spiegazione dettagliata
Certamente. La tua immagine mostra un diagramma del **CBC-MAC** (Cipher Block Chaining Message Authentication Code) con un'indicazione sul blocco finale, che viene etichettato come "CBC residue".

Nel contesto di un'implementazione standard di CBC-MAC, la funzione hash finale per generare il _Message Authentication Code_ (MAC) non è una semplice concatenazione del "residue" con l'intero messaggio cifrato. Al contrario, **il MAC è il blocco finale intero e non modificato (il "residue") o una sua versione troncata**.

Ecco il dettaglio di come viene generato il MAC a partire dal "CBC residue":

---

### 🔑 Generazione del MAC in CBC-MAC

Il diagramma che hai fornito mostra il processo di applicazione dell'algoritmo di cifratura a blocchi (E) in modalità CBC a una sequenza di blocchi di messaggio ($m_1, m_2, ..., m_n$).

1. Iterazione CBC: Il processo CBC (XOR con il blocco cifrato precedente, seguito dalla cifratura $E$) continua fino all'ultimo blocco di messaggio $m_n$ (nel tuo diagramma, $m_6$).
    
    $$c_i = E_K(m_i \oplus c_{i-1})$$
    
    (Dove $c_0$ è l'IV, solitamente $0$ in CBC-MAC).
    
2. **Il "CBC Residue":** Il risultato della cifratura dell'ultimo blocco di messaggio, $c_n$ (o $c_6$ nel tuo esempio), è il **blocco finale** generato da tutta la catena. Questo blocco è il "CBC residue".
    
3. **Il MAC:** Il Tag di Autenticazione (MAC) finale, che viene inviato con il messaggio per garantirne l'integrità, viene creato a partire da questo blocco $c_n$ in uno di due modi:
    
    - **MAC Intero:** Il Tag è il blocco $c_n$ stesso. Ad esempio, se si usa AES, il MAC è l'intero blocco di **128 bit**.
        
    - **MAC Troncato (più comune):** Per ragioni di sicurezza o di dimensione ridotta del tag, il MAC è costituito dai soli **primi $t$ bit** di $c_n$ (dove $t < 128$). Questa è la pratica più comune per aumentare la sicurezza contro gli attacchi a forza bruta del tag.
        

> **❗ Non è una concatenazione:** È cruciale capire che il MAC è **il blocco finale $c_n$**, o parte di esso. Non viene concatenato _con_ il ciphertext $c_1, c_2, ..., c_{n-1}$, ma è un **output separato** che autentica l'intero messaggio originale ($m_1, ..., m_n$).

### 💡 Come Avviene la Trasmissione

Quando il mittente invia il messaggio:

$$\text{Messaggio Inviato} = \text{Messaggio in Chiaro } (m_1, ..., m_n) \ || \ \text{MAC}$$

Il MAC è, nel caso del diagramma, il blocco $c_6$ o una sua porzione troncata.

### ⚠️ CBC-MAC e Sicurezza

È importante notare che la modalità standard di **CBC-MAC** è sicura solo per **messaggi di lunghezza fissa**.

- Per autenticare messaggi di **lunghezza variabile**, sono state sviluppate varianti come **CMAC (Cipher-based MAC)**, che introduce un passaggio finale con una chiave derivata aggiuntiva per garantire la sicurezza del padding e dell'autenticazione.

Domanda: quindi si possono usare AES-CBC per la [[Confidentiality]] e [[CBC-MAC]] per l'[[Integrity]] e [[Authenticity]], **con la stessa chiave** (esempio di [[EtM]] ma con la stessa chiave)? Assolutamente no! mai usare la stessa chiave! vedi in [[non usare la stessa chiave per autenticazione e cifratura]]. 

Vedi anche [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1#CBC Mode MACs]]

Certamente. Ecco una definizione di **CBC-MAC** che integra e struttura i tuoi appunti, spiegando la sua vulnerabilità critica.

---


### 🚨 Vulnerabilità Critica: Insecurità su Messaggi di Lunghezza Variabile

Questa è la caratteristica fondamentale del CBC-MAC: è un algoritmo **sicuro SOLO per messaggi di lunghezza fissa e nota**. È completamente insicuro quando i messaggi possono avere lunghezze variabili.

Un attaccante che conosce anche solo una coppia valida messaggio-tag $(m, t)$ può, con una certa facilità, falsificare i tag per altri messaggi. Se l'attaccante conosce due coppie $(m, t)$ e $(m', t')$, può condurre un attacco di _forgery_ (falsificazione) molto potente.

#### L'Attacco di Falsificazione ([[Forgery]] attack)

Un attaccante che conosce due coppie messaggio-tag valide, $(m, t)$ e $(m', t')$, può costruire un **nuovo messaggio** $m''$ (più lungo) che il verificatore accetterà erroneamente con il tag $t'$.

Costruzione dell'Attacco:

L'attaccante concatena il primo messaggio $m$ con una versione modificata del secondo messaggio $m'$:

$$m'' = m \mathbin{||} (m1' \oplus t) \mathbin{||} m2' \mathbin{||} \dots \mathbin{||} m\ell'$$

Dove $m1', m2', \dots$ sono i blocchi del messaggio $m'$.

Dimostrazione Tecnica (Perché funziona):

Il CBC-MAC funziona come una catena. L'output di un blocco diventa l'IV (vettore di inizializzazione) per il blocco successivo.

1. **Fase 1:** Il verificatore processa il messaggio $m$. L'ultimo blocco di cifratura (lo stato CBC interno) è, per definizione, $t$.
    
2. **Fase 2:** Il verificatore processa il blocco successivo, che l'attaccante ha creato come $P_{new} = (m1' \oplus t)$.
    
3. **Fase 3 (Il "trucco"):** L'input al cifrario a blocchi è `TestoInChiaroCorrente \oplus CifraturaPrecedente`.
    
    - L'input diventa: $P_{new} \oplus t$
        
    - Che si espande in: $(m1' \oplus t) \oplus t$
        
4. **Fase 4:** A causa delle proprietà dell'operatore XOR, $t \oplus t$ si annulla (diventa 0). L'input al cifrario è quindi semplicemente $m1'$.
    
5. **Fase 5:** L'output di questa fase è $E_K(m1')$ (supponendo un IV a zero per l'inizio del messaggio $m'$), che è _esattamente_ lo stesso stato interno che si avrebbe dopo aver processato il primo blocco di $m'$.
    

Da questo punto in poi, l'elaborazione dei restanti blocchi ($m2', m3'$, ecc.) segue un percorso identico all'elaborazione originale di $m'$, portando inevitabilmente allo stesso tag finale $t'$.

Perché è Pericoloso:

Anche se $m''$ è costruito da blocchi visti in precedenza, la sequenza concatenata può assumere un significato completamente diverso a livello applicativo (es. concatenare più bonifici bancari, comandi IoT, o combinare parti di un firmware) e causare danni reali.

---

### Conclusioni su CBC-MAC

- È sicuro **solo** per messaggi di lunghezza fissa e nota.
    
- **Non devi usare CBC-MAC** per dati di lunghezza variabile. Preferisci alternative moderne come **CMAC** (che è la versione "sistemata" di CBC-MAC) o **HMAC**.
    
- Se è necessaria anche la confidenzialità (cifratura), puoi usare la modalità CBC, ma devi usare una **chiave condivisa diversa** per la cifratura e per il MAC.
    
- Capire questa vulnerabilità è cruciale per una progettazione sicura.
    
- L'unica ragione per cui un ingegnere dovrebbe utilizzare CBC-MAC oggi è per garantire la **retrocompatibilità** con sistemi legacy che non possono essere aggiornati. In tutti gli altri casi, è da considerarsi obsoleto e insicuro.