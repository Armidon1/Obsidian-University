# Web Hacking Tools

> [!abstract] In una riga **Burp Suite è l'hub.** Tieni uno strumento standalone solo se fa _una cosa specializzata_ meglio di Burp. Tutto il resto della lista di HE7 è storia.

## Il cambio di paradigma

HE7 (2012) elenca tanti **browser plugin** e tool separati, uno per funzione. Quel mondo è finito: i plugin Firefox in tecnologia XUL sono stati spazzati via da **Firefox 57 "Quantum" (nov 2017)**, che è passato alle WebExtensions. Da allora il flusso di lavoro ruota attorno a un unico **intercepting proxy** (Burp/ZAP) che racchiude tutte quelle funzioni più gli scanner.

> [!tip] La regola di decisione Parti da **Burp**. Aggiungi un tool standalone **solo** se copre qualcosa che Burp non fa (o fa peggio): es. _sfruttare_ la SQLi, ricognizione di rete, brute forcing.

## Tabella di riferimento

| Strumento                                  | Cosa fa di unico                                                                                                        | Stato                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **[[Burp Suite]]**                         | Intercepting proxy = hub di tutto (Proxy, Repeater, Intruder, Scanner). "Il toolkit di web pentest #1"                  | ✅ Standard                                |
| **OWASP ZAP**                              | Come Burp ma 100% gratis e open source. Consigliato da Mozilla come rimpiazzo dei vecchi plugin                         | ✅ Standard (free)                         |
| **sqlmap**                                 | _Sfrutta_ la [[SQL Injection]]: fingerprint del DB, dump tabelle, comandi sul server. Burp la trova, sqlmap la spreme   | ✅ Standard                                |
| **Nikto**                                  | Scan rapido del **web server** (file d'esempio, config, versioni note) → lega a [[Sample Files]], [[Server Extensions]] | ✅ In uso                                  |
| **nmap**                                   | Ricognizione porte/servizi, **lato server**, a monte di tutto                                                           | ✅ Standard                                |
| **THC-Hydra**                              | Brute forcing di credenziali su login e servizi di rete                                                                 | ✅ In uso                                  |
| **curl / wget**                            | Richieste HTTP manuali; scaricare/clonare il sito                                                                       | ✅ Sempre utili                            |
| **WebInspect · AppScan · Acunetix**        | DAST commerciali enterprise (a pagamento)                                                                               | 💰 Esistono, **non servono per studiare** |
| **TamperData · Firebug · LiveHTTPHeaders** | Vecchi plugin Firefox (intercettare, ispezionare cookie/header)                                                         | ❌ Morti con Firefox 57                    |
| **Paros · WebScarab**                      | Vecchi proxy intercettanti                                                                                              | ❌ Morti → oggi ZAP/Burp                   |
| **Brutus · Teleport Pro · Black Widow**    | Brute forcer / "site ripper" datati                                                                                     | ❌ Storici                                 |

## Come leggerla

- ✅ **Da saper usare:** Burp (+ ZAP come alternativa free) come centro, **sqlmap** come secondo pilastro, poi Nikto / nmap / Hydra / curl come strumenti specializzati.
- 💰 **Da saper nominare:** gli scanner commerciali (categoria DAST), giusto per riconoscerli.
- ❌ **Da archiviare come storia:** browser plugin e vecchi proxy. Capisci _cosa facevano_ (intercettare e manomettere richieste), non come si installano.

> [!note] Nota concettuale **Firebug** non è semplicemente sparito: è stato assorbito nei **DevTools integrati** del browser (tasto F12). Per l'ispezione veloce al volo i DevTools bastano; per il pentest vero si usa il proxy.

## Collegamenti

- ⬆️ [[Web Application Hacking]] · [[Web Server Hacking]]
- ↔️ [[SQL Injection]] · [[Sample Files]] · [[Server Extensions]]