import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import math
dp=input("enter dp:")
ds=input("enter ds:")
wp=input("enter wp:")
ws=input("enter ws:")
def cnx(N,x):
	if(x<1):
		c=np.cos(N*np.arccos(x))
	else:
		c=np.cosh(N*np.arccosh(x))
	return c
wp=wp*2*np.pi
ws=ws*2*np.pi
eps=(1/((dp*dp))-1)**0.5
print eps
y=(1/eps)*((1/(ds*ds)-1)**0.5)
x=ws/wp
N=1
while(1):
	r=cnx(N,x)
	if(r>=y):
		break
	N+=1
print N
w=np.linspace(0,6000*2*np.pi,1000)
h=np.zeros(1000)
for i in range(1000): 
	h[i]=1/(1+(eps*cnx(N,w[i]/wp))**2)**0.5
plt.plot(w/(2*np.pi),h)
plt.show()
