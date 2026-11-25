"""
Esercizi a buchi, parte 2: interi <-> bytes (il ponte verso RSA).

Come si usa: come esercizi_conversioni.py.
  python3 esercizi_interi.py
Le risposte attese stanno in _correttore_interi.py: non aprirlo prima di finire.

------------------------------------------------------------------------
L'idea in tre righe
------------------------------------------------------------------------
RSA lavora su NUMERI, non su byte: per cifrare un messaggio bisogna prima
trasformarlo in un unico intero, e dopo aver decifrato ritrasformarlo in byte.

Il trucco è leggere i byte come le cifre di un numero in base 256,
esattamente come "42" sono le cifre di un numero in base 10:

    "42"   in base 10  ->  4 * 10  + 2   = 42
    b"AB"  in base 256 ->  65 * 256 + 66 = ?

L'ordine conta. "big-endian": la prima cifra è la più pesante (come scriviamo
noi). "little-endian": la prima cifra è la meno pesante (come x86 mette gli
interi in memoria: è quello che fa p32 di pwntools).

    int.from_bytes(b, "big")        bytes -> int
    n.to_bytes(lunghezza, "big")    int -> bytes (la lunghezza in byte la scegli tu)
    n.bit_length()                  quanti bit servono per scrivere n
    hex(n) / int(testo, 16)         int <-> testo hex di UN numero
    pow(base, esp, mod)             base**esp % mod, ma veloce anche con numeri enormi
------------------------------------------------------------------------
"""

___ = NotImplemented   # il "buco": non toccare questa riga


# =====================================================================
# 1. I byte come cifre in base 256
# =====================================================================

def es01():
    # Quanto vale b"AB" letto come numero big-endian?
    # Fai il conto A MANO con 65, 66 e 256 (scrivi l'espressione, es. 3*10+4)
    return ___

def es02():
    # Ora fallo fare a Python, con la funzione giusta, sempre big-endian.
    return ___

def es03():
    # Stessi byte, ma little-endian. Prima prevedi il risultato, poi scrivilo.
    return ___

def es04():
    # Il contrario: da 16706 ai bytes, big-endian, in 2 byte. Deve venire b"AB".
    n = 16706
    return ___

def es05():
    # Quanti BYTE servono per scrivere n? Usa n.bit_length().
    # (8 bit = 1 byte, ma 9 bit ne vogliono già 2: occhio all'arrotondamento)
    n = 65536
    return ___

def es06():
    # (300).to_bytes(1, "big") esplode. Quale eccezione solleva?
    # Restituisci la CLASSE dell'eccezione (es. ValueError, TypeError, ...).
    # Prima ragiona: quanto vale al massimo 1 byte?
    return ___

def es07():
    # pwntools: p32(0xdeadbeef) produce 4 byte little-endian.
    # Ottieni gli stessi 4 byte SENZA pwntools.
    n = 0xdeadbeef
    return ___


# =====================================================================
# 2. Un intero scritto in hex (diverso dai bytes in hex!)
# =====================================================================

def es08():
    # Scrivi 255 in hex con la funzione integrata. Nota cosa c'è davanti.
    return ___

def es09():
    # Il server ti manda il numero "ff" (testo hex). Dammi l'intero.
    return ___

def es10():
    # La trappola: n = 0xabc. hex(n) è "0xabc": tolto "0x" restano 3 caratteri,
    # e bytes.fromhex("abc") dà ValueError (lunghezza dispari).
    # Ottieni comunque i bytes di n: deve venire b"\x0a\xbc".
    n = 0xabc
    return ___


# =====================================================================
# 3. pycryptodome fa la stessa cosa
# =====================================================================

from Cryptodome.Util.number import bytes_to_long, long_to_bytes

def es11():
    # Trasforma b"flag" in intero con bytes_to_long.
    return ___

def es12():
    # E ritorno: 1718378855 di nuovo in bytes, con long_to_bytes.
    return ___

def es13():
    # Prevedi senza eseguire: il giro
    #     long_to_bytes(bytes_to_long(b"\x00\x01"))
    # ti restituisce di nuovo b"\x00\x01"? Restituisci True o False.
    # (pensa: 007 e 7 sono lo stesso numero?)
    return ___


# =====================================================================
# 4. Mini RSA
# =====================================================================

N = 741348649304170817312109831184301147516910309979
E = 65537
D = 740941420542174538119846693689033054133880356905
C = 589412313191246388894716486114227230133925174672

def es14():
    # Decifra C. In RSA: m = C^D mod N. Poi m è un numero: rendilo bytes.
    # Deve venire una flag ccit{...}
    return ___

def es15():
    # Cifra tu: parti dal messaggio in bytes, rendilo intero, poi c = m^E mod N.
    # Deve venire esattamente C.
    msg = b"ccit{rsa_e_byte}"
    return ___


if __name__ == "__main__":
    from _correttore_interi import corri
    corri(globals())
