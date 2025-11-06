# VLAN (Virtual LAN)
Le VLAN si possono implementare solo grazie ai Switch. Le VLAN funzionano grazie a Router per cui una specifica porta ethernet è associata come VLAN1 mentre un altra porta ethernet è VLAN2. in questo caso, una sottorete che è collegata alla porta VLAN1 non è in grado di comunicare con una VLAN2 (da approfondire meglio). 

Le [[VLAN]] sono la tecnologia più comune per implementare la **segmentazione logica**.

- Funzionano al **Livello 2 OSI** (Data Link).
    
- Sono implementate da quasi tutti gli switch di rete commerciali.
    
- Permettono a un'unica infrastruttura fisica di rete di essere suddivisa in più domini di broadcast _logici_.
    

![[Pasted image 20251105150400.png]]
Recuperare che cos'è un [[Trunk link]]. I trunk link si possono effettuare solamente tra Router.![[Pasted image 20251105150418.png]]
Definiamo trusted i Switch ma non necessariamente i Client.
![[Pasted image 20251105150428.png]]
Notiamo che siamo a Livello 3, non possiamo lavorare solamente a Livello 2 (di collegamento). quindi la presenza di un router è necessario. 
![[Pasted image 20251105150447.png]]Come mostrato nei diagrammi, i dispositivi sulla VLAN 10 (HR) e sulla VLAN 20 (Finance) possono essere collegati allo stesso switch fisico ma non possono comunicare direttamente.

Per comunicare _tra_ VLAN (es. per far accedere l'impiegato HR al DB HR), il traffico deve passare attraverso un **dispositivo di Livello 3 (un router, ricordiamo il livello di rete)**. Questo router funge da checkpoint dove vengono applicate le Access Control List (ACL) per imporre le regole di sicurezza. 