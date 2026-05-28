# Server Extensions

> [!abstract] In una riga Moduli che ampliano il server e **girano con i suoi privilegi**: un loro bug è gravissimo.

## Cos'è

Il server web di base fa poco; le funzioni avanzate arrivano da **estensioni / moduli** caricati nel suo processo. Esempi:

- **ISAPI extensions** (IIS)
- **moduli** Apache (`mod_*`)
- **WebDAV** (editing remoto di file via HTTP)
- **FrontPage Server Extensions**
- **librerie SSL/TLS**

Poiché girano **dentro il processo del server**, un difetto in un'estensione = compromissione dell'intero server, spesso con esecuzione di codice.

## Esempi storici

- **ISAPI `.printer`** (IIS): buffer overflow → esecuzione di codice remoto.
- **ISAPI `.ida` / `.idq`** (Indexing Service): l'overflow sfruttato dal worm **Code Red**.
- **WebDAV `ntdll.dll`** (IIS): overflow via richieste WebDAV malformate.
- **OpenSSL** (Apache): la falla sfruttata dal worm **Slapper**.

## Difese

- **Disabilitare** tutte le estensioni/moduli **non utilizzati** (riduce la superficie d'attacco).
- **Patch** immediate: sono componenti molto bersagliati.
- Eseguire il server con **minimo privilegio**.

## Collegamenti

- ⬆️ [[Web Server Hacking]]
- ↔️ [[Input Validation]] (gli overflow nascono da input non validato) · [[Denial of Service]]