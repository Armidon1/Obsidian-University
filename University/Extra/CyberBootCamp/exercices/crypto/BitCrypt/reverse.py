from pwn import *

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def key_from_plaintext_and_cyphertext(pt, ct):
    ct = bytes.fromhex(ct.decode())
    return xor(ct,pt)
   
    
DEBUG = 1
if DEBUG == 1:
    context.log_level = "debug"

#p = process(["python3", "server.py"])
p = remote("cyberchallenge.diag.uniroma1.it", "5147")

p.recvuntil("Enter your choice (1/2/3): ")
p.sendline("1")
p.recvuntil("Enter the message to encrypt: ")
pt = "SucchiamiIlPiselloAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
p.sendline(pt)
ct = p.recvline()
ct = ct.split()
ct = ct[2]
print(ct)
key = key_from_plaintext_and_cyphertext(pt.encode(), ct)
#print(key)

p.sendline("2")
p.recvuntil("Enter your choice (1/2/3): ")
flag = p.recvline()
print(flag)
flag = flag.split()[2]
flag = xor(bytes.fromhex(flag.decode()), key)
print(flag)




