# SOAP — Simple Object Access Protocol

**Categoria:** #protocollo #web #networking  
**Formato messaggi:** XML  
**Trasporto:** HTTP, HTTPS, SMTP

---

## 📖 Cos'è

SOAP è un protocollo di comunicazione basato su **XML** per scambiare informazioni strutturate tra applicazioni in rete. È uno standard W3C nato in ambito enterprise/Microsoft, oggi considerato legacy rispetto alle API REST moderne.

---

## 🏗️ Struttura di un messaggio SOAP

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Header>
        <!-- metadati opzionali: autenticazione, routing, ecc. -->
    </soap:Header>
    <soap:Body>
        <!-- il messaggio vero e proprio -->
        <GetUser>
            <UserID>123</UserID>
        </GetUser>
    </soap:Body>
</soap:Envelope>
```

Ogni messaggio ha tre parti:

- **Envelope** → contenitore obbligatorio, definisce il namespace
- **Header** → opzionale, contiene metadati
- **Body** → obbligatorio, contiene il payload del messaggio

---

## 🔄 Come funziona

```
Client                          Server
  |                               |
  |-- HTTP POST (body = XML) ---> |
  |   <Envelope>                  |
  |     <Body>                    |
  |       <comando/>              |
  |     </Body>                   |
  |   </Envelope>                 |
  |                               |
  |                    elabora il comando
  |                               |
  | <-- HTTP 200 (body = XML) --- |
  |   <Envelope>                  |
  |     <Body>                    |
  |       <risposta/>             |
  |     </Body>                   |
  |   </Envelope>                 |
```

---

## 🔐 Rilevanza per la sicurezza

### WinRM usa SOAP

WinRM trasporta i comandi PowerShell dentro messaggi SOAP over HTTP — per questo nmap vede HTTP sulla porta 5985 invece di un protocollo proprietario.

```
Evil-WinRM → SOAP/XML → HTTP:5985 → Windows esegue il comando
```

### SOAP Injection

Come la SQL Injection ma per SOAP — se l'input utente viene inserito direttamente in un messaggio XML senza sanitizzazione:

```xml
<!-- Input attaccante: </UserID><admin>true</admin><UserID> -->
<GetUser>
    <UserID></UserID><admin>true</admin><UserID></UserID>
</GetUser>
```

### XXE (XML External Entity)

SOAP usa XML → vulnerabile a XXE se il parser non è configurato correttamente:

```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<soap:Body>
    <Input>&xxe;</Input>
</soap:Body>
```

---

## 📊 SOAP vs REST

||SOAP|REST|
|---|---|---|
|Formato|XML|JSON / XML / altro|
|Protocollo|HTTP, SMTP, altri|HTTP only|
|Complessità|Alta|Bassa|
|Stato|Stateful|Stateless|
|Sicurezza|WS-Security integrata|Dipende dall'implementazione|
|Uso tipico|Enterprise, Microsoft, banking|Web API moderne|

---

## 📚 Lezioni apprese

- SOAP è la ragione per cui WinRM appare come HTTP in nmap
- È un protocollo legacy ma ancora molto presente in ambienti enterprise e Microsoft
- Basato su XML → soggetto a vulnerabilità XML come XXE e SOAP Injection
- Oggi quasi tutte le nuove API usano REST/JSON invece di SOAP

---

## 🔗 Riferimenti

- [[WinRM]] — usa SOAP over HTTP
- [W3C SOAP Specification](https://www.w3.org/TR/soap/)
- [HackTricks - XXE](https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity)

---

## Tags

#soap #xml #protocollo #web #winrm #xxe #enterprise #microsoft