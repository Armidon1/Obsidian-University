# Login Trojan Horse (Cavallo di Troia del Login)

**Tags:** #cybersecurity #authentication #malware #social_engineering #attacchi #password

## 1. Definizione e Concetto

Il Login Trojan Horse è una minaccia specifica mirata al furto di credenziali (password).

Si tratta di un programma malevolo che simula fedelmente l'interfaccia di login del sistema operativo o di un'applicazione.

L'obiettivo è ingannare l'utente inducendolo a inserire le proprie credenziali in una finestra falsa controllata dall'attaccante, invece che nel vero modulo di autenticazione del sistema.

> [!failure] Il punto debole
> 
> Questo attacco sfrutta il fattore umano. L'utente medio autentica il sistema "a vista": se la schermata sembra quella giusta, l'utente si fida e digita.

## 2. Meccanismo d'Azione

L'attacco segue solitamente questa sequenza logica:

1. **Infezione:** L'attaccante riesce a eseguire un programma sulla macchina vittima (o ha accesso fisico).
    
2. **Simulazione:** Il programma disegna una finestra grafica o testuale identica alla schermata di login standard (es. prompt di Windows, terminale Linux/Unix).
    
3. **Cattura:** L'utente ignaro digita `Username` e `Password`.
    
4. **Furto e Uscita:** Il Trojan salva le credenziali, le invia all'attaccante e spesso termina l'esecuzione mostrando un falso messaggio di errore ("Password errata"), restituendo poi il controllo al vero sistema operativo. L'utente riprova, entra nel sistema vero, e pensa di aver solo commesso un errore di battitura la prima volta.
    

> [!abstract] Visual Analysis: L'Esempio VAX/VMS
> 
> Nelle slide viene mostrato un classico esempio storico su terminale NetBSD/vax 3.
> 
> - **Aspetto:** Una schermata nera, testuale, noiosa e assolutamente standard.
>     
> - **Pericolosità:** Proprio perché appare "normale" e legittima, l'utente non ha motivo di sospettare che sia un falso prompt gestito da un malware.
>     

## 3. Contromisure: Secure Attention Key (SAK)

Come ci si difende da un programma che disegna pixel identici a quelli del sistema operativo?

La soluzione non è grafica, ma hardware/architetturale.

Si utilizza una **Secure Attention Key (SAK)** o **Secure Attention Sequence (SAS)**.

- **Concetto:** Una combinazione di tasti speciale che invia un segnale di interrupt direttamente al Kernel del Sistema Operativo, bypassando qualsiasi applicazione utente.
    
- **Garanzia:** Se l'utente preme questa combinazione, il sistema operativo sospende tutti i processi utente (incluso l'eventuale Trojan) e mostra il vero prompt di login fidato.
    
- **Esempio più famoso:** `Ctrl + Alt + Canc` su Windows (nella configurazione di dominio/sicura).
    

> [!tip] Exam Focus
> 
> Se un sistema operativo richiede di premere una combinazione di tasti fisica prima di inserire la password, lo fa per garantire che il prompt di login successivo sia autentico e non un Login Trojan.