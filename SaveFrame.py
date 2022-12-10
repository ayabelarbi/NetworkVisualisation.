import extraction

def saveFrame(trames):
    for trame in trames:
        if(extraction.ipv4(trame) and extraction.tcp(trame) and extraction.http(trame)):
            print("Couche la plus haute : HTTP")
            print(extraction.ipsource(trame),"\t"*12,extraction.ipdestination(trame))
            print("\t"*6,extraction.methodhttp(trame))
            print("   ",extraction.tcpsrcport(trame),"-"*100,">",extraction.tcpdstport(trame))
        if(extraction.ipv4(trame) and extraction.tcp(trame) and not extraction.http(trame)):
            print("Couche la plus haute : TCP")
            print(extraction.ipsource(trame),"\t"*12,extraction.ipdestination(trame))
            print("\t\t",extraction.tcpflags2(trame),extraction.tcpflags(trame), "Win =",extraction.tcpwindow(trame),"Len =", extraction.tcplen(trame),"Seq =",extraction.tcpseq(trame),"Ack =",extraction.tcpack(trame))
            print("  ",extraction.tcpsrcport(trame),"-"*100,">",extraction.tcpdstport(trame))
            #print("Commentaire : ",tcpsrcport(trame), " -> ", tcpdstport(trame), tcpflags2(trame),"Seq =",tcpseq(trame), tcpflags(trame), "Win =", tcpWindow(trame), "Len =", tcplen(trame))
        if(extraction.ipv4(trame) and not extraction.tcp(trame) and not extraction.http(trame)):
            print("IP source", extraction.ipsource(trame), "--------> IP destination", extraction.ipdestination(trame))
        print("\n")






