# Exiftool — Metadata Extractor

#linux #cybersecurity #osint #metadata #linux-basics-for-hackers

---

## 🗂️ Overview

**ExifTool** è uno strumento open-source per leggere, scrivere e modificare i **metadati** incorporati nei file. Creato da Phil Harvey, è lo standard de facto per l'analisi dei metadati in ambito forense e OSINT.

I metadati sono **informazioni nascoste dentro i file** — invisibili aprendo normalmente il file, ma leggibili con exiftool. Possono rivelare chi ha creato il file, quando, dove, con quale dispositivo e con quale software.

```
File visibile:   una foto di una vacanza
Metadati:        GPS 41.9028°N 12.4964°E → Roma, Via del Corso
                 Camera: iPhone 14 Pro
                 Data: 2026-03-15 14:23:11
                 Autore: Mario Rossi
```

---

## 🛠️ Installazione

```bash
# Debian/Ubuntu/Kali/Parrot
sudo apt install exiftool -y

# Verifica
exiftool -ver
```

---

## 📋 Sintassi Base

```bash
exiftool file                    # tutti i metadati
exiftool -TAG file               # metadato specifico
exiftool -TAG1 -TAG2 file        # più metadati
exiftool directory/              # analizza intera directory
exiftool -r directory/           # ricorsivo nelle sottodirectory
exiftool -ext jpg directory/     # solo file .jpg
```

---

## 📸 Foto — Il Caso Più Ricco

Le foto scattate da smartphone sono la fonte più ricca di metadati:

```bash
exiftool foto.jpg
```

```
GPS Latitude          : 41.9028° N
GPS Longitude         : 12.4964° E
GPS Altitude          : 120 m
Camera Model Name     : iPhone 14 Pro
Lens ID               : 6.86mm f/1.78
Date/Time Original    : 2026:03:15 14:23:11
Software              : 16.3.1
F Number              : 1.8
ISO                   : 400
Flash                 : Off, Did not fire
```

### Estrarre solo GPS

```bash
exiftool -GPSLatitude -GPSLongitude -GPSAltitude foto.jpg

# Formato decimale diretto (più utile)
exiftool -GPSLatitude# -GPSLongitude# foto.jpg

# Converti in link Google Maps
exiftool -p '$GPSLatitude, $GPSLongitude' foto.jpg
# → 41.9028, 12.4964
# Incolli su maps.google.com → posizione esatta
```

### Estrarre data e ora

```bash
exiftool -DateTimeOriginal foto.jpg
exiftool -CreateDate foto.jpg
exiftool -ModifyDate foto.jpg
```

---

## 📄 Documenti — Nome Reale e Azienda

I documenti Office e PDF sono miniere di informazioni aziendali:

```bash
exiftool documento.docx
exiftool documento.pdf
exiftool presentazione.pptx
exiftool foglio.xlsx
```

```
Author            : Mario Rossi           ← nome reale
Last Modified By  : m.rossi               ← username interno
Company           : Studio Legale Nolèx   ← azienda
Creator           : Microsoft Word 2019   ← software e versione
Create Date       : 2024:01:15 09:30:00
Modify Date       : 2024:03:20 16:45:22
Template          : Normal.dotm           ← template aziendale
```

> [!tip] Hacking Note `Author` e `Last Modified By` nei documenti rivelano spesso lo **username di dominio** usato internamente — direttamente utilizzabile per attacchi su VPN, Active Directory, o email aziendale.

---

## 🎨 File Creativi — Software e Identità

```bash
exiftool artwork.psd
exiftool design.ai
exiftool document.indd
```

```
Creator Tool      : Adobe Photoshop 2024
Author            : Armidon22_RealName
Rights            : © 2024 Mario Rossi
Create Date       : 2024:06:10 18:22:05
Color Mode        : RGB
```

---

## 🎬 Video e Audio

```bash
exiftool video.mp4
exiftool audio.mp3
```

```
# Video
GPS Coordinates   : 41.9028° N, 12.4964° E
Camera Model      : GoPro Hero 11
Duration          : 0:02:34
Create Date       : 2026:02:20 10:15:30

# Audio (MP3)
Artist            : Mario Rossi
Album             : Demo 2024
Comment           : Recorded at Studio Roma
Encoded By        : Audacity 3.4
```

---

## 🔍 Ricerche Specifiche — Grep Integration

```bash
# Solo GPS
exiftool foto.jpg | grep -i "GPS"

# Solo informazioni autore
exiftool file.pdf | grep -iE "Author|Creator|Company|Producer"

# Solo date
exiftool file.jpg | grep -i "Date"

# Solo info dispositivo
exiftool foto.jpg | grep -iE "Camera|Model|Software|Make"

# Su directory intera — trova tutti i file con GPS
exiftool -r -if '$GPSLatitude' -filename -GPSLatitude -GPSLongitude ./
```

---

## 📁 Analisi in Bulk — Directory Intere

```bash
# Tutti i metadati di tutti i file JPG in una cartella
exiftool -r /path/to/photos/

# Esporta in CSV per analisi
exiftool -csv -r /path/to/photos/ > metadati.csv

# Solo campi specifici su tutti i file
exiftool -r -Author -Company -CreateDate /path/to/documents/

# Trova tutti i file con GPS in una directory
exiftool -r -if '$GPSLatitude' /path/to/photos/

# Estrai coordinate di tutte le foto
exiftool -r -GPSLatitude# -GPSLongitude# -FileName /path/
```

---

## ✏️ Modificare e Rimuovere Metadati

Exiftool può anche **scrivere** e **cancellare** metadati — utile per proteggere la propria privacy prima di pubblicare file.

```bash
# Rimuovi TUTTI i metadati da un file
exiftool -all= foto.jpg

# Rimuovi solo il GPS
exiftool -GPSLatitude= -GPSLongitude= -GPSAltitude= foto.jpg

# Rimuovi metadati da tutti i JPG in una cartella
exiftool -all= *.jpg

# Modifica l'autore
exiftool -Author="Anonimo" documento.pdf

# Modifica la data
exiftool -DateTimeOriginal="2024:01:01 00:00:00" foto.jpg

# Copia metadati da un file a un altro
exiftool -TagsFromFile source.jpg destination.jpg
```

> [!warning] Per default exiftool crea un backup del file originale con estensione `_original`. Per sovrascrivere senza backup:
> 
> ```bash
> exiftool -overwrite_original -all= foto.jpg
> ```

---

## 🕵️ Workflow OSINT con Exiftool

### Caso 1 — Immagine da profilo social/artistico

```bash
# 1. Scarica l'immagine
wget "https://url-immagine.jpg" -O target.jpg

# 2. Analisi completa
exiftool target.jpg

# 3. Cerca GPS
exiftool target.jpg | grep -i GPS

# 4. Se GPS trovato → converti in link Maps
exiftool -GPSLatitude# -GPSLongitude# target.jpg
# → apri su maps.google.com
```

### Caso 2 — Documento PDF aziendale

```bash
# 1. Scarica il PDF dal sito aziendale
wget "https://azienda.com/documento.pdf" -O doc.pdf

# 2. Estrai info aziendali
exiftool doc.pdf | grep -iE "Author|Creator|Company|Producer|Modified"

# Output tipico:
# Author      : mario.rossi          ← username AD
# Company     : Azienda Target SRL
# Producer    : Microsoft Word 2019  ← versione software interna
```

### Caso 3 — Analisi massiva di un sito

```bash
# Scarica tutti i PDF di un sito
wget -r -A.pdf https://target.com/

# Analizza tutti insieme
exiftool -csv -r target.com/ > tutti_metadati.csv

# Cerca autori unici
cat tutti_metadati.csv | cut -d',' -f5 | sort -u
# → lista di tutti gli username/nomi interni trovati
```

---

## 🛡️ Difendersi — Rimuovere Metadati Prima di Pubblicare

```bash
# Foto da pubblicare online
exiftool -overwrite_original -all= foto_da_pubblicare.jpg

# Documento da inviare a clienti
exiftool -overwrite_original -all= documento.pdf

# Batch — tutte le foto in una cartella
exiftool -overwrite_original -all= /path/to/photos/*.jpg

# Verifica che siano stati rimossi
exiftool foto_da_pubblicare.jpg | grep -iE "GPS|Author|Camera"
# → nessun output = metadati rimossi ✅
```

> [!tip] Social network come Instagram, Facebook e Twitter rimuovono automaticamente i metadati EXIF al momento dell'upload. **ArtStation, Imgur, e molti forum NON lo fanno** — le immagini vengono pubblicate con tutti i metadati originali.

---

## 📊 Formati Supportati

|Categoria|Formati|
|---|---|
|**Immagini**|JPG, PNG, TIFF, RAW, HEIC, WebP, GIF|
|**Video**|MP4, MOV, AVI, MKV, 3GP|
|**Audio**|MP3, FLAC, WAV, AAC, OGG|
|**Documenti**|PDF, DOCX, XLSX, PPTX, ODT|
|**Creativi**|PSD, AI, INDD, EPS, SVG|
|**Archivi**|ZIP (metadati limitati)|

---

## ⚖️ Exiftool vs Altri Tool

||ExifTool|Strings|Binwalk|
|---|---|---|---|
|**Metadati strutturati**|⭐⭐⭐⭐⭐|❌|❌|
|**GPS**|✅|❌|❌|
|**Scrittura metadati**|✅|❌|❌|
|**Formati supportati**|100+|Tutti (testo grezzo)|Binari/firmware|
|**Output leggibile**|✅|Grezzo|Strutturato|
|**Uso OSINT**|⭐⭐⭐⭐⭐|⭐⭐|⭐|

---

## 🔗 Command Cheat Sheet

```bash
# Lettura
exiftool file                              # tutti i metadati
exiftool -GPSLatitude -GPSLongitude file   # solo GPS
exiftool -Author -Company file             # autore e azienda
exiftool -DateTimeOriginal file            # data originale
exiftool -r directory/                     # ricorsivo

# Ricerca con grep
exiftool file | grep -i GPS
exiftool file | grep -iE "Author|Creator|Company"
exiftool file | grep -i "Camera\|Model\|Software"

# Export
exiftool -csv -r directory/ > output.csv  # esporta CSV

# Rimozione
exiftool -all= file                        # rimuovi tutto
exiftool -GPSLatitude= file                # rimuovi GPS
exiftool -overwrite_original -all= file    # rimuovi senza backup

# Bulk
exiftool -all= *.jpg                       # tutti i JPG
exiftool -r -if '$GPSLatitude' directory/  # solo file con GPS
```

---

## 🔗 Related Notes

- [[Sherlock]]
- [[OSINT & Footprinting]]
- [[GHDB_Google_Hacking_Database]]
- [[theHarvester]]
- [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Scanning/Nmap]]

---

_References: https://exiftool.org · https://book.hacktricks.xyz · Linux Basics for Hacking — OccupyTheWeb_