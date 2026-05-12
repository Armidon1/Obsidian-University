# TFTP — Trivial File Transfer Protocol

Tags: #networking #enumeration #protocols #hacking-exposed

---

## Cos'è

TFTP è una versione ridotta all'osso di FTP, progettata per essere il più semplice possibile. Gira su **UDP porta 69** e non ha autenticazione — ci si connette e si richiedono file direttamente.

---

## Differenze con FTP

| |FTP (porta 21)|TFTP (porta 69)|
|---|---|---|
|Trasporto|TCP|**UDP**|
|Autenticazione|Username + password|**Nessuna**|
|Directory listing|Sì|No|
|Resume trasferimenti|Sì|No|
|Gestione errori|Robusta|Minimale|
|Complessità|Full featured|Trivialmente semplice|

---

## Usi legittimi

Esiste per trasferire file a dispositivi che non hanno ancora un OS o hanno risorse molto limitate:

- **Network booting (PXE)** — un server bare metal richiede la sua immagine di avvio via TFTP prima ancora di avere un OS caricato
- **Firmware update router/switch** — dispositivi di rete che scaricano config o firmware da un server TFTP sulla LAN
- **IP phone / VoIP** — i telefoni VoIP scaricano la loro configurazione all'avvio
- **Sistemi embedded** — qualsiasi dispositivo troppo leggero per un client FTP completo

---

## Perché è interessante per l'attaccante

**Nessuna autenticazione** è il problema ovvio. Se un server TFTP è esposto o mal configurato, puoi richiedere file direttamente per nome senza credenziali:

```bash
# Connessione e richiesta file
tftp 10.10.10.x
tftp> get /etc/passwd
tftp> get config.txt
tftp> get cisco-config.cfg
```

Non c'è directory listing → devi **indovinare i nomi dei file** (wordlist o nomi comuni).

### Target comuni su TFTP mal configurati

|File|Contenuto sensibile|
|---|---|
|Config router/switch|Credenziali in chiaro|
|Config VoIP/SIP|Credenziali SIP|
|Immagini PXE|Modificabili per evil maid attack|
|File dimenticati dal sysadmin|Qualsiasi cosa|

---

## Rilevamento con Nmap

TFTP gira su **UDP** → serve `-sU`:

```bash
sudo nmap -sU -p 69 10.10.10.x

# Con versione
sudo nmap -sU -sV -p 69 10.10.10.x
```

> ⚠️ Gli scan UDP sono lenti — limita le porte quando puoi

---

## Workflow su HTB

Se Nmap mostra UDP porta 69 aperta, il path tipico è:

```
1. Connetti con tftp
2. Prova nomi di file comuni (wordlist o intuizione)
3. Scarica file sensibile (config, credenziali...)
4. Usa le info trovate per pivot o accesso successivo
```

```bash
# Esempio pratico
tftp 10.10.10.x
tftp> get secret.txt
tftp> get id_rsa
tftp> get .htpasswd
tftp> get backup.tar.gz
```

---

## Contromisure

- Non esporre TFTP su interfacce pubbliche — solo su LAN interna
- Firewall che blocca UDP/69 dall'esterno
- Limitare i file accessibili con permessi stretti sul filesystem
- Preferire SFTP o SCP quando possibile

---

## Riferimenti

- _Hacking Exposed 7_ — Cap. Enumeration
- RFC 1350 — The TFTP Protocol
- `man tftp`