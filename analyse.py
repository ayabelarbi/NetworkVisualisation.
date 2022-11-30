from tkinter import ttk
import tkinter as tk
from tkinter.constants import NONE, X, Y
from typing import AnyStr, Protocol

Type_val={'1':"A (Host adress) (1)",'2':"NS (Authoritative name server) (2)",'3':"MD (Mail destination) (3)",
    '4':"MF (Mail forwarder) (4)",'5':"CNAME (Canonical name for an alias) (5)",'6':"SOA (Start of a zone of authority) (6)",
    '7':"MB (Milbox domain name) (7)",'8':"MG (Mail group member) (8)",'9':"MR (Mail rename domain name) (9)",
    '10':"NULL (Null RR) (10)",'11':"WKS (Well known service description (11)",'12':"PTR (Domain name pointer) (12)",
    '13':"HINFO (Host information) (13)",'14':"MINFO (Mailbox or mail list information (14)",'15':"MX (Mail exchange) (15)",
    '16':"TXT (Text strings) (16)",'252':"AXFR (Transfer of an entire zone) (252)",'253':"MAILB (Mailbox-related records) (253)",
    '254':"MAILA (Mail agent RRs) (254)"}
class_val={'1':"IN (0x0001)",'2':"CS (0x0002)",'3':"CH (0x0003)",'4':"HS (0x0004)"}
name_dic={}
options= {'0':"Pad",'1':"Subnet Mask",'2':"Time Offset",'3':"Router",'4':"Time Server",'5':"Name Server",'6':"Domain Server",'7':"Log Server",'8':"Quotes Server",'9':"LPR Server",'10':"Impress Server",'11':"RLP Server",'12':"Hostname",'13':"Boot File Size",'14':"Merit Dump File",'15':"Domain Name",'16':"Swap Server",'17':"Root Path",'18':"Extension File",'19':"Forward On/Off",'20':"SrcRte On/Off",'21':"Policy Filter",'22':"Max DG Assembly",'23':"Default IP TTL",'24':"MTU Timeout",'25':"MTU Plateau",'26':"MTU Interface",'27':"MTU Subnet",'28':"Broadcast Address",'29':"Mask Discovery",'30':"Mask Supplier",'31':"Router Discovery",'32':"Router Request",'33':"Static Route",'34':"Trailers",'35':"ARP Timeout",'36':"Ethernet",'37':"Default TCP TTL",'38':"Keepalive Time",'39':"Keepalive Data",'40':"NIS Domain",'41':"NIS Servers",'42':"NTP Servers",'43':"Vendor Specific",'44':"NETBIOS Name Srv",'45':"NETBIOS Dist Srv",'46':"NETBIOS Node Type",'47':"NETBIOS Scope",'48':"X Window Font",'49':"X Window Manager",'50':"Address Request",'51':"Address Time",'52':"Overload",'53':"DHCP Msg Type",'54':"DHCP Server Id",'55':"Parameter List",'56':"DHCP Message",'57':"DHCP Max Msg Size",'58':"Renewal Time",'59':"Rebinding Time",'60':"Class Id",'61':"Client Id",'62':"NetWare/IP Domain",'63':"NetWare/IP Option",'64':"NIS-Domain-Name",'65':"NIS-Server-Addr",'66':"Server-Name",'67':"Bootfile-Name",'68':"Home-Agent-Addrs",'69':"SMTP-Server",'70':"POP3-Server",'71':"NNTP-Server",'72':"WWW-Server",'73':"Finger-Server",'74':"IRC-Server",'75':"StreetTalk-Server",'76':"STDA-Server",'77':"User-Class",'78':"Directory Agent",'79':"Service Scope",'80':"Rapid Commit",'81':"Client FQDN",'82':"Relay Agent Information",'83':"iSNS",'85':"NDS Servers",'86':"NDS Tree Name",'87':"NDS Context",'88':"BCMCS Controller",'89':"BCMCS Controller IPv4 address option",'90':"Authentication",'91':"client-last-transaction time option",'92':"associated-ip option",'93':"Client System",'94':"Client NDI",'95':"LDAP",'97':"UUID/GUID",'98':"User-Auth",
'99':"GEOCONF_CIVIC",'100':"PCode",'101':"TCode",'108':"IPv6-Only Preferred",'109':"OPTION_DHCP4O6_S46_SADDR",'112':"Netinfo Address",'113':"Netinfo Tag",'114':"DHCP Captive-Portal",'116':"Auto-Config",'117':"Name Service Search",'118':"Subnet Selection Option",'119':"Domain Search",'120':"SIP Servers DHCP Option",'121':"Classless Static Route Option",'122':"CCC",'123':"GeoConf Option",'124':"V-I Vendor Class",'125':"V-I Vendor-Specific Information",'128':"PXE - undefined (vendor specific)",'129':"Kernel options. Variable length string",'130':"PXE - undefined (vendor specific)",'131':"PXE - undefined (vendor specific)"	,'132':"PXE - undefined (vendor specific)",'133':"PXE - undefined (vendor specific)",'134':"Diffserv Code Point (DSCP) for VoIP signalling and media streams",'135':"PXE - undefined (vendor specific)",'136':"OPTION_PANA_AGENT",'137':"OPTION_V4_LOST",'138':"OPTION_CAPWAP_AC_V4",'139':"OPTION-IPv4_Address-MoS",'140':"OPTION-IPv4_FQDN-MoS",'141':"SIP UA Configuration Service Domains",'142':"OPTION-IPv4_Address-ANDSF",'143':"OPTION_V4_SZTP_REDIRECT",'144':"GeoLoc",'145':"FORCERENEW_NONCE_CAPABLE",'146':"RDNSS Selection",'147':"OPTION_V4_DOTS_RI",'148':"OPTION_V4_DOTS_ADDRESS",'150':"TFTP server address",'151':"status-code",'152':"base-time",'153':"start-time-of-state",'154':"query-start-time",'155':"query-end-time",'156':"dhcp-state",'157':"data-source",'158':"OPTION_V4_PCP_SERVER",'159':"OPTION_V4_PORTPARAMS",'161':"OPTION_MUD_URL_V4",'175':"Etherboot (Tentatively Assigned - 2005-06-23)",'176':"IP Telephone (Tentatively Assigned - 2005-06-23)",'177':"Etherboot (Tentatively Assigned -2005-06-23)",'208':"PXELINUX Magic",'209':"Configuration File",'210':"Path Prefix",'211':"Reboot Time",'212':"OPTION_6RD",'213':"OPTION_V4_ACCESS_DOMAIN",'220':"Subnet Allocation Option",'221':"Virtual Subnet Selection (VSS) Option",'224':"Private use",'225':"Private use",'226':"Private use",'227':"Private use",'228':"Private use",'229':"Private use",'230':"Private use",'231':"Private use",'232':"Private use",'233':"Private use",'234':"Private use",'235':"Private use",'236':"Private use",'237':"Private use",'238':"Private use",'239':"Private use",'240':"Private use",'241':"Private use",'242':"Private use",'243':"Private use",'244':"Private use",'245':"Private use",'246':"Private use",'247':"Private use",'248':"Private use",'249':"Private use",'250':"Private use",'251':"Private use",'252':"Private use",'253':"Private use",'254':"Private use",'255':"End"}


def lc(str) : #label counter
    j=0
    for i in str : 
        if i == ".":
            j+=1
    return j+1

def tds(b,i) : # to decimal string
    a=int(b,16)*i
    return str(a)

def tostring(a): 
    return str(a)

def hex_to_ascii(tab): #convertir des octets en chaine de caractere
    hex_string=""
    for i in tab :
        hex_string+=i
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode('utf-8')
    return ascii_string

def Datagram_IP(Trame,tab) :
    version = Trame[14][0]
    ihl = tds(Trame[14][1],4) +" Bytes ("+ tds(Trame[14][1],1 )+")"
    tos="0x"+Trame[15]
    tl=tds(Trame[16]+Trame[17],4)
    id="0x"+Trame[18]+Trame[19]+" ("+tds(Trame[18]+Trame[19],1)+")"
    fgs="0x"+Trame[20]+Trame[21]
    tmp=format(int(Trame[20]+Trame[21],16),"016b")
    rb=tmp[0]
    df=tmp[1]
    mf=tmp[2]
    tmp_off=int(tmp[3:],2)
    offset=tostring(tmp_off)
    ttl=tds(Trame[22],1)
    if Trame[23] == '01':
        prot="ICMP (1)"
    elif Trame[23] == '11':
        prot="UDP (17)"
    elif Trame[23] == '06':
        prot="TCP (6)"
    hc="0x"+Trame[24]+Trame[25]
    src=tds(Trame[26],1)+'.'+tds(Trame[27],1)+'.'+tds(Trame[28],1)+'.'+tds(Trame[29],1)
    dst=tds(Trame[30],1)+'.'+tds(Trame[31],1)+'.'+tds(Trame[32],1)+'.'+tds(Trame[33],1)
    rest=int(Trame[14][1],16) *4 -20
    if rest ==0 :
        return [version,ihl,tos,tl,id,fgs,rb,df,mf,offset,ttl,prot,hc,src,dst,rest]
    if Trame[34] == "07":
        type="Record Route"
    elif Trame[34] == "83":
        type="Loose Source Route"
    elif Trame[34] == "89":
        type="Strict Source Route"
    elif Trame[34] == "44":
        type="Time Stamp"
    op_len=tds(Trame[35],1)
    pointer=tds(Trame[36],1)
    if Trame[34] == "07" or "83" or "89" :
        for i in range(1,int(op_len,16)-2,4):
            str=tds(Trame[36+i],1)+'.'+tds(Trame[37+i],1)+'.'+tds(Trame[38+i],1)+'.'+tds(Trame[39+i],1)
            tab.append(str)
        return [version,ihl,tos,tl,id,fgs,rb,df,mf,offset,ttl,prot,hc,src,dst,rest,type,op_len,pointer]
    elif Trame[34] == "44":
        overflow=Trame[37][0]
        flag = Trame[37][1]
        for i in range ((op_len,16)-3,8):
            str=tds(Trame[37+i],1)+'.'+tds(Trame[38+i],1)+'.'+tds(Trame[39+i],1)+'.'+tds(Trame[40+i],1)
            tab.append(str)
            time=tds(Trame[41+i]+Trame[42+i]+Trame[43+i]+Trame[44+i],1)
            tab.append(time)
        return [version,ihl,tos,tl,id,fgs,rb,df,mf,offset,ttl,prot,hc,src,dst,rest,type,op_len,pointer,overflow,flag]
    
def Ethernet(Trame) :   
    dest = Trame[0]+':'+Trame[1]+':'+Trame[2]+':'+Trame[3]+':'+Trame[4]+':'+Trame[5]
    src = Trame[6]+':'+Trame[7]+':'+Trame[8]+':'+Trame[9]+':'+Trame[10]+':'+Trame[11]
    type = ''
    if Trame[12]+Trame[13] == '0800' :
        type = '0x0800 (IPv4)'
    elif Trame[12]+Trame[13] == '0806' :
        type = '0x0806 (ARP)'
    return [dest,src,type]
    
def Datagram_UDP (Trame) :
    debut=int(Trame[14][1],16)*4+14
    sp=tds(Trame[debut]+Trame[debut+1],1)
    dp=tds(Trame[debut+2]+Trame[debut+3],1)
    len="0x"+Trame[debut+4]+Trame[debut+5] + " ("+tds(Trame[debut+4]+Trame[debut+5],1) +" Bytes)"
    cs="0x"+Trame[debut+6]+Trame[debut+7]
    return [sp,dp,len,cs]

def DHCP(Trame,tab) :
    d=int(Trame[14][1],16)*4+22 #debut dhcp
    if Trame[d] == "01" :
        opcode = "Boot request (1)"
    elif Trame[d] == "02":
        opcode = "Boot reply (2)"
    else :
        opcode = "Error, wrong value"
    if Trame[d+1] =="01":
        ht="Ethernet (0x01)"
    else : ht=""
    hal=tds(Trame[d+2],1)
    hop=tds(Trame[d+3],1)
    tid="0x"+Trame[d+4]+Trame[d+5]+Trame[d+6]+Trame[d+7]
    nos=tds(Trame[d+8]+Trame[d+9],1)
    flag="0x"+Trame[d+10]+Trame[d+11]
    tmp=format(int(Trame[d+10]+Trame[d+11],16),"016b")
    bf=tmp[0]+"... .... .... ...."
    tp="Unicast"
    if tmp[0] == "1":
        tp="Brodcast"
    rf="."+tmp[1]+tmp[2]+tmp[3]+" "+tmp[4]+tmp[5]+tmp[6]+tmp[7]+" "+tmp[8]+tmp[9]+tmp[10]+tmp[11]+" "+tmp[12]+tmp[13]+tmp[14]+tmp[15]
    rf1=hex(int(tmp[1]+tmp[2]+tmp[3],2))+Trame[d+10][1]+Trame[d+11]
    cip=tds(Trame[d+12],1)+'.'+tds(Trame[d+13],1)+'.'+tds(Trame[d+14],1)+'.'+tds(Trame[d+15],1)
    yip=tds(Trame[d+16],1)+'.'+tds(Trame[d+17],1)+'.'+tds(Trame[d+18],1)+'.'+tds(Trame[d+19],1)
    sip=tds(Trame[d+20],1)+'.'+tds(Trame[d+21],1)+'.'+tds(Trame[d+22],1)+'.'+tds(Trame[d+23],1)
    gip=tds(Trame[d+24],1)+'.'+tds(Trame[d+25],1)+'.'+tds(Trame[d+26],1)+'.'+tds(Trame[d+27],1)
    cma=Trame[d+28]+':'+Trame[d+29]+':'+Trame[d+30]+':'+Trame[d+31]+':'+Trame[d+32]+':'+Trame[d+33]
    cmap=''
    for i in Trame[d+34:d+43]:
        cmap+=i
    test=0
    for i in Trame[d+44:d+107]:
        if i =="00":
            test+=1
    if test==len(Trame[d+44:d+107]):
        shn="not given"
    else :
        shn=hex_to_ascii(Trame[d+44:d+107])
    test=0
    for i in Trame[d+108:d+235]:
        if i =="00":
            test+=1
    if test==len(Trame[d+108:d+235]):
        bfn="not given"
    else :
        bfn=hex_to_ascii(Trame[d+108:d+235])
    mc="DHCP" #print (Trame[d+236:d+240])
    rest = int(Trame[16]+Trame[17],16)*4 +14- (d+240)
    if rest == 0 :
        return [opcode,ht,hal,hop,tid,nos,flag,tp,bf,rf,rf1,cip,yip,sip,gip,cma,cmap,shn,bfn,mc]
    do=d+240
    msg_type={'01':"Discover",'02':"Offer",'03':"Request",'05':"ACK",'07':"Release"}
    Item_list={}
    while (not (Trame[do]=="ff")):
        option="Option: ("+tds(Trame[do],1)+") "+options[tds(Trame[do],1)]
        tab.append(option)
        lg="Length: "+tds(Trame[do+1],1)
        tab.append(lg)
        if tds(Trame[do],1)=="53" :
            typ="DHCP: "+msg_type[Trame[do+2]]+" ("+Trame[do+2][1]+")"
            tab.append(typ)
        elif tds(Trame[do],1)=="61" :
            for i in range(1,int(Trame[do+1],16),7):
                hardt="Hardware type: Ethernet (0x01)"
                tab.append(hardt)
                cm="Client MAC adress: "+Trame[do+2+i]+":"+Trame[do+3+i]+":"+Trame[do+4+i]+":"+Trame[do+5+i]+":"+Trame[do+6+i]+":"+Trame[do+7+i]
                tab.append(cm)
        elif tds(Trame[do],1)=="54" :
            dsi="DHCP Server Identifier: "+tds(Trame[do+2],1)+'.'+tds(Trame[do+3],1)+'.'+tds(Trame[do+4],1)+'.'+tds(Trame[do+5],1)
            tab.append(dsi)
        elif tds(Trame[do],1)=="116" :
            ac="DHCP Auto-Configuration: DoNotAutoConfigure (0)"
            if tds(Trame[do+2],1)=="01":
                ac="DHCP Auto-Configuration: AutoConfigure (1)"
            tab.append(ac)
        elif tds(Trame[do],1)=="50" :
            rip="Resquested IP Adresse: "+tds(Trame[do+2],1)+'.'+tds(Trame[do+3],1)+'.'+tds(Trame[do+4],1)+'.'+tds(Trame[do+5],1)
            tab.append(rip)
        elif tds(Trame[do],1)=="12" :
            hn="Host Name: "+hex_to_ascii(Trame[do+2:do+2+int(Trame[do+1],16)])
            tab.append(hn)
        elif tds(Trame[do],1)=="60" :
            vci="Vendor class identifier: "+hex_to_ascii(Trame[do+2:do+2+int(Trame[do+1],16)])
            tab.append(vci)
        elif tds(Trame[do],1)=="1" :
            sm="Subnet Mask: "+tds(Trame[do+2],1)+'.'+tds(Trame[do+3],1)+'.'+tds(Trame[do+4],1)+'.'+tds(Trame[do+5],1)
            tab.append(sm)
        elif tds(Trame[do],1)=="3" :
            r="Router: "+tds(Trame[do+2],1)+'.'+tds(Trame[do+3],1)+'.'+tds(Trame[do+4],1)+'.'+tds(Trame[do+5],1)
            tab.append(r)
        elif tds(Trame[do],1)=="6" :
            for i in range(1,int(Trame[do+1],16),4):
                dom="Domain Name Server: "+tds(Trame[do+1+i],1)+'.'+tds(Trame[do+2+i],1)+'.'+tds(Trame[do+3+i],1)+'.'+tds(Trame[do+4+i],1)
                tab.append(dom)
        elif tds(Trame[do],1)=="15" :
            dn="Domain Name: "+hex_to_ascii(Trame[do+2:do+2+int(Trame[do+1],16)])
            tab.append(dn)
        elif tds(Trame[do],1)=="51" :
            time=int(Trame[do+2]+Trame[do+3]+Trame[do+4]+Trame[do+5],16)//86400
            ialt="IP Adress Lease Time: ("+tds(Trame[do+2]+Trame[do+3]+Trame[do+4]+Trame[do+5],1)+"s) "+str(time)+" day"
            tab.append(ialt)
        elif tds(Trame[do],1)=="55" :
            for i in range(1,int(Trame[do+1],16)+1):
                pr="Parameter Request List Item: ("+tds(Trame[do+1+i],1)+") "+options[tds(Trame[do+1+i],1)]
                tab.append(pr)
        tab.append(NONE)
        do=do+2+int(Trame[do+1],16)
    option="Option: (255) End"
    tab.append(option)
    oe="Option End: 255"
    tab.append(oe)
    rst=int(Trame[16]+Trame[17],16)+14 - do -1
    padding='' 
    if rst>20: 
        for i in range(20):
            padding+='00'
        padding+='....'
    else :
        for i in range(rst):
            padding+='00'
        
    return [opcode,ht,hal,hop,tid,nos,flag,tp,bf,rf,rf1,cip,yip,sip,gip,cma,cmap,shn,bfn,mc,padding]

def resource_records(dn,d,Trame,tab1):
    
        if Trame[dn]=="c0" or Trame[dn]=="C0" : 
            if int(Trame[dn+1],16) in name_dic :
                    name=name_dic[int(Trame[dn+1],16)]  
            else:
                tmp1=d+int(Trame[dn+1],16)
                tname=""
                for j in range(1,1+int(Trame[tmp1],16)):
                    tname+=hex_to_ascii(Trame[tmp1+j])
                name_dic[tmp1]=tname 
                name=tname 
            dn+=1
        else: 
            tmp=dn           
            name=""
            while (Trame[dn]!="00"):
                name+='.'
                for i in range(1,1+int(Trame[dn],16)):
                    name=name+hex_to_ascii(Trame[dn+i])
                dn+=1+int(Trame[dn],16)
            name=name[1:]
            name_dic[tmp-d]=name
        
        qname="Name: "+name
        type="Type: "+Type_val[tds(Trame[dn+1]+Trame[dn+2],1)]
        typ=tds(Trame[dn+1]+Trame[dn+2],1)
        clas="Class: "+class_val[tds(Trame[dn+3]+Trame[dn+4],1)]
        ttl="Time to live: "+tds(Trame[dn+5]+Trame[dn+6]+Trame[dn+7]+Trame[dn+8],1)
        dl="Data lenth: "+tds(Trame[dn+9]+Trame[dn+10],1)
        l=int(Trame[dn+9]+Trame[dn+10],16)
        title=name+": type "+Type_val[tds(Trame[dn+1]+Trame[dn+2],1)].split(' ')[0]+", class"+class_val[tds(Trame[dn+3]+Trame[dn+4],1)]
        dn=dn+11
        tab1.append(title)
        tab1.append(qname)
        tab1.append(type)
        tab1.append(clas)
        tab1.append(ttl)
        tab1.append(dl)

        if typ == "1":
            address="Adress: "+tds(Trame[dn],1)+"."+tds(Trame[dn+1],1)+"."+tds(Trame[dn+2],1)+"."+tds(Trame[dn+3],1)
            tab1.append(address)
            dn=dn+l

        elif typ == "2":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn<tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l    
            ns="Name server: "+cname
            tab1.append(ns)

        elif typ == "3":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn< tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            md="Mail destination: "+cname
            tab1.append(md)
            
        elif typ == "4":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn<tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            mf="Mail forwarder: "+cname
            tab1.append(mf)
            
        elif typ == "5":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00"):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            cn="CNAME: "+cname
            tab1.append(cn)
            
        elif typ == "6":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00"or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            pns="Primary name server: "+cname


            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            resp="Responsible name server: "+cname
            sn="Serial Number: "+tds(Trame[dn]+Trame[dn+1]+Trame[dn+2]+Trame[dn+3],1)
            ref="Refresh Interval: "+tds(Trame[dn+4]+Trame[dn+5]+Trame[dn+6]+Trame[dn+7],1)+"s"
            ret="Retry Interval: "+tds(Trame[dn+8]+Trame[dn+9]+Trame[dn+10]+Trame[dn+11],1)+"s"
            el="Expire limit: "+tds(Trame[dn+12]+Trame[dn+13]+Trame[dn+14]+Trame[dn+15],1)+"s"
            mtt="Minimum TTL: "+tds(Trame[dn+16]+Trame[dn+17]+Trame[dn+18]+Trame[dn+19],1)+"s"
            tab1.append(pns)
            tab1.append(resp)
            tab1.append(sn)
            tab1.append(ref)
            tab1.append(ret)
            tab1.append(el)
            tab1.append(mtt)
            dn=temp+l

        elif typ == "7":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            mb="Mailbox domain name: "+cname
            tab1.append(mb)
            dn=dn+l

        elif typ == "8":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            mg="Mail group member: "+cname
            tab1.append(mg)
            dn=dn+l

        elif typ == "9":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            mr="Mail rename domain name: "+cname
            tab1.append(mr)
            dn=dn+l

        elif typ == "10":
            null=''
            for f in Trame[dn:dn+l] :
                null+=f
            null="Null RR: "+null
            tab1.append(null)
            dn=dn+l

        elif typ == "11":
            address="Adress: "+tds(Trame[dn],1)+tds(Trame[dn+1],1)+tds(Trame[dn+2],1)+tds(Trame[dn+3],1)
            tab1.append(address)
            prot="Protocol: 0x"+Trame[dn+5]
            bm=''
            for f in Trame[dn+6:dn+l] :
                bm+=f
            bmap="Bit map:"+bm
            tab1.append(address)
            tab1.append(prot)
            tab1.append(bmap)
            dn=dn+l

        elif typ == "12":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            ptr="Pointer name: "+cname
            dn=tmp+l
            tab1.append(ptr)

        elif typ == "13":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            cpu="CPU: "+cname

            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            os="OS: "+cname
            tab1.append(cpu)
            tab1.append(os)
            dn=temp+l

        elif typ == "14":
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            rmail="RMAILBX: "+cname
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l ):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname        
            dn=tmp+l
            email="EMAILBX : "+cname
            tab1.append(rmail)
            tab1.append(email)

        elif typ == "15":
            pref="Preference: "+tds(Trame[dn]+Trame[dn+1],1)
            dn=dn+2
            tmp=dn
            cname=""
            index=int(Trame[dn+1],16)
            if Trame[dn] in {"C0","c0"} :
                tmp1=int(Trame[dn+1],16)+d
                while(Trame[tmp1]!="00"):
                    cname+='.'
                    if Trame[tmp1] in {"C0","c0"}:
                        if name_dic.get(int(Trame[tmp1+1],16)) is None :
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                cname=cname+hex_to_ascii(Trame[tmp1+i])
                            tmp1+=1+int(Trame[tmp1+d],16)
                        else: 
                            cname+=name_dic[int(Trame[tmp1+1],16)]
                            tmp1+=1
                            break
                    else:
                        for i in range(1,1+int(Trame[tmp1],16)) :
                            cname=cname+hex_to_ascii(Trame[tmp1+i])
                        tmp1+=1+int(Trame[tmp1],16)
                cname=cname[1:]
                name_dic[index]=cname
            else:
                while(Trame[dn]!="00" or dn < tmp+l ):
                    cname+='.'
                    if Trame[dn] in {"C0","c0"}:
                        tmp1=int(Trame[dn+1],16)+d
                        if name_dic.get(tmp1) is None :
                            temp=""
                            for i in range(1,1+int(Trame[tmp1],16)) :
                                temp+=hex_to_ascii(Trame[tmp1+i])
                            name_dic[tmp1-d]=temp
                            cname+=temp
                            dn+=1+int(Trame[tmp1],16)
                        else: 
                            cname+=name_dic[int(Trame[dn+1],16)]
                            dn+=1
                    else:
                        for i in range(1,1+int(Trame[dn],16)) :
                            cname=cname+hex_to_ascii(Trame[dn+i])
                        dn+=1+int(Trame[dn],16)
                cname=cname[1:]
                name_dic[index]=cname
            exc="Exchange: "+cname
            tab1.append(pref)
            tab1.append(exc)
            dn=dn+l

        elif typ == "16":
            txt=hex_to_ascii(Trame[dn:dn+l])
            tab1.append(txt)
            dn=dn+l
        
        tab1.append(NONE)
        return dn

def DNS(Trame,tab,tab1,tab2,tab3) :
    d=int(Trame[14][1],16)*4+22 #debut dns
    id= "Transaction ID: 0x"+Trame[d]+Trame[d+1]
    tmp=format(int(Trame[d+2]+Trame[d+3],16),"016b")
    flags ="Flags: 0x"+Trame[d+2]+Trame[d+3]
    if tmp[0] =="0" :
        qr="0... .... .... .... = Response: Message is a query"
    elif tmp[0] == "1":
        qr=" 1... .... .... .... = Response: Message is a response"
    if tmp[1]+tmp[2]+tmp[3]+tmp[4] == "0000" :
        opcode =".000 0... .... .... = Opcode: Standard query (0)"
    elif tmp[1]+tmp[2]+tmp[3]+tmp[4] == "0001" :
        opcode =".000 1... .... .... = Opcode: Inverse query (1)"
    elif tmp[1]+tmp[2]+tmp[3]+tmp[4] == "0010" :
        opcode =".001 0... .... .... = Opcode: Server status request (2)"
    elif tmp[1]+tmp[2]+tmp[3]+tmp[4] == "0100" :
        opcode =".010 0... .... .... = Opcode: Notfiy (4)"
    elif not (tmp[1]+tmp[2]+tmp[3]+tmp[4] == "0011") :
        opcode =".000 1... .... .... = Opcode: Reserved ("+str(int(tmp[1]+tmp[2]+tmp[3]+tmp[4],2))+")"
    if tmp[5]=="0":
        aa=".... .0.. .... .... = Authoritative: Server is not an authority for domain "
    else: 
        aa=".... .1.. .... .... = Authoritative: Server is an authority for domain "
    if tmp[6]=="0":
        tr=".... ..0. .... .... = Truncated: Message is not truncated"
    else:
        tr=".... ..1. .... .... = Truncated: Message is truncated"
    if tmp[7]=="1":
        rd=".... ...1 .... .... = Recusion desired: Do query recusively"
    else:
        rd=".... ...0 .... .... = Recusion desired: Do query iteratively"
    if tmp[8]=="1": 
        ra=".... .... 1... .... = Recursion available: Server can do recursive query"
    else:
        ra=".... .... 0... .... = Recursion available: Server can not do recursive query"
    if tmp[9]=="0":
        z=".... .... .0.. .... = Z: reserved (0)"
    else :
        z=".... .... .1.. .... = Z: reserved (1)"
    if tmp[10]=="0":
        aat=".... .... ..0. .... = Answer-authenticated: not authenticated by the server"
    else:
        aat=".... .... ..1. .... = Answer-authenticated: authenticated by the server"
    if tmp[11]=="0":
        an=".... .... ...0 .... = Non-authenticated data: Unacceptable"
    else:
        an=".... .... ...1 .... = Non-authenticated data: Acceptable"
    if tmp[12]+tmp[13]+tmp[14]+tmp[15] =="0000":
        rc=".... .... .... 0000 = Reply code: No error (0)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0001":
        rc=".... .... .... 0001 = Reply code: Format error (1)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0010":
        rc=".... .... .... 0010 = Reply code: Server failure (2)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0011":
        rc=".... .... .... 0011 = Reply code: Name error (3)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0100":
        rc=".... .... .... 0100 = Reply code: Not implemented (4)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0101":
        rc=".... .... .... 0101 = Reply code: Refused (5)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0110":
        rc=".... .... .... 0110 = Reply code: YXDomain (6)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "0111":
        rc=".... .... .... 0111 = Reply code: YXRRSet (7)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "1000":
        rc=".... .... .... 1000 = Reply code: NXRRSet (8)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "1001":
        rc=".... .... .... 1001 = Reply code: NotAuth (9)"
    elif tmp[12]+tmp[13]+tmp[14]+tmp[15] == "1010":
        rc=".... .... .... 1010 = Reply code: NotZone (10)"
    tq="Questions: "+tds(Trame[d+4]+Trame[d+5],1)
    anr="Answer RRs: "+tds(Trame[d+6]+Trame[d+7],1)
    aur="Authority RRs: "+tds(Trame[d+8]+Trame[d+9],1)
    adr="Additional RRs: "+tds(Trame[d+10]+Trame[d+11],1)
    dn=d+12
    
    i=0
    queries=int(Trame[d+4]+Trame[d+5],16)
    answers=int(Trame[d+6]+Trame[d+7],16)
    authority=int(Trame[d+8]+Trame[d+9],16)
    additional=int(Trame[d+10]+Trame[d+11],16)
    
    while(i<queries):
        if Trame[dn]=="c0" or Trame[dn]=="C0" : 
            name = name_dic[int(Trame[dn+1],16)-d]
            dn+=1
        else: 
            tmp=dn
            name=""
            while (Trame[dn]!="00"):
                name+='.'
                for i in range(1,1+int(Trame[dn],16)):
                    name=name+hex_to_ascii(Trame[dn+i])
                dn+=1+int(Trame[dn],16)
            name=name[1:]
            name_dic[tmp-d]=name
        qname="Name: "+name
        name_length="Name Length: "+ str(len(name))
        label_count="Label Count: "+ str(lc(name))
        #print(tds(Trame[dn+1]+Trame[dn+2],1))
        type="Type: "+Type_val[tds(Trame[dn+1]+Trame[dn+2],1)]
        clas="Class: "+class_val[tds(Trame[dn+3]+Trame[dn+4],1)]
        #print(Type_val[tds(Trame[dn+1]+Trame[dn+2],1)].split(' ')[0])
        title=name+": type "+Type_val[tds(Trame[dn+1]+Trame[dn+2],1)].split(' ')[0]+", class "+class_val[tds(Trame[dn+3]+Trame[dn+4],1)].split(' ')[0]
        tab.append(title)
        tab.append(qname)
        tab.append(name_length)
        tab.append(label_count)
        tab.append(type)
        tab.append(clas)
        tab.append(NONE)
        dn=dn+5
        i+=1 
    i=0
    while(i<answers):
        dn=resource_records(dn,d,Trame,tab1)
        i+=1
    i=0
    while(i<authority):
        dn=resource_records(dn,d,Trame,tab2)
        i+=1
    i=0
    while(i<additional):
        dn=resource_records(dn,d,Trame,tab3)
        i+=1   
    return [id,flags,qr,opcode,aa,tr,rd,ra,z,aat,an,rc,tq,anr,aur,adr]

def tree(frame,str) :
    tree=ttk.Treeview(frame)
    if "Error line" in str:
        error=tree.insert("",1,text=str+" : the number of hex to extract isn't enough ")
    else :
        p=int(str[16]+str[17],16)+14
        str=str[:p]
        Eth=Ethernet(str)
        Ethern=tree.insert("",1,text="Ethernet:")
        tree.insert(Ethern,"end",text="Destination: "+Eth[0])
        tree.insert(Ethern,"end",text="Source: "+Eth[1])
        tree.insert(Ethern,"end",text="Type: "+Eth[2])
        if str[12]+str[13] == '0800' :
            tab=[]
            iph=Datagram_IP(str,tab)
            ip=tree.insert("",2,text="Internet Protocol:")
            tree.insert(ip,"end",text="Version: "+iph[0])
            tree.insert(ip,"end",text="Header Length: "+iph[1])
            tree.insert(ip,"end",text="Type Of Service: "+iph[2])
            tree.insert(ip,"end",text="Total Length: "+iph[3])
            tree.insert(ip,"end",text="Identification: "+iph[4])
            flags=tree.insert(ip,"end",text="Flags: "+iph[5])
            if iph[6] =="0":
                tree.insert(flags,"end",text=iph[6]+"... .... .... .... = Reserved bit: Not set")
            else :
                tree.insert(flags,"end",text=iph[6]+"... .... .... .... = Reserved bit: Set")
            if iph[7] =="0":
                tree.insert(flags,"end",text="."+iph[7]+".. .... .... .... = Don't fragment: Not set")
            else :
                tree.insert(flags,"end",text="."+iph[7]+".. .... .... .... = Don't fragment: Set")
            if iph[8] =="0":
                tree.insert(flags,"end",text=".."+iph[8]+". .... .... .... = More fragments: Not set")
            else :
                tree.insert(flags,"end",text=".."+iph[8]+". .... .... .... = More fragments: Set")
            tree.insert(ip,"end",text="Fragment Offset: "+iph[9])
            tree.insert(ip,"end",text="Time to live: "+iph[10])
            tree.insert(ip,"end",text="Protocol: "+iph[11])
            tree.insert(ip,"end",text="Header checksum: "+iph[12])
            tree.insert(ip,"end",text="Source: "+iph[13])
            tree.insert(ip,"end",text="Destination: "+iph[14])
            if not (iph[15] == 0):
                options=tree.insert(ip,"end",text="Options: ("+tostring(iph[15])+"bytes), "+iph[16])
                option1=tree.insert(options,"end",text="IP Options - "+iph[16]+" ("+iph[17]+"bytes)")
                tree.insert(option1,"end",text="Type: "+tds(str[34],1))
                tree.insert(option1,"end",text="Length: "+iph[17])
                tree.insert(option1,"end",text="Pointer: "+iph[18])
                if str[34] == "44" :
                    tree.insert(option1,"end",text="Overflow: "+iph[19])
                    tree.insert(option1,"end",text="Flag: "+iph[20])
                    for i in range(0,len(tab),2) :
                        tree.insert(option1,"end",text="IP address: "+tab[i])
                        tree.insert(option1,"end",text="Time Stamp: "+tab[i+1]+"ms")
                else :
                    for i in tab :
                        tree.insert(option1,"end",text="Recorded Route: "+i)
                    option2=tree.insert(options,"end",text="IP Options - End of options List (EOL)")
                    tree.insert(option2,"end",text="Type: 0")
        if str[23]=="11":
            ud=Datagram_UDP(str)
            udp=tree.insert("",3,text="User Datagram Protocol:")
            tree.insert(udp,"end",text="Source Port: "+ud[0])
            tree.insert(udp,"end",text="Destination Port: "+ud[1])
            tree.insert(udp,"end",text="Length: "+ud[2])
            tree.insert(udp,"end",text="Checksum: "+ud[3])
            if ud[1]=="67" or ud[0]=="67":
                tab=[NONE]
                dhc=DHCP(str,tab)
                dhcp=tree.insert("",4,text="Dynamic Host Configuration Protocol: ")
                tree.insert(dhcp,"end",text="Opcode: "+dhc[0])
                tree.insert(dhcp,"end",text="Hardware type: "+dhc[1])
                tree.insert(dhcp,"end",text="Hardware adress length: "+dhc[2])
                tree.insert(dhcp,"end",text="Hops: "+dhc[3])
                tree.insert(dhcp,"end",text="Transaction ID: "+dhc[4])
                tree.insert(dhcp,"end",text="Seconds elapsed: "+dhc[5])
                boot=tree.insert(dhcp,"end",text="Bootp flags: "+dhc[6]+" ("+dhc[7]+")")
                tree.insert(boot,"end",text=dhc[8]+" = Brodcast flag: "+dhc[7])
                tree.insert(boot,"end",text=dhc[9]+" = Reserved flags: "+dhc[10])
                tree.insert(dhcp,"end",text="Client IP adress: "+dhc[11])
                tree.insert(dhcp,"end",text="Your (Client) IP adress: "+dhc[12])
                tree.insert(dhcp,"end",text="Next server IP adress: "+dhc[13])
                tree.insert(dhcp,"end",text="Relay agent IP adress: "+dhc[14])
                tree.insert(dhcp,"end",text="Client Mac adress: "+dhc[15])
                tree.insert(dhcp,"end",text="Client Hardware adress padding: "+dhc[16])
                tree.insert(dhcp,"end",text="Server host name: "+dhc[17])
                tree.insert(dhcp,"end",text="Boot file name: "+dhc[18])
                tree.insert(dhcp,"end",text="Magic Cookie: "+dhc[19])
                for i in range(1,len(tab)):
                    if tab[i] == NONE :
                        continue
                    if tab[i-1] == NONE:
                        option=tree.insert(dhcp,"end",text=tab[i])
                    else:
                        tree.insert(option,"end",text=tab[i])
                tree.insert(dhcp,"end",text="Padding: "+dhc[20])
            elif ud[1]=="53" or ud[0]=="53":
                tab=[NONE]
                tab1=[NONE]
                tab2=[NONE]
                tab3=[NONE]
                d=DNS(str,tab,tab1,tab2,tab3)
                dns=tree.insert("",4,text="Domain Name System:")
                tree.insert(dns,"end",text=d[0])
                flags=tree.insert(dns,"end",text=d[1])
                for i in d[2:12]:
                    tree.insert(flags,"end",text=i)
                tree.insert(dns,"end",text=d[12])
                tree.insert(dns,"end",text=d[13])
                tree.insert(dns,"end",text=d[14])
                tree.insert(dns,"end",text=d[15])
                if len(tab) > 1:
                    querie=tree.insert(dns,"end",text="Queries")
                    for i in range(1,len(tab)):
                        if tab[i] == NONE :
                            continue
                        if tab[i-1] == NONE:
                            option=tree.insert(querie,"end",text=tab[i])
                        else:
                            tree.insert(option,"end",text=tab[i])
                if len(tab1) > 1:
                    answer=tree.insert(dns,"end",text="Answers")
                    for i in range(1,len(tab1)):
                        if tab1[i] == NONE :
                            continue
                        if tab1[i-1] == NONE:
                            option=tree.insert(answer,"end",text=tab1[i])
                        else:
                            tree.insert(option,"end",text=tab1[i])
                if len(tab2) > 1:
                    autho=tree.insert(dns,"end",text="Authorities")
                    for i in range(1,len(tab2)):
                        if tab2[i] == NONE :
                            continue
                        if tab2[i-1] == NONE:
                            option=tree.insert(autho,"end",text=tab2[i])
                        else:
                            tree.insert(option,"end",text=tab2[i])
                if len(tab3) > 1:
                    additional=tree.insert(dns,"end",text="Additionals")
                    for i in range(1,len(tab3)):
                        if tab3[i] == NONE :
                            continue
                        if tab3[i-1] == NONE:
                            option=tree.insert(additional,"end",text=tab3[i])
                        else:
                            tree.insert(option,"end",text=tab3[i])
    tree.pack(fill='both',expand=True)


