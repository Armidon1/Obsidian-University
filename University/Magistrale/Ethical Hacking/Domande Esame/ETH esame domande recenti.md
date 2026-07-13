# Giugno 2025
-  footprinting
-  network ping sweeps
-  android security measures
-  cronjob with tar
-  BOF with ROP chain

# Luglio 2024
- Windows security measures
- Files da controllare dopo un apt attack
- Android remote attacks (data stealing, url sourced malware e carrier iq)
- Cronjob 
- BoF per fare ret2win

# Giugno 2024
- Windows enumeration
- Password dumping e cracking su windows
- Voip hacking

# Gennaio 2024
- SNMP
- 4 WINDOWS SECURITY FEATURES
- VoIP
- SYN E TCP CONNECT
- Esercizio su sql


# Settembre 2023

- Footprinting
- Windows covering track
- Android hacking: remote shell with 0 permission, htc logger, url  sourced-malware
- unix permission


# Luglio 2023

- SNMP enumeration
- Attacks over VoiP
- WPA enterprise attack (EAP attacks)
- Integer Overflow
- esercizio exploit suid, su variable $PATH

# Giugno 2023
-  wireless interface sniffing and reverse Firmware
- rooting andorid and cross-compiler
- why html staless? sessions? 
- return to programming exercise
- 6 step APT

# Settembre 2022
Prima domanda era su covering tracks in Windows, rootkit, tutti i tool che si usano, le contromisure e dove generalmente vengono piazzati i rootkit in Windows

Seconda domanda era su bus sniffing per interfacce wireless e firmware reversing, sempre con tool e contromisure

Terza domanda erano le vulnerabilità di Android, nello specifico:
- remote shell with zero permission
- HTC logger
- URL-sourced malware
Sempre tool e contromisure.

Quarta domanda era spiegare il sistema di permessi di UNIX ed i file SUID.

Quinta domanda era un classico buffer overflow ma nel main stava una strlen che controllava la lunghezza del buffer, e se era >128 non ti faceva andare nella funzione vulnerabile.
Veniva chiesto se fosse possibile fare BOV, e se si perché, o se non fosse possibile, e se no perché e come avresti modificato il codice per farlo funzionare