---
title: Informazioni Generali
aliases:
  - LASS — Informazioni Generali
tags:
  - lab-architetture-software-sicurezza
  - organizzazione-corso
source: 0 - General Info.pdf
---

# Informazioni Generali

> [!abstract]
> Slide introduttive del **Laboratorio di Architetture Software e Sicurezza Informatica** (codice AAF1569, Sapienza): docenti, argomenti, orari, pagina Classroom e modalità d'esame. Il corso insegna a **progettare e sviluppare applicazioni web multi-livello con garanzie di sicurezza**: si parte dal processo di sviluppo ([[01 - LASS - Software Development Process]]) e dalle architetture ([[02 - LASS - Software Architectures]]), si impara Ruby e Rails (lezioni 3–7), si passa al testing (BDD/TDD, lezioni 8 e 15) e si chiude con la sicurezza delle web app (lezioni 13, 14, 17).
>
> Indice dei concetti: [[MOC - Lab Architetture Software e Sicurezza]].

---

## Docenti

| Docente | Ufficio (DIAG, Via Ariosto 25) | Contatti |
|---|---|---|
| **Leonardo Querzoni** | II piano, stanza B208 | querzoni@diag.uniroma1.it — diag.uniroma1.it/querzoni |
| **Daniele Cono D'Elia** | I piano, stanza B112 | delia@diag.uniroma1.it — diag.uniroma1.it/~delia |

Dalle slide si capisce anche la divisione del lavoro: le parti su Ruby/Rails/BDD (lezioni 1–8) hanno il materiale su GitHub di D'Elia (`dcdelia/lab-assi`), mentre le parti di sicurezza (13, 14, 17) sono di Querzoni.

## Di cosa parla il corso

*Design and development of multi-layer web applications and services with security guarantees*, cioè progettazione e sviluppo di applicazioni e servizi web **multi-livello** (*multi-layer*: presentazione, logica applicativa, dati; vedi [[02 - LASS - Software Architectures#Layers|Layers]]) con garanzie di sicurezza. Quattro filoni:

- **processo di sviluppo e architetture software**: come si organizza un progetto e come si struttura un sistema;
- **sviluppo collaborativo**: lavorare in gruppo (metodologie Agile, git, user story);
- **sviluppo di web application/service**: Ruby on Rails, REST, MVC;
- **sicurezza**: autenticazione, gestione delle password, vulnerabilità comuni (OWASP Top 10).

## Organizzazione

Lezioni teoriche + laboratori pratici:

| Giorno | Orario | Luogo |
|---|---|---|
| Martedì | 15:00–18:00 (~3h) | Laboratori "Paolo Ercoli", Via Tiburtina 205, Aula 16 |
| Giovedì | 15:00–18:00 (~2–3h) | Edificio Marco Polo, Viale dello Scalo S. Lorenzo 82, Aula 106 |

## Pagina del corso

Il corso è su **Google Classroom**, codice `dpesv77`: informazioni, annunci, materiale e riferimenti. Le iscrizioni erano aperte fino al 15 marzo.

![[LASS-L00-p05.png]]

Il QR code della slide serve, presumibilmente, a raggiungere la classe Classroom dal telefono (la slide non dice dove punta).

## Esame

- Esito **idoneo / non idoneo** (*passed / not passed*), senza voto.
- L'esame è un **progetto**, proposto dai docenti o dagli studenti, da svolgere in gruppi di **3–5 persone** (con poche eccezioni).
- Il gruppo deve:
  - sviluppare una **web application funzionante** con gli strumenti visti nel corso (Ruby on Rails, test con Cucumber/RSpec…);
  - consegnare una **breve documentazione tecnica**;
  - **presentare** il lavoro con una demo e rispondere a qualche domanda sui contenuti del corso.
- Il progetto può essere usato anche come **prova finale della laurea triennale**.

> [!tip] Perché il corso è fatto così
> Tutto il programma converge sul progetto: il [[01 - LASS - Software Development Process|processo Agile]] spiega come lavorare in gruppo, [[05 - LASS - Rails Parte 1|Rails]] è lo strumento per costruire l'app, [[08 - LASS - Behavior-Driven Development|BDD]] e [[15 - LASS - Testing BDD e TDD|TDD]] servono a verificarla, e le lezioni di sicurezza indicano gli errori da evitare.
