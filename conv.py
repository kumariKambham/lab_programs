import numpy as np
import matplotlib.pyplot as plt
j=np.complex(0,1)
a=input("enter length of input")
a1=input("enter length of input")
N=a+a1-1
print(N)
x2=[]
x1=[]
for b in range(0,a):
	c=input("enter value")
	x1.append(c)
print(x1)
for b1 in range(0,a1):
	c1=input("enter value")
	x2.append(c1)
print(x2)
y=np.zeros(a+a1-1)
for i in range(0,N):
	for k in range(0,a):
		if((i-k)>=0 and (i-k)<=2):
			y[i]=y[i]+(x1[k]*x2[i-k])
plt.subplot(311)
plt.stem(x1)
plt.subplot(312)
plt.stem(x2)
plt.subplot(313)
plt.stem(y)
plt.show()
print(y)
