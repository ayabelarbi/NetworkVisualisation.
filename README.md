# Visualisateur de trafic réseaux

Le projet repose sur la construction d'un visualisateur de trafic réseaux. Nous nous inspirons de l'application Wireshark, afin de réaliser le projet. 
Le but de ce projet est de programmer un visualiseur de trafic réseau. Le trafic désigne les trames échangées dans le cadre du protocole dans le cadre d’un protocole exécuté par deux machines, chacune identifiée par une adresse MAC, Adresse IP et éventuellement numéro de port.

Le visualisateur prendra en entrée un fichier trace au format texte contenant les 
octets capturés préalablement sur un réseau Ethernet. Le programme s'affichera dans une interface graphique.

Notre visualisateur de trafic réseaux sera écrit avec le langage de programmation Python. 

# Etape de l'écriture du programme : 
La liste des protocoles que votre analyseur sera en mesure de comprendre sont les
suivants :
- Couche 2: Ethernet
- Couche 3: IPv4
- Couche 4: TCP
- Couche 7: HTTP


Le visualisateur affichera toutes les trames dans l'ordre chronologique correspondant à l'ordre dans lequel ils apparaissent dans le fichier trace.
 
 Pour chaque trame, le visualisateur affichera les informations suivantes : 
- L’adresse IP des deux machines impliquées.
- Le numéro de port utilisé.

Liste de chose a faire pour le projet : 

affichage du temps (ListBox gauche)                                          affichage des adresse 
1 : 00000 
2 : 00001 ( temps que la trame recoivent les ACK/)


Pour HTTP : 

adress IP source         adress IP destination
        |                           |
        |                           |
        |                           |
numéro de port src          numero de port dest 
    >= 1024                         80 (WEB)




