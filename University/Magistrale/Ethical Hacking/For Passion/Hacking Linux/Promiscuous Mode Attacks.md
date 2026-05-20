---

tags:

- network
- sniffing
- promiscuous-mode
- parser-vulnerabilities
- hacking-exposed-7
- attacco-rete
- rce aliases:
- attaccare il sniffer
- promiscuous mode attack
- sniffer exploit

---

# Promiscuous Mode Attacks — Attaccare chi Sniffa

## 1. Il concetto

La modalità promiscua è normalmente un vantaggio per l'attaccante: vede tutto il traffico della rete. Ma ha un costo nascosto — **espone il software di sniffing a input non fidato che normalmente non processerebbe mai**.

> [!abstract] Il ribaltamento L'attaccante che mette la NIC in promiscuous mode diventa a sua volta un **bersaglio**. Chiunque sulla stessa rete può iniettare pacchetti crafted per sfruttare vulnerabilità nel sniffer.

---

## 2. Perché promiscuous mode amplia la superficie d'attacco

In modalità normale una NIC scarta i frame non indirizzati a lei — il driver e il software non li vedono mai. In modalità promiscua **tutto il traffico arriva al software**, che deve parsarlo.

```
Modalità normale:
[Frame → NIC] → MAC check → scarta se non per me
                          → passa al kernel se per me

Modalità promiscua:
[Frame → NIC] → nessun filtro → tutto passa al kernel → tutto al sniffer
```

Risultato: tcpdump / Wireshark / qualsiasi sniffer deve **parsare ogni singolo frame** sul segmento di rete, inclusi quelli che non gli erano destinati e quelli deliberatamente malformati.

---

## 3. Il vettore d'attacco

```
[Attaccante A] sniffa la rete in promiscuous mode
                    ↓
[Difensore / Attaccante B] inietta pacchetto crafted:
  - header malformato per triggerare bug nel parser
  - payload progettato per heap overflow / use-after-free
  - in un protocollo esotico che il sniffer parsa raramente
                    ↓
tcpdump / Wireshark / libpcap processa il frame
                    ↓
Bug nel dissector → crash o RCE sulla macchina di A
```

---

## 4. Lo stesso schema — pattern ricorrente

Questa è **la stessa logica** già vista con il browser:

|Contesto|Input non fidato|Software che lo parsa|Risultato se bug|
|---|---|---|---|
|**Browser**|Pagine web|Motore JS, decoder media, parser HTML|RCE nel renderer|
|**Mail client**|Allegati|Parser PDF, Office, immagini|RCE sul client|
|**Sniffer**|Pacchetti di rete|Dissector di protocollo|RCE sulla macchina che sniffa|
|**Antivirus**|File scansionati|Parser di ogni formato|RCE con privilegi elevati|

> [!tip] Il pattern universale **Processo untrusted input → parser complesso → bug di memoria → RCE** Ogni volta che un software deve interpretare dati arbitrari dall'esterno, quella superficie è potenzialmente attaccabile. Più protocolli/formati supportati = più superficie.

---

## 5. Non è teorico — Wireshark ha una storia di CVE

Wireshark ha avuto **decine di vulnerabilità nei protocol dissectors** — i moduli che decodificano singoli protocolli. Il motivo è strutturale:

- Supporta **3000+ protocolli** (inclusi protocolli industriali, telecom, reti proprietarie)
- Molti dissector sono codice C legacy scritto per scopo educativo/forense, non con security-first mindset
- Un pacchetto malformato per un protocollo raramente usato può triggerare codepath mai testati

Esempi di classi di bug ricorrenti nei dissector:

- Heap overflow (lunghezza campo non validata)
- Use-after-free (gestione lifetime oggetti nel parsing)
- Stack overflow (ricorsione su strutture nested)
- Integer overflow su length fields

> [!warning] Implicazione pratica Se lanci Wireshark su una rete ostile stai parsando traffico potenzialmente crafted ad hoc contro di te. Wireshark stesso avverte di non girare come root e consiglia l'architettura separata `dumpcap` + analisi offline.

---

## 6. Architettura sicura per il sniffing

Wireshark ha risposto a questo problema con separazione dei privilegi:

```
dumpcap (processo minimale, gira con CAP_NET_RAW o setuid)
    ↓ scrive pcap su disco / pipe
Wireshark (processo non privilegiato, parsa il file)
```

- `dumpcap` fa solo cattura raw, superficie minima, codice minimale
- Wireshark, che ha la superficie enorme (tutti i dissector), processa il file **già catturato**, non il traffico live
- Se Wireshark viene compromesso da un pacchetto crafted nel pcap, gira come utente normale

> [!note] Analogia Linux È il principio di `setuid` + separazione dei processi che conosci da sysadmin: il processo privilegiato fa il minimo indispensabile, il grosso del lavoro lo fa un processo non privilegiato.

---

## 7. Uso offensivo — attaccare il ricognitore

Un defender che sa di essere sotto sniffing può **ribaltare la situazione**:

```
Defender accorge che qualcuno sniffa la rete
    ↓
Invia pacchetti crafted per protocolli con dissector noti vulnerabili
    ↓
Possibile RCE sulla macchina del sniffer
```

È un caso di **active counterattack** contro ricognizione passiva. Raro in pratica, ma concettualmente importante: la ricognizione passiva non è mai completamente priva di rischio per chi la conduce.

Lo stesso principio si applica ad altri strumenti di recon:

- **nmap** — ha avuto bug nel parsing delle risposte
- **Metasploit auxiliary scanner** — parser di banner, certificati TLS, response HTTP
- **Qualsiasi tool che parsa risposte di rete**

---

## 8. Contromisure per chi fa sniffing

|Contromisura|Cosa mitiga|
|---|---|
|**Non girare il sniffer come root**|Limita il danno in caso di exploit riuscito|
|**Architettura dumpcap + analisi offline**|Separa cattura (privilegiata, minima) da parsing (non privilegiata, massima superficie)|
|**Aggiornare tcpdump / Wireshark**|Chiude CVE noti nei dissector|
|**Sniffare in VM / container isolato**|Sandbox blast radius in caso di compromise|
|**Sniffare su rete isolata / tap**|Riduce traffico non fidato sulla stessa rete|
|**Leggere pcap offline**|Il file è statico, non c'è injection live|

---

## Takeaways

1. **Promiscuous mode = superficie d'attacco ampliata** — il sniffer processa tutto il traffico, incluso quello crafted ad hoc
2. Il vettore è lo stesso del browser attack: **parser complesso che processa input non fidato → bug di memoria → RCE**
3. Wireshark ha avuto molti CVE nei dissector proprio per questo — 3000+ protocolli supportati = superficie enorme
4. La contromisura architetturale è **separazione dei privilegi**: dumpcap (minimale, privilegiato) + Wireshark (massiva superficie, non privilegiato)
5. Un defender consapevole può **iniettare pacchetti crafted** per attaccare chi lo sta sniffando — ricognizione passiva non è mai risk-free
6. Il pattern **"attacco il ricognitore"** si applica a qualsiasi tool che parsa risposte di rete (nmap, scanner, ecc.)

---

## Wiki-links

- [[promiscuous_mode]]
- [[browser_attack]]
- [[arp_poisoning]]
- [[network_recon]]
- [[parser_vulnerabilities]]
- [[least_privilege]]
- [[wireshark]]
- [[tcpdump]]
- [[hacking_exposed_7_unix]]