import numpy as np
import matplotlib.pyplot as plt
import math
j=np.complex(0,1)
a=input("enter length of input")
f=0
x1=np.zeros(a)
x2=np.zeros(a)
for b in range(0,a):
	c=input("enter value")
	x1[b]=c
for d in range(0,a):
	x2[d]=x1[a-d-1]
print(x1)
print(x2)
def DFT(x):
	N=100
	w=np.linspace(-np.pi,np.pi,N)	
	y=[]
	for n in range(0,N):
		w_t=w[n]
		o=0			
		for k in range(0,a):
			o+=(x[k]*np.exp(-2*j*k*(n)*np.pi/N))
		y.append(o)
	return y
y1=DFT(x1)
y2=DFT(x2)
N=100
plt.subplot(321)
plt.stem(x1)
plt.subplot(322)
plt.stem(y1)
plt.subplot(323)
plt.stem(x2)
plt.subplot(324)
plt.stem(y2)
plt.subplot(325)
plt.show()
