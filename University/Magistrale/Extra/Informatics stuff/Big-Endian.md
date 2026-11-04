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

### Letture più corte

Dato che il byte più significativo è al primo indirizzo, partendo da `1000` e leggendo meno byte ottieni **la parte alta** del numero. Per ottenere quella bassa devi partire da un indirizzo più alto:

|**Lettura**|**Byte presi**|**Valore**|
|---|---|---|
|4 byte da `1000`|`1A 2B 3C 4D`|`0x1A2B3C4D`|
|2 byte da `1000`|`1A 2B`|`0x1A2B` (parte alta)|
|2 byte da `1002`|`3C 4D`|`0x3C4D` (parte bassa)|
|1 byte da `1003`|`4D`|`0x4D` (parte bassa)|

Questo offset non rende il Big Endian più lento in modo significativo: spesso il compilatore lo calcola già in fase di compilazione. L'esempio completo è in [[Big-Endian and Little-Endian#Esempio: letture di dimensioni diverse|Letture di dimensioni diverse]].

Vedi anche [[Big-Endian and Little-Endian]].