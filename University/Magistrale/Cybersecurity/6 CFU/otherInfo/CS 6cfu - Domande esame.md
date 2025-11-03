### 1. Concetti Base, Confidenzialità e Integrità

- Spiegare i termini confidenzialità ed integrità1.
    
- Definire il concetto di data integrity e motivare la sua rilevanza2.
    
- Discutere a un livello alto almeno due approcci per applicare la data integrity, evidenziando i rispettivi punti di forza3.
    
- Se Alice deve pubblicare un file su un server web pubblico, quali misure può adottare per rassicurare gli utenti sull'integrità del file? (Lei è un editore di contenuti) 4.
    

---

### 2. Crittografia Simmetrica (Modi Operativi, Teoria, OTP)

- Descrivere cosa sono i "modes of operations" (modi operativi) nell'ambito dei cifrari a blocchi e le caratteristiche più rilevanti da considerare per la loro analisi5.
    
- Illustrare un modo operativo che fa sì che l'uso di un cifrario a blocchi si comporti in modo simile a quello di un cifrario a flusso (stream cipher) e discuterne la sicurezza6.
    
- Supponiamo che tu debba garantire l'integrità di un file ma ti sia permesso usare solo AES (e una chiave simmetrica): cosa si può fare?7.
    
- Alice e Bob hanno concordato una chiave simmetrica per cifrare messaggi. Entrambi hanno dispositivi hardware per eseguire la cifratura, ma nessuno strumento di decifratura. Devono impostare uno schema semplice per la privacy basato sui loro crittografi hardware. Progettare lo schema 8. (Domanda simile: con soli decrittatori hardware e senza crittografi 9).
    
- Migliorare lo schema precedente per garantire anche l'integrità contro avversari attivi. Non sono disponibili ulteriori risorse (no hash, no HMAC), ma Alice e Bob possono stabilire più di una chiave 10101010.
    
- Definire cos'è un "perfect cipher" (cifrario perfetto)1111111111.
    
- Provare che la proprietà che definisce un cifrario perfetto vale anche se scambiamo i ruoli di ciphertext e plaintext12.
    
- Provare che un cifrario non può essere perfetto se la dimensione del suo spazio delle chiavi è inferiore alla dimensione del suo spazio dei messaggi13.
    
- Descrivere il Cifrario di Vernam (a.k.a. One Time Pad) e stabilire chiaramente la proprietà che deve valere affinché sia un cifrario perfetto14.
    
- Data un algoritmo di cifratura A, perché 2-A (cifrare di nuovo il testo cifrato di A) non è molto più sicuro di A?15.
    
- Spiegare perché è male riutilizzare lo stesso keystream in OTP (One Time Pad)16.
    
- Cosa produce il comando "openssl aes-128-cbc -p -in file.txt -out file.txt.enc"? Descrivere in dettaglio, analizzando anche il formato di output17.
    

---

### 3. Crittografia Asimmetrica (RSA e Padding)

- Descrivere come funzionano la cifratura e la decifratura RSA18.
    
- Spiegare qual è la relazione matematica tra _e_ e _d_ (i due esponenti usati in RSA)19.
    
- Perché l'implementazione "textbook" (da manuale) di RSA non è sicura? Fornire almeno un esempio20.
    
- Dati $p=13$ e $q=17$ per RSA, qual è il range per l'esponente _e_?21212121.
    
- Considerando l'esempio RSA textbook con $p=7$, $q=11$ e $e=3$:
    
    - Fornire un algoritmo generale per calcolare _d_ ed eseguirlo con gli input dati22.
        
    - Qual è l'intero massimo che può essere cifrato? Spiegare23.
        
    - Ci sono cambiamenti nelle risposte precedenti se scambiamo i valori di _p_ e _q_? Spiegare24.
        
- Cos'è l'Optimal Asymmetric Encryption Padding (OAEP) e perché fornisce sicurezza "all-or-nothing"?25.
    

---

### 4. Scambio Chiavi (Diffie-Hellman)

- Discutere i maggiori punti di forza e di debolezza del protocollo Diffie-Hellman per definire una chiave segreta26.
    
- Discutere una soluzione che risolva le debolezze del protocollo (D-H)27.
    
- Descrivere in dettaglio come due parti possono stabilire una chiave segreta usando lo schema Diffie-Hellman e discutere la vulnerabilità dell'approccio282828282828282828.
    
- Generalizzare Diffie-Hellman in modo che tre parti possano stabilire una chiave segreta condivisa29292929.
    
- Descrivere uno schema per l'autenticazione mutua che sia forte rispetto agli attacchi a dizionario e che usi Diffie-Hellman per definire una chiave di sessione. Le vulnerabilità discusse prima (MitM) sono ancora valide? 30303030.
    
- Spiegare in dettaglio come un attaccante può eseguire un attacco man-in-the-middle (contro D-H) e quali risultati può ottenere31.
    
- Suggerire un meccanismo per rendere sicuro Diffie-Hellman rispetto agli attacchi man-in-the-middle32.
    

---

### 5. Funzioni di Hash e MAC (Integrità)

- La resistenza debole alle collisioni implica la resistenza forte?33.
    
- Descrivere cosa intendiamo per integrità dei dati (data integrity) e discutere l'uso di HMAC (keyed HMACs) per garantire l'integrità di un file trasmesso in rete (non sono richieste altre garanzie)34.
    
- Descrivere i requisiti che devono essere soddisfatti da una funzione di hash crittografica35.
    
- Descrivere la costruzione Merkle–Damgård per l'hashing di un messaggio più lungo di un singolo blocco36.
    
- Confrontare l'hashing "keyed" (con chiave) e "non-keyed" (senza chiave) e discutere la sicurezza di $k|m$, $m|k$, $k|m|k$ (dove $m$ è il messaggio, $k$ la chiave segreta) 37.
    
- Domande varie sull'Hashing (Esame 19/1/2024) 38383838:
    
    - Una funzione di hashing fortemente resistente è anche debolmente resistente? (S/N)
        
    - Una funzione di hashing debolmente resistente è anche fortemente resistente? (S/N)
        
    - Le funzioni di hashing non-keyed sono più sicure di quelle keyed? (S/N)
        
    - F1 (range n-bit) e F2 (range k-bit, k<n). Il numero tot di collisioni di F1(F2(x)) è > di F2(F1(x))? (S/N)
        
    - H(x) = $x^2$. H(x) è crittografica? (S/N)
        

---

### 6. Firme Digitali (DSS, RSA, ElGamal)

- Alice vuole inviare file di grandi dimensioni a Bob. Se Alice invia: `EncPKB(f, SignSKA(H(f)))`. Questo garantisce confidenzialità e integrità? È efficiente per dispositivi mobili? 39.
    
- Descrivere le caratteristiche di base dell'approccio DSS (Digital Signature Standard) alla firma digitale. Qual è il vantaggio di usare due coppie di chiavi per ogni firma? 40404040.
    
- Illustrare i processi (generici) per la generazione e la verifica delle firme digitali41.
    
- Descrivere concettualmente il processo di apposizione di una firma digitale RSA su un documento PDF, includendo la verifica 42.
    
- ElGamal signature vs. DSS (disegnare una tabella ed essere schematici)43.
    
- Come usare una firma digitale per l'autenticazione, essendo robusti contro l'attacco di replay?44.
    

---

### 7. Autenticazione e Protocolli

- Mostrare un protocollo che usi un nonce per la mutua autenticazione fra due utenti che condividono una password segreta45.
    
- Mostrare un protocollo che usi un nonce per la mutua autenticazione fra due utenti che hanno una chiave pubblica46.
    
- Mostrare un protocollo basato su timestamp per la mutua autenticazione fra due utenti che condividono una chiave con un server centrale sicuro (come in Kerberos)47.
    
- Dato il protocollo (A→B: $W\{n_{A}\}$, B→A: $W\{n_{A}+1\}$, A→B: (F, H(F), w{H(F)}) ):
    
    - Mostrare come un attaccante può agire al posto di Alice e inviare un file a Bob48.
        
    - Correggere il protocollo49.
        
- Quale schema può essere usato per generare one-time passwords?50.
    
- Alice, Bob e Charlie devono autenticarsi reciprocamente (ognuno certo dell'identità degli altri due). Il processo ha successo solo se tutte le coppie sono autenticate. Presentare due soluzioni (a) crittografia simmetrica, (b) crittografia a chiave pubblica 51.
    
- (Esami 2016) Domande su "Secure client-server authentication" e "Secure client authentication" (smartphone/dispositivi mobili) 52525252.
    

---

### 8. Sicurezza di Rete (Firewall, Proxy, WiFi)

- Discutere le principali differenze fra il filtraggio dei pacchetti stateless e stateful (cinque righe)53.
    
- Disegnare uno schema che illustri come posizionare un firewall (basato su filtraggio pacchetti) per una piccola organizzazione (server Web, mail server, rete locale con DB)54.
    
- Mostrare come configurare il firewall per consentire verso l'esterno solo connessioni Web (porta 80) e FTP (porta 21 controllo, 20 dati)55.
    
- Domande su Proxy (Bastion Host B, application-level proxy):
    
    - Può B consentire file HTML e negare file JPG in connessioni HTTP?56.
        
    - Può B consentire file HTML e negare file JPG in connessioni HTTPS?57.
        
    - Può B consentire file HTML e negare file JPG in connessioni HTTP VPN?58.
        
- iptables può filtrare datagrammi in entrata che sono pacchetti IPSec-tunnelled diretti alla porta 25?59595959.
    
- Alice arriva in hotel e trova una rete "FreeHotelWiFi" (aperta, non cifrata). Discutere le preoccupazioni di Alice (privacy, man-in-the-middle) e suggerire comportamenti sicuri 60.
    
- Spiegare la differenza tra packet filtering e session filtering61.
    
- Domande varie su Firewall (Esame 2015/2016) 62626262.
    

---

### 9. Protocolli di Sicurezza (TLS, IPSec, SSH)

- Qual è il protocollo che implementa il port forwarding?63636363.
    
- Quali sono le principali differenze tra la sicurezza end-to-end fornita da IPSec e quella fornita da TLS? 64.
    
- Fornire una "security association" (associazione di sicurezza) adatta per un utente domestico che deve connettersi in modo sicuro a una rete aziendale per accedere in lettura ai file condivisi65.
    
- Descrivere a un livello alto i principali obiettivi di sicurezza di TLS66.
    
- Descrivere a un livello alto i principali obiettivi di sicurezza di IPSec67.
    
- Descrivere uno scenario applicativo/infrastrutturale in cui TLS sembra più utile di IPSec68.
    
- Descrivere uno scenario applicativo/infrastrutturale in cui IPSec sembra più utile di TLS69.
    
- Spiegare attentamente cosa significa "end-to-end" nel caso della sicurezza TLS70.
    
- Descrivere cos'è il port forwarding all'interno del protocollo SSH71.
    
- TLS vs IPsec (disegnare una tabella)72.
    

---

### 10. Controllo degli Accessi (DAC, MAC, HRU, Bell-LaPadula)

- Illustrare il modello DAC (da Harrison-Ruzzo-Ullman, o HRU), definire il concetto di "safety" (sicurezza) del sistema di protezione e discutere quali problemi pratici emergono nel modello73737373.
    
- Perché tale modello DAC (HRU) è vulnerabile ai Trojan? Quale tipo di modello di controllo accessi può impedire loro di accedere illegalmente a dati privati? Discutere 74747474.
    
- In un dipartimento universitario (professori, studenti, segreteria), scegliere un modello di controllo accessi, descriverlo e motivare la scelta 75.
    
- Il modello scelto (Q4.1) è robusto rispetto ai Trojan? Discutere76.
    
- Descrivere brevemente le principali differenze tra i modelli di controllo accessi MAC e DAC77.
    
- Descrivere il modello Bell-LaPadula: obiettivo e idee principali (classi di accesso, clearance, assiomi, ecc.)78.
    
- Descrivere cos'è il mandatory access control (MAC)79.
    
- Perché il modello HRU non è in grado di proteggere dai Trojan horses?80.
    
- Il modello HRU è un modello DAC o MAC? Elaborare81.
    
- Una organizzazione paramilitare ha classificato i documenti (C, CC, S, TS). Quale approccio al controllo accessi raccomanderesti e perché? 82.
    
- Perché i modelli DAC non sono in grado di proteggere i dati dai Trojan Horses incorporati nei programmi applicativi? Elaborare83.
    

---

### 11. Sicurezza Applicativa (Web, Cookie)

- Spiegare brevemente quali sono gli aspetti fondamentali di questo tipo di sicurezza (Sicurezza delle applicazioni)84.
    
- Illustrare il meccanismo dei cookie nei browser, spiegando quali sono gli usi impropri e i rischi corsi dall'utente. Spiegare come prevenire tali rischi85.
    

---

### 12. Protocolli Specifici (Shamir, Leader Selection, Time-stamping, etc.)

- (Protocollo Leader Selection) Discutere la sicurezza del protocollo rispetto a comportamenti fraudolenti di A, B e/C. È possibile per alcune parti scegliere deterministicamente il leader?86868686.
    
- Correggere il protocollo di Leader Selection87878787.
    
- Descrivere lo schema di Shamir (k, n) per la condivisione di un segreto88888888.
    
- Fare un esempio numerico per il caso Shamir (2, 4), per condividere il segreto numero 6. Mostrare come vengono calcolati i 4 frammenti 89898989.
    
- (Protocollo Fair dice rolling) Discutere la sicurezza del protocollo, mostrare come una parte può controllare il risultato finale 90.
    
- Correggere il protocollo Fair dice rolling (senza introdurre terze parti)91.
    
- (Servizio Time-stamping) Progettare uno schema per associare un time-stamp a un file e a una firma digitale 92.
    
- Discutere la sicurezza dello schema di time-stamping. Se necessario, migliorare il protocollo del time-server (senza firmare digitalmente i time-stamp) 93.
    
- (A,B,C firmano accordo) Descrivere l'infrastruttura e i passi necessari per firmare digitalmente e allegare un time-stamp sicuro a ciascuna firma 94949494.
    
- (Rock-paper-scissors game...) 95.
    
- (Secure server-mediated messaging...) 96.
    

---

### 13. Teoria degli Attacchi (MitM, Birthday, Reflection, Forgery, etc.)

- Definire il "birthday bound"97.
    
- Spiegare cos'è un attacco "man in the middle"98. (Vedi anche D-H Q2.2 99).
    
- Spiegare cos'è un "chosen-ciphertext attack"100.
    
- Descrivere cos'è un "reflection attack" (senza esempi)101.
    
- Dare un (qualsiasi) esempio di reflection attack102102102102.
    
- Cos'è il "birthday attack"?103.
    
- Descrivere una tecnica generale per contrastare i "replay attacks"104.
    
- Spiegare cos'è un "adaptive chosen-plaintext attack"105.
    
- Cos'è l'"existential forgery attack"?106.
    
- Definire l'"existential forgery attack" e indicare i passaggi la cui cattiva implementazione può facilitare una falsificazione esistenziale107.
    
- Descrivere l'attacco "Meet-In-The-Middle" (da non confondere con Man-In-The-Middle) e uno scenario d'uso108.
    
- Dare una stima della lunghezza massima della chiave che può essere attaccata con successo da Meet-In-The-Middle, dati certi parametri (RAM, tempo, etc.) 109.
    
- Illustrare il cosiddetto "paradosso del compleanno" e descrivere quale tipo di attacco (birthday attack) può essere preparato sfruttando questa proprietà110.
    
- Il "birthday bound" è influenzato dalla qualità della funzione di hash (crittografica o non)? Elaborare111.
    

---

### 14. Domande Varie (Matematica e Teoria)

- $\Phi(7)=?$ (Funzione toziente di Eulero)112.
    
- $\Phi(12)=?$113.
    
- Trovare l'inverso moltiplicativo di 5 (mod 6)114.
    
- $\Phi(10)=?$115115115115.
    
- Qual è il gruppo moltiplicativo $Z_{10}$ (o ${Z_{10}}^{*}$)?116116116116.
    
- $\Phi(11)=?$117.
    
- Enunciare il Teorema di Galois sui Campi di Galois118.
    
- Determinare l'inverso moltiplicativo di 47 mod 64119.
    
- Dati i primi 23 e 11, trovare un intero $\alpha$ tale che $\alpha^{11} = 1 \mod 23$120.
    
- Dati i primi 11 e 5, trovare $\alpha > 1$ tale che $\alpha^5 = 1 \mod 11$ (No calcolatrici)121.