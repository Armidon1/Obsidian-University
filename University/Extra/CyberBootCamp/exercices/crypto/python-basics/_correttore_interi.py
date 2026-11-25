# Correttore di esercizi_interi.py: contiene le risposte, non aprirlo prima di finire.

CHECKS = [
    ("es01", 16706, "65 * 256 + 66"),
    ("es02", 16706, "int.from_bytes(..., \"big\")"),
    ("es03", 16961, "little: 66 è la cifra pesante → 66 * 256 + 65"),
    ("es04", b"AB", "n.to_bytes(2, \"big\")"),
    ("es05", 3, "(n.bit_length() + 7) // 8 arrotonda per eccesso"),
    ("es06", OverflowError, "1 byte arriva al massimo a 255"),
    ("es07", b"\xef\xbe\xad\xde", "n.to_bytes(4, \"little\")"),
    ("es08", "0xff", "hex(255)"),
    ("es09", 255, "int(testo, 16)"),
    ("es10", b"\x0a\xbc", "salta l'hex: n.to_bytes(2, \"big\")"),
    ("es11", 1718378855, "bytes_to_long(b\"flag\")"),
    ("es12", b"flag", "long_to_bytes(...)"),
    ("es13", False, "gli zeri iniziali di un numero si perdono: 0x0001 == 1"),
    ("es14", b"ccit{rsa_e_byte}", "long_to_bytes(pow(C, D, N))"),
    ("es15", 589412313191246388894716486114227230133925174672, "pow(bytes_to_long(msg), E, N)"),
]

def corri(ns):
    fatti = 0
    for nome, atteso, aiuto in CHECKS:
        try:
            r = ns[nome]()
        except Exception as e:
            print(f"  ✗ {nome}: errore {type(e).__name__}: {e}")
            continue
        if r is NotImplemented:
            print(f"  · {nome}: da fare")
        elif r == atteso and type(r) == type(atteso):
            print(f"  ✓ {nome}")
            fatti += 1
        else:
            print(f"  ✗ {nome}: hai restituito {r!r} ({type(r).__name__})")
            print(f"           (se ti blocchi chiedimi un aiuto)")
    print(f"\n{fatti}/{len(CHECKS)} corretti")
