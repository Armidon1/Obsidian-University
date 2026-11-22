#include <stdio.h>
#include <string.h>

void decodeThat(char* dumbflag, int size){
    char flag[size];
    memcpy(flag, dumbflag, size);
    for(int i = 39; i > 0; --i){
        flag[i] ^= flag[i-1];
    }
    printf("%s",flag);
    return;
}