from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk 
from tkinter.ttk import *

from random import randint 

import tkinter.font as TkFont 
import extraction
import tkinter as tk
import os


class Visualisateur: 
    #creation du constructeur
    def __init__(self):
        #création d'une première interface, 
        self.interface = tk.Tk()
        #Personnalisation de cette fenêtre 
        self.interface.title("Visualisateur de Trafic réseau")
        self.interface.geometry("1200x720")
        self.interface.minsize(1200,720)
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

        fichier_lecture= open(fichier, "r") 
        #print(fichier_lecture.read())
        lines = [l for l in (line.strip() for line in fichier_lecture) if l]  # retire les lignes vides
        Trames = []
        Trame = []
        first = True
        for l in lines :
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
        Trames.append(Trame)
        #ferme le fichier
        fichier_lecture.close()

        #j'ouvre la deuxième fenetre
        self.visualisateur_structure()
        #je repartie les donnée dans les piles (cad listBox)
        self.affichageFrame(Trames)


#front du visualisateur 2ème page du visualisateur 
    def visualisateur_structure(self): 
        self.bienvenu.destroy()
        self.btn.destroy()
      

        #creation d'un menu permettant d'afficher les cadres des listbox et en scrollbar
        self.frame = tk.Frame(self.interface, width=1080, height=720 )
        self.frame.pack(side=TOP)

             
        #listboxsrc = source ip
        self.listboxsrc= Listbox(self.frame,width=17,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxsrc.grid(row=1,column=0,pady=30)
        ip1label=Label(self.frame,text="ip src",font=("Courier", 14))
        ip1label.grid(row=0,column=0,sticky="s",pady=(40,0))
        
        #listboxdestination = destination ip
        self.listboxdestination=Listbox(self.frame,width=17,height=16,borderwidth=0, foreground= "red",highlightthickness=0,font=("Courier", 14))
        self.listboxdestination.grid(row=1,column=3,pady=30)
        ip2label=Label(self.frame,text="ip dest", foreground= "red", font=("Courier", 14))
        ip2label.grid(row=0,column=3,sticky="s",pady=(40,0))


        # listboxsrc_port = port source
        self.listboxsrc_port = Listbox(self.frame, width=7, height=16,borderwidth=0, foreground= "red", highlightthickness=0,font=("Courier", 14))
        self.listboxsrc_port.grid(row=1,column=1,pady=30)
        src_port=Label(self.frame,text="port src", foreground= "red", font=("Courier", 14))
        src_port.grid(row=0,column=1,sticky="s",pady=(30,0))
        #listboxdestinationport = port destination
        self.listboxdestinationport=Listbox(self.frame,width=7,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxdestinationport.grid(row=1,column=4,pady=30)
        dest_port=Label(self.frame,text="port dest",font=("Courier", 14))
        dest_port.grid(row=0,column=4,sticky="s",pady=(20,0))


        # listboxfleche = fleche 
        self.listboxfleche=Listbox(self.frame,width=17,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listboxfleche.grid(row=1,column=2)


        
        #listboxProtocol = protocol encapsulé
        self.listboxProtocol=Listbox(self.frame,width=10,height=16,borderwidth=0,highlightthickness=0, foreground= "red",font=("Courier", 14))
        self.listboxProtocol.grid(row=1,column=5,pady=30)
        protocol=Label(self.frame,text="Protocol",font=("Courier", 14), foreground="red")
        protocol.grid(row=0,column=5,sticky="s",pady=(30,0))


        # listBoxDescription = Description
        self.listBoxDescription=Listbox(self.frame,width=35,height=16,borderwidth=0,highlightthickness=0,font=("Courier", 14))
        self.listBoxDescription.grid(row=1,column=6,pady=30)
        description=Label(self.frame,text="Description",font=("Courier", 14))
        description.grid(row=0,column=6,sticky="s",pady=(40,0))

        #scrollbar
        scroll = Scrollbar(self.frame, orient='vertical')
        scroll.grid(row=1,column=7,pady=30,sticky="ns")
        scroll.config(command=self.__multiple_yview)

        self.listboxsrc.config(yscrollcommand=scroll.set)
        self.listboxsrc_port.config(yscrollcommand=scroll.set)
        self.listboxfleche.config(yscrollcommand=scroll.set)
        self.listboxdestination.config(yscrollcommand=scroll.set)
        self.listboxdestinationport.config(yscrollcommand=scroll.set)
        self.listboxProtocol.config(yscrollcommand=scroll.set)
        self.listBoxDescription.config(yscrollcommand=scroll.set)


    #si une listbox scrolls, toute les autres se scroll aussi 
    def __multiple_yview(self,*args): 
        self.listboxsrc.yview(*args)
        self.listboxsrc_port.yview(*args)
        self.listboxfleche.yview(*args)
        self.listboxdestination.yview(*args)
        self.listboxdestinationport.yview(*args)
        self.listboxProtocol.yview(*args)
        self.listBoxDescription.yview(*args)


   
        
    def affichageFrame(self, listTrame): 
        with open("FrameOutput.txt", "w") as f: 
            msg="Ip-src        port-src"+"          "+"  Ip-dest          port-dest   protocole           description\n\n"

            for trame in listTrame: 

                src_ip = extraction.ip_source(trame)
                dest_ip = extraction.ip_destination(trame)
                fleche = "--------------->"
                srcport = extraction.tcp_srcport(trame)
                destport = extraction.tcp_destport(trame)
                description = extraction.drapeau_tcp(trame)
                

                #condition pour tester si http dans trame  
                if(extraction.ipv4(trame) and extraction.is_tcp(trame) and extraction.is_http(trame)):
                    self.listboxsrc.insert(END, src_ip)
                    self.listboxsrc_port.insert(END, srcport)
                    self.listboxfleche.insert(END, fleche)
                    self.listboxdestination.insert(END, dest_ip)
                    self.listboxdestinationport.insert(END, destport)
                    self.listboxProtocol.insert(END, "HTTP")
                    methodhttp = extraction.HTTP_method(trame)
                    description.append(methodhttp)
                    self.listBoxDescription.insert(END, description)
                    msg+=str(src_ip)+"   "+str(srcport)+"--------------->"+str(dest_ip)+"        "+str(destport) +"   "+"   HTTP"+"             "+str(description)+"   "+"\n"


                if(extraction.ipv4(trame) and extraction.is_tcp(trame) and not extraction.is_http(trame)):
                    self.listboxsrc.insert(END, src_ip)
                    self.listboxsrc_port.insert(END, srcport)
                    self.listboxfleche.insert(END, fleche)
                    self.listboxdestination.insert(END, dest_ip)
                    self.listboxdestinationport.insert(END, destport)
                    self.listboxProtocol.insert(END, "TCP")
                    self.listBoxDescription.insert(END, description)
                    msg+=str(src_ip)+"   "+str(srcport)+"--------------->"+str(dest_ip)+"        "+str(destport) +"   "+"   TCP"+"              "+str(description)+"   "+"\n"

                if(extraction.ipv4(trame) and not extraction.is_tcp(trame) and not extraction.is_http(trame)):
                    self.listboxsrc.insert(END, src_ip)
                    self.listboxsrc_port.insert(END, "vide")
                    self.listboxfleche.insert(END, fleche)
                    self.listboxdestination.insert(END, dest_ip)
                    self.listboxdestinationport.insert(END, "vide")
                    self.listboxProtocol.insert(END, "IP seul")
                    self.listBoxDescription.insert(END, "pas de protocole encapsulant http ni tcp ")
                    msg+=str(src_ip)+"   "+"vide"+"--------------->"+str(dest_ip)+"        "+"vide" +"   "+"   IP seul"+"              "+"pas de protocole encapsulant http ni tcp "+"   "+"\n"
                self.i = self.i+1

            f.write(msg)  
        print(msg)
        f.close()
        

    def affichage(self):
        self.interface.mainloop()
      

if __name__ == "__main__":
    newinterface = Visualisateur()
    #newinterface.affichage()
    newinterface.affichage()



