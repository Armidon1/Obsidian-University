---

tags:

- network
- firewall
- hacking-exposed-7
- attacco-rete
- ip-options
- legacy aliases:
- source routing
- LSR
- SSR
- IP options exploit

---

# IP Source Routing — Firewall Bypass via IP Options

## 1. Il meccanismo base

Normalmente il percorso di un pacchetto IP è deciso dai **router intermedi**: ogni router guarda il campo Destination e sceglie il next-hop in autonomia. Il mittente non ha voce in capitolo.

**IP Source Routing** è un'opzione legacy dell'header IP (campo Options, RFC 791) che inverte questa logica: il mittente può specificare esplicitamente uno o più router che il pacchetto **deve** attraversare.

|Tipo|Comportamento|
|---|---|
|**LSR — Loose Source Routing**|Specifica alcuni hop obbligatori, il resto è libero ai router|
|**SSR — Strict Source Routing**|Specifica esattamente _tutti_ gli hop, nessuna deviazione|

> [!note] Analogo nella vita reale È come spedire un pacco e scrivere sulla busta "deve passare obbligatoriamente per il deposito di Milano prima di arrivare a Roma", invece di lasciare che il corriere scelga il percorso.

---

## 2. La struttura del pacchetto source-routed

Il campo Destination nell'header IP **non è la destinazione finale** — è il **prossimo hop** nella lista. La destinazione finale è embedded nel campo Options.

```
IP Header di un pacchetto LSR:
┌─────────────────────────────────┐
│ Destination = 10.0.0.1          │  ← firewall (prossimo hop)
│ Options: LSR = [192.168.1.10]   │  ← host interno (destinazione finale)
└─────────────────────────────────┘
```

Quando il router che riceve il pacchetto processa il source route:

1. Legge il campo LSR / SSR
2. **Swappa il suo IP** nella lista al posto di quello letto
3. Avanza il puntatore al prossimo hop
4. Forwarda il pacchetto verso l'indirizzo che era in lista

---

## 3. Il vettore d'attacco — bypass del firewall

```
[Attaccante esterno]
        |
        | pacchetto: Dest=firewall, LSR=[host_interno]
        ↓
[Firewall / router perimetrale]
        |  ← vede dest=se stesso → ingress rules: OK ✓
        |  ← source routing abilitato → forwarda a host_interno
        ↓
[Host interno]  ← normalmente irraggiungibile dall'esterno
```

### Perché il firewall non blocca la seconda fase?

Su **packet-filter classici** (l'era di HE7, iptables semplici), il processing del source routing avveniva in un **code path separato** dalla policy di filtraggio:

- La regola di ingress controlla `dest = firewall` → passa ✓
- Il forwarding source-routed verso l'interno **non coincide** con nessuna chain `INPUT` né con la chain `FORWARD` standard (che controlla source/dest normali, non route embedded nelle options)

> [!warning] La confusione comune Il bypass **non ignora le rule tables** — le _circumnaviga_ arrivando con un destination address lecito (il firewall stesso) e sfruttando il forwarding come vettore separato. È un problema di **trust implicita nella fase di routing**, non di regole mancanti sul destination address.

### Packet-filter vs Stateful firewall

|Tipo di firewall|Vulnerabile?|
|---|---|
|**Packet-filter classico** (iptables semplici, ACL router)|✅ Sì — ispeziona header per header, non traccia il contesto|
|**Stateful firewall moderno** (nftables, pf, Cisco ASA, ecc.)|❌ No — ispeziona ogni pacchetto in ogni direzione indipendentemente dal dest|

---

## 4. Il fix — disabilitare source routing nel kernel

La soluzione più robusta è droppare i pacchetti con IP source route option **prima che arrivino al firewall applicativo**, nel kernel stesso:

```bash
# Linux — disabilita accept_source_route (default su sistemi moderni)
sysctl -w net.ipv4.conf.all.accept_source_route=0
sysctl -w net.ipv4.conf.default.accept_source_route=0

# Permanente in /etc/sysctl.conf:
net.ipv4.conf.all.accept_source_route = 0

# Verifica stato attuale:
cat /proc/sys/net/ipv4/conf/all/accept_source_route
# output: 0  ← disabilitato correttamente
```

Con `accept_source_route = 0` il problema non esiste nemmeno, indipendentemente da come sono scritte le regole firewall.

---

## 5. Rilevanza oggi

> [!abstract] Stato attuale Praticamente **zero** in ambienti moderni — tutti i router, kernel Linux e Windows droppano source-routed packets di default da anni. È rimasto nei libri per ragioni storiche e concettuali.

### Perché è ancora utile studiarlo

Il principio sottostante — **policy bypass tramite layer/campo non ispezionato** — si ripresenta in forme moderne:

- **IPv6 Extension Headers**: header di tipo Routing (tipo 0) aveva vulnerabilità analoghe, deprecato con RFC 5095 (2007)
- **Tunnel / overlay network** (GRE, VXLAN): se il firewall non ispeziona il payload del tunnel, un attaccante può incapsulare traffico bloccato
- **NAT traversal e double encapsulation**: tecniche simili per VLAN hopping

---

## 6. Contesto HE7

Questo attacco appare nel capitolo **"Hacking Unix" / "Route through a UNIX system"** come tecnica per circumnavigare firewall basati su UNIX. Il contesto è reti con host UNIX che fungono da firewall/router perimetrali con source routing abilitato per default.

---

## Takeaways

1. **IP Source Routing** permette al mittente di imporre il percorso — il dest nell'header IP è il next-hop, non la destinazione finale
2. Il bypass sfrutta la **separazione tra ingress filter e forwarding source-routed** nei packet-filter classici
3. Non si tratta di "ignorare le rule tables" ma di arrivare con un destination lecito e sfruttare il forwarding come vettore alternativo
4. Il fix è al livello kernel (`accept_source_route=0`), non solo nelle regole firewall
5. Il pattern concettuale (policy bypass via campo non ispezionato) è ancora rilevante in contesti moderni

---

## Wiki-links

- [[promiscuous_mode]]
- [[arp_poisoning]]
- [[firewall_evasion]]
- [[ip_header_options]]
- [[network_recon]]
- [[hacking_exposed_7_unix]]