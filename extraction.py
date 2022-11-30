import re
import string
from tkinter.constants import NONE

from analyse import Ethernet

def Test_Offset(a) :
    if len(a)> 4 or a.isalpha():
        return False
    else :
        return True

def Extract_line(result,a,tab,l):
    tmp=[]
    for i in range(len(tab)):
        if len(tab[i])==2 and all(c in string.hexdigits for c in tab[i]) :
            tmp.append(tab[i])
    if len(tmp) >= a :
        for j in range(a):
            result.append(tmp[j])
    else :
        return "Error line "+str(l)
    return NONE

def Extract_final_line(result,tab) :
    line=Last_line(tab).split(' ')[1:]
    tmp=[]
    for i in range(len(line)):
        if len(line[i])==2 and all(c in string.hexdigits for c in line[i]) :
            tmp.append(line[i])
    for j in range(len(tmp)):
        result.append(tmp[j])

def No_empty(tab):
    tmp=[]
    for i in range(len(tab)):
        if not (tab[i]=='') :
            tmp.append(tab[i])
    return tmp
 
def Last_line(trame):
    i=1
    while (not Test_Offset(trame[len(trame)-i].split(' ')[0])):
        trame=trame[:i]
        i+=1
    return trame[len(trame)-1]

def Extract_Trame(trame):
    result =[]
    p_line=trame.split('\n')[0].split(' ')
    p_offset='0'
    tmp=No_empty(trame.split('\n')[1:])
    if tmp == [] :
        return p_line
    #print(tmp)
    for i in range(len(tmp)) :
        line=tmp[i].split(' ')
        offset=line[0]
        if not Test_Offset(offset) :
            continue
        diff = int(int(offset,16) - int(p_offset,16))
        error=Extract_line(result,diff,p_line,i+1)
        if error is not NONE : 
            return error
        p_line=line[1:]
        p_offset=offset
    Extract_final_line(result,tmp)
    return result

def Clean_file (trame_raw) :
    f = open("Trame_Clear.txt", "w")
    for i in trame_raw :
        trame_clean=Extract_Trame(i)
        p=int(trame_clean[16]+trame_clean[17],16)+14
        trame_clean=trame_clean[:p]
        if "Error line" not in trame_clean:
            for j in trame_clean:
                f.write(j)
                f.write(' ')
            f.write('\n\n')
    f.close