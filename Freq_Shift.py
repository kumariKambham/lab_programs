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
N=len(x1)
x2=[]
for m in range(N):
	d=x1[m]*(np.exp(-j*2*np.pi*m*5/N))
	x2.append(d)	
y1=DFT(x1)
y2=DFT(x2)
y3=[]
print(y2)
M=len(y2)
for u in range(0,M-5):
	y3.append(y2[u+5])
print(y3)
plt.subplot(221)
plt.plot(y1)
plt.subplot(222)
plt.plot(y2)
plt.subplot(223)
plt.plot(y3)
plt.show()
