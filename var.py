def inter(nvbar):
    l=[]
    for i in range(2**nvbar):
        n=bin(i)[2:]
        n2=n[::-1]
        n2+="0"*(nvbar-len(n2))
        t=[]
        for j in range(len(n2)):
            if n2[j] == "0":
                t+=[False]
            else:
                t+=[True]
        l+=[tuple(t)]
    return l
    


def TV(FP,n):
    v=inter(n)
    l=[]
    for i in range(len(v)):
        V=v[i]
        r=eval(FP)
        l+=[(v[i]+(r,))]
    return l

#print(TV("V[0] and V[1]",2))
    
def Satisfaisable(FP,n):
    l=[]
    v=TV(FP,n)
    for i in range(len(v)):
        V=v[i]
        if V[-1]==True:
            l+=[V[:-1]]
    return l
print(inter(3))
print(TV('V[0] and V[1]', 2))
print(Satisfaisable("V[0] and V[1]",2))

        
    
    