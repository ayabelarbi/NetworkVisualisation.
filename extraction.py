import parsing 
import sys
import os

#Tuple des protocol
Eth=tuple[str,str,str] #adress dest, adress src, type 
Ip=tuple[str,str,str,str,str,str,str,str,str,str,str]
ip_flags=tuple[str,str]
tcp= tuple[str,str,str,str,str,str,str,str,str]
tcp_flags= tuple[str,str,str,str,str,str]

def ipv4(Trame):
    return (Trame[0][12] == "08" and Trame[0][13] == "00")
    
def tcp(Trame):
    return ((Trame[1][7]) == "06")
   
def udp(Trame):
    return (Trame[1][7] == "11")
   
def http(Trame):
    #parcourir la trame pour trouver le http
    if (tcpdstport(Trame) == 80 or tcpsrcport(Trame) == 80):
        for i in range(len(Trame)):
            for j in range(3,len(Trame[i])):
                if (Trame[i][j-3] == "48" and Trame[i][j-2] == "54" and Trame[i][j-1] == "54" and Trame[i][j] == "50"):
                    return True
    return False

#hexadecimal -> decimal 
def to_decimal(a) :
    return int(a,base=16)

def ipsource(Trame):
    ipsrc = str(to_decimal(Trame[1][10])) + "." + str(to_decimal(Trame[1][11])) + "." + str(to_decimal(Trame[1][12])) + "." + str(to_decimal(Trame[1][13]))
    return ipsrc

def ipdestination(Trame):
    ipdst = str(to_decimal(Trame[1][14])) + "." + str(to_decimal(Trame[1][15])) + "." + str(to_decimal(Trame[2][0])) + "." + str(to_decimal(Trame[2][1]))
    return ipdst

def tcpdstport(Trame):
    tcpdst = to_decimal(Trame[2][4] + Trame[2][5])
    return tcpdst

def tcpsrcport(Trame):
    tcpsrc = to_decimal(Trame[2][2] + Trame[2][3])
    return tcpsrc

def tcpflags(Trame):
    #return the different flags if they are set
    flags = to_decimal(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    if (flags[6] == '1'):
        res = "Urgent =" + " " + flags[6]
    if (flags[7] == '1'):
        res = "Ack =" + " " + flags[7]
    if (flags[8] == '1'):
        res = "Push =" + " " + flags[8]
    if (flags[9] == '1'):
        res = "Reset =" + " " + flags[9]
    if (flags[10] == '1'):  
        res = "Syn =" + " " + flags[10]
    if (flags[11] == '1'):
        res = "Fin =" + " " + flags[11]
    return res

def tcpflags2(Trame):
    #return the flags if they are set in a table
    flags = to_decimal(Trame[2][14][1]+Trame[2][15])
    flags = bin(flags)[2:].zfill(12)
    res = []
    if (flags[6] == '1'):
        res.append("URG")
    if (flags[7] == '1'):
        res.append("ACK")
    if (flags[8] == '1'):
        res.append("PSH")
    if (flags[9] == '1'):
        res.append("RST")
    if (flags[10] == '1'):
        res.append("SYN")
    if (flags[11] == '1'):
        res.append("FIN")
    return res


def tcplen(Trame):
    tcptotallen = to_decimal(Trame[1][0] + Trame[1][1]) - to_decimal(Trame[0][14][1])*4
    tcplen = tcptotallen - to_decimal(Trame[2][14][0])*4
    return tcplen

def tcpack(Trame):
    tcpack = to_decimal(Trame[2][10] + Trame[2][11] + Trame[2][12] + Trame[2][13])
    return tcpack

def tcpseq(Trame):
    tcpseq = to_decimal(Trame[2][6] + Trame[2][7] + Trame[2][8] + Trame[2][9])
    return tcpseq

def tcpWindow(Trame):
    tcpwindow = to_decimal(Trame[3][0] + Trame[3][1])
    return tcpwindow

def udpport(Trame):
    udpsrc = to_decimal(Trame[2][2] + Trame[2][3])
    return udpsrc

def methodhttp(Trame):
    #retourne la methode les elemetnts de Trame jusqu'a un saut de ligne
    res = ""
    i = 3
    j = 6
    while (Trame[i][j] != "0d"):
        if(i==len(Trame)-1):
            i=0
        if(j==len(Trame[i])-1):
            j=0
            i = i+1
        res = res + chr(to_decimal(Trame[i][j]))
        j = j + 1
    return res

"""
def extraction_flags_ip(flags_offset:str) -> tuple[str,str]:
    #function permettant de décortiquer la trame ip 
    return #le drapeau et l'offset 

#0000   f4 20 01 bb a2 f6 9e d7 64 df d3 13 50 10 02 02   . ......d...P...
#0010   c8 f8 00 00                                       ....

#Extraction de la trame ethernet en decimal 
def extraction_eth(trame)->Eth:
    print("voici la trame", trame)
    print("voici ce qu'il y a dans la trame[1]",trame[0])
    print("voici ce qu'il y a dans la trame[2]",trame[1])
    dest_addres = trame[1] +':'+ trame[2]+':'+ trame[3]+':'+ trame[4] +':'+ trame[5]+':'+ trame[6]
    src_addres = trame[7] +':'+  trame[8] +':'+ trame[9]+':'+  trame[10] +':'+  trame[11] +':'+ trame[12]
    type_eth = trame[13] + trame[14]

    return (dest_addres, src_addres,type_eth)


#taille d'une adresse IP = 20 octets
def extraction_ip(trame)-> Ip: 
    
    #version = trame[1]
    #header_length = trame[2]
    #protocol = trame[]
    #total_length = trame[]
    #identifier = trame[]
    #fragment_offset = trame[]
    #ttl = trame[]
    #flags = trame[]
    #flags, fragment_offset = extraction_flags_ip(fragment_offset)
    return (version, header_length, total_length, identifier, flags, fragment_offset, protocol, src_address, dest_address,options) 

def extraction_flags_ip(trame) ->ip_flags: 
    ip_flags = tuple[str,str]
    return ip_flags 



#creation de l'adress IP 
#fonction qui converti une adresse décimal en chaîne de caractère 
def address_IP(adress : int)->str: 
    return 


def extraction_tcp(trame)->tcp: 
    return #l'entête ip (header, ihl ...)


def extraction_flags_tcp(trame)->tcp_flags: 
    #SYN, FIN, RST, ACK, PSH, URG 
    return #les flags tcp 



#déclaration de booléen afin de définir le protocol encapsuler dans les trames 
def is_trame_ip(trame)-> bool:
    #trame ip trame[12:14]=['08','00']
    return (trame[12:14] == ['08','00'] and trame[14][0]=='4')


def is_trame_tcp(trame)->bool:
    #si le 23ème octet est 06 alors trame encapsule tcp 
    return trame[23] =='06'


def is_trame_http(trame)->bool: 
    #extraction de la trame tcp
    tcp = extraction_tcp(trame)

    #si addresse_source=80 (50 en hexa) ou addresse_dest=80 alors http 
    return(tcp[0] == '50' or tcp[1] =='50')

#hexadecimal -> decimal 
def to_decimal(a) :
    return int(a,base=16)
"""