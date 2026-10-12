---
title: Device File e ioctl
tags:
  - sistemi-operativi
  - concetto
  - file-system
  - io
---

# Device File e ioctl

> [!summary] In breve
> In Unix i dispositivi sono file in `/dev` (block: con seek, es. dischi; character: stream, es. seriali); le operazioni specifiche del dispositivo passano per `ioctl(fd, request, ...)`.

- `/dev/sda`, `/dev/sda1`, `/dev/ttyACM0`, `/dev/video0`.
- `cat file > /dev/ttyACM0`, `cat /dev/ttyACM0 > file`.
- `ioctl` è un gancio verso il driver: ogni driver registra i propri codici `request` e il proprio handler.
- I terminali e le seriali si configurano con **termios**.
- "**Tutto è un file**": anche ciò che non lo è (socket, pipe) ha un'interfaccia simile a un file.

## Collegamenti

- **Concetti correlati**: [[Driver e Block Device]] · [[File Descriptor]] · [[UART]] · [[Memory Mapped IO]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[12 - SO - File System#Dispositivi come file|Lezione 12 — Dispositivi come file]]
> - [[12 - SO - File System#ioctl e driver|Lezione 12 — ioctl e driver]]
> - [[12 - SO - File System#Tutto è un file|Lezione 12 — Tutto è un file]]
