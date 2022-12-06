from parsing import lecture 

Eth=tuple[str,str,str] #adress dest, adress src, type 
Ip=tuple[str,str,str,str,str,str,str,str,str,str,str]
ip_flags=tuple[str,str]
tcp= tuple[str,str,str,str,str,str,str,str,str]
tcp_flags= tuple[str,str,str,str,str,str]


def extraction_flags( offset:str) -> tuple[str,str]:
    #function permettant de décortiquer la trame ip 
    return #le drapeau et l'offset 



#Extraction de la trame ethernet en decimal 
def extraction_eth(trame)->Eth:
    return #entête eth 


#taille d'une adresse IP = 20 octets
def extraction_ip(trame)-> Ip: 

    return #l'entête ip (header, ihl ...)

def extraction_flags_ip(trame) ->ip_flags: 
    return 




#creation de l'adress IP 
#fonction qui convertie une adresse décimal en chaîne de caractère 
def address_IP(adress : int)->str: 
    return 


def extraction_tcp(trame)->Tcp: 
    return #l'entête ip (header, ihl ...)

def extraction_flags_tcp(trame)->tcp_flags: 
    return #les flags tcp 



#déclaration de booléen afin de définir le protocol encapsuler dans les trames 
def is_trame_ip(trame)-> bool:
    #trame ip trame[12:14]=['08','00']
    return 

def is_trame_tcp(trame)->bool:
    #trame tcp si trame[23] = "06"
    #23ème octet de la trame annonce si la trame est un tcp 
    return #booleen 

def is_trame_http(trame)->bool: 
    #extraction de la trame tcp
    # si le port dest ou port src = 80 alors tcp encapsule http 

    #tcp[1] ou tcp[0] = 50 (cf wireshark)
    return #booleen 