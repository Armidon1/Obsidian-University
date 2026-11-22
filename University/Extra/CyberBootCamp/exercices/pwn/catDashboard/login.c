unsigned __int64 login()
{
  unsigned int time; // eax
  int random_number; // [rsp+Ch] [rbp-64h]
  char username[32]; // [rsp+10h] [rbp-60h] BYREF
  char string_random_number[32]; // [rsp+30h] [rbp-40h] BYREF
  char password[24]; // [rsp+50h] [rbp-20h] BYREF
  unsigned __int64 canary; // [rsp+68h] [rbp-8h]

  canary = __readfsqword(0x28u);                // canary 
  
  //trova il time corrente e lo usa come seed per rand. nota che time è in secondi
  time = ::time(timer: nullptr);                // returns the current time (actually is the amount of seconds passed starting in 01/01/1970)
  srand(seed: time);                            // it use time as the seed of random (we can predict the randomness in this way)
  random_number = rand();                       // returns a random number from 0 to RAND_MAX (which is big)
  sprintf(s: string_random_number, format: "%d", random_number);// i'm writing the random number into s (notice that i'm representing random number in decimal, but i'm saving it as a string, that's why is a char*
  
  //prende le credenziali in input
  printf(format: "Username: ");
  fgets(s: username, n: 40, stream: stdin);
  printf(format: "Password: ");\
  fgets(s: password, n: 20, stream: stdin);
  
  //check delle credenziali
  if ( strncmp(s1: username, s2: "admin", n: 5u) == 0 )// first vulnerability: checks if the first 5 bytes are into username. adminxxxx also could work
  {
    if ( strncmp(s1: password, s2: string_random_number, n: 19u) == 0 )// password = string random number
    {
      puts(s: "Welcome back!");
      auth = 1;
    }
    else
    {
      puts(s: string_random_number);            // mostra il cazzo in chat e poi ti dice che hai sbaglaito. il cazzo cambia ogni volta 
      puts(s: "Invalid password!");
    }
  }
  else
  {
    puts(s: "Invalid username!");
  }
  return canary - __readfsqword(0x28u);         // check canary
}