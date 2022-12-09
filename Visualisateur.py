from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from tkinter.ttk import *

from random import randint 

import tkinter.font as TkFont 
import os
import sys
import extraction
import tkinter as tk

import parsing
import projet




class Visualisateur: 
    #creation du constructeur
    def __init__(self):
        #création d'une première interface, 
        self.interface = tk.Tk()
        #Personnalisation de cette fenêtre 
        self.interface.title("Visualisateur de Trafic réseau")
        self.interface.geometry("1080x720")
        self.interface.minsize(1080,720)

        self.premier_fichier_ouvert = True
        self.interface.config(background ='#548f6f')
        self.interface.resizable(height=True, width=True)
        self.btn=ttk.Button(self.interface, text =" Veuillez ouvrir un fichier contenant une trame", command=self.openfile)
        self.bienvenu=Label(self.interface, font=("Courier", 20), background='#548f6f', text="Bienvenue dans le visualisateur de trafic réseau !")
        self.bienvenu.pack()

        #configuration des boutons et du texte 
        self.btn.config(width=60, padding=10, style="")

        self.btn.pack(side=TOP, pady=25, fill=X)
        self.btn.place(relx=0.5, rely= 0.5, anchor=CENTER)
        self.bienvenu.place(relx= 0.5, rely= 0.3, anchor=CENTER)
        self.i = 0

    def lecture(file):
    #ouvre le fichier texte
        with open(file, "r+") as file:
            lines = [l for l in (line.strip() for line in file) if l]  # retire les lignes vides
            Trames = []
            Trame = []
            first = True
            for l in lines:
                #retirer les espace au debut et a la fin de la ligne
                l = l.strip()
                #on separe l'offset et le code hexa
                split = l.split("  ")
                offset = split[0]
                if (offset == "0000"):
                    if not first:
                        Trames.append(Trame)
                        Trame = []
                    first = False
                #on split par des espaces
                ltrame = split[1].split(" ")
                #on retire les espaces vides
                ltrame = [x for x in ltrame if x]
                #converti l'offset en hexa
                offset = int(split[0], 16) 
                Trame.append(ltrame)
        #ferme le fichier
        file.close()
        return Trames


    def openfile(self):

        filetypes = ( 
            (('text files', '*.txt'),
            ('All files', '*.*')
        ))

        fichier = fd.askopenfilename(
                                initialdir = os.getcwd(),
                                title = 'Selectionner un fichier',
                                filetypes= filetypes)

        self.fichier_frames=  Visualisateur.lecture(fichier)

        if (self.premier_fichier_ouvert):
            self.visualisateur_structure()


        #affichage des différentes frames (il peut y en avoir plusieurs dans le fichier) 
        self.affichageFrame(self.fichier_frames)
        self.premier_fichier_ouvert=False
        print(self.fichier_frames)

    
    
#front du visualisateur 2ème page du visualisateur 
    def visualisateur_structure(self): 
        self.bienvenu.destroy()
        self.btn.destroy()
        self.interface.config(background ='white')


        #creation d'un menu permettant d'afficher les cadres des listbox et en scrollbar
        self.frame = Frame(self.interface, width=1000, height=720 )
        self.frame.pack(side=TOP)

        # listboxsrc = src_ip
        self.listboxsrc = Listbox(self.frame, width=14, height=16,borderwidth=0,highlightthickness=0,font=("Courier", 16))
        self.listboxsrc.grid(row=0,column=0,pady=30)
        ip1label=Label(self.listboxsrc,text="ip1",font=("Courier", 14))
        ip1label.grid(row=0,column=0,sticky="s",pady=(30,0))
        self.listboxlabel1=Label(self.frame,text="Ip1",font=("Courier", 14))

        # listboxsrc_port = port source
        self.listboxsrc_port = Listbox(self.frame, width=14, height=16,borderwidth=0,highlightthickness=0,font=("Courier", 16))
        self.listboxsrc_port.grid(row=1,column=1,pady=30)
        src_port=Label(self.frame,text="port1",font=("Courier", 14))
        src_port.grid(row=0,column=1,sticky="s",pady=(30,0))
        # listboxfleche = fleche 
        self.listboxfleche=Listbox(self.frame,width=20,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 16))
        self.listboxfleche.grid(row=0,column=2,pady=30)

        #listboxdestination = destination 
        self.listboxdestination=Listbox(self.frame,width=14,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxdestination.grid(row=1,column=3,pady=30)
        ip2label=Label(self.frame,text="ip2",font=("Courier", 14))
        ip2label.grid(row=0,column=3,sticky="s",pady=(30,0))

        #listboxdestinationport = port destination
        self.listboxdestinationport=Listbox(self.frame,width=7,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxdestinationport.grid(row=1,column=4,pady=30)
        port2label=Label(self.frame,text="port2",font=("Courier", 14))
        port2label.grid(row=0,column=4,sticky="s",pady=(30,0))
        #listboxProtocol = protocol encapsulé
        self.listboxProtocol=Listbox(self.frame,width=9,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxProtocol.grid(row=1,column=5,pady=30)
        protocol=Label(self.frame,text="Protocol",font=("Courier", 14))
        protocol.grid(row=0,column=5,sticky="s",pady=(30,0))
        # listBoxDescription = Description
        self.listBoxDescription=Listbox(self.frame,width=35,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listBoxDescription.grid(row=1,column=6,pady=30)
        description=Label(self.frame,text="Description",font=("Courier", 14))
        description.grid(row=0,column=6,sticky="s",pady=(30,0))

        #scrollbar
        scroll = Scrollbar(self.frame, orient='vertical')
   
        self.listboxsrc.config(yscrollcommand=scroll.set)
        self.listboxsrc_port.config(yscrollcommand=scroll.set)
        self.listboxfleche.config(yscrollcommand=scroll.set)
        self.listboxdestination.config(yscrollcommand=scroll.set)
        self.listboxdestinationport.config(yscrollcommand=scroll.set)
        self.listboxProtocol.config(yscrollcommand=scroll.set)
        self.listBoxDescription.config(yscrollcommand=scroll.set)

        scroll.pack()  
        #creation de la liste de liste, permettant d'acceuillir toute les listes obtenue
        #par la fonction analyse
        #self.listListBox = Listbox(self.listBox, )

        #CREATION D'UNE SCROLLBAR POUR SCROOL LA LISTE BOX 

        

      # scroll one listbox scrolls all others
    def __multiple_yview(self,*args): 
        self.listboxsrc.yview(*args)
        self.listboxsrc_port.yview(*args)
        self.listboxfleche.yview(*args)
        self.listboxdestination.yview(*args)
        self.listboxdestinationport.yview(*args)
        self.listboxProtocol.yview(*args)
        self.listBoxDescription.yview(*args)

    """def analyse(self,trame):
  
        gui = Tk()

        scrollbar = Scrollbar(gui)
        scrollbar.pack( side = RIGHT, fill = Y )

        liste = Listbox(gui, yscrollcommand = scrollbar.set )
        for i in range(1,201):
            liste.insert(END, str(i) + " - Hello World!")

        liste.pack(side = LEFT, fill = BOTH )
        scrollbar.config(command = liste.yview )
    """


   
        
    def affichageFrame(self, listTrame): 

        for trame in listTrame: 
            src_ip, srcport, fleche, dest_ip, destport, protocole, description = self.analyse(listFrame)
            self.listboxsrc.insert(END, src_ip)
            self.listboxsrc_port.insert(END, srcport)
            self.listboxfleche.insert(END, fleche)
            self.listboxdestination.insert(END, dest_ip)
            self.listboxdestinationport.insert(END, destport)
            self.listboxProtocol.insert(END, protocole)
            self.listBoxDescription.insert(END, description)
        
            self.i = self.i+1

        
    

    def analyse(self,trame):

        flecheDroite="--------→"

        #creation des entetes différentes 
        eth_entete  = extraction.extraction_eth(trame)
        ip_entete = extraction.extraire_ip(trame)
        tcp_entete = extraction.extraction_tcp(trame)
        str_ip_src = extraction.str_ip[7]
        str_ip_dest = extraction.str_ip[8]
        protocole = "TCP"

        if (not extraction.is_trame_ip(trame)): 
            pas_eth = (eth_entete[1], "",flecheDroite,eth_entete[0],"", "vide",'Pas une trame Ethernet')
            return pas_eth

        #verification de l'entete IP, minimum 20 octet de longueur
        if (int(ip_entete[1],16)*4 < 20): 
            return(eth_entete[1], " ", flecheDroite, eth_entete[0], "", "vide", "Pas une trame IP car l'entete est inferieur a 20 octets")

        #Adresse IP 
        #verification de l'adresse IP 
        ipsrc_ipdest =self.couple_ip(ip_entete[7], ip_entete[8])

        if (ipsrc_ipdest  == None): 
            print("Les adresses IP ne sont pas couplé, veuillez insérer une trame correcte")

        # ABSENCE DE LA FRAGMENTATION IP 
        if (not extraction.is_trame_tcp(trame)):
            return (str_ip_src, "", flecheDroite, str_ip_dest,"","IP" "Ce n'est pas une trame TCP")

        #entete tcp < 20 
        if(tcp_entete[4]<20):
            return (str_ip_src,"vide", flecheDroite, str_ip_dest,"vide","IP","Pas une trame TCP car l'entete est inferieur a 20")
        
        #entete TCP et ces drapeau 
        tcp_drapeau = tcp_entete[5]
        if (tcp_drapeau[0] =='1'):
            description = description + "[URG]"
        if (tcp_drapeau[1] =='1'): 
            description = description + "[ACK]"
        if (tcp_drapeau[2] =='1'): 
            description = description + "[PSH]"
        if (tcp_drapeau[3] == '1'):
            description = description + "[RST]"
        if (tcp_drapeau[4] == '1'):
            description = description + "[SYN]"
        if (tcp_drapeau[5] == '1'): 
            description = description + "[FIN]"

        #si le port n'est pas 80 
        if (tcp_entete[0] =='0050' or tcp_entete[1] =='0050'): 
            http = extraction.extraction_http(trame)
            description = description+ " " + http 
            protocole = protocole+"/HTTP"
        
        return (str_ip_src, str(int(tcp_entete[0],16)), flecheDroite,str_ip_dest, str(int(tcp_entete[1], 16)), protocole, description)


    def affichage(self):
        self.interface.mainloop()
      

if __name__ == "__main__":
    newinterface = Visualisateur()
    #newinterface.affichage()
    newinterface.affichage()



