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

    """lecturefile = []"""

    def openfile(self):

        filetypes = ( 
            (('text files', '*.txt'),
            ('All files', '*.*')
        ))

        fichier = fd.askopenfilename(
                                initialdir = os.getcwd(),
                                title = 'Selectionner un fichier',
                                filetypes= filetypes)

        self.fichier_frames= parsing.parsing(fichier)

        if (self.premier_fichier_ouvert):
            self.visualisateur_structure()

        """
        self.analyse(fichier)
        self.lecturefile.insert(projet.lecture(fichier))
        """

        #affichage des différentes frames (il peut y en avoir plusieurs dans le fichier ) 
        self.affichageFrame(self.fichier_frames)
        self.premier_fichier_ouvert=False
        print(self.fichier_frames)

    
    
#front du visualisateur 
    def visualisateur_structure(self): 
        self.bienvenu.destroy()
        self.btn.destroy()
        self.interface.config(background ='white')


        #creation d'un menu permettant d'afficher les cadres des listbox et en scrollbar
        self.frame = Frame(self.interface, width=1020, height=720 )
        self.frame.pack(side=TOP)
   
        # create listboxes to display the frames


        # listbox1 = source
        self.listboxsrc = Listbox(self.frame, width=14, height=16,borderwidth=0,highlightthickness=0,font=("Helvetica", 14),exportselection=0,activestyle="none",background="#f0f0f0")
        self.listboxsrc.grid(row=1,column=0,pady=30)
        ip1label=Label(self.listboxsrc,text="Ip1",font=("Helvetica", 14))
        ip1label.grid(row=0,column=0,sticky="s",pady=(30,0))
        self.listboxlabel1=Label(self.listboxsrc,text="Ip1",font=("Helvetica", 14))

        #creation des différentes listBoxe pour afficher les différentes partie de la trame
        #self.listBox = Listbox(self.frame, font="Times", width=90, height=30)
        #self.listBox.pack(side= LEFT)
        self.framelistBox = Frame(self.interface, width=1020, height=720)
        self.framelistBox.pack(side=TOP)
        
        #creation d'une liste box 
        self.listBox = Listbox(self.framelistBox, font="Times", width=90, height=30)
        self.listBox.pack(side= LEFT, fill = BOTH)
        
    

        #creation de la liste de liste, permettant d'acceuillir toute les listes obtenue
        #par la fonction analyse
        #self.listListBox = Listbox(self.listBox, )

        #CREATION D'UNE SCROLLBAR POUR SCROOL LA LISTE BOX 
        scroll = Scrollbar(self.frame, orient='vertical')
        scroll.pack()  
        #scroll.pack(fill="both", expand="yes", padx = 10, pady=10)       
        scroll.config(command=self.frame.yview)
        self.listBox.config(yscrollcommand=scroll.set)

    def analyse(self,trame):

        #retourne la trame analyse 
        scrollbar = Scrollbar(self.listBox, orient='vertical')
        scrollbar.pack(side = RIGHT, fill=Y, expand="yes", padx = 10, pady=10)
        scrollbar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scrollbar.set)
    
        
        """
        gui = Tk()

        scrollbar = Scrollbar(gui)
        scrollbar.pack( side = RIGHT, fill = Y )

        liste = Listbox(gui, yscrollcommand = scrollbar.set )
        for i in range(1,201):
            liste.insert(END, str(i) + " - Hello World!")

        liste.pack(side = LEFT, fill = BOTH )
        scrollbar.config(command = liste.yview )
        """

        
    
    """
    def analyse(self,Trame):

        for Trame in Trame:
            if(extraction.ipv4(Trame) and extraction.tcp(Trame) and extraction.http(Trame)):
                self.listBox.insert("Couche la plus haute : HTTP"+"\n")
                self.listBox.insert(extraction.ipsource(Trame),"                                                                                       ",extraction.ipdestination(Trame)+"\n")
                self.listBox.insert("                                             ",extraction.methodhttp(Trame)+"\n")
                self.listBox.insert("   ",extraction.tcpsrcport(Trame),"------------------------------------------------------------------------------------------------->",extraction.tcpdstport(Trame)+"\n")
            if(extraction.ipv4(Trame) and extraction.tcp(Trame) and not extraction.http(Trame)):
                self.listBox.insert("Couche la plus haute : TCP"+"\n")
                self.listBox.insert(extraction.ipsource(Trame),"                                                                                       ",extraction.ipdestination(Trame)+"\n")
                self.listBox.insert("               ",extraction.tcpflags2(Trame),extraction.tcpflags(Trame), "Win =",extraction.tcpWindow(Trame),"Len =", extraction.tcplen(Trame),"Seq =",extraction.tcpseq(Trame),"Ack =",extraction.tcpack(Trame)+"\n")
                self.listBox.insert("   ",extraction.tcpsrcport(Trame),"------------------------------------------------------------------------------------------------->",extraction.tcpdstport(Trame)+"\n")
                #print("Commentaire : ",tcpsrcport(Trame), " -> ", tcpdstport(Trame), tcpflags2(Trame),"Seq =",tcpseq(Trame), tcpflags(Trame), "Win =", tcpWindow(Trame), "Len =", tcplen(Trame))
            if(extraction.ipv4(Trame) and not extraction.tcp(Trame) and not extraction.http(Trame)):
                self.listBox.insert("IP source", extraction.ipsource(Trame), "--------> IP destination", extraction.ipdestination(Trame)+"\n")
            self.listBox.insert("\n")
    """


    
    def affichageFrame(self, listFrame): 
        for frames in listFrame: 
            src_ip, srcport, fleche, dest_ip, destport, prot, des, = self.analyse(listFrame)
            self.listbox.insert(END, src_ip)
            self.listbox.insert(END, srcport)
            self.listbox.insert(END, fleche)
            self.listbox.insert(END, dest_ip)
            self.listbox.insert(END, destport)
            self.listbox.insert(END, prot)
            self.listbox.insert(END, des)
        
            self.i = self.i+1
    

    """
    def analyse(self,trame):

        flecheDroite="--------→"
        flecheGauche="←--------"

        eth_entete  = extraction.extraction_eth(trame)
        
        if (not extraction.is_trame_ip(trame)): 
            pas_eth = (eth_entete[1], "",flecheDroite,eth_entete[0],"", "None",'Pas une trame Ethernet')
            return pas_eth

        entete_ip = extraction.extraire_ip(trame)
       



        #adresses ip pair
        couple=self.couple_ip(entete_ip[7], entete_ip[8])
    #A FINIR 
    """
        



    def affichage(self):
        self.interface.mainloop()
      

if __name__ == "__main__":
    newinterface = Visualisateur()
    #newinterface.affichage()
    newinterface.affichage()



