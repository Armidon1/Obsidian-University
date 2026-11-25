import os

key = os.urandom(500)

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

with open('flag.txt') as f:
    lines = f.readlines()

with open('flag.enc', 'w') as f:
    for line in lines:
        f.write(xor(line.strip().encode(), key).hex())
        f.write('\n')