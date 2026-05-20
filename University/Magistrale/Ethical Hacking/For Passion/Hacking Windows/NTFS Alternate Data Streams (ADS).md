# NTFS Alternate Data Streams (ADS)

## Cos'è un file in NTFS, davvero

Il modello mentale "file = nome + blob di byte" funziona su FAT32 e ext4, ma su NTFS è sbagliato.

In NTFS ogni file è un **record nella Master File Table (MFT)** — una struttura dati che contiene una lista di **attributi tipizzati**. Non è "un nome e dei dati": è un dizionario dove ogni voce ha un tipo, un nome opzionale, e un payload.

![[Pasted image 20260517190849.png]]

Un record MFT tipico per `secret.txt` contiene:

| Tipo                    | Codice | Nome         | Contenuto                           |
| ----------------------- | ------ | ------------ | ----------------------------------- |
| `$STANDARD_INFORMATION` | 0x10   | —            | timestamps, flags, owner SID        |
| `$FILE_NAME`            | 0x30   | —            | "secret.txt", parent dir, namespace |
| `$DATA`                 | 0x80   | `""` (vuoto) | il contenuto "normale" del file     |
| `$DATA`                 | 0x80   | `"hidden"`   | ← **alternate data stream**         |

La chiave è che **`$DATA` può esistere più volte nello stesso record**, differenziato solo dal campo **name**. Il sistema operativo sa quale stream restituire in base al nome richiesto nel path.

> [!info] Resident vs non-resident Se il contenuto di uno stream è piccolo (< ~700 byte per record da 1KB), viene salvato **direttamente dentro il record MFT** (resident). Se è grande, il record contiene solo una "run list" — una lista di cluster su disco dove i dati si trovano. Un file può avere stream resident e non-resident allo stesso tempo.

---

## Come funzionano gli ADS

La sintassi per accedere a uno stream alternativo è:

```
nomefile.ext:nomestream
```

### Creare uno stream

```cmd
echo payload nascosto > secret.txt:hidden
```

Questo scrive "payload nascosto" dentro l'attributo `$DATA` con name `"hidden"` del file `secret.txt`. Il file `secret.txt` esiste già (o viene creato vuoto se non esiste). La dimensione mostrata da `dir` rimane quella dello stream di default.

### Leggere uno stream

```cmd
more < secret.txt:hidden
notepad secret.txt:hidden
type secret.txt:hidden
```

Devi conoscere il nome dello stream — non c'è modo di "scoprire" gli stream con i tool normali.

### Nascondere un eseguibile

```cmd
type mimikatz.exe > legit_document.txt:tool.exe
```

L'exe è ora nascosto dentro un file di testo. Su Windows XP/2003 era possibile eseguirlo direttamente:

```cmd
start legit_document.txt:tool.exe
```

Su sistemi moderni questa esecuzione diretta è bloccata, ma si può ancora copiare lo stream in un path normale e poi eseguirlo.

### Nascondere uno script

```cmd
echo WScript.Shell.Run "cmd /c whoami > C:\out.txt" > legit.txt:payload.vbs
wscript legit.txt:payload.vbs
```

---

## Cosa vede dir vs cosa c'è davvero

```
$ dir secret.txt
secret.txt        24 bytes    ← solo lo stream di default

$ dir /r secret.txt
secret.txt        24 bytes
secret.txt:hidden 20 bytes    ← ADS finalmente visibile
```

L'opzione `/r` di `dir` mostra gli stream alternativi. È uno degli unici tool nativi Windows che li espone.

---

## Detection

### Tool nativi

```cmd
dir /r C:\path\cartella\
```

### PowerShell

```powershell
Get-Item -Path C:\secret.txt -Stream *
Get-ChildItem -Recurse | Get-Item -Stream * | Where-Object Stream -ne ':$DATA'
```

### Sysinternals Streams

```cmd
streams.exe -r C:\path\
```

Utile per scansioni ricorsive — `dir /r` su cartelle grandi è scomodo.

---

## Limitazioni importanti

> [!warning] ADS è NTFS-only Gli stream alternativi sono una feature **esclusiva di NTFS**. Copiare un file con ADS su:
> 
> - FAT32 / exFAT (chiavette USB) → stream **persi silenziosamente**, nessun errore
> - SMB share (dipende dal filesystem del server)
> - Linux ext4 → stream persi
> 
> Windows mostra un warning solo in alcuni casi. Questo è sia un vettore di detection (monitorare copie da NTFS a FAT rivela possibile exfiltration) sia un rischio operativo per l'attaccante (perde il payload copiandolo nel posto sbagliato).

> [!info] Mark of the Web — un ADS che già conosci Quando scarichi un file da internet, Windows scrive automaticamente un ADS:
> 
> ```
> nomefile.exe:Zone.Identifier
> [ZoneTransfer]
> ZoneId=3
> ```
> 
> Questo è il motivo per cui Windows ti avvisa "questo file proviene da internet". Il pulsante "Sblocca" nelle proprietà del file elimina questo stream. Gli attaccanti a volte cercano l'assenza di `Zone.Identifier` come prova che un file non è stato scaricato ma è stato creato localmente — utile in analisi forense.

---

## Contesto storico (HE7)

> [!warning] Tool del libro obsoleti HE7 fa riferimento a tool come **Winzapper** per la manipolazione selettiva dei log, e discute ADS nel contesto di evasione della detection. Su Windows XP/2003 il formato dei file era più semplice e tool come `lads.exe` (List Alternate Data Streams) erano necessari per la detection.
> 
> Su sistemi moderni:
> 
> - `dir /r` e PowerShell gestiscono la detection nativamente
> - L'esecuzione diretta da ADS (`start file:stream.exe`) è bloccata
> - Molti AV scansionano gli stream alternativi come parte della scansione on-access
> - Windows SmartApp Control può bloccare eseguibili estratti da ADS

---

## Paragone con Linux ext4

> [!analogy] Linux parallel In **ext4**, un inode ha un singolo puntatore ai blocchi dati — non esiste il concetto di stream alternativo nativo. Le opzioni più vicine sono:
> 
> |Concetto|Linux|NTFS|
> |---|---|---|
> |Metadati extra piccoli|`xattr` (extended attributes)|`$DATA` named stream|
> |Contenuto alternativo|file separato|ADS|
> |Fork di risorsa|non supportato nativamente|`$DATA:"stream"`|
> 
> `xattr` su Linux è concettualmente simile — aggiungi metadati a un inode — ma è pensato per piccoli dati strutturati (etichette SELinux, capabilities POSIX), non per payload arbitrari di dimensioni arbitrarie.
> 
> **macOS** ha le **resource fork** (`:rsrc` in HFS+/APFS) — questo è l'antecedente storico da cui Microsoft ha preso ispirazione per gli ADS in NTFS.

---

## Perché conta in un pentest

|Uso offensivo|Difficoltà detection|Note|
|---|---|---|
|Nascondere tool (mimikatz, nc)|Media|`dir /r` e Sysinternals li trovano|
|Hiding di script VBS/PS1|Media|AV moderni scansionano anche gli ADS|
|Exfiltration staging|Media|Persi se copiati su FAT|
|Persistenza (wscript da ADS)|Alta se combinato con altri trick|Meno comune oggi|
|Zone.Identifier removal|Bassa|Tecnica difensiva contro forensics|

Il valore reale degli ADS oggi non è tanto nascondere i file dal difensore umano (che con i giusti tool li trova subito), ma **bypassare tool legacy e script di monitoring che non controllano gli stream** — ancora presenti in molti ambienti enterprise.

---

## Takeaways

1. **Un file NTFS non è un blob di byte** — è un record MFT con una lista di attributi tipizzati. `$DATA` può avere più istanze, differenziate dal nome. Questo è il meccanismo che permette gli ADS.
    
2. **ADS sono invisibili a dir e Esplora File** — ma `dir /r`, PowerShell `Get-Item -Stream *`, e Sysinternals `streams.exe` li vedono tutti.
    
3. **Sono NTFS-only** — qualsiasi copia su FAT li cancella silenziosamente. Pericoloso per l'attaccante, utile per il difensore.
    
4. **Zone.Identifier** è un ADS che usi ogni giorno senza saperlo — la "mark of the web" di Windows.
    
5. **Su Windows moderno, l'esecuzione diretta da ADS è bloccata** — il vettore del libro (HE7 era) non funziona più out of the box.
    

---

## Wiki-links

- [[port_redirection_fpipe]] — altro capitolo HE7, evasione firewall
- [[lab_session_3_lsass_dump_windows11_defenses]] — anti-forensics in NTFS collegato al tema
- [[credential_dumping_lsa_vs_lsass]] — LSA Secrets, altro meccanismo di hiding di dati sensibili in Windows

