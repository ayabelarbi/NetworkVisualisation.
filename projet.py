import sys
import os


def lecture(file):
    #ouvre le fichier texte
    with open(file, "r+") as file:
        lines = [l for l in (line.strip() for line in file) if l]  # retire les lignes vides
        Trames = []
        Trame = []
        first = True
        for l in lines:
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
        #ferme le fichier
        file.close()
        return Trames




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

def flowgraph(Trames):
    for Trame in Trames:
        if(ipv4(Trame) and tcp(Trame) and http(Trame)):
            print("Couche la plus haute : HTTP")
            print(ipsource(Trame),"                                                                                       ",ipdestination(Trame))
            print("                                             ",methodhttp(Trame))
            print("   ",tcpsrcport(Trame),"------------------------------------------------------------------------------------------------->",tcpdstport(Trame))
        if(ipv4(Trame) and tcp(Trame) and not http(Trame)):
            print("Couche la plus haute : TCP")
            print(ipsource(Trame),"                                                                                       ",ipdestination(Trame))
            print("               ",tcpflags2(Trame),tcpflags(Trame), "Win =",tcpWindow(Trame),"Len =", tcplen(Trame),"Seq =",tcpseq(Trame),"Ack =",tcpack(Trame))
            print("   ",tcpsrcport(Trame),"------------------------------------------------------------------------------------------------->",tcpdstport(Trame))
            #print("Commentaire : ",tcpsrcport(Trame), " -> ", tcpdstport(Trame), tcpflags2(Trame),"Seq =",tcpseq(Trame), tcpflags(Trame), "Win =", tcpWindow(Trame), "Len =", tcplen(Trame))
        if(ipv4(Trame) and not tcp(Trame) and not http(Trame)):
            print("IP source", ipsource(Trame), "--------> IP destination", ipdestination(Trame))
        print("\n")
        
flowgraph(lecture(sys.argv[1]))
