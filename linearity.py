import numpy as np
import matplotlib.pyplot as plt
import math
j=np.complex(0,1)
a=input("enter length of input")
x1=[]
for b in range(0,a):
	c=input("enter value")
	x1.append(c)
a1=input("enter length of input")
x2=[]
for b1 in range(0,a1):
	c1=input("enter value")
	x2.append(c1)
x3=[]
for m in range(0,a):
	p=x1[m]+x2[m]
	x3.append(p)
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
y2=DFT(x2)
y3=DFT(x3)
y4=[]
N=1000
for e in range(0,N):
	f=y1[e]+y2[e]
	y4.append(f)
plt.subplot(321)
plt.plot(x1)
plt.subplot(322)
plt.plot(y1)
plt.subplot(323)
plt.plot(x2)
plt.subplot(324)
plt.plot(y2)
plt.subplot(325)
plt.plot(y4)
plt.subplot(326)
plt.plot(y3)
plt.show()
