import numpy as np
import matplotlib.pyplot as plt
import math
j=np.complex(0,1)
a=input("enter length of input")
f=0
m=input("enter delay time")
x1=np.zeros(a+m)
x2=np.zeros(a+m)
for b in range(0,a):
	c=input("enter value")
	x1[b]=c
for d in range(m,a+m):
	x2[d]=x1[d-m]
print(x1)
print(x2)
def DFT(x):
	N=100
	w=np.linspace(-np.pi,np.pi,N)	
	y=[]
	print(m)
	for n in range(0,N):
		w_t=w[n]
		o=0			
		for k in range(0,a+m):
			o+=(x[k]*np.exp(-2*j*k*(n)*np.pi/N))
		y.append(o)
	return y
y1=DFT(x1)
y2=DFT(x2)
N=100
y3=[]
for i in range(N):
	g=0	
	g+=y1[i]*np.exp(-2*j*np.pi*i*m/N)
	y3.append(g)
plt.subplot(321)
plt.stem(x1)
plt.subplot(322)
plt.stem(y1)
plt.subplot(323)
plt.stem(x2)
plt.subplot(324)
plt.stem(y2)
plt.subplot(325)
plt.stem(y3)
plt.show()
