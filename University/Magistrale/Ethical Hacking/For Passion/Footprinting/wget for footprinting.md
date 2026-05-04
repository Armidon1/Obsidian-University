# Wget

## Cos'è

`wget` è un tool da riga di comando per **scaricare file e pagine web** da internet. Supporta HTTP, HTTPS e FTP. Non richiede un browser — funziona in modo completamente non interattivo, utile per automazione e scripting.

---

## Utilizzo base

```bash
wget https://example.com/file.pdf        # Scarica un singolo file
wget https://example.com                 # Scarica la pagina principale
```

---

## Mirroring completo di un sito

```bash
wget --mirror --convert-links --page-requisites --no-parent https://target.com
```

Questo comando scarica una **copia locale completa e navigabile** del sito. Ecco cosa fa ogni flag:

### `--mirror`

Scorciatoia che attiva tre opzioni insieme:

- Ricorsione infinita (segue tutti i link interni)
- Salvataggio dei timestamp originali
- Nessun limite di profondità

Senza questo flag wget scaricherebbe solo la pagina principale.

### `--convert-links`

Dopo il download converte tutti i link interni da assoluti (`https://target.com/about`) a relativi (`./about`), così puoi navigare il sito salvato **offline dal browser** come se fosse live.

### `--page-requisites`

Scarica tutto il necessario per visualizzare ogni pagina correttamente:

- Immagini
- CSS
- JavaScript
- Font

Senza questo avresti solo l'HTML nudo senza stili né immagini.

### `--no-parent`

Impedisce a wget di risalire sopra la directory specificata. Se stai mirrorando `target.com/blog/` non andrà a scaricare anche `target.com/shop/` o la root. Ti mantiene focalizzato sul target esatto.

---

## Altri flag utili

|Flag|Funzione|
|---|---|
|`-r`|Ricorsione (meno completo di `--mirror`)|
|`-l [N]`|Limita la profondità di ricorsione a N livelli|
|`-q`|Modalità silenziosa, nessun output|
|`-o log.txt`|Salva l'output in un file di log|
|`--user-agent="..."`|Cambia lo user agent (simula un browser)|
|`--wait=1`|Aspetta 1 secondo tra una richiesta e l'altra|
|`--random-wait`|Aggiunge un'attesa casuale tra le richieste|
|`-e robots=off`|Ignora il file robots.txt|
|`--reject "*.jpg,*.png"`|Esclude certi tipi di file dal download|

---

## Nel footprinting

Il mirroring completo è utile per:

### 1. Cercare commenti HTML nascosti

Gli sviluppatori spesso lasciano commenti con informazioni sensibili:

```bash
grep -ri '<!--' ./target.com/
```

Cosa cercare:

- Path interni (`<!-- /admin/config -->`)
- Versioni software (`<!-- v2.3.1 -->`)
- Note dei developer (`<!-- TODO: rimuovere prima del deploy -->`)
- Credenziali dimenticate

### 2. Cercare informazioni di contatto

```bash
grep -ri "email\|telefono\|p.iva\|partita" ./target.com/
```

### 3. Analizzare la struttura del sito

```bash
find ./target.com -type f | sort
```

### 4. Cercare file sensibili scaricati

```bash
find ./target.com -name "*.php" -o -name "*.bak" -o -name "*.txt"
```

---

## Useless Use of Cat

Un errore comune è usare `cat` + `grep` invece di passare il file direttamente a grep:

```bash
# Sbagliato (ridondante)
cat index.html | grep 'pattern'

# Corretto
grep 'pattern' index.html

# Per cercare in tutti i file ricorsivamente
grep -ri 'pattern' ./target.com/
```

---

## Attenzione con zsh

In zsh le virgolette doppie espandono caratteri speciali come `!`. Usare sempre **virgolette singole** nei pattern grep:

```bash
grep '<!--' index.html      # ✅ Corretto
grep "<!--" index.html      # ❌ Errore in zsh (! è speciale)
```

---

## Related Notes

- [[DirBuster]]
- [[Privoxy]]
- [[OSINT & Footprinting]]
- [[HTML Comments — Information Disclosure]]

---

_References: man wget · Linux Basics for Hacking — OccupyTheWeb · https://www.gnu.org/software/wget/manual/_