# Trusted Third Party (TTP) & Key Distribution Center (KDC)

**Tags:** #engineering #cybersecurity #authentication #TTP #KDC #architettura

## 1. Definizione e Concetto Base

Una Trusted Third Party (TTP) è un'entità intermediaria di cui entrambe le parti (Alice e Bob) si fidano ciecamente.

In ambito di autenticazione, la TTP agisce come un garante che emette credenziali crittografiche per provare l'identità degli utenti e permettere comunicazioni sicure tra soggetti che non hanno mai interagito prima2.

Spesso assume il ruolo tecnico di **[[KDC (Key Distribution Center)]]** o **Authentication Server**3.

## 2. Perché serve? (Il Problema della Scalabilità)

Senza una TTP, in una rete di $N$ utenti, ogni coppia dovrebbe scambiarsi una chiave segreta in anticipo ([[Symmetric Encryption]] per [[Authentication]]). 

- **Complessità Quadratica:** Servirebbero $\frac{N(N-1)}{2}$ chiavi totali4.
    
- **Ingestibilità:** Ogni volta che un nuovo utente entra nella rete, dovrebbe contattare tutti gli altri per scambiare chiavi.
    

### La Soluzione TTP (Architettura a Stella)

Con la TTP, ogni utente condivide **una sola chiave segreta** a lungo termine direttamente con il server TTP ($K_{AC}$ per Alice, $K_{BC}$ per Bob)5.

- **Vantaggio:** Semplifica drasticamente la gestione della fiducia. Invece di gestire $N$ chiavi, ogni utente ne gestisce 16.
    
- **Obiettivo:** La TTP usa queste chiavi per generare e distribuire una **Session Key ($K$)** temporanea e fresca che Alice e Bob useranno solo per quella specifica conversazione7.
    

## 3. Rischi Strutturali

L'accentramento della fiducia introduce un rischio critico:

- **Single Point of Failure (SPoF):** Se la TTP viene compromessa (hackerata) o diventa indisponibile (down), l'intero sistema di sicurezza crolla e nessuno può più comunicare8.
    

## 4. Flusso di Autenticazione Generico

Il processo standard prevede che la TTP distribuisca la chiave di sessione $K$ garantendo tre proprietà 9:

1. Solo Alice, Bob e la TTP conoscono $K$.
    
2. Alice e Bob sanno che solo loro (e la TTP) conoscono $K$.
    
3. $K$ è nuova e generata casualmente.
    

### Protocollo Base (Vulnerabile)

Un approccio ingenuo potrebbe essere:

1. Alice chiede alla TTP di parlare con Bob: $A \to TTP: (A, B)$10.
    
2. La TTP genera $K$ e invia ad Alice due pacchetti cifrati:
    
    - $K_{AC}(K)$: La chiave per Alice.
        
    - $K_{BC}(K)$: La chiave per Bob (che Alice non può leggere ma deve inoltrare) 11.
        
3. Alice inoltra a Bob il suo pacchetto 12.
    

> [!failure] Vulnerabilità: Identity Misbinding
> 
> In questo schema base, un attaccante (Trudy) può intercettare la richiesta e confondere le identità. Se Trudy riceve un pacchetto destinato a Bob, potrebbe ingannare Alice facendole credere di parlare con qualcun altro, poiché all'interno del messaggio cifrato $K_{AC}(K)$ spesso non c'è scritto esplicitamente "Questa chiave è per parlare con Bob" 13.
> 
> **Soluzione:** Includere sempre l'identità dei partecipanti _dentro_ la cifratura (es. $K_{AC}(K, B)$) per legare la chiave al destinatario specifico 14.

## 5. Esempio Reale: Needham-Schroeder

Il protocollo più famoso basato su TTP è il Needham-Schroeder, che è la base teorica di Kerberos 15.

Utilizza i Nonce ($N$) per prevenire i Replay Attack, costringendo la TTP a dimostrare che il messaggio è stato generato in risposta a una richiesta specifica e attuale 16.

$$\begin{align} 1. \ A &\rightarrow TTP : A, B, N_A \\ 2. \ TTP &\rightarrow A : K_{AC}(N_A, B, K, \text{Ticket}_B) \\ 3. \ A &\rightarrow B : \text{Ticket}_B \end{align}$$

_(Dove $\text{Ticket}_B = K_{BC}(K, A)$)_

vedi anche [[10 CS Lower Level - Authentication - Introduction and Attacker Models#Autenticazione con Terza Parte Fidata (TTP)]].