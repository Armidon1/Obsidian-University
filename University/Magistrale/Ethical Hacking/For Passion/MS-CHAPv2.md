---
tags: [ethl, autenticazione, ms-chapv2, ntlm, hash, leap, peap, concetto]
tipo: concetto
data: 2026-07-13
collegamenti: ["[[ETHL - Cap 8 Wireless Hacking]]", "[[ETHL - Cap 7 Remote Connectivity e VoIP Hacking]]", "[[ETHL - LAN Manager (LM) vs NTLM]]"]
---

# ETHL — MS-CHAPv2

> [!abstract] Il filo
> MS-CHAPv2 è un challenge-response *mutuo* basato sull'hash NT della password: sembra sicuro perché la password non viene mai spedita, ma ha due peccati. Il primo è l'hash NT **senza sale** (stessa password → stesso hash → rainbow table). Il secondo, molto più grave, è strutturale: la sua sicurezza **collassa a una sola chiave DES-56**, quindi è crackabile *a prescindere da quanto è forte la password*. Nudo (PPTP, LEAP) è morto; regge **solo** se incapsulato in un tunnel TLS con certificato validato (PEAP, EAP-TTLS). È lo stesso mondo degli hash NT senza salt di [[ETHL - LAN Manager (LM) vs NTLM]].

## Cos'è e dove si usa

MS-CHAPv2 (Microsoft Challenge-Handshake Authentication Protocol v2, RFC 2759) è un protocollo di autenticazione **mutua** a sfida-risposta: sia il client sia il server si autenticano a vicenda, e la prova di possesso passa dall'**hash NT** della password senza trasmetterla mai in chiaro. Non è un protocollo «di rete» a sé: è un mattone che ricompare in tre posti che contano per il corso — le **VPN PPTP**, il protocollo wireless **LEAP** (Cisco), e come **autenticazione interna** di **PEAP** ed **EAP-TTLS**, cioè al cuore di WPA2-Enterprise.

## Come funziona (l'handshake)

Lo scambio, semplificato, è questo. Il server manda una **Authenticator Challenge** di 16 byte. Il client genera una propria **Peer Challenge** di 16 byte e calcola un **Challenge Hash** = `SHA1(PeerChallenge || AuthChallenge || username)`, di cui prende i primi 8 byte. Poi calcola l'**hash NT** della password, `NThash = MD4(UTF-16LE(password))`, lungo 16 byte. Da qui deriva la **NT Response**, e il modo in cui la deriva è la sua rovina (sotto). Il client rimanda `Peer Challenge + NT Response + username`; il server, che conosce l'hash NT dal proprio database, rifà lo stesso conto e verifica. Infine il server calcola una **Authenticator Response** (sempre a partire dall'hash NT) e la rispedisce, così anche il client verifica il server: è la parte «mutua».

<svg width="100%" viewBox="0 0 860 1120" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Segoe UI, system-ui, sans-serif">
<rect x="0" y="0" width="860" height="1120" rx="16" fill="#1f2023"/>
<text x="30" y="40" text-anchor="start" font-size="18" fill="#e8eaed" font-weight="700">MS-CHAPv2 — handshake e costruzione della NT Response</text>
<line x1="250" y1="70" x2="250" y2="560" stroke="#4b5563" stroke-width="1" stroke-dasharray="4 5"/>
<line x1="610" y1="70" x2="610" y2="560" stroke="#4b5563" stroke-width="1" stroke-dasharray="4 5"/>
<text x="430" y="87" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">1. Avvio / Identity (username)</text>
<line x1="258" y1="95" x2="602" y2="95" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="602,95 596,91 596,99" fill="#9aa0a8"/>
<text x="430" y="120" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">2. Authenticator Challenge — 16 byte</text>
<line x1="602" y1="128" x2="258" y2="128" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="258,128 264,124 264,132" fill="#9aa0a8"/>
<rect x="55.0" y="148" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="167.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">3. Peer Challenge — 16 byte (generata dal client)</text>
<rect x="55.0" y="186" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="205.2" text-anchor="middle" font-size="12" fill="#f0e2b8" font-weight="400">4. Challenge Hash  C = SHA1(Peer + Auth + User) → 8 byte</text>
<rect x="55.0" y="224" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="243.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">5. NT hash = MD4(password) → 16 byte</text>
<rect x="55.0" y="262" width="430" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="270" y="281.025" text-anchor="middle" font-size="11.5" fill="#f0e2b8" font-weight="400">6. NT Response = DES(C,K1)+DES(C,K2)+DES(C,K3) → 24 byte</text>
<text x="430" y="312" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">7. Peer Challenge + NT Response + Username</text>
<line x1="258" y1="320" x2="602" y2="320" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="602,320 596,316 596,324" fill="#9aa0a8"/>
<rect x="420.0" y="344" width="380" height="30" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="610" y="363.375" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">8. Ricalcola col proprio hash NT e verifica</text>
<text x="430" y="397" text-anchor="middle" font-size="12.5" fill="#e8eaed" font-weight="400">9. Success + Authenticator Response</text>
<line x1="602" y1="405" x2="258" y2="405" stroke="#9aa0a8" stroke-width="1.4"/>
<polygon points="258,405 264,401 264,409" fill="#9aa0a8"/>
<rect x="25.0" y="428" width="460" height="38" rx="6" fill="#3a3115" stroke="#a98b3a" stroke-width="1.4" opacity="1"/>
<text x="255" y="444.0" text-anchor="middle" font-size="12.5" fill="#f0e2b8" font-weight="400">10. Il client verifica l'Authenticator Response</text>
<text x="255" y="460.0" text-anchor="middle" font-size="11" fill="#f0e2b8" font-weight="400">→ server autenticato (autenticazione MUTUA)</text>
<rect x="185.0" y="505" width="130" height="46" rx="6" fill="#232a4d" stroke="#3b4a7a" stroke-width="1.4" opacity="1"/>
<text x="250" y="533.25" text-anchor="middle" font-size="15" fill="#c7d2fe" font-weight="400">Client</text>
<rect x="545.0" y="505" width="130" height="46" rx="6" fill="#232a4d" stroke="#3b4a7a" stroke-width="1.4" opacity="1"/>
<text x="610" y="532.725" text-anchor="middle" font-size="13.5" fill="#c7d2fe" font-weight="400">Server (RADIUS)</text>
<line x1="200" y1="600" x2="660" y2="600" stroke="#4b5563" stroke-width="3"/>
<text x="30" y="646" text-anchor="start" font-size="15" fill="#9ca3af" font-weight="400">Dove il Response è il seguente:</text>
<rect x="180.0" y="672" width="180" height="46" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="270" y="692.0" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">Hash NT — 16 byte</text>
<text x="270" y="708.0" text-anchor="middle" font-size="11" fill="#c9f2e6" font-weight="400">fa da chiave</text>
<rect x="525.0" y="672" width="190" height="46" rx="6" fill="#5a4517" stroke="#c69a3a" stroke-width="1.4" opacity="1"/>
<text x="620" y="692.0" text-anchor="middle" font-size="12.5" fill="#f2e2b0" font-weight="400">Challenge Hash C — 8 byte</text>
<text x="620" y="708.0" text-anchor="middle" font-size="11" fill="#f2e2b0" font-weight="400">fa da testo in chiaro</text>
<rect x="200.0" y="738" width="140" height="36" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="270" y="760.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">Pad → 21 byte</text>
<rect x="145.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="210" y="826.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K1 — 7 byte</text>
<rect x="335.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="400" y="826.55" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K2 — 7 byte</text>
<rect x="525.0" y="800" width="130" height="44" rx="6" fill="#12564c" stroke="#2ea88f" stroke-width="1.4" opacity="1"/>
<text x="590" y="819.0" text-anchor="middle" font-size="13" fill="#c9f2e6" font-weight="400">K3 — 7 byte</text>
<text x="590" y="835.0" text-anchor="middle" font-size="11" fill="#c9f2e6" font-weight="400">2 byte reali + 5 zeri</text>
<rect x="145.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="210" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="210" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K1</text>
<rect x="335.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="400" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="400" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K2</text>
<rect x="525.0" y="876" width="130" height="44" rx="6" fill="#33383f" stroke="#6b7280" stroke-width="1.4" opacity="1"/>
<text x="590" y="895.0" text-anchor="middle" font-size="13" fill="#e5e7eb" font-weight="400">DES</text>
<text x="590" y="911.0" text-anchor="middle" font-size="11" fill="#e5e7eb" font-weight="400">cifra C con K3</text>
<rect x="190.0" y="952" width="420" height="46" rx="6" fill="#3f356e" stroke="#7c6bc4" stroke-width="1.4" opacity="1"/>
<text x="400" y="972.0" text-anchor="middle" font-size="13.5" fill="#e6ddff" font-weight="400">Response — 24 byte</text>
<text x="400" y="988.0" text-anchor="middle" font-size="11" fill="#e6ddff" font-weight="400">i tre output DES concatenati (3 × 8)</text>
<line x1="270" y1="718" x2="270" y2="738" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="270,738 266,732 274,732" fill="#2ea88f"/>
<line x1="270" y1="774" x2="210" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="210,800 206,794 214,794" fill="#2ea88f"/>
<line x1="270" y1="774" x2="400" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="400,800 396,794 404,794" fill="#2ea88f"/>
<line x1="270" y1="774" x2="590" y2="800" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="590,800 586,794 594,794" fill="#2ea88f"/>
<line x1="210" y1="844" x2="210" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="210,876 206,870 214,870" fill="#2ea88f"/>
<line x1="400" y1="844" x2="400" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="400,876 396,870 404,870" fill="#2ea88f"/>
<line x1="590" y1="844" x2="590" y2="876" stroke="#2ea88f" stroke-width="1.3"/>
<polygon points="590,876 586,870 594,870" fill="#2ea88f"/>
<line x1="620" y1="718" x2="620" y2="858" stroke="#c69a3a" stroke-width="1.3"/>
<line x1="210" y1="858" x2="620" y2="858" stroke="#c69a3a" stroke-width="1.3"/>
<line x1="210" y1="858" x2="210" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="210,876 206,870 214,870" fill="#c69a3a"/>
<line x1="400" y1="858" x2="400" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="400,876 396,870 404,870" fill="#c69a3a"/>
<line x1="590" y1="858" x2="590" y2="876" stroke="#c69a3a" stroke-width="1.3"/>
<polygon points="590,876 586,870 594,870" fill="#c69a3a"/>
<line x1="210" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<line x1="400" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<line x1="590" y1="920" x2="400" y2="952" stroke="#6b7280" stroke-width="1.3"/>
<polygon points="400,952 396,946 404,946" fill="#6b7280"/>
<rect x="185" y="1016" width="490" height="44" rx="8" fill="none" stroke="#7c6bc4" stroke-width="1.2" opacity="1"/>
<text x="430" y="1034" text-anchor="middle" font-size="12" fill="#cdbff5" font-weight="400">K3 ha solo 16 bit e i tre DES cifrano lo stesso C noto:</text>
<text x="430" y="1051" text-anchor="middle" font-size="12" fill="#cdbff5" font-weight="400">la sicurezza crolla a una singola chiave DES-56 → crack garantito.</text>
<rect x="250" y="1082" width="14" height="14" rx="3" fill="#12564c" stroke="#2ea88f" stroke-width="1.2" opacity="1"/>
<text x="272" y="1093" text-anchor="start" font-size="12" fill="#9ca3af" font-weight="400">chiave (dall'hash)</text>
<rect x="430" y="1082" width="14" height="14" rx="3" fill="#5a4517" stroke="#c69a3a" stroke-width="1.2" opacity="1"/>
<text x="452" y="1093" text-anchor="start" font-size="12" fill="#9ca3af" font-weight="400">testo in chiaro (la challenge)</text>
</svg>

> [!info] La NT Response
> Il cuore fragile. L'hash NT (16 byte) viene **riempito di zeri fino a 21 byte** e spezzato in **tre chiavi DES da 7 byte**; ciascuna cifra (DES) lo stesso **Challenge Hash** di 8 byte, producendo 24 byte di risposta. Due dettagli letali: le tre chiavi derivano tutte dall'*unico* hash NT, e il Challenge Hash è **noto** a chi ascolta (è SHA1 di valori tutti trasmessi in chiaro). L'attaccante ha quindi *testo in chiaro noto + testo cifrato* per tre operazioni DES imparentate.

## Perché è debole

| Peccato | Perché | Conseguenza |
|---|---|---|
| Hash NT senza sale | `NThash = MD4(password)`, deterministico | rainbow table precalcolate (~4 GB) |
| Riduzione a DES-56 | 3 chiavi DES dallo stesso hash, stesso plaintext noto | crack **garantito** dell'hash NT |
| Terza chiave DES | 2 byte reali + 5 di zeri (16 bit) | si forza in un istante (2¹⁶) |
| Username in chiaro | spedito nello scambio | bersaglio noto, alimenta il Challenge Hash |

Il difetto strutturale merita un affondo. La terza delle tre chiavi DES è fatta da soli 2 byte dell'hash NT più 5 byte di zeri: 16 bit di entropia, quindi si bruteforza all'istante e regala gli ultimi 2 byte dell'hash. Ma il colpo vero è un altro: siccome le tre operazioni DES cifrano lo *stesso* Challenge Hash noto usando materiale che è l'*unico* hash NT, l'intera sicurezza di MS-CHAPv2 si riduce alla fatica di crackare **una singola chiave DES a 56 bit** — ed è esattamente ciò che ha mostrato Moxie Marlinspike nel 2012 (chapcrack + CloudCracker su FPGA): recupero **garantito** in ~24 ore per ~200 $.

> [!danger] Sicurezza = DES-56
> Il punto da fissare per l'esame: questo attacco recupera l'**hash NT**, non la password — e ciò basta, perché con l'hash ci si autentica (pass-the-hash) o lo si cracca offline con calma. Soprattutto, colpisce la chiave DES derivata dall'hash, **non indovina la password**: per questo una password lunga e complessa **non salva** MS-CHAPv2. La sua robustezza è fissa a DES-56, qualunque sia la password.

## Dove morde

| Contesto | Protezione attorno a MS-CHAPv2 | Esito |
|---|---|---|
| PPTP (VPN) | nessuna | crackabile → Microsoft dice di abbandonarlo (2012) |
| LEAP (Wi-Fi) | nessuna, scambio sull'aria in chiaro | dizionario offline con **asleap** → evitare come WEP |
| PEAP / EAP-TTLS | **tunnel TLS** con certificato | sicuro *solo se* il client valida il certificato |

La differenza è tutta nell'involucro. In PPTP e LEAP MS-CHAPv2 gira scoperto, quindi chi cattura sfida e risposta lo attacca offline. In PEAP ed EAP-TTLS gira invece **dentro un tunnel TLS**: chi ascolta vede solo byte cifrati, e la debolezza di MS-CHAPv2 resta neutralizzata — a una condizione. Se il client è mal configurato e non valida il certificato del server RADIUS, un attaccante fa **AP impersonation / MITM** (hostapd + FreeRADIUS-WPE), diventa il terminatore del tunnel, e si ritrova di nuovo MS-CHAPv2 in chiaro da bruteforzare con asleap. Vedi la sezione WPA-Enterprise di [[ETHL - Cap 8 Wireless Hacking]].

## Contromisure

Mai usarlo **nudo**: niente PPTP, niente LEAP. Quando è l'autenticazione interna di PEAP/EAP-TTLS, l'unica cosa che lo protegge è il tunnel, quindi è **obbligatorio** validare il certificato del server RADIUS su *tutti* i client — meglio ancora fissando la CA attesa e il nome del server, non «un certificato qualsiasi». Dove possibile si preferisce **EAP-TLS**, che usa certificati su entrambi i lati e niente password. Microsoft, dopo il 2012, raccomanda **PEAP, L2TP/IPsec, IPSec+IKEv2 o SSTP** al posto di PPTP/MS-CHAP.

> [!summary] In una riga
> MS-CHAPv2 prova la password via hash NT senza trasmetterla, ma l'hash è senza sale e la struttura a tre DES riduce tutto a una chiave DES-56: crack garantito dell'hash a prescindere dalla password. Sopravvive solo dentro un tunnel TLS con certificato validato (PEAP/TTLS); scoperto (PPTP, LEAP) è da abbandonare.

> [!question] Domanda d'esame
> «Perché una password forte non mette al sicuro MS-CHAPv2?» → Perché l'attacco non indovina la password: recupera l'hash NT crackando una singola chiave DES-56 derivata dall'hash. L'hash è deterministico (niente sale) e la robustezza è fissa a 56 bit, indipendente dalla complessità della password.

> [!tip] Candidati Excalidraw
> Due schizzi «con un movimento»: l'**handshake** (Auth Challenge → Peer Challenge → Challenge Hash → NT Response con le 3 chiavi DES → Authenticator Response), e il **collasso a DES-56** (hash NT → 3 DES sullo stesso plaintext noto → si cracca come un'unica chiave). Grezzi, 3–4 minuti.
