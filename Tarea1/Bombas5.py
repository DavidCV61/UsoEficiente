import math 

#Datos 

#fv=3e-3,4e-3,5,6,7,8e-3
rho= 983.3  #kg/m3
g= 9.81  #m/s2
h= 40 #m
L= 70 #m
d= 0.012 #m
mu=0.467e-3#kg/ms
epsilon=0.00005 #m
k=0.72
v=2


#Calculos

s=math.pi*d**2/4
print("s=",s,"[m]")
fv=s*v
print("Caudal=", fv)
dph=rho*g*h 
Re=rho*v*d/mu
print("Re=",Re)
if Re < 3000:
    f=64/Re
elif Re>3000:
    F=-1.8*math.log(6.9/Re+(epsilon/(3.7*d))**1.11,10)
    f=1/F**2
else:
    print ('ERROR')
    
print("Por lo tanto f=",f)
hf=f*(L*(v**2)/(2*d*g))
print("hf=",hf,"[m]")
hcodos=0.9*v**2/(2*g)*6
print("hcodos=",hcodos,"[m]")
hvalvulas=5*v**2/(2*g)*2
print("hvalvulas=",hvalvulas,"[m]")
ht=hf+hcodos+hvalvulas
print("ht=",ht,"[m]")
P=rho*g*fv*ht
print("P=",P,"[W]")
Pin=P/0.82
print("Pentrada=",Pin,"[W]")
