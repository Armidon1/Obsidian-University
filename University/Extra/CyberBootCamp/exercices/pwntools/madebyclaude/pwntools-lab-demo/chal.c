#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// La funzione "premio": non viene MAI chiamata dal programma.
// L'obiettivo dell'exploit e' arrivarci lo stesso, dirottando il flusso.
void win() {
    puts("[win] Hai dirottato l'esecuzione! Ecco la shell:");
    system("/bin/sh");
}

void vuln() {
    char buf[32];                 // buffer da 32 byte sullo stack
    puts("Come ti chiami?");
    fgets(buf, 200, stdin);       // BUG: legge fino a 200 byte in 32 -> overflow
    printf("Ciao, %s", buf);
}                                 // al 'ret' di vuln, la CPU salta al return
                                  // address salvato sullo stack: se l'abbiamo
                                  // sovrascritto, controlliamo dove va.

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
