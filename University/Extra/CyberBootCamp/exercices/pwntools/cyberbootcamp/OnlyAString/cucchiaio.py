from pwn import *
import ctypes

fanculo = ctypes.CDLL("./fanculo.so")
#context.debug = "debug"

p = remote("cyberchallenge.diag.uniroma1.it", "5246")

encoded_flag = p.recvline()
flag = bytearray(encoded_flag) #bytes are immutable in python, so i'm converting bytes into arraybytes
print(f"encoded_flag = ", encoded_flag)
i = 39
while i!=0:
    flag[i] ^=flag[i-1]
    i-=1

#fanculo.decodeThat.argtypes = [ctypes.c_char_p, ctypes.c_int]
#fanculo.decodeThat(encoded_flag, 41)   

print(flag.decode())