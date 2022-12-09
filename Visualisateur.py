from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from tkinter.ttk import *

from random import randint 

import tkinter.font as TkFont 
import os
import sys
import extraction

import parsing


class Visualisateur: 
    #creation du constructeur
    def __init__(self):
        #création d'une première interface, 
        self.interface = Tk()
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
    




    def affichageFrame(self, frames): 
        for frame in frames: 
            src_ip, srcport, fleche, dest_ip, destport, prot, description, = self.analyse(frame)
            self.itemlist.append((src_ip, srcport, fleche, dest_ip, destport, prot, description))


            self.listbox.insert(END, src_ip)
            self.listbox.insert(END, srcport)
            self.listbox.insert(END, fleche)
            self.listbox.insert(END, dest_ip)
            self.listbox.insert(END, destport)
            self.listbox.insert(END, prot)
            self.listbox.insert(END, description)
        
            self.i = self.i+1
        



    def affichage(self):
        self.interface.mainloop()
      

if __name__ == "__main__":
    newinterface = Visualisateur()
    #newinterface.affichage()
    newinterface.affichage()



