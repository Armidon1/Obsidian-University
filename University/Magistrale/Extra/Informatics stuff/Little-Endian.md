**Little-Endian** è un formato di ordinamento dei byte (endianness) in cui il byte meno significativo (**Least Significant Byte** o **LSB**) di un dato multi-byte viene memorizzato all'indirizzo di memoria più basso.

È l'ordine "opposto" a come leggiamo i numeri. Il "piccolo" (little) capo del numero viene per primo.

---

### 🏛️ Esempio Pratico

Immaginiamo di voler memorizzare lo stesso numero intero a 32 bit (4 byte):

**`0x1A2B3C4D`**

- Il byte più significativo (MSB) è **`1A`**.
    
- Il byte meno significativo (LSB) è **`4D`**.
    

Se il computer (un sistema Little-Endian, come un PC Intel x86) decide di salvare questo numero a partire dall'indirizzo di memoria `1000`, la disposizione sarà questa:

|**Indirizzo Memoria**|**Valore (Byte)**|**Significato**|
|---|---|---|
|**`1000` (più basso)**|`4D`|**LSB** (il "little end")|
|`1001`|`3C`||
|`1002`|`2B`||
|`1003` (più alto)|`1A`|**MSB**|

Come puoi vedere, il byte `4D` (la parte "piccola") va all'indirizzo `1000` (quello "piccolo").

Questo formato è quello dominante nel mondo dei personal computer (usato da Intel, AMD e architetture ARM in modalità Little-Endian).

vedi anche [[Big-Endian and Little-Endian]]