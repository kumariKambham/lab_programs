import numpy as np
import matplotlib.pyplot as plt
import math
j=np.complex(0,1)
a=input("enter length of input")
x1=[]
for b in range(0,a):
	c=input("enter value")
	x1.append(c)
def DFT(x):
	N=1000
	w=np.linspace(-np.pi,np.pi,N)	
	y=[]
	for n in range(0,N):
		w_t=w[n]
		o=0			
		for k in range(0,a):
			o+=(x[k]*np.exp(-2*j*k*n*np.pi/N))
		y.append(o)
	return y
y1=DFT(x1)
m=np.abs(y1)
p=np.angle(y1)
plt.subplot(221)
plt.plot(x1)
plt.subplot(222)
plt.plot(y1)
plt.subplot(223)
plt.plot(m)
plt.subplot(224)
plt.plot(p)
plt.show()
