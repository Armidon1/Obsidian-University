#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Niente funzione win()! Stavolta devi costruire TU la chiamata a system("/bin/sh").
char *binsh = "/bin/sh";   // la stringa "/bin/sh" e' presente nel binario

// Gadget utile garantito nel binario: pop rdi ; ret
void gadget() {
    asm volatile("pop %rdi; ret");
}

void vuln() {
    char buf[64];
    puts("Inserisci i dati:");
    fgets(buf, 300, stdin);     // overflow: 300 byte in 64
    printf("Ricevuto: %s", buf);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    system("echo avvio");       // garantisce che system sia nella PLT
    vuln();
    return 0;
}
