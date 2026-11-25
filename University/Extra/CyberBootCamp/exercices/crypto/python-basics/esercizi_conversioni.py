"""
Esercizi a buchi: str, bytes, interi, hex, XOR.

Come si usa:
  1. Sostituisci ogni ___ con il codice giusto (una sola espressione).
  2. Lancia:  python3 esercizi_conversioni.py
  3. Per ogni esercizio vedi OK, oppure cosa hai restituito e un suggerimento.

Finché un esercizio contiene ___ viene segnato come "da fare", non come errore.
Puoi farli in qualunque ordine, ma sono pensati per andare dall'alto in basso.
Schema di riferimento: Concetti/pycryptodome.md, sezione
"Schema delle conversioni str, bytes e hex".
"""

___ = NotImplemented   # il "buco": non toccare questa riga


# =====================================================================
# 1. Tipo e valore
# =====================================================================

def es01():
    # Che TIPO ha b"4369616f"? Restituisci il tipo stesso (es. int, str, ...)
    return bytes

def es02():
    # Quanto è lungo "4369616f" (testo hex)? E quanti byte veri rappresenta?
    # Restituisci una tupla (lunghezza_hex, numero_di_byte_veri)
    return (8,4)


# =====================================================================
# 2. Un byte è un numero da 0 a 255
# =====================================================================

def es03():
    # Quanto vale b"Ciao"[0]?  (scrivi il numero, non calcolarlo con Python)
    return 67

def es04():
    # Trasforma b"Ciao" nella lista dei suoi interi: [67, 105, 97, 111]
    x = b"Ciao"
    return list(x)

def es05():
    # Dalla lista di interi ricostruisci i bytes: deve venire b"Hi"
    numeri = [72, 105]
    return bytes(numeri)

def es06():
    # Codice numerico del carattere "A", e carattere del numero 97.
    # Restituisci la tupla (codice_di_A, carattere_97)
    return (ord("A"), chr(97))


# =====================================================================
# 3. str <-> bytes
# =====================================================================

def es07():
    # Hai scritto tu il plaintext come testo. Portalo in bytes.
    pt = "flag"
    return pt.encode()

def es08():
    # Il server ti ha mandato questi bytes. Rendili una str leggibile.
    riga = b"ccit{ciao}"
    return riga.decode()


# =====================================================================
# 4. Hex: un modo di SCRIVERE i byte
# =====================================================================

def es09():
    # Scrivi b"AB" in hex (deve venire la str "4142")
    return bytes.hex(b"AB")

def es10():
    # Il server ha stampato questo hex. Dammi i byte VERI.
    ct_hex = "4142"
    return bytes.fromhex(ct_hex)

def es11():
    # Come es10, ma l'hex ti arriva come bytes da recvline(), con lo \n.
    # Pulisci, converti in str, poi in byte veri. Deve venire b"AB".
    riga = b"4142\n"
    return bytes.fromhex(riga.strip().decode())

def es12():
    # Estrai i byte veri del ciphertext dall'ultima parola della riga.
    riga = b"Encrypted message: 48656c6c6f\n"
    return bytes.fromhex(riga.split()[2])

def es13():
    # La trappola di BitCrypt: quale di queste due variabili va passata
    # a bytes.fromhex()?  Restituisci la stringa "a" oppure "b".
    a = b"Succhiami"          # plaintext scritto da te, .encode()-ato
    b = b"53756363686961"     # ciphertext stampato dal server
    return "b"


# =====================================================================
# 5. XOR, zip, slicing
# =====================================================================

def es14():
    # XOR tra due NUMERI: 65 xor 3
    return 65^3

def es15():
    # Scrivi la funzione xor con un ciclo for normale (niente comprehension).
    def xor(a, b):
        out = []
        for x, y in zip(a, b):
            out.append(x^y)   # cosa va aggiunto? lo XOR di x e y
        if NotImplemented in out:
            return NotImplemented
        return bytes(out)
    return xor(b"AB", b"\x01\x02")

def es16():
    # Ora la stessa xor in UNA riga, con la comprehension.
    a, b = b"AB", b"\x01\x02"
    return bytes(x^y for x,y in zip(a,b))

def es17():
    # Mini BitCrypt. Ricava la chiave da pt e ct_hex, poi decifra la flag.
    pt = b"AAAAAAAA"
    ct_hex = "222832352a3c3e3c"
    flag_hex = "000a1a0010472200"
    # suggerimento: definisci la xor dentro questa funzione, poi
    # key = ..., poi restituisci la flag in chiaro (bytes)
    def xor(a,b):
        return bytes([x^y for x,y in zip(a,b)])
    key = xor(pt, bytes.fromhex(ct_hex))
    flag = xor(key, bytes.fromhex(flag_hex))
    return flag

def es18():
    # Slicing: dai primi 5 byte di x restituisci quelli dalla posizione 1
    # alla 3 compresa.  Deve venire b"BCD".
    x = b"ABCDE"
    return x[1:4]

def es19():
    # Il giro completo. Parti da "flag", portala in hex, poi torna indietro
    # fino a una str. Restituisci la tupla (forma_hex, str_finale).
    s = "flag"
    forma_hex = bytes.hex(s.encode())
    str_finale = bytes.fromhex(forma_hex).decode()
    return (forma_hex, str_finale)


# =====================================================================
# Correttore: non serve leggerlo
# =====================================================================

CHECKS = [
    (es01, bytes, "b'...' è sempre bytes, anche se dentro c'è testo hex"),
    (es02, (8, 4), "ogni byte vero = 2 caratteri hex"),
    (es03, 67, "indicizzare bytes dà un intero: il codice ASCII di 'C'"),
    (es04, [67, 105, 97, 111], "list(...) su dei bytes"),
    (es05, b"Hi", "bytes(...) su una lista di interi"),
    (es06, (65, "a"), "ord() e chr()"),
    (es07, b"flag", ".encode()"),
    (es08, "ccit{ciao}", ".decode()"),
    (es09, "4142", ".hex() su dei bytes"),
    (es10, b"AB", "bytes.fromhex(...)"),
    (es11, b"AB", ".strip(), poi .decode(), poi bytes.fromhex"),
    (es12, b"Hello", ".split()[-1], poi come es11"),
    (es13, "b", "fromhex serve solo per l'hex stampato dal server"),
    (es14, 66, "l'operatore XOR in Python è ^"),
    (es15, b"@@", "dentro append va x ^ y"),
    (es16, b"@@", "bytes(x ^ y for x, y in zip(a, b))"),
    (es17, b"ccit{:]}", "key = xor(pt, ct); flag = xor(flag_ct, key); ricorda fromhex"),
    (es18, b"BCD", "x[inizio:fine]: fine è esclusa"),
    (es19, ("666c6167", "flag"), "encode → hex → fromhex → decode"),
]

def main():
    fatti = 0
    for fn, atteso, aiuto in CHECKS:
        nome = fn.__name__
        try:
            r = fn()
        except Exception as e:
            print(f"  ✗ {nome}: errore {type(e).__name__}: {e}")
            print(f"           suggerimento: {aiuto}")
            continue
        if r is NotImplemented:
            print(f"  · {nome}: da fare")
        elif r == atteso and type(r) == type(atteso):
            print(f"  ✓ {nome}")
            fatti += 1
        else:
            print(f"  ✗ {nome}: hai restituito {r!r} ({type(r).__name__})")
            print(f"           suggerimento: {aiuto}")
    print(f"\n{fatti}/{len(CHECKS)} corretti")

if __name__ == "__main__":
    main()
