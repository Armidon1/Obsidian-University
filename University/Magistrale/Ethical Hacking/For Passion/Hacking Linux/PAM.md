**PAM = Pluggable Authentication Modules.** È il _framework di autenticazione_ di Linux (nato in Solaris, poi Linux-PAM). Risolve un problema preciso di disaccoppiamento.

**Il problema.** Prima di PAM, ogni programma che doveva autenticare un utente — `login`, `sshd`, `su`, `sudo`, `passwd`, lo screen locker, l'FTP daemon — implementava l'autenticazione _al suo interno_: tipicamente leggeva `/etc/passwd` + `/etc/shadow` e faceva `crypt()` a mano. Conseguenza: per cambiare _come_ si autentica (aggiungere LDAP, Kerberos, 2FA, regole di complessità password, lockout dopo N tentativi) avresti dovuto **ricompilare ognuno** di quei programmi. Non scala.

**L'inversione.** PAM mette uno strato in mezzo. L'applicazione si linka a `libpam` e dice solo _"autenticami questo utente"_ via una API standard (`pam_authenticate()` ecc.). È poi PAM a consultare una **configurazione** che elenca quali **moduli** eseguire. I moduli sono **file `.so`** (shared object). Cambi la config → cambi l'autenticazione di _tutte_ le app PAM-aware, zero ricompilazioni.

**Architettura concreta:**

- Config in `/etc/pam.d/<servizio>` — un file per servizio: `/etc/pam.d/sshd`, `/etc/pam.d/login`, `/etc/pam.d/sudo`...
- Ogni riga: `tipo control-flag modulo.so [argomenti]`.
- I moduli stanno in una directory tipo `/lib/security/` o `/lib/x86_64-linux-gnu/security/`.
- I quattro **tipi** di modulo (management groups):

|Tipo|A cosa serve|Modulo tipico|
|---|---|---|
|`auth`|verifica l'identità (controlla la password / il token)|`pam_unix.so`|
|`account`|l'account è valido? (scaduto, orario consentito, host)|`pam_unix.so`, `pam_time.so`|
|`password`|aggiornamento del token (cambio password, complessità)|`pam_pwquality.so`|
|`session`|setup/teardown attorno alla sessione (mount home, limiti, log)|`pam_systemd.so`, `pam_limits.so`|

- I **control flag** (`required`, `requisite`, `sufficient`, `optional`) decidono come si combinano successi/fallimenti dei moduli impilati → è la **"PAM stack"**: i moduli di un tipo girano dall'alto in basso e il risultato viene aggregato.
- Moduli reali: `pam_unix.so` (il check classico su `/etc/shadow`), `pam_sss.so` (LDAP/AD via SSSD), `pam_krb5.so`, `pam_google_authenticator.so` (TOTP), `pam_faillock.so` (lockout).

**Perché è il vettore di trojan perfetto** — il punto della nota `[[trojan_binaries]]`:

1. Un modulo PAM malevolo è solo un `.so` che espone i simboli giusti (`pam_sm_authenticate`...). Lo droppi e aggiungi **una riga** a `/etc/pam.d/common-auth` (o trojanizzi direttamente `pam_unix.so`).
2. Gira **nel contesto di processo di ogni app che autentica** — `sshd`, `login`, `sudo`, `su`, il display manager. Un modulo solo = credenziali raccolte da _tutti_ i punti d'ingresso.
3. PAM consegna al modulo la **password in chiaro** (gli serve per fare hash-e-confronto). Quindi il modulo malevolo la logga _prima_ di passare al check vero. Oppure fa: _"se password == magica → `PAM_SUCCESS`"_ → **password universale**, backdoor su ogni servizio.
4. **Batte HE7**: non hai toccato `/bin/login` né `/usr/sbin/sshd` — quei binari restano byte-identici al vendor, quindi `rpm -V` / `debsums` / AIDE su di essi non vedono **nulla**. La malizia è in una _libreria_ + _config_, che il controllo d'integrità dei binari nominati non copre. E sopravvive a un `apt upgrade` di `openssh-server`, perché non hai modificato i suoi file.

È letteralmente "il `login` trojanizzato" di HE7, fatto al livello giusto. In ATT&CK: T1556.003 — Modify Authentication Process: _Pluggable Authentication Modules_. È una tecnica documentata e ricorrente nel malware Linux reale.

Contromisura coerente: estendere il File Integrity Monitoring a `/etc/pam.d/` e alla directory dei moduli `security/`, non solo ai binari di sistema. Se controlli solo `/bin/login`, questo attacco ti passa sotto.
