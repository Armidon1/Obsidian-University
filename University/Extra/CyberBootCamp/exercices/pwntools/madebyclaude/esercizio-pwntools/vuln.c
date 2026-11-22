#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Obiettivo dell'esercizio: arrivare QUI, anche se nessuno la chiama.
void shell_segreta() {
    puts("[*] Codice corretto. Shell aperta:");
    system("/bin/sh");
}

void login() {
    char codice[48];                 // buffer da 48 byte
    puts("Codice di accesso:");
    fgets(codice, 256, stdin);       // overflow: 256 byte in 48
    printf("Negato: %s", codice);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    login();
    return 0;
}
