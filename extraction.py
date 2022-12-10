import sys
import os


def ipv4(Trame):
    return (Trame[0][12] == "08" and Trame[0][13] == "00")
    
def is_tcp(Trame):
    return ((Trame[1][7]) == "06")
   
def is_http(Trame):
    #parcourir la trame pour trouver le http
    if (tcp_destport(Trame) == 80 or tcp_srcport(Trame) == 80):
        for i in range(len(Trame)):
            for j in range(3,len(Trame[i])):
                if (Trame[i][j-3] == "48" and Trame[i][j-2] == "54" and Trame[i][j-1] == "54" and Trame[i][j] == "50"):
                    return True
    return False

#hexadecimal -> decimal 
def hexa_to_decimal (a) :
    return int(a,base=16)


#retourne l'adresse ip source de la trame
def ip_source(Trame):
    src_ip = str(hexa_to_decimal(Trame[1][10])) + "." + str(hexa_to_decimal(Trame[1][11])) + "." + str(hexa_to_decimal(Trame[1][12])) + "." + str(hexa_to_decimal(Trame[1][13]))
    return src_ip

#retourne l'adresse ip destination
def ip_destination(Trame):
    dest_ip = str(hexa_to_decimal(Trame[1][14])) + "." + str(hexa_to_decimal(Trame[1][15])) + "." + str(hexa_to_decimal(Trame[2][0])) + "." + str(hexa_to_decimal(Trame[2][1]))
    return dest_ip

#retourne le port tcp destination
def tcp_destport(Trame):
    tcpdst = hexa_to_decimal(Trame[2][4] + Trame[2][5])
    return tcpdst

#retourne le port tct source
def tcp_srcport(Trame):
    tcpsrc = hexa_to_decimal(Trame[2][2] + Trame[2][3])
    return tcpsrc

#retourne le drapeau  ainsi que les différentes option tcp 
def drapeau_tcp(Trame):
    #return the flags if they are set in a table
    flags = hexa_to_decimal(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    drapeau = []
    if (flags[6] == '1'):
        drapeau.append("URG")
    if (flags[7] == '1'):
        drapeau.append("ACK")
    if (flags[8] == '1'):
        drapeau.append("PSH")
    if (flags[9] == '1'):
        drapeau.append("RST")
    if (flags[10] == '1'):
        drapeau.append("SYN")
    if (flags[11] == '1'):
        drapeau.append("FIN")
    return drapeau

#retounr la taille de la trame tcp 
def taille_trame_tcp(Trame):
    tcptotallen = hexa_to_decimal(Trame[1][0] + Trame[1][1]) - hexa_to_decimal(Trame[0][14][1])*4
    taille_trame_tcp = tcptotallen - hexa_to_decimal(Trame[2][14][0])*4
    return taille_trame_tcp

#retourne le paquet tcp 
def paquet_tcp(Trame):
    return hexa_to_decimal(Trame[2][10] + Trame[2][11] + Trame[2][12] + Trame[2][13])

#retourne l'option sequence de tcp 
def sequence_tcp(Trame):
    return hexa_to_decimal(Trame[2][6] + Trame[2][7] + Trame[2][8] + Trame[2][9])

#retourne la window de tcp 
def tcpWindow(Trame):
    return hexa_to_decimal(Trame[3][0] + Trame[3][1])

#retourne la methode http 
def HTTP_method(trame):
    # On récupère la ligne de requete
    msg = ""
    i = 3  # ligne
    j = 6  # col
    while (trame[i][j] != "0d"):
        msg += chr(hexa_to_decimal(trame[i][j]))
        if(j==len(trame[i])-1):
            j=0
            i = i+1
        else:
            j = j+1
    return msg