import parsing 

#Tuple des protocol
Eth=tuple[str,str,str] #adress dest, adress src, type 
Ip=tuple[str,str,str,str,str,str,str,str,str,str,str]
ip_flags=tuple[str,str]
tcp= tuple[str,str,str,str,str,str,str,str,str]
tcp_flags= tuple[str,str,str,str,str,str]


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


#def test_extraction_eth(trame)-> Eth: 
#    extraction_eth(trame)


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
