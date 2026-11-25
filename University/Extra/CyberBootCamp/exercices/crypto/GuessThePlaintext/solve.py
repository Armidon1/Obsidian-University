'''GUESS THE PLAINTEXT — cyberchallenge.diag.uniroma1.it 5161
Challenge 1: Can you guess the plaintext?
 i'm using AES ECB mode.
Enter a key (hex): ...

Teoria: ../../06 - CB - Crypto 1.md  (sezione "ECB — Electronic Codebook")
'''
from pwn import *
from Cryptodome.Cipher import AES

# scrivi qui il tuo script :)

DEBUG = 1
if DEBUG ==1: context.log_level = "debug"

p = remote("cyberchallenge.diag.uniroma1.it", "5128")
p.recvuntil("(hex): ")

key = b"A"*16 

#FIRST CHALLENGE
p.sendline(key.hex())
ct = p.recvline()
#print(ct)
ct = ct[34:98]
ct = bytes.fromhex(ct.decode())
print(ct)

cipherboy = AES.new(key, AES.MODE_ECB)
pt = cipherboy.decrypt(ct)
print(pt)
p.sendline(pt)

#SECOND CHALLENGE
p.recvuntil("(hex): ")
p.sendline(key.hex())
iv = p.recvline()
iv = iv[22:54]
print(iv)
iv = bytes.fromhex(iv.decode())
ct = p.recvline()
ct = ct[34:98]
print(ct)
ct = bytes.fromhex(ct.decode())
#print(ct)

cipherboy = AES.new(key,AES.MODE_CBC, iv)
pt = cipherboy.decrypt(ct)
print(pt)
p.sendline(pt)

#THIRD CHALLENGE
p.recvuntil(b" i'm using AES CTR mode.\n")
key = p.recvline()
key = key[22:54]
key = bytes.fromhex(key.decode())
noncee = p.recvline()
noncee = noncee[24:24+16]
noncee = bytes.fromhex(noncee.decode())
flag = p.recvline()
flag = flag[34:34+44]
flag = bytes.fromhex(flag.decode())

cipherboy = AES.new(key, AES.MODE_CTR, nonce=noncee)
flag = cipherboy.decrypt(flag)
print(flag)

while True:
    print(p.recvline())

#AES.new(key, AES.MODE_ECB).decrypt(ct)

