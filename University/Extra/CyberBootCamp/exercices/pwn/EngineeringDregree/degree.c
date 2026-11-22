unsigned __int64 degree()
{
  char buf[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v2; // [rsp+28h] [rbp-8h]

  v2 = __readfsqword(0x28u);                    // stack canary
  printf(format: "Excuse me mr/mrs... should i call you mr or ms?\n>");
  read(fd: 0, buf, nbytes: 0x50u);              // leaking the canary here
  printf(format: "Hey %s, look here! Would you please sign this paper with your name?\n>", buf);
  read(fd: 0, buf, nbytes: 0x50u);              // exploiting the BOF for win
  puts(s: "Thank you!\nCome back in 1203892347289374 years after we're done printing you degree!");
  return v2 - __readfsqword(0x28u);
}