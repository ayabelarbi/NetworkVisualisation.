from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from tkinter.ttk import *


import tkinter.font as TkFont 
import os
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

        self.interface.config(background ='#548f6f')
        self.interface.resizable(height=True, width=True)
        self.btn=ttk.Button(self.interface, text =" Ouvrir un fichier", command=self.openfile)
        self.bienvenu=Label(self.interface, text="Bienvenue dans le visualisateur de trafic réseau !")
        self.bienvenu.pack()

        #configuration des boutons et du texte 
        self.btn.config(width=20, padding=10, style="")

        self.btn.pack(side=TOP)
        self.btn.place(relx=0.5, rely= 0.5, anchor=CENTER)
        self.bienvenu.place(relx= 0.5, rely= 0.3, anchor=CENTER)



    def openfile(self):

        filetypes = ( 
            (('text files', '*.txt'),
            ('All files', '*.*')
        ))

        fichier = fd.askopenfilename(
                                initialdir = os.getcwd(),
                                title = 'Selectionner un fichier',
                                filetypes= filetypes)

        self.frames= parsing.parsing(fichier)


        #affichage des différentes frames (il peut y en avoir plusieurs dans le fichier ) 
        self.affichageFrame(self.frames)
        self.first=False
        print(self.affichageFrame)


    def parsingTrame(self): 
        self.bienvenu.destroy()
        self.btn.destroy()

        #creation d'un menu permettant d'afficher les cadres des listbox et en scrollbar
        self.framelistBox = Frame(self.interface, width=1200, height=500)
        self.framelistBox.pack(side=TOP)
        #creation d'une liste box 
        self.listBox = Listbox(self.framelistBox, font="Times", width=90, height=30)
        self.listBox.pack(side= LEFT)
        
        #CREATION D'UNE SCROLLBAR POUR SCROOL LA LISTE BOX 
        scroll = Scrollbar(self.listBox, orient='vertical')
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scroll.set)




    def affichageFrame(self, frames): 
        for frame in frames: 
            src, srcport, fleche, dest, destport, prot, des, = self.analyse(frame)
            self.listbox.insert(END, src)
            self.listbox.insert(END, srcport)
            self.listbox.insert(END, fleche)
            self.listbox.insert(END, dest)
            self.listbox.insert(END, destport)
            self.listbox.insert(END, prot)
            self.listbox.insert(END, des)
        
            self.i = self.i+1
        


    def analyse(self,trame):
        flecheDroite="--------→"
        flecheGauche="←--------"

        eth_entete  = extraction.extraction_eth(trame)
        
        if (not extraction.is_trame_ip(trame)): 
            pas_eth = (eth_entete[1], "",flecheDroite+eth_entete[0],"", "None",'Pas une trame Ethernet')
            return pas_eth

        entete_ip = extraction.extraire_ip(trame)
        
        #adresses ip pair
        couple=self.couple_ip(entete_ip[7], entete_ip[8])
    #A FINIR 
    



    def affichage(self):
        self.interface.mainloop()
      

if __name__ == "__main__":
    newinterface = Visualisateur()
    #newinterface.affichage()
    newinterface.affichage()



