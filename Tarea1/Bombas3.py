import math 

#Datos 
fv =18/1800 #m3/s  
#fv=3e-3,4e-3,5,6,7,8e-3
rho= 920  #kg/m3
g= 9.81  #m/s2
h= 40 #m
L= 25 #m
d= 0.04 #m
mu=0.045 #kg/ms
epsilon=0 #m
k=2.5


#Calculos

s=math.pi*d**2/4
print("s=",s,"[m]")
v=fv/s
print("v=",v,"[m/s]")
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
hf=f*L*v**2/(2*d*g)
print("hf=",hf,"[m]")
hm=2.5*v**2/(2*g)
print("hm=",hm,"[m]")
ht=hf+hm+5
print("ht=",ht,"[m]")
P=rho*g*fv*ht
print("P=",P,"[W]")
Pin=P/0.82
print("Pentrada=",Pin,"[W]")
