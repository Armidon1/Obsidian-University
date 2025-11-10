# 🔄 Output Feedback (OFB)

### Definizione
**OFB (Output Feedback)** è una modalità operativa che trasforma un cifrario a blocchi (come AES) in un **cifrario a flusso sincrono** ([[Symmetric Encryption|synchronous]] [[Stream Cipher]] ).

In questa modalità, il _keystream_ viene generato crittografando ripetutamente un valore di inizializzazione. La caratteristica chiave è che l'**output** della funzione di cifratura viene "reimmesso" (feedback) come **input** per il blocco successivo. Il keystream risultante viene poi combinato (tramite XOR) con il plaintext per produrre il ciphertext.

### Meccanismo di Funzionamento

Il flusso di dati è separato dalla generazione del keystream.

1. **Inizializzazione:** Si parte con un **IV (Initialization Vector)**.
    
2. **Generazione Keystream:** L'IV viene cifrato con la chiave $K$ per ottenere il primo blocco di keystream ($O_1$).
    
3. Feedback: Questo output $O_1$ diventa l'input per la successiva operazione di cifratura per generare $O_2$, e così via.
    
    $$O_i = E_K(O_{i-1})$$
    
    (con $O_0 = \text{IV}$)
    
1. Cifratura/Decifratura: Il blocco di keystream $O_i$ viene messo in XOR con il blocco di plaintext $P_i$ (o ciphertext $C_i$).
    
    ![[Pasted image 20251110235237.png]]$$C_i = P_i \oplus O_i$$
    ![[Pasted image 20251110235533.png]]
    $$P_i = C_i \oplus O_i$$
    

### Dettagli Tecnici per Ingegneri

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Tipo di Cifrario**|Stream Cipher Sincrono. Il keystream è indipendente dai dati.|
|**Error Propagation**|**Nessuna propagazione**. Un errore di un bit nel ciphertext durante la trasmissione causa un errore di un solo bit nel plaintext decifrato. Utile su canali rumorosi.|
|**Parallelizzazione**|**Non possibile per la generazione del keystream** (ogni blocco dipende dal precedente). Tuttavia, se il keystream è **pre-calcolato**, la cifratura/decifratura effettiva (l'operazione XOR) può essere parallelizzata.|
|**Pre-computazione**|**Possibile**. Poiché il keystream dipende solo da $K$ e IV (non dal plaintext), può essere generato in anticipo per ridurre la latenza durante la trasmissione effettiva.|
|**Padding**|**Non necessario**. Poiché funziona come uno stream cipher, può cifrare dati di lunghezza arbitraria (non multipli della dimensione del blocco) troncando l'ultimo blocco di keystream.|
|**Requisiti IV**|**CRITICO: Deve essere un Nonce (Number used ONCE).** Non deve mai essere riutilizzato con la stessa chiave.|

### Implicazioni di Sicurezza

1. **Catastrofe del Riuso dell'IV:** Se un IV viene riutilizzato con la stessa chiave, viene generato lo **stesso identico keystream**.
    
    - Se un attaccante intercetta due messaggi cifrati con stesso IV e chiave ($C_1 = P_1 \oplus K_{stream}$ e $C_2 = P_2 \oplus K_{stream}$), può calcolare $C_1 \oplus C_2 = (P_1 \oplus K_{stream}) \oplus (P_2 \oplus K_{stream}) = P_1 \oplus P_2$.
        
    - Questo espone lo XOR dei due testi in chiaro, spesso portando alla compromissione totale di entrambi i messaggi (simile alla violazione di un _One-Time Pad_).
        
2. **Integrità:** Come tutte le modalità "pure" ([[ECB]], [[CBC]], CFB, [[CTR]]), OFB **non fornisce [[Integrity]]** dei dati. Un attaccante può invertire bit specifici nel ciphertext sapendo che causeranno un'inversione prevedibile nel plaintext (attacco _bit-flipping_). È necessario utilizzare un [[MAC]] (Message Authentication Code) per l'[[Authentication]].