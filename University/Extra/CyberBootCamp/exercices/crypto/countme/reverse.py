from pwn import *

def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

DEBUG = 1
if DEBUG:
    context.log_level = "debug"

#p = process(["python3", "./server_local.py"])
p = remote("cyberchallenge.diag.uniroma1.it", "5254")


# FIRST STEP: RECEIVE AN ENCRYPTED KNOWN MESSAGE
p.recvuntil(b"Enter your choice: ")
p.sendline(b"2")
p.recvuntil(b"Enter the message you want to encrypt: ")
messaggiopococordiale = b"Desidero rubarti la chiave per le tue mutandine"
p.sendline(messaggiopococordiale)
p.recvline()    #remove that \n at the beginning of the string
encrypted_message = p.recvline()
print(encrypted_message)
encrypted_message= bytes.fromhex(encrypted_message.split()[-1].decode())
print(encrypted_message)

print(f"this is my encrypted messaggiopococordiale : {encrypted_message}\n")

# SECOND STEP: RECEIVE THE ENCRYPTED FLAG            
p.recvuntil(b"Choose an option:\n1: Encrypt flag\n2: Encrypt custom message\n3: Exit\nEnter your choice: ")
p.sendline(b"1")
p.recvline()    #that \n again
flag = bytes.fromhex(p.recvline().split()[-1].decode())
print(f"encrypted flag: {flag}\n")
flag = xor(xor(flag, encrypted_message), messaggiopococordiale)
print(f"ed ecco la nostra flag succulenta {flag}\n")