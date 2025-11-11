# 🔒 Perfect Forward Secrecy (PFS)

### Definizione

La **Perfect Forward Secrecy (PFS)**, o **Segretezza Inoltrata Perfetta**, è una **proprietà di sicurezza** fondamentale dei protocolli di scambio chiavi.

Un protocollo che offre PFS garantisce che la compromissione della **chiave privata a lungo termine** (long-term key) di un server **non** comprometta la confidenzialità delle **sessioni di comunicazione passate**.

In termini più semplici: anche se un aggressore registra tutto il tuo traffico cifrato per un anno e _poi_ riesce a rubare la chiave privata del server, **non può** utilizzare quella chiave per tornare indietro e decifrare le sessioni registrate.

### Il Problema (Senza PFS) vs. La Soluzione (Con PFS)

Per un ingegnere, la differenza è nel _modo_ in cui viene generata la chiave di sessione simmetrica (es. la chiave AES).

| **Scenario**       | **Non-PFS (es. Scambio RSA Statico)**                                                                                                        | **PFS (es. ECDHE)**                                                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Come funziona**  | Il client cifra la chiave di sessione (o i suoi componenti) usando la **chiave pubblica a lungo termine** del server.                        | Client e server usano **Diffie-Hellman Effimero ([[ECDHE]])**. Generano **nuove chiavi private temporanee** (effimere) _solo per questa sessione_.                                                                               |
| **Il Fallimento**  | Un aggressore ruba la **chiave privata a lungo termine** del server.                                                                         | Un aggressore ruba la **chiave privata a lungo termine** del server.                                                                                                                                                             |
| **La Conseguenza** | L'aggressore usa la chiave rubata per decifrare tutte le sessioni passate che aveva registrato. **Tutto il traffico passato è compromesso.** | Le sessioni passate sono state cifrate usando chiavi temporanee che **sono state distrutte** e non esistono più. La chiave a lungo termine (usata solo per _firmare_ lo scambio DH) è inutile. **Il traffico passato è sicuro.** |

### Dettagli Tecnici e Implicazioni

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Protocollo Chiave**|**ECDHE** (Elliptic Curve Diffie-Hellman **Ephemeral**). La "E" finale (Ephemeral, effimero) è ciò che garantisce PFS.|
|**Meccanismo**|Le chiavi private usate per lo scambio Diffie-Hellman sono **generate al momento** (on-the-fly) e **distrutte** immediatamente dopo aver derivato la chiave di sessione.|
|**Ruolo della Chiave a Lungo Termine**|In un sistema PFS (come ECDHE), la chiave privata a lungo termine del server (es. RSA o ECDSA) **non viene usata per la cifratura della chiave**. Viene usata solo per l'**autenticazione**, cioè per **firmare** digitalmente i parametri dello scambio effimero. Questo dimostra al client che sta parlando con il server corretto, senza compromettere la segretezza futura.|
|**Applicazione Pratica**|PFS è uno standard _de facto_ per la navigazione web sicura ed è **obbligatorio in TLS 1.3**. È il motivo per cui le _cipher suite_ moderne iniziano quasi sempre con `TLS_ECDHE_...`.|