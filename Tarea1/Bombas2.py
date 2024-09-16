import math 

#Datos 
fv =3 #m3/s  
#fv=3e-3,4e-3,5,6,7,8e-3
rho= 1000  #kg/m3
g= 9.81  #m/s2
h= 40 #m
L= 1500 #m
d= 0.9 #m
visco=1e-6 #m²/s
epsilon=0.003 #m



#Calculos 1

s=math.pi*d**2/4
print("s=",s,"[m²]")
v=fv/s
print("v=",v,"m/2")
dph=rho*g*h 
Re=v*d/visco
print("Re=", Re)
if Re < 3000:
    f=64/Re
elif Re>3000:
    F=-1.8*math.log(6.9/Re+(epsilon/(3.7*d))**1.11,10)
    f=1/F**2
else:
    print ('ERROR')
    
print("Por lo tanto f=",f)
h=f*L*v**2/(2*d*g)
print("h=",h, "[m]")

P=rho*g*fv*h
print("P=",P, "[W]")

#Calculos 2

dr=0.86
epsilonr=0.04e-3 #m

sr=math.pi*dr**2/4
print("sr=",sr,"[m²]")
vr=fv/sr
print("vr=",vr,"m/2")
Rer=vr*dr/visco
print("Rer=",Rer)
if Rer < 3000:
    fr=64/Rer
elif Rer>3000:
    Fr=-1.8*math.log(6.9/Rer+(epsilonr/(3.7*dr))**1.11,10)
    fr=1/Fr**2
else:
    print ('ERROR')
print("Por lo tanto fr=",fr)

hr=fr*L*v**2/(2*dr*g)
print("h=",hr, "[m]")

Pr=rho*g*fv*hr
print("P=",Pr, "[W]")

Por=(P-Pr)/P

print("%=",Por)
