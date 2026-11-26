int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned int counter; // [rsp+8h] [rbp-38h]
  int counter_flag; // [rsp+Ch] [rbp-34h]
  int len_flag_redacted; // [rsp+10h] [rbp-30h]
  unsigned int number_iteration; // [rsp+18h] [rbp-28h]
  char str_number_iteration[11]; // [rsp+2Dh] [rbp-13h] BYREF
  unsigned __int64 canary; // [rsp+38h] [rbp-8h]

  canary = __readfsqword(0x28u);
  len_flag_redacted = strlen(s: "ccit{___________________REDACTED___________________}");
  printf(format: "Enter the number of iterations: ");
  fflush(stream: stdout);
  fgets(s: str_number_iteration, n: 11, stream: stdin);// no BOF
  if ( str_number_iteration[strlen(s: str_number_iteration) - 1] == '\n' )// if finishes with \n, change it with \0
    str_number_iteration[strlen(s: str_number_iteration) - 1] = '\0';
  if ( strlen(s: str_number_iteration) > 9 )    // weak check, i need at least: 
                                                // >>> step = 69273666
                                                // >>> total = step*(5+len_flag)
                                                // >>> print(total) = 3948598962, which is 10 chars
                                                // but i can put '-1' and atoi will save it as an int but will be assignet to number_iteration, which is unsigned (INTEGER OVERFLOW)
  {
    puts(s: "Too many iterations! Exiting...");
    exit(status: 1);
  }
  number_iteration = atoi(nptr: str_number_iteration);
  printf(format: "Progress: [");
  counter = 0;
  counter_flag = 0;
  while ( number_iteration > counter )
  {
    if ( counter % (0xFFFFFFFF / (len_flag_redacted + 10)) == 0 )// one step each counter += 69.273.666 
    {
      if ( counter_flag <= 4 )                  // firts 5 times prints #
      {
        putchar(c: '#');
        fflush(stream: stdout);
      }
      if ( len_flag_redacted < counter_flag - 4 )// if we have finished printing the flag, print more 5 #
        putchar(c: '#');
      else
        putchar(c: aCcitRedacted[counter_flag - 5]);// starts printing the flag, the -5 is for the first 5 # printed before
      fflush(stream: stdout);
      ++counter_flag;
    }
    ++counter;
  }
  puts(s: "]\nDone!");
  return 0;
}