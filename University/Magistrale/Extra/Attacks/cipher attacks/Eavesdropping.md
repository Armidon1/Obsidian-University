# **Eavesdropping (intercettazione o sniffing)**

> **Eavesdropping** è un attacco **passivo** in cui l’attaccante **ascolta o cattura le comunicazioni** tra due o più parti per ottenere informazioni sensibili, **senza alterare i dati** o interferire direttamente con la trasmissione.

Il termine deriva da _“to eavesdrop”_ (origliare): l’attaccante si limita ad ascoltare ciò che viene trasmesso.

---

### **Caratteristiche principali**

- **Tipo di attacco:** passivo (nessuna modifica ai dati).
    
- **Obiettivo:** ottenere informazioni riservate (password, messaggi, credenziali, numeri di carte, dati aziendali).
    
- **Livello:** può avvenire su rete (sniffing di pacchetti), su linea telefonica, su canali wireless o persino tramite segnali elettromagnetici.
    

---

### **Esempi pratici**

- **Packet sniffing:** l’attaccante usa strumenti come _Wireshark_, _tcpdump_ o _Ettercap_ per catturare pacchetti su una rete locale non cifrata.
    
- **Wi-Fi sniffing:** intercettare traffico su reti Wi-Fi pubbliche (specialmente se non protette da WPA2/WPA3).
    
- **VoIP e intercettazioni telefoniche:** registrare chiamate non cifrate.
    
- **Email sniffing:** leggere messaggi SMTP/POP3/IMAP non cifrati.
    
- **Eavesdropping su Bluetooth o NFC:** intercettare comunicazioni tra dispositivi vicini.
    

---

### **Differenza con Man-in-the-Middle (MITM)**

- **Eavesdropping:** solo ascolto → attacco **passivo**.
    
- **MITM:** ascolto **e modifica/iniezione** di dati → attacco **attivo**.
    

> In pratica, l’eavesdropping è spesso la **fase iniziale** o “di ricognizione” di un attacco MITM.

---

### **Contromisure**

1. **Cifratura end-to-end:**
    
    - HTTPS / TLS per il traffico web.
        
    - SSH per l’accesso remoto.
        
    - VPN per cifrare tutto il traffico su reti insicure.
        
    - Signal / WhatsApp / Matrix per messaggistica cifrata end-to-end.
        
2. **Reti wireless sicure:** WPA2 o WPA3, password forti, disattivare reti aperte.
    
3. **Segmentazione e VLAN:** per isolare il traffico sensibile da reti pubbliche.
    
4. **Network monitoring:** IDS/IPS per rilevare sniffing o port mirroring non autorizzato.
    
5. **Evitare protocolli insicuri:** come Telnet, HTTP, FTP, POP3, IMAP senza TLS.
    
6. **VPN obbligatoria su reti pubbliche.**
    
7. **Cablare reti critiche:** meno vulnerabili a sniffing radio.
    
8. **Educazione degli utenti:** evitare l’uso di reti Wi-Fi sconosciute o non cifrate.
    

---

### **In breve**

> **Eavesdropping** = “origliare” la rete.  
> Un attacco **passivo** in cui un avversario **intercetta il traffico** per leggere dati sensibili.
> 
> 🔒 Difesa: **cifratura end-to-end (TLS, VPN, HTTPS)** + **reti protette e segmentate** + **monitoraggio di rete**.