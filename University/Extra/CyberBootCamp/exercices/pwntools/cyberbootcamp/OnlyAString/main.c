#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char flag[41];
    FILE* f = fopen("flag.txt", "r");
    fgets(flag, 41, f);
    fclose(f);

    for(int i = 0; i < 39; i++){
        flag[i+1] ^= flag[i];
        // print hex of char
    }
    fwrite(flag, 1, 40, stdout);
    puts("");

    return 0;

}