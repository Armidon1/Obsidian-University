ssize_t sussy()
{
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF
  const void *retaddr; // [rsp+28h] [rbp+8h]

  putchar(c: 62);
  read(fd: 0, buf, nbytes: 0x50u);
  printf(format: "you said: %s\n", buf);
  printf(format: "address is: %p\n", retaddr);
  printf(format: "sussy address: %p\n", sussy);
  return read(fd: 0, buf, nbytes: 0x50u);
}