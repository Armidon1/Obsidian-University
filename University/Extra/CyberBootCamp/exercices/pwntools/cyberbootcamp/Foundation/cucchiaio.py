from pwn import *
context.log_level = 'debug'

laws = [
    'A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
    'A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.',
    'A robot must protect its own existence as long as such protection does not conflict with the First or Second Law.'
]

#p = process(["python3", "./server.py"])
p = remote("cyberchallenge.diag.uniroma1.it", "5237")

for i in range(100):
    while(True):
        sentence = p.recvline()
        if (b'First'in sentence) or (b'Second' in sentence) or (b'Third' in sentence):
            break
    if b'First' in sentence:
        p.sendline(laws[0])
    elif b'Second' in sentence:
        p.sendline(laws[1])
    elif b'Third' in sentence:
        p.sendline(laws[2])

flag = p.recvline()
print(flag)
