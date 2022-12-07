import re # 
import string 

#lecture d'un fichier de trame et retour d'une liste de trame 
def parsing(filename):
    #creation d'une liste acceuillant les trames 
    trame = []
    trame_courrante = []

    with open(filename,'r') as f: 
        lignes = f.readlines()
        print(lignes)
        prems = lignes[0]
        print(prems)
        for ligne in lignes: 
            ligne_indice = ligne.strip().split(' ')
            #si l'offset = '0000'
            if ligne_indice[0] == '0000': 
                #si la trame courrante n'est pas vide, mais que l'offset = '0000'
                if trame_courrante !=[] : 
                    #rajout des trames courrante
                    trame.append(trame_courrante)
                    trame_courrante=[]
            
            #déclanchement des exceptions si la trame n'est pas nettoyer 
            #if(ligne_indice[0] == '0000' and prems == ligne): 
                #raise Exception("Trame invalid numéro 1 (l'offset est invalide)")  


    trame.append(trame_courrante)

    return trame 


#permet de convertir les fichiers hexa to ascii 
def hex_to_ascii(tab): #convertir des octets en chaine de caractere
    hex_string=""
    for i in tab :
        hex_string+=i
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode('utf-8')
    return ascii_string

#verification si hexadecimal
def check_hex(l:list):
    return 
