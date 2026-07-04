---
tags: [ethl, hacking-exposed-7, credential-dumping, sam, syskey, cap4]
capitolo: 4
data: 2026-07-02
collegamenti: ["[[ETHL - LSASS Credential Dumping]]", "[[ETHL - LAN Manager (LM) vs NTLM]]", "[[ETHL 0x12 - Cap 4 Hacking Windows]]"]
---

# SAM (Security Accounts Manager)

> [!abstract] Di cosa parla
> Il database degli account **locali** di una macchina Windows: dove sta, cosa contiene, come è protetto e come si estraggono i suoi hash. È la controparte Windows di `/etc/passwd` già incontrata in enumeration, e la fonte "a disco/registro" del terzetto SAM / LSASS / LSA Secrets. Chiave di lettura: il SAM riguarda gli utenti *locali* di quella singola macchina, indipendentemente dal dominio.

---

## Cos'è e dove sta

> [!info] Database account locali
> Il SAM contiene gli account **locali** della macchina e i loro **hash NT** (storicamente anche LM). È ortogonale ad Active Directory: esiste anche su una macchina standalone, e contiene l'**Administrator locale** e gli altri utenti definiti su *quella* macchina — non gli utenti di dominio (quelli stanno in `ntds.dit` sul domain controller).

> [!info] Percorsi
> Due posti, stesso dato: il file `%systemroot%\system32\config\SAM` e la chiave di registro `HKLM\SAM`. Il file è **lockato** mentre l'OS gira (non lo copi banalmente), ma è montato come ramo di registro accessibile con privilegi adeguati. Per decifrare gli hash serve anche il ramo `HKLM\SYSTEM`, che contiene la chiave SYSKEY.

---

## SYSKEY

> [!info] La cifratura del SAM
> Gli hash nel SAM non stanno in chiaro: sono cifrati con una chiave (**SYSKEY**, o bootkey) derivata da valori sparsi nel ramo `HKLM\SYSTEM`. Per questo, per estrarre gli hash, servono **entrambi** i rami: `SAM` (gli hash cifrati) e `SYSTEM` (il materiale per ricostruire la SYSKEY). Con solo uno dei due non si arriva agli hash utilizzabili.

> [!warning] Backup e boot alternativo
> Storicamente il SAM si prendeva anche da vie laterali: il backup del **Repair Disk** (`%systemroot%\repair\`), o bootando un **OS alternativo** per copiare i file a disco lockato aggirato. Ma il backup è protetto da SYSKEY, quindi molto più duro/inutile da craccare senza il ramo SYSTEM corrispondente. La difesa fisica (disco cifrato, BitLocker) chiude queste vie offline.

---

## Come si estraggono gli hash

> [!info] Idea generale
> Non si "legge" un file di password: si esportano i rami `SAM` e `SYSTEM`, si ricostruisce la SYSKEY dal secondo, la si usa per decifrare gli hash del primo. Serve privilegio **SYSTEM / admin locale** (o accesso offline al disco). Il risultato è un elenco di `utente:RID:LM:NT:::` — cioè gli hash NT riusabili per pass-the-hash o da craccare offline.

> [!info] Da locale con mimikatz
> Sulla macchina viva, con privilegi adeguati:

```text
mimikatz # token::elevate
mimikatz # lsadump::sam
```

> [!info] Da remoto o offline con Impacket
> `secretsdump.py` è il flusso tipico su HTB: estrae il SAM (più LSA Secrets e cache) da remoto con credenziali admin, oppure offline dai rami esportati.

```bash
# Remoto, con credenziali admin
secretsdump.py DOMINIO/administrator:password@<IP-target>

# Offline, da rami di registro salvati (es. reg save HKLM\SAM sam.hive)
secretsdump.py -sam sam.hive -system system.hive LOCAL
```

> [!tip] Cosa esce e come si usa
> Escono gli **hash NT** degli account locali. Si **riusano** direttamente con pass-the-hash (l'hash è la credenziale, niente cracking) oppure si **craccano** offline con hashcat/John. L'hash dell'**Administrator locale** è il bersaglio d'oro: se la stessa password admin locale è riusata su molte macchine, un solo hash le apre tutte.

---

## Perché conta per il movimento laterale

> [!info] Password locale riusata
> Il rischio maggiore non è il singolo hash, ma il **riuso**: se l'immagine aziendale imposta la stessa password Administrator locale ovunque, l'hash preso da una macchina fa pass-the-hash su tutte le altre. È il classico movimento laterale "orizzontale". La contromisura strutturale è **LAPS**, che assegna a ogni macchina una password Administrator locale **diversa e ruotata**, spezzando la catena.

---

## Contromisure

> [!warning] Come si difende
> Privilegio **SYSTEM** già necessario per leggere il SAM → difesa a monte: least privilege, EDR, non farsi ottenere admin locale. **LAPS** per uccidere il riuso della password locale. **Disabilitare LM** perché il SAM non conservi l'hash LM debole accanto all'NT. Sicurezza **fisica** (BitLocker) contro l'estrazione offline via boot alternativo o furto del disco. Password locali forti, così che anche l'hash craccato resti fuori portata.

---

## Fili rossi

> [!tip] Come si lega al resto
> **SAM = /etc/passwd**: il ponte con l'enumeration del Cap. 3. **Hash NT = credenziale**: stesso principio della nota NTLM e di Pass-the-Hash — l'hash del SAM si riusa senza craccare. **Tre fonti**: il SAM è la fonte "registro/disco" accanto a LSASS (RAM) e LSA Secrets — vedi la nota LSASS. **Retrocompatibilità = buco**: l'hash LM ancora presente accanto all'NT è l'ennesimo caso.

---

## Punti aperti

> [!question] Da verificare
> Il dettaglio di come la SYSKEY è derivata dal ramo SYSTEM (obfuscation dei valori) rispetto al solo concetto "serve anche SYSTEM". Da confermare se l'esame chiede il formato `utente:RID:LM:NT` e le vie offline (Repair Disk, boot alternativo) o solo l'estrazione moderna via secretsdump.
