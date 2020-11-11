import numpy as np

def fonctionMax(c,p,pc,pp) :
    return pc*c+pp*p

def meilleurPrix(Pc,Pp,F,B,Fc,Fp,Bc,Bp) :
    x=min(F/Fc,B/Bc)
    y=min(F/Fp,F/Bp)
    i=B/Bp
    j=F/Fp
    k=B/Bc
    l=F/Fc

    s1=i/k
    s2=j/l

    monX=(i-j)/(s1-s2)

    
    print ([(x,0),
            (0,y),
            (monX,-s2*monX+j)
             ])

    
    print ([fonctionMax(x,0,Pc,Pp),
            fonctionMax(0,y,Pc,Pp),
            fonctionMax(monX,-s2*monX+j,Pc,Pp)
             ])



print (np.pi)     
meilleurPrix(1,1.5,10,15,1,1.5,1.7,2.5)
