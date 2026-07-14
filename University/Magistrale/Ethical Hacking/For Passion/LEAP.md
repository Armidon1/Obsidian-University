---
tags: [ethl, wireless, wifi, leap, eap, 802-1x, cisco, ms-chapv2, concetto]
tipo: concetto
data: 2026-07-13
collegamenti: ["[[ETHL - Cap 8 Wireless Hacking]]", "[[ETHL - MS-CHAPv2]]", "[[ETHL - LAN Manager (LM) vs NTLM]]"]
---

# ETHL — LEAP (Lightweight EAP)

> [!abstract] Il filo
> LEAP nasce per **rimediare a WEP** ma finisce «da evitare come WEP» — ed è proprio questa parabola il punto. È uno schema 802.1X/RADIUS proprietario Cisco che poggia interamente su **MS-CHAPv2**, ma lo manda sull'aria **nudo**, senza alcun tunnel. Così eredita tutte le debolezze di MS-CHAPv2 senza nulla dietro cui nascondersi: chi ascolta cattura sfida e risposta e fa un attacco a **dizionario offline**. La lezione da portare a casa: un'autenticazione interna debole è sicura solo se la **incapsuli** — PEAP ed EAP-TTLS lo fanno, LEAP no.

## Cos'è

LEAP (Lightweight Extensible Authentication Protocol) è un metodo **EAP proprietario di Cisco** del 2000, uno schema 802.1X che si appoggia a un server **RADIUS**. Fu creato apposta per tappare le falle di WEP: portava un'autenticazione utente vera (username + password) e, dopo il login, distribuiva **chiavi WEP dinamiche per sessione** invece dell'unica chiave statica condivisa — ed era il suo argomento di vendita. Ebbe grande diffusione all'inizio: il corso cita che nel 2004 il **46%** dei responsabili IT aziendali dichiarava di usarlo.

## Come funziona

Si muove nel framework 802.1X classico: **supplicant** (client) ↔ **authenticator** (l'AP, che fa da tramite) ↔ **server RADIUS**. LEAP usa **MS-CHAPv2** come meccanismo di sfida-risposta, in modo mutuo — il RADIUS sfida il client e il client sfida il server — per provare la conoscenza della password senza trasmetterla. Ad autenticazione riuscita, ricava le chiavi di cifratura di sessione.

## Perché è debole

Il peccato non è tanto MS-CHAPv2 in sé, quanto il fatto che LEAP lo espone **sull'aria in chiaro**, senza avvolgerlo in nessun tunnel. Il risultato è **zero resistenza al dizionario offline**: chi cattura la coppia sfida/risposta prova password su password in locale (calcola `NThash → risposta MS-CHAPv2 → confronto`), e le **rainbow table** precalcolate (~4 GB) rendono il tutto rapidissimo. Tutte le fragilità di MS-CHAPv2 — hash NT senza sale, riduzione a una chiave DES-56, username in chiaro — qui agiscono indisturbate; il meccanismo è in [[ETHL - MS-CHAPv2]].

> [!warning] Nessun tunnel
> È qui tutta la differenza con PEAP/EAP-TTLS. Quei protocolli usano *lo stesso* MS-CHAPv2 debole, ma lo fanno girare **dentro un tunnel TLS**, così chi ascolta vede solo byte cifrati. LEAP no: manda MS-CHAPv2 scoperto, e per questo è attaccabile offline mentre PEAP (se il certificato è validato) non lo è.

## La difesa di Cisco (e perché fallisce)

Cisco sosteneva che LEAP fosse sicuro **a patto** di usare password lunghe e casuali — almeno 10 caratteri con maiuscole, minuscole, numeri e simboli. Nella realtà quasi nessuna organizzazione rispetta requisiti così stringenti, quindi in pratica le password LEAP si crackano in **giorni o minuti**.

## L'attacco pratico: asleap

Lo strumento di riferimento è **asleap** (Joshua Wright): estrae e cracca le password LEAP deboli da access point e schede Cisco. È integrato con **Air-Jack** per buttare giù gli utenti già autenticati con un deauth: alla **riautenticazione forzata**, la nuova sfida/risposta viene risniffata e crackata. È la variante attiva — non aspetti che qualcuno si colleghi, lo costringi tu.

## Verdetto e migrazione

Evitarlo **come WEP**. Il percorso di uscita: **EAP-FAST** (il successore Cisco, che incapsula proprio l'inner auth in un tunnel via PAC), o meglio **PEAP / EAP-TTLS** (tunnel TLS), o **EAP-TLS** (certificati su entrambi i lati, niente password da crackare).

| Metodo EAP | Auth interna | Protezione | Attaccabile offline? |
|---|---|---|---|
| **LEAP** | MS-CHAPv2 | nessuna (in chiaro sull'aria) | sì — dizionario con asleap |
| PEAP / EAP-TTLS | MS-CHAPv2 ecc. | tunnel TLS | no, se il certificato è validato |
| EAP-FAST | MS-CHAPv2 | tunnel (PAC) | no, con provisioning sicuro |
| EAP-TLS | certificati | mutua a certificati | no (niente password) |

> [!summary] In una riga
> LEAP è 802.1X/RADIUS Cisco basato su MS-CHAPv2 mandato **nudo** sull'aria: eredita ogni debolezza di MS-CHAPv2 senza tunnel a proteggerlo, quindi crackabile offline con asleap (forzabile via deauth). Nato per rimediare a WEP, è finito nella stessa lista nera. Migrare a PEAP/EAP-TTLS o EAP-TLS.

> [!question] Domanda d'esame
> «Se PEAP usa lo stesso MS-CHAPv2, perché LEAP è insicuro e PEAP no?» → Perché LEAP espone MS-CHAPv2 in chiaro sull'aria, mentre PEAP lo avvolge in un tunnel TLS. Stessa autenticazione interna debole: cambia solo che una la nasconde e l'altra no — e la protezione di PEAP regge finché il client valida il certificato del server.

> [!tip] Candidati Excalidraw
> Uno schizzo utile: il triangolo 802.1X (supplicant → AP → RADIUS) con l'attaccante che sniffa la sfida/risposta MS-CHAPv2 *in chiaro*, affiancato dallo stesso schema con PEAP dove lo stesso scambio è chiuso in un tunnel TLS. Rende visivo il «nudo vs incapsulato». Grezzo, 3–4 minuti.
