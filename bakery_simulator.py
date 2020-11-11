import numpy as np

def MAX(dot,PriceX,PriceY) :
    return PriceX*dot[0]+PriceY*dot[1]

def solver(PriceX,PriceY,LimitA,LimitB,Ax,Ay,Bx,By) :
    
    #calcul du point minimal sur l'axe X
    MinXA=LimitA/Ax
    MinXB=LimitB/Bx
    MinX=(min(MinXA,MinXB),0)

    #calcul du point minimal sur l'axe Y
    MinYA=LimitA/Ay
    MinYB=LimitB/By
    MinY=(0,min(MinYA,MinYB))
    
    #calcul du point d'intersection

    InterX=(MinYB-MinYA)/((MinYB/MinXB)-(MinYA/MinXA))
    Inter=(InterX,-(MinYB/MinXB)*InterX+MinYB)
    
    print ("Les trois points retenus sont "+str(MinX)+ " " +str(MinY)+ " " +str(Inter))
    print ("Les prix de ces points sont "+str(MAX(MinX,PriceX,PriceY))+" "+str(MAX(MinY,PriceX,PriceY))+" "+str(MAX(Inter,PriceX,PriceY)))

    listPoint=[MinX, MinY, Inter]
    listPointPrix=[MAX(MinX,PriceX,PriceY),MAX(MinY,PriceX,PriceY),MAX(Inter,PriceX,PriceY)]

    best=max(range(len(listPointPrix)), key=listPointPrix.__getitem__)

    print ("La meilleure solution est "+str(listPoint[best]))

solver(1,1.5,10,12,1,1.5,2,1)
