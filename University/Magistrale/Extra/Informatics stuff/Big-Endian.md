**Big-Endian** è un formato di ordinamento dei byte (endianness) in cui il byte più significativo (**Most Significant Byte** o **MSB**) di un dato multi-byte viene memorizzato all'indirizzo di memoria più basso.

È l'ordine "naturale" con cui leggiamo i numeri. Il "grande" (big) capo del numero viene per primo.

---

### 🏛️ Esempio Pratico

Immaginiamo di voler memorizzare il numero intero a 32 bit (4 byte):

**`0x1A2B3C4D`**

- Il byte più significativo (MSB) è **`1A`**.
    
- Il byte meno significativo (LSB) è **`4D`**.
    

Se il computer (un sistema Big-Endian) decide di salvare questo numero a partire dall'indirizzo di memoria `1000`, la disposizione sarà questa:

|**Indirizzo Memoria**|**Valore (Byte)**|**Significato**|
|---|---|---|
|**`1000` (più basso)**|`1A`|**MSB** (il "big end")|
|`1001`|`2B`||
|`1002`|`3C`||
|`1003` (più alto)|`4D`|**LSB**|

Come puoi vedere, il byte `1A` (la parte "grande") va all'indirizzo `1000` (quello "piccolo").

Questo formato è lo standard utilizzato nei protocolli di rete ed è noto come **Network Byte Order**.

Vedi anche [[Big-Endian and Little-Endian]].