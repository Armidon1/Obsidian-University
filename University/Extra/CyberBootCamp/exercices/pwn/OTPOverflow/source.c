void __fastcall generate_otp(char *buffer, int len)
{
  int i; // [rsp+10h] [rbp-10h]
  int bytes_read; // [rsp+14h] [rbp-Ch]
  FILE *fp; // [rsp+18h] [rbp-8h]

  fp = fopen(filename: "/dev/urandom", modes: "r");// /dev/urandom is a crittographically secure pseudorandom bytes generator made by the kernel itself
  bytes_read = fread(ptr: buffer, size: 1u, n: len, stream: fp);// reads 32 bytes and uses the otp_password as buffer
  fclose(stream: fp);
  if ( bytes_read != len )                      // check if all bytes have been written
    exit(status: 1);
  for ( i = 0; i < len; ++i )
    buffer[i] = (unsigned __int8)buffer[i] % 26u + 65;
  buffer[len - 1] = 0;
}

int __fastcall main(int argc, const char **argv, const char **envp)
{
  char user_password[32]; // [rsp+0h] [rbp-50h] BYREF
  char otp_password[32]; // [rsp+20h] [rbp-30h] BYREF
  unsigned __int64 canary; // [rsp+48h] [rbp-8h]

  canary = __readfsqword(0x28u);                // canary 
  setvbuf(stream: stdout, buf: nullptr, modes: 2, n: 0);
  setvbuf(stream: stdin, buf: nullptr, modes: 2, n: 0);
  puts(s: "------------------------------------------------------------");
  puts(s: "----------------[ Cyber Challenge Bootcamp ]----------------");
  puts(s: "------------------------------------------------------------");
  memset(user_password, 0, sizeof(user_password));
  memset(otp_password, 0, sizeof(otp_password));
  generate_otp(buffer: otp_password, len: 32);
  printf(format: "Enter password: ");
  fgets(s: user_password, n: 50, stream: stdin);// overflow
  user_password[strcspn(s: user_password, reject: "\n")] = 0;
  if ( user_password[0] == 0 )
  {
    puts(s: "Invalid input...");
    exit(status: 1);
  }
  if ( strcmp(s1: user_password, s2: otp_password) == 0 )// this is my target
  {
    puts(s: "Authenticated!");
    system(command: "/bin/sh");
  }
  else
  {
    puts(s: "Authentication failed...");
  }
  return canary - __readfsqword(0x28u);         // canary check
}