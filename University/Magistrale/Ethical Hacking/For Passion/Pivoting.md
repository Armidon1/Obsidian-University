Il **pivoting** è la tecnica con cui un attaccante usa una macchina già compromessa come **trampolino** per raggiungere reti o host che altrimenti sarebbero irraggiungibili.

L'idea di base: tu (attaccante) puoi parlare solo con la macchina A (esposta su Internet). Dietro A c'è una rete interna con la macchina B, raggiungibile solo da A. Il pivoting fa sì che il tuo traffico verso B **passi attraverso A** come se A fosse il tuo router.

```
Attaccante ──→ Macchina A (compromessa) ──→ Macchina B (rete interna)
               [pivot point]
```

In Meterpreter il meccanismo tipico è `portfwd` (mappa una porta locale dell'attaccante su una porta di B passando per A) o `autoroute` (aggiunge una rotta nel routing di Metasploit affinché tutto il traffico verso la subnet interna passi automaticamente per la sessione attiva).

Il motivo per cui è potente: la macchina B non vede mai l'IP dell'attaccante — vede solo le connessioni in arrivo da A, che è una macchina legittima sulla sua rete. Quindi i firewall perimetrali e i sistemi di rilevamento orientati verso l'esterno sono ciechi rispetto a questo movimento.

Dal punto di vista difensivo si contrasta con **segmentazione di rete** (zero-trust tra segmenti, non bastano firewall solo sul perimetro esterno) e con il monitoraggio del traffico **est-ovest** (laterale) dentro la rete, che è molto più difficile da fare rispetto al monitoraggio nord-sud (in/out da Internet).

Per l'esame: se ti chiedono Meterpreter e dici "pivoting", aggancialo sempre alla narrativa — _avere una shell su A non significa avere accesso alla rete interna; il pivoting è il passo che allarga il raggio d'azione senza mai esporre direttamente l'attaccante verso i target interni._