# Pseudo Terminal

![[Pasted image 20260609112147.png]]

Un PTY (pseudo-terminal) è una coppia di file descriptor creata dal kernel che simula un terminale hardware seriale, ma in software.

È composto da due estremi: il **master** (`/dev/ptmx`), tenuto aperto da chi fa da "schermo" (un emulatore di terminale, un server SSH/Telnet), e lo **slave** (`/dev/pts/0`, `/dev/pts/1`…), tenuto aperto dalla shell o dal programma che ci gira dentro. Tutto ciò che viene scritto su un estremo appare leggibile dall'altro — è essenzialmente una pipe bidirezionale con in più il supporto per le funzionalità di un terminale (dimensioni dello schermo, segnali da tastiera come Ctrl+C, echo dei caratteri, ecc.).

Il motivo per cui esiste è che le shell e molti programmi Unix si aspettano di parlare con un terminale — usano le sue API per sapere quanto è larga la finestra, per mandare sequenze di escape per i colori, per ricevere SIGINT quando premi Ctrl+C. Un PTY dà loro questa interfaccia anche quando il "terminale" reale è una finestra grafica, una connessione SSH o un processo che registra l'output.

# Esempio [[Telnet]]

Ottima scelta — telnet rende il PTY molto più chiaro perché il "master" è su una macchina remota.**La differenza chiave rispetto al diagramma originale** (che mostrava `script`) è che in Telnet il "master" non è più sullo stesso host — è il `telnetd` sul server, che fa da proxy tra la rete TCP e il PTY master del kernel.

![[Pasted image 20260609112108.png]]

Il flusso concreto quando digiti `ls`:

il tasto viaggia come byte TCP sulla porta 23 → `telnetd` riceve i dati e li scrive su `/dev/ptmx` (PTY master) → il kernel li specchia automaticamente sul PTY slave (`/dev/pts/0`) → `bash` legge da `fd[0]` (che punta a `/dev/pts/0`), esegue il comando, scrive l'output su `fd[1]` → il kernel rimanda l'output al master → `telnetd` lo manda indietro via TCP → il tuo terminale lo stampa sullo schermo.

`/dev/pts/0` che hai visto prima è esattamente lo slave di questa catena — `bash` non sa e non gli importa se il "terminale" dall'altra parte è fisico, una finestra grafica, o un tunnel di rete.