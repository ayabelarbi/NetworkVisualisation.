
import re


#lecture de la trames 
def lecture(filename):
    return 

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
