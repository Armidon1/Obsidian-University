int granny()
{
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  puts(s: "Old granny says to you: oh my dear... I can't remember the flag anymore...\nBut I can make you a cake!");
  puts(s: "What flavor do you want?");
  putchar(c: '>');
  read(fd: 0, buf, nbytes: 0x50u);
  if ( buf[0] != 115
    || buf[1] != 116
    || buf[2] != 114
    || buf[3] != 97
    || buf[4] != 119
    || buf[5] != 98
    || buf[6] != 101
    || buf[7] != 114
    || buf[8] != 114
    || buf[9] != 121 )
  {
    printf(format: "I'm sorry, I don't have any %s in my fridge...\n", buf);
    exit(status: 0);
  }
  printf(
    format: "How lucky! I happen to have some %s in  my fridge! And what would you like the topping to be?\n"
    "1]Caramel\n"
    "2]Strawberries",
    buf);
  putchar(c: 62);
  read(fd: 0, buf, nbytes: 0x60u);
  return printf(format: "Ok now wait a second here... I'll cook something really special for you!");
}