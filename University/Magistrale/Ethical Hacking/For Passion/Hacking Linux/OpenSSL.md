---
tags:
  - cybersecurity
  - ethical-hacking
  - openssl
  - dos
  - hacking-exposed-7
aliases:
  - THC-SSL-DOS
date: 2026-05-21
---
---

## tags: [eth, cryptography, tls, memory-corruption, library-vulnerabilities] capitolo: extra (non in HE7) collegato: [[integer_overflow_attacks]], [[dangling_pointers]], [[dns_attacks]]

# OpenSSL — Architettura e Vulnerabilità Storiche

## Cos'è e perché conta

**OpenSSL** è una libreria crittografica open-source. **Non è SSH.** Sono cose diverse:

| |OpenSSL|OpenSSH|
|---|---|---|
|Cos'è|Libreria crypto (TLS, x509, hash, cifrari)|Implementazione del protocollo SSH|
|Linguaggio|C|C|
|Usata da|Apache, nginx, curl, OpenSSH stesso, tutto HTTPS|Te quando fai `ssh user@host`|
|Porta|Nessuna (è una lib)|22/tcp|

OpenSSL fornisce:

- Implementazione TLS/SSL (la cifratura sotto HTTPS, IMAPS, SMTPS, ecc.)
- Primitive crittografiche (AES, RSA, ECDSA, SHA, ecc.)
- Gestione certificati X.509 (CA, CRL, OCSP)
- PRNG (random number generator)
- Tool CLI (`openssl`) per ogni operazione crypto

**Perché è target privilegiato**: gira nello stesso processo del web server con accesso alle chiavi private e ai dati cifrati. Una vulnerabilità in OpenSSL = compromise massivo trasversale a milioni di sistemi.

---

## Architettura Componenti

|Modulo|Funzione|
|---|---|
|`libcrypto`|Primitive crittografiche pure (cifrari, hash, big numbers, ASN.1)|
|`libssl`|Protocollo TLS/SSL costruito sopra libcrypto|
|`openssl` CLI|Frontend a riga di comando|

Un'applicazione tipica (es. nginx) linka libssl, che linka libcrypto. Una vulnerabilità in una di queste = vulnerabile l'intero ecosistema HTTPS.

---

## CLI Cheatsheet (offensivo/difensivo)

```bash
# Testa la cifratura supportata da un server
openssl s_client -connect target.com:443

# Verifica certificato di un server
openssl s_client -connect target.com:443 -showcerts

# Vedi info di un certificato
openssl x509 -in cert.pem -text -noout

# Genera chiave + CSR
openssl req -newkey rsa:4096 -keyout key.pem -out req.csr

# Hash di un file
openssl dgst -sha256 file.txt

# Cifra/decifra simmetrico
openssl enc -aes-256-cbc -in plain.txt -out cipher.bin

# Forza versione TLS specifica (test downgrade)
openssl s_client -connect target.com:443 -tls1
openssl s_client -connect target.com:443 -ssl3   # se ancora supportato → POODLE
```

Per pentest: `testssl.sh` o `nmap --script ssl-enum-ciphers` automatizzano tutto.

---

## Vulnerabilità Storiche Iconiche

### 1. Heartbleed (CVE-2014-0160) — Aprile 2014

**La regina delle vulnerabilità OpenSSL.** Out-of-bounds read nell'estensione TLS Heartbeat.

#### Meccanismo

TLS ha un'estensione "Heartbeat" (RFC 6520) — keepalive. Funziona così:

```
client → server: HeartbeatRequest
                 payload = "hello"
                 length  = 5         ← lunghezza dichiarata del payload

server → client: HeartbeatResponse
                 echo back gli stessi 5 byte
```

**Il bug**: il server fidava ciecamente del campo `length` dichiarato dal client, senza verificare la lunghezza effettiva del payload.

```
client → server: HeartbeatRequest
                 payload = "x"       ← 1 byte di payload reale
                 length  = 65535     ← length dichiarata 64 KB

server: memcpy(response, payload_ptr, 65535)
        ← copia 65535 byte a partire dal payload
        ← legge ben oltre il payload, dentro la memoria del processo

server → client: HeartbeatResponse di 65535 byte
                 contiene quello che capita in RAM accanto al buffer
```

#### Cosa veniva leakato

Il processo OpenSSL (parte del web server) ha in RAM:

- **Chiavi private TLS** del server (game over totale)
- Cookie di sessione di altri utenti
- Username / password in transito durante login
- Token di autenticazione
- Contenuti di altre richieste HTTP

E si poteva ripetere l'attacco indefinitamente, **senza autenticazione, senza lasciare traccia nei log**.

#### Bug class

Out-of-bounds read da mancata validazione di campo length controllato dall'utente. Parente stretto degli [[integer_overflow_attacks]] ma più semplice: qui non c'è nemmeno overflow, è proprio l'assenza di un check.

```c
// pseudo-bug (semplificato)
struct ssl_record {
    uint16_t length;
    uint8_t *payload;
};

void heartbeat_response(struct ssl_record *rec) {
    char *response = malloc(rec->length);
    memcpy(response, rec->payload, rec->length);  // ← rec->length è user-controlled!
    send_to_client(response, rec->length);
}
```

Il fix è banale: validare che `rec->length` non sia maggiore della lunghezza effettiva del payload ricevuto.

#### Impatto

- ~17% dei server HTTPS internet-facing vulnerabili al disclosure
- Chiavi private di Yahoo, Cloudflare, Reddit, GitHub esposte
- Cloudflare lanciò una "Heartbleed Challenge" per dimostrare che le chiavi private potevano essere estratte → confermato in ore
- Tutti i certificati TLS dei server vulnerabili da revocare e ri-emettere
- **Lezione**: una singola riga di C in una libreria diffusa = compromise globale

#### Fix

OpenSSL 1.0.1g (aprile 2014). Disabilitazione dell'estensione Heartbeat con `OPENSSL_NO_HEARTBEATS`.

---

### 2. Debian OpenSSL PRNG Bug (CVE-2008-0166) — 2006-2008

Un manutentore Debian, per silenziare un warning di Valgrind, commenta una riga in OpenSSL che inizializzava il pool di entropia del PRNG. Conseguenza:

> Il PRNG di OpenSSL su Debian (e derivati: Ubuntu, ecc.) generava chiavi crittografiche **prevedibili**. L'entropia totale si riduceva al solo PID del processo → 32768 possibilità.

**Impatto**: ogni chiave SSH/SSL/TLS generata su Debian/Ubuntu per due anni era una delle 32768 possibili. Era possibile **brute-forcearle tutte e farne un dizionario**. Hacker e ricercatori fecero esattamente questo. Servizi compromessi senza che nessuno se ne accorgesse per anni.

Lezione: cambiare codice crypto senza capire le conseguenze = catastrofe silenziosa.

---

### 3. POODLE (CVE-2014-3566) — Ottobre 2014

**Padding Oracle On Downgraded Legacy Encryption.** Padding oracle attack su SSL 3.0 (CBC mode).

```
1. Attaccante è MitM
2. Forza il client a fare downgrade a SSL 3.0 (interrompe handshake TLS)
3. Sfrutta che SSL 3.0 non valida i byte di padding CBC
4. Modifica byte cifrati e osserva accept/reject → padding oracle
5. Decifra 1 byte alla volta del traffico (es. cookie di sessione)
```

Tecnicamente è un problema del protocollo SSL 3.0, ma OpenSSL lo implementava ancora. Fix: disabilitare SSL 3.0 ovunque. Da quel punto SSL è morto definitivamente, TLS è lo standard.

---

### 4. CCS Injection (CVE-2014-0224) — Giugno 2014

OpenSSL accettava il messaggio `ChangeCipherSpec` in punti dell'handshake in cui non doveva. Un MitM poteva forzare l'uso di chiavi predicibili → decifrare l'intera sessione.

**Affetti**: OpenSSL < 0.9.8za, < 1.0.0m, < 1.0.1h. Sia client sia server.

---

### 5. FREAK (CVE-2015-0204) — Marzo 2015

**Factoring RSA Export Keys.** Eredità degli anni '90 (regole USA export grade crypto a 512 bit).

```
1. MitM forza il server a usare RSA "export" (512 bit) durante handshake
2. RSA 512 bit è factorizzabile in ore con cloud (~$100)
3. Una volta fattorizzata la chiave, MitM decifra tutto il traffico
```

OpenSSL aveva un bug che permetteva il downgrade silenzioso anche a client che non chiedevano export grade. Fix: rimozione totale del supporto a cifrari export.

---

### 6. DROWN (CVE-2016-0800) — Marzo 2016

**Decrypting RSA with Obsolete and Weakened eNcryption.** Cross-protocol attack: se un server supporta sia TLS che SSLv2 sulla **stessa chiave**, un attaccante può usare bug in SSLv2 per decifrare connessioni TLS.

Impatto: ~33% dei server HTTPS al momento del disclosure vulnerabili (perché supportavano ancora SSLv2 per backward compat).

Fix: disabilitare SSLv2 ovunque, mai più riusare chiavi tra protocolli.

---

### 7. Lucky Thirteen (CVE-2013-0169) — Febbraio 2013

Timing side channel attack su TLS CBC. La differenza microscopica nel tempo di elaborazione tra padding valido e invalido permette di estrarre il plaintext byte per byte.

Concetto importante: **timing attacks su crypto sono reali e pratici**, non solo accademici. OpenSSL ha avuto multiple varianti negli anni.

---

## Pattern Comune

Le vulnerabilità OpenSSL si raggruppano in categorie ricorrenti:

|Categoria|Esempi|
|---|---|
|Out-of-bounds read|Heartbleed|
|Out-of-bounds write|Vari CVE memory corruption|
|Logic flaws nel protocollo state machine|CCS Injection|
|Downgrade attacks|POODLE, FREAK, DROWN|
|Side channels (timing, padding oracle)|Lucky 13, varianti BEAST/CRIME|
|PRNG / entropy issues|Debian bug, RSA weak keys|

**Filo conduttore**: una libreria crittografica è scritta in C, gestisce input untrusted da internet, e implementa protocolli con state machine complessi. Ogni componente è una potenziale bug factory — stesso principio strutturale di rpc.statd ([[dns_attacks]] e [[nfs_attacks]]).

---

## Fork e Alternative

Heartbleed scatenò una crisi di fiducia in OpenSSL. Reazioni:

|Progetto|Origine|Filosofia|
|---|---|---|
|**LibreSSL**|OpenBSD, 2014|Fork post-Heartbleed, focus su pulizia del codice e rimozione del legacy|
|**BoringSSL**|Google, 2014|Fork interno per uso Google (Chrome, Android) — non garantisce stabilità API|
|**mbedTLS**|Pre-esistente (PolarSSL)|Implementazione separata, leggera, per embedded|
|**rustls**|Recente|Riscrittura in Rust — niente memory corruption per design|

OpenSSL 3.x (2021+) è una riscrittura significativa con architettura più pulita (provider-based). Lo standard de facto rimane OpenSSL ma il monopolio si è incrinato.

---

## Countermeasures generali

|Pratica|Perché|
|---|---|
|**Update OpenSSL aggressivamente**|I CVE sopra sono il motivo. Patch in tempo non opzionali.|
|Disabilita SSLv2, SSLv3, TLS 1.0, TLS 1.1|POODLE, DROWN, FREAK — sono morti|
|Solo TLS 1.2 e 1.3|Standard sicuri attuali|
|Forward Secrecy (ECDHE)|Anche se la chiave privata viene compromessa, le sessioni passate restano cifrate|
|Certificate pinning (mobile app)|MitM con CA compromessa diventa difficile|
|HSTS + HSTS preload|Forza HTTPS, impedisce downgrade|
|Monitor con `testssl.sh` / SSL Labs|Audit periodico della config|
|Key rotation regolare|Limita la finestra di esposizione se chiave compromessa|
|**Considera alternative**|LibreSSL, BoringSSL, rustls per nuovi progetti|

---

## TL;DR esame

1. OpenSSL ≠ OpenSSH. OpenSSL = libreria crypto (TLS, certificati, primitive). OpenSSH = client/server SSH.
2. Heartbleed (2014): out-of-bounds read nell'estensione heartbeat → leak di chiavi private, cookie, password da server HTTPS. Senza auth, senza log. La vulnerabilità più famosa della storia recente.
3. Debian PRNG (2008): chiavi crypto prevedibili per 2 anni su Debian/Ubuntu. Lezione: non toccare crypto code senza capire.
4. POODLE / FREAK / DROWN / CCS / Lucky13: famiglia di attacchi protocollo/downgrade/side-channel su SSL/TLS legacy.
5. Pattern: libreria C + input untrusted + crypto complessa = bug factory. Vale anche per BIND, sendmail, qualsiasi cosa.
6. Fork post-Heartbleed: LibreSSL, BoringSSL, rustls — il monopolio OpenSSL non è più totale.
7. Fix universali: update, disabilita protocolli vecchi, forward secrecy, monitoraggio.