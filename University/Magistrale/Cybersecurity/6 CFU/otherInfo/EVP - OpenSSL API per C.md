# Guida rapida all’API EVP di OpenSSL

---
## 🔹 Cos'è l’API EVP

`EVP_*` (Envelope) è un’astrazione di alto livello che nasconde i dettagli dei singoli algoritmi (es. AES, SHA256, RSA).

Si usa tramite **contesti (`EVP_MD_CTX`, `EVP_CIPHER_CTX`, …)** e **funzioni di inizializzazione, aggiornamento e finalizzazione**.

  
---

## 🔹 Esempio 1: Calcolare un hash (SHA-256)

```c

#include <openssl/evp.h>
#include <stdio.h>
#include <string.h>

int main(void) {

EVP_MD_CTX *ctx = EVP_MD_CTX_new();
unsigned char hash[EVP_MAX_MD_SIZE];
unsigned int hash_len;

const char *message = "Hello, world!";

// 1. Inizializza il contesto e scegli l’algoritmo
EVP_DigestInit_ex(ctx, EVP_sha256(), NULL);

// 2. Aggiorna con i dati
EVP_DigestUpdate(ctx, message, strlen(message));

// 3. Finalizza e ottieni il digest
EVP_DigestFinal_ex(ctx, hash, &hash_len);

  

// 4. Stampa l’hash in esadecimale
printf("SHA256(\"%s\") = ", message);
for (unsigned int i = 0; i < hash_len; i++)
	printf("%02x", hash[i]);
printf("\n");

EVP_MD_CTX_free(ctx);
return 0;
}

```
  
Compila con:

```bash

gcc -o hash_example hash_example.c -lcrypto

```

---

## 🔹 Esempio 2: Cifratura simmetrica (AES-256-CBC)

```c
#include <openssl/evp.h>
#include <string.h>
#include <stdio.h>

int main() {
	EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
	unsigned char key[32] = "01234567890123456789012345678901";
	unsigned char iv[16] = "0123456789012345";
	unsigned char plaintext[] = "Test message";
	unsigned char ciphertext[128];
	unsigned char decrypted[128];

	int len, ciphertext_len, decrypted_len;

	// Encrypt
	EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);

	EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, strlen((char *)plaintext));

	ciphertext_len = len;
	EVP_EncryptFinal_ex(ctx, ciphertext + len, &len);

	ciphertext_len += len;


	EVP_CIPHER_CTX_reset(ctx); // reset del contesto

  

	// Decrypt
	EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv);
	EVP_DecryptUpdate(ctx, decrypted, &len, ciphertext, ciphertext_len);
	decrypted_len = len;
	EVP_DecryptFinal_ex(ctx, decrypted + len, &len);
	decrypted_len += len;

	decrypted[decrypted_len] = '\0';
	printf("Decrypted text: %s\n", decrypted);

	EVP_CIPHER_CTX_free(ctx);

	return 0;
}

```

Compila con:
```bash

gcc -o aes_example aes_example.c -lcrypto

```

---

  

## 🔹 Struttura generale (digest o cipher)

  

Tutti i flussi EVP seguono lo schema:

  

```c

EVP_*Init_ex(ctx, algo, NULL);

EVP_*Update(ctx, data, len);

EVP_*Final_ex(ctx, out, &out_len);

```

  

---

  

## 🔹 Funzioni EVP più comuni

| Tipo operazione                      | Funzioni principali                                              | Esempi di algoritmo                      |
| ------------------------------------ | ---------------------------------------------------------------- | ---------------------------------------- |
| Hashing                              | `EVP_DigestInit_ex`, `EVP_DigestUpdate`, `EVP_DigestFinal_ex`    | `EVP_sha256()`, `EVP_sha512()`           |
| Cifratura simmetrica                 | `EVP_EncryptInit_ex`, `EVP_EncryptUpdate`, `EVP_EncryptFinal_ex` | `EVP_aes_128_cbc()`, `EVP_aes_256_gcm()` |
| Decifratura                          | `EVP_DecryptInit_ex`, `EVP_DecryptUpdate`, `EVP_DecryptFinal_ex` | idem                                     |
| Firma/Verifica (chiavi asimmetriche) | `EVP_DigestSign*`, `EVP_DigestVerify*`                           | RSA, ECDSA                               |
  

---

## 🔹 Documentazione utile

  Puoi consultare:
```bash

man EVP_DigestInit

man EVP_EncryptInit

```
oppure online:
👉 [https://www.openssl.org/docs/man3.0/man3/EVP_EncryptInit.html](https://www.openssl.org/docs/man3.0/man3/EVP_EncryptInit.html)


---
# Guida dettagliata a EVP_EncryptInit_ex, EVP_EncryptUpdate e EVP_EncryptFinal_ex

## 1) Ruolo generale
Le tre funzioni fanno parte dell’interfaccia di alto livello per la cifratura simmetrica (EVP cipher). Il flusso tipico è:
1. **Inizializzazione**: prepara il `EVP_CIPHER_CTX` con algoritmo, chiave, IV, opzioni. (`EVP_EncryptInit_ex`)

2. **Streaming**: invii uno o più blocchi di plaintext da cifrare; l’API può emettere dati cifrati parzialmente a ogni chiamata. (`EVP_EncryptUpdate`)

3. **Finalizzazione**: cifra i dati residui (padding) e conclude l’operazione. (`EVP_EncryptFinal_ex`). ([manpages.opensuse.org][1])


---
## 2) Prototipi (tipici)

```C

#include <openssl/evp.h>

int EVP_EncryptInit_ex( EVP_CIPHER_CTX *ctx,
						const EVP_CIPHER *type,
						ENGINE *impl,
						const unsigned char *key,
						const unsigned char *iv);

int EVP_EncryptUpdate(  EVP_CIPHER_CTX *ctx,
						unsigned char *out,
						int *outl,
						const unsigned char *in,
						int inl);

int EVP_EncryptFinal_ex(EVP_CIPHER_CTX *ctx,
						unsigned char *out,
						int *outl);
```

  Tutte ritornano `1` in caso di successo, `0` in caso di errore (o <1 in versioni/varianti). ([docs.openssl.org][2])

---
## 3) EVP_EncryptInit_ex — dettagli pratici
```C
int EVP_EncryptInit_ex( EVP_CIPHER_CTX *ctx,
						const EVP_CIPHER *type,
						ENGINE *impl,
						const unsigned char *key,
						const unsigned char *iv);
```
* **Scopo**: impostare il contesto `ctx` ("*context*") per una nuova operazione di cifratura (algoritmo, chiave, IV, engine).

* **`type`**: puntatore a `EVP_CIPHER` (es. `EVP_aes_256_cbc()` o, in OpenSSL 3.0, un `EVP_CIPHER_fetch()` result). Se `NULL`, puoi solo cambiare chiave/IV o riusare il tipo già impostato. ([manpages.opensuse.org][1])

* **`impl` (ENGINE)**: quasi sempre `NULL` oggi (era per implementazioni hardware/engine).

* **`key` e `iv`**: se passati, inizializzano la chiave e l’IV; puoi anche impostarli dopo con controlli o chiamate specifiche.

* **Effetto su `ctx`**: azzera/inizializza lo stato interno necessario (es. buffer di blocco, conteggi) — non libera `ctx`. Se riusi lo stesso `EVP_CIPHER_CTX`, meglio usare `EVP_CIPHER_CTX_reset()` o chiamare `EVP_EncryptInit_ex` appropriatamente. ([manpages.opensuse.org][1])

**Consigli**:
* Verifica il valore di ritorno e gestisci errori con le funzioni di OpenSSL `ERR_get_error()` se necessario.

* In OpenSSL 3.0 preferisci `EVP_CIPHER_fetch()` per ottenere `EVP_CIPHER` da provider, poi `EVP_EncryptInit_ex(ctx, cipher, NULL, key, iv)`. ([manpages.opensuse.org][3])
---
## 4) EVP_EncryptUpdate — comportamento e regole
```C
int EVP_EncryptUpdate(  EVP_CIPHER_CTX *ctx,
						unsigned char *out,
						int *outl,
						const unsigned char *in,
						int inl);

```
* **Scopo**: cifrare `inl` byte da `in` e scrivere il risultato in `out`; `*outl` esce con il numero di byte prodotti.

* **Streaming**: può essere chiamata molte volte; i dati vengono processati incrementally. Questo è utile per file/stream. ([manpages.opensuse.org][3])

* **Quanto può scrivere `out`?** Dipende dall'allineamento ai blocchi:

* Per cifre a blocchi con padding abilitato (default): l’output di `EVP_EncryptUpdate` può essere compreso tra `0` e `inl + block_size - 1`.

* In pratica, quando chiami `EVP_EncryptUpdate`, fornisci un buffer `out` di dimensione almeno `inl + EVP_CIPHER_block_size(cipher)` per essere sicuro. ([man.openbsd.org][4])

* **Con cifre a flusso / modalità stream (es. CTR, AES-GCM come flusso per la parte di cifratura)**: `EVP_EncryptUpdate` normalmente emetterà esattamente `inl` byte (non c’è padding).

* **Aead / GCM / CCM**: per modalità AEAD (es. GCM) il comportamento differisce: non c’è padding e la tag viene recuperata con `EVP_CIPHER_CTX_ctrl(..., EVP_CTRL_AEAD_GET_TAG, ...)` **dopo** `EVP_EncryptFinal_ex`. Inoltre per associare AAD si usa `EVP_EncryptUpdate` con `in == NULL` e `inl == 0`? (vedi documentazione AEAD). ([wiki.openssl.org][5])


**Errori comuni**:
* Buffer `out` troppo piccolo → overflow o errore.

* Chiamare `EVP_EncryptUpdate` dopo `EVP_EncryptFinal_ex` (non corretto). ([manpages.opensuse.org][3])

---
# 5) EVP_EncryptFinal_ex — cosa fa esattamente
```C
int EVP_EncryptFinal_ex(EVP_CIPHER_CTX *ctx,
						unsigned char *out,
						int *outl);
```
* **Scopo**: finalizzare l’operazione di cifratura. Per cifrature a blocchi con **padding abilitato** (default), questa funzione:
	* Applica il padding ai byte rimanenti in buffer (PKCS#7 / PKCS#5 style), cifra quel blocco e scrive il blocco padded in `out`.
	* Imposta `*outl` al numero di byte scritti (tipicamente la dimensione del blocco).
* **Se il padding è disabilitato** (`EVP_CIPHER_CTX_set_padding(ctx,0)`):
	* `EVP_EncryptFinal_ex` NON aggiunge padding; se ci sono dati residuali la chiamata fallirà (perché i dati non sono multipli del block size). Quindi devi garantire tu che i dati siano esattamente multipli del block size. ([manpages.opensuse.org][6])
* **AEAD (GCM, CCM)**:
	* Non vi è padding; `EVP_EncryptFinal_ex` generalmente non emette dati addizionali (o può), ma **dopo** la finalizzazione devi ottenere il tag con `EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_AEAD_GET_TAG, tag_len, tag_buf)`. Per GCM, l’ordine e le chiamate specifiche sono importanti. ([wiki.openssl.org][5])

**Nota**: dopo `EVP_EncryptFinal_ex` l’operazione è conclusa: non chiamare più `EVP_EncryptUpdate` per quel contesto senza reinizializzarlo.

---
## 6) Padding — cosa succede (più pratica)

* Default: **padding abilitato**. OpenSSL usa padding PKCS (aggiunge N bytes con valore N dove N è il numero di padding bytes).

* Esempio: se block size = 16 e restano 5 byte, si aggiungono 11 byte di valore `0x0b`. Se il plaintext è già multiplo di 16, si aggiunge un intero blocco di 16 bytes di padding (per poter togliere ambiguità al de-padding). ([manpages.opensuse.org][6])

* Se disabiliti il padding, tu gestisci l’allineamento: utile per protocolli che fanno padding manualmente o per cifre a flusso.

---
## 7) Dimensionamento dei buffer — regole pratiche
* Per cifrare `N` bytes in una singola chiamata:

* Alloca `out` di dimensione almeno `N + block_size` per stare sicuro (quando il padding è abilitato).

* Per cifratura in streaming (più `Update`):  

* Somma i `outl` prodotti ad ogni `EVP_EncryptUpdate` e aggiungi lo spazio per un blocco extra per `EVP_EncryptFinal_ex`.

* Esempio: se leggi file a chunk di 4096 bytes, usa un buffer di `4096 + EVP_CIPHER_block_size(cipher)` per il ciphertext per ogni Update. ([man.openbsd.org][4])

---
## 8) Riuso del contesto / reset
* Per cifrare più messaggi con la stessa chiave:

* Puoi chiamare `EVP_EncryptInit_ex(ctx, NULL, NULL, key, iv)` riutilizzando `ctx` dopo un `EVP_CIPHER_CTX_reset()` o seguendo le linee guida. Alcuni esempi nella community mostrano che si può riusare il contesto per performance, ma attenzione allo stato residuo; spesso è più chiaro chiamare `EVP_CIPHER_CTX_reset()` e poi `EVP_EncryptInit_ex` con i parametri nuovi. ([Stack Overflow][7])

---
# 9) Error handling (pratico)

* Controlla il valore di ritorno (`1` successo, `0` errore).

* In caso di errore, usa `ERR_get_error()` e `ERR_error_string()` per capire cosa è successo.

* Per AEAD, controlla sempre che il tag sia scritto e verificato (lato decrypt), perché la mancanza di verifica può permettere manipolazioni. ([docs.openssl.org][2])
---
# 10) Esempio minimale completo (AES-256-CBC, padding di default)

```c

EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
const unsigned char key[32] = { /* 32 bytes key */ };
const unsigned char iv[16] = { /* 16 bytes iv */ };

unsigned char inbuf[4096];
unsigned char outbuf[4096 + EVP_CIPHER_block_size(EVP_aes_256_cbc())];
int inlen, outlen, tmplen;

/* Init */
if (1 != EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv)) handle_error();

/* Update - possibile loop su file */
if (1 != EVP_EncryptUpdate(ctx, outbuf, &outlen, inbuf, inlen)) handle_error();

/* use first outlen bytes in outbuf */

/* Finalize */
if (1 != EVP_EncryptFinal_ex(ctx, outbuf + outlen, &tmplen)) handle_error();
outlen += tmplen;

/* outbuf[0..outlen-1] contiene il ciphertext completo */  

/* Cleanup */
EVP_CIPHER_CTX_free(ctx);

```
(Questo è lo schema base; in pratica itera `EVP_EncryptUpdate` su chunk di input e accumula gli `outlen` prodotti.) ([man.openbsd.org][4])

---
# 11) Note avanzate e punti di attenzione
* **AEAD (GCM/CCM):** gestisci AAD e tag con le chiamate dedicate (`EVP_EncryptUpdate` per i dati, `EVP_CIPHER_CTX_ctrl` per il tag). Non usare padding per AEAD. ([wiki.openssl.org][5])

* **Provider model (OpenSSL 3.0):** per compatibilità considera `EVP_CIPHER_fetch()` per ottenere `EVP_CIPHER` da un provider, invece di chiamare le funzioni legacy; ma `EVP_EncryptInit_ex` rimane il punto di inizializzazione. ([manpages.opensuse.org][3])

* **Thread-safety:** le funzioni sono thread-safe a patto di non riusare lo stesso `EVP_CIPHER_CTX` simultaneamente da più thread. Crea contesti separati per thread.

* **Versioni**: API e raccomandazioni possono evolvere; controlla la pagina man della versione di OpenSSL che usi. ([docs.openssl.org][2])
---
## 12) Riferimenti ufficiali (letture consigliate)
* OpenSSL man pages (EVP_EncryptInit_ex / EVP_EncryptUpdate / EVP_EncryptFinal_ex). ([manpages.opensuse.org][1])

* OpenSSL Wiki — Symmetric encryption & AEAD examples. ([wiki.openssl.org][8])

# Dimensione del IV
La relazione tra **IV** e **dimensione del blocco** è diretta e importante, ma non è che _l’IV “impone” la dimensione del blocco_ — è **l’algoritmo di cifratura** a determinarla.  
Vediamolo bene.

---
## 🔹 1️⃣ La dimensione del blocco (block size)

Ogni cifrario a blocchi (come AES, DES, ecc.) lavora su blocchi di dimensione fissa.  
Per esempio:

|Algoritmo|Block size|
|---|---|
|AES (qualsiasi variante: 128/192/256 bit di chiave)|**128 bit = 16 byte**|
|DES|64 bit = 8 byte|
|Blowfish|64 bit = 8 byte|
|ChaCha20, RC4|**non a blocchi** (sono stream cipher → no IV nel senso tradizionale)|

Quindi se usi **AES**, il **blocco di elaborazione interno è sempre di 16 byte (128 bit)**, indipendentemente dalla lunghezza della chiave.

---

## 🔹 2️⃣ Il ruolo dell’IV (Initialization Vector)

L’**IV** è un _vettore di inizializzazione_: serve a **randomizzare la cifratura** del primo blocco in modalità come **CBC**, **CFB**, **OFB**, **CTR**, ecc.  
La regola è:

> 🔸 La lunghezza dell’IV deve essere **uguale alla dimensione del blocco** del cifrario.

Quindi:

- Se usi AES → IV da **16 byte**
    
- Se usi DES → IV da **8 byte**
    
- Se usi ChaCha20 → IV da **12 byte** (perché è definito così nella costruzione dello stream cipher)
    

---

## 🔹 3️⃣ Perché la stessa dimensione del blocco?

In modalità **CBC** (Cipher Block Chaining), ad esempio, funziona così:

```
C_0 = IV
C_i = E_K(P_i XOR C_{i-1})
```

Dove:

- `P_i` = blocco di plaintext i-esimo
    
- `C_i` = blocco di ciphertext i-esimo
    
- `E_K` = funzione di cifratura con chiave `K`
    

Per poter fare `P_i XOR C_{i-1}`, i due vettori devono avere **la stessa dimensione**.  
Dato che ogni `C_i` è lungo quanto un blocco dell’algoritmo, **anche l’IV deve essere lungo un blocco**.

Ecco perché nel codice:

```c
unsigned char iv[16] = "0123456789012345"; // 16 byte
```

ha senso _solo_ perché stiamo usando AES (blocco da 16 byte).

---

## 🔹 4️⃣ Non stai “imponendo” la dimensione, la stai rispettando

In altre parole:

> Non è l’IV che definisce la dimensione del blocco,  
> ma è la dimensione del blocco dell’algoritmo che **definisce la lunghezza necessaria dell’IV**.

Se scegli un algoritmo diverso (`EVP_des_cbc()`), l’IV dovrà essere di 8 byte.

---

## 🔹 5️⃣ E lo XOR?

Sì — proprio perché IV e blocchi hanno la stessa lunghezza, puoi fare l’operazione di **XOR** senza problemi:

- il primo blocco di plaintext viene XORato con l’IV;
    
- i blocchi successivi con il ciphertext precedente (`C_{i-1}`).
    

È questo che crea la **dipendenza tra i blocchi** nella modalità CBC.

---

## 🔹 6️⃣ Se l’IV fosse sbagliato?

- Se l’IV è troppo corto → errore a runtime (`EVP_EncryptInit_ex` fallisce).
    
- Se l’IV è troppo lungo → viene troncato.
    
- Se l’IV non cambia → la cifratura non è più semanticamente sicura (stesso plaintext → stesso ciphertext iniziale).
    

---

✅ **Riassumendo**

- L’IV non _impone_ la lunghezza del blocco, la _segue_.
    
- In AES (qualsiasi versione), blocco = 16 byte → IV = 16 byte.
    
- Serve per poter fare XOR correttamente nel primo passaggio (e in generale per evitare ripetizioni prevedibili).
    

---

# Come generare IV e KEY
La KEY deve essere casuale mentre IV non è del tutto necessario: è **fondamentale** per la sicurezza 🔐  
Ti rispondo in modo pratico e dettagliato:

- quando conviene randomizzare **IV** e **KEY**,
    
- **come** farlo correttamente in C con OpenSSL,
    
- e **come gestirle** (salvarle, riutilizzarle, trasmetterle).
    

---

## 🔹 1️⃣ Randomizzare IV e chiave: sì, ma in modo diverso

### 🧊 **IV**

✅ **Deve essere casuale o univoco ad ogni cifratura**.

- Serve per garantire che lo stesso plaintext cifrato due volte produca ciphertext diversi.
    
- **Può essere pubblico** (non serve tenerlo segreto).
    
- **Deve essere trasmesso o memorizzato insieme al ciphertext** (tipicamente all’inizio del file o del pacchetto).
    

### 🔑 **Chiave**

⚠️ **Deve essere segreta**, ma **non deve cambiare per ogni blocco** o messaggio a meno che tu non voglia farlo.

- Di solito la chiave deriva da una password o da un key exchange (es. PBKDF2, HKDF, Diffie–Hellman, ecc.).
    
- Puoi anche generarla casualmente per sessioni temporanee, ma allora devi salvarla o condividerla in modo sicuro.
    

---

## 🔹 2️⃣ Come generarle correttamente in C con OpenSSL

OpenSSL fornisce una funzione sicura per numeri casuali crittografici:

```c
#include <openssl/rand.h>

int RAND_bytes(unsigned char *buf, int num);
```

---

### 🔸 Esempio completo: generazione casuale di KEY e IV (AES-256-CBC)

```c
#include <openssl/evp.h>
#include <openssl/rand.h>
#include <stdio.h>
#include <string.h>

int main() {
    unsigned char key[32]; // 256 bit = 32 byte
    unsigned char iv[16];  // 128 bit = 16 byte (block size AES)

    // 1. Genera key e IV casuali
    if (RAND_bytes(key, sizeof(key)) != 1) {
        fprintf(stderr, "Errore nella generazione della chiave\n");
        return 1;
    }

    if (RAND_bytes(iv, sizeof(iv)) != 1) {
        fprintf(stderr, "Errore nella generazione dell'IV\n");
        return 1;
    }

    // 2. Stampa (solo per test!)
    printf("Chiave generata:\n");
    for (int i = 0; i < sizeof(key); i++) printf("%02x", key[i]);
    printf("\n\nIV generato:\n");
    for (int i = 0; i < sizeof(iv); i++) printf("%02x", iv[i]);
    printf("\n");

    // ... ora puoi usare key e iv in EVP_EncryptInit_ex(...)
    return 0;
}
```

Compila con:

```bash
gcc -o gen_key_iv gen_key_iv.c -lcrypto
```

---

## 🔹 3️⃣ Come gestire i valori generati

### 🧊 **IV**

- Lo puoi **scrivere all’inizio del file cifrato**, es.:
    
    ```
    [16 byte IV][ciphertext...]
    ```
    
- Quando decifri, leggi i primi 16 byte → quelli sono l’IV.
    

### 🔑 **Chiave**

- Va **protetta**.  
    Non la salvi mai in chiaro su disco.  
    Puoi:
    
    - derivarla da una password (vedi sotto),
        
    - cifrarla con una chiave pubblica (RSA),
        
    - oppure conservarla in un keystore o TPM.
        

---

## 🔹 4️⃣ Derivare la chiave da password (metodo pratico)

Se vuoi che l’utente inserisca una password e da quella ricavi una chiave “forte” da 256 bit, puoi usare **PBKDF2**:

```c
#include <openssl/evp.h>
#include <openssl/rand.h>

unsigned char key[32];
unsigned char salt[16];
const char *password = "mia_password_sicura";

// Genera salt casuale
RAND_bytes(salt, sizeof(salt));

// Deriva la chiave (100.000 iterazioni SHA-256)
PKCS5_PBKDF2_HMAC(password, strlen(password),
                  salt, sizeof(salt),
                  100000, EVP_sha256(),
                  sizeof(key), key);
```

✔️ Il **salt** è pubblico (serve solo per rendere unica la derivazione).  
✔️ La **password** è segreta.  
✔️ La **chiave derivata** è usata in `EVP_EncryptInit_ex`.

---

## 🔹 5️⃣ In sintesi

|Cosa|Deve essere casuale?|Deve restare segreta?|Deve cambiare ogni volta?|
|---|---|---|---|
|**IV**|✅ Sì|❌ No|✅ Sì|
|**KEY**|✅/❌ (dipende)|✅ Sì|❌ No (tranne sessioni temporanee)|
|**SALT (PBKDF2)**|✅ Sì|❌ No|✅ Sì|

---

## 🔹 6️⃣ Best practices di sicurezza

- Usa sempre `RAND_bytes()` per entropia crittografica.
    
- Non usare `rand()` o `srand()`: **non sono sicuri**.
    
- Non riutilizzare IV con la stessa chiave.
    
- Non salvare le chiavi in chiaro su file o codice sorgente.
    
- Per lunghe sessioni, considera cifratura AEAD (AES-GCM) con IV random e tag di autenticazione.
    

---