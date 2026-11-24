unsigned __int64 parrot()
{
  char buf[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v2; // [rsp+28h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts(s: "We only have orange parrots, that will be 13.99$ wanna proceed?");
  printf(format: "[yes/no]>");
  read(fd: 0, buf, nbytes: 256u);               // huge 256 overflow
  if ( strcmp(s1: buf, s2: "yes") == 0 )
    puts(s: "Ok, here is your parrot, have a nice day!");
  else
    puts(s: "Ok, come back again!");
  return v2 - __readfsqword(0x28u);
}

unsigned __int64 canary()
{
  char buf[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v2; // [rsp+28h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts(s: "What color would you like your canary to be?");
  putchar(c: '>');
  read(fd: 0, buf, nbytes: 41u);                // overflow of 1 byte
  printf(format: "Ok so we got some %s colored canary for you, that will be 5.99$ wanna proceed?\n", buf);
  printf(format: "[yes/no]>");
  read(fd: 0, buf, nbytes: 0x29u);
  if ( strcmp(s1: buf, s2: "yes") == 0 )
    puts(s: "Ok, here is your canary, have a nice day!");
  else
    puts(s: "Ok, come back again!");
  return v2 - __readfsqword(0x28u);
}

unsigned __int64 birdShop()
{
  int v1; // [rsp+4h] [rbp-Ch] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);                    // stack canary
  printf(format: "%s", format);
  while ( 1 )
  {
    puts(s: "What do you want to do?");
    puts(s: "1. Buy a canary");
    puts(s: "2. Buy a parrot");
    puts(s: "3. Buy a penguin");
    puts(s: "4. Buy a raven");
    puts(s: "5. Buy a chicken");
    puts(s: "6. Exit");
    putchar(c: '>');
    __isoc99_scanf(a1: "%d", &v1);
    switch ( v1 )
    {
      case 1:
        canary();
        break;
      case 2:
        parrot();
        break;
      case 3:
        penguin();
      case 4:
        raven();
        break;
      case 5:
        chicken();
        break;
      case 6:
        return v2 - __readfsqword(0x28u);
      default:
        puts(s: "Invalid choice");
        break;
    }
  }
}