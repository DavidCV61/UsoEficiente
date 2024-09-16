import math 

#Datos 
fv =4e-3 #m3/s  
#fv=3e-3,4e-3,5,6,7,8e-3
rho= 1000  #kg/m3
g= 9.81  #m/s2
h= 20+58#m
L= 420 #m
d= 0.05 #m
mu=0.00131 #kg/ms
epsilon=0.0015e-3 #m
k=12
n=1

#Calculos

s=math.pi*d**2/4
print("s=",s,"[m]")
v=fv/s
print("v=",v," [m/s]")
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
print("hf=",hf, " [m]")
hm=k*v**2/(2*g)
print("hm=",hm,"[m]")
htotal=hf+hm+h
print('htotal=',htotal,"m")
P=rho*g*fv*htotal/0.75
print("P=",P,"[W]")
