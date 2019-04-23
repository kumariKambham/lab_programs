import math
import numpy as np
import matplotlib.pyplot as plt
p=input("enter pass band amp")#0.707
s=input("enter stop band amp")#0.01
ws=input("enter stop band freq")#6282
wp=input("enter pass band freq")#3141
r=(1/(p*p))-1
q=(1/(s*s))-1
t=np.log(ws/wp)
x=0.5*np.log(r/q)
N=x/t
n=np.around(N)
n=np.abs(n)
print(n)
wc=(wp/((r)**(2*n)))
print(wc)
H=np.zeros(10000)
for i in range(0,10000):
	k=((i/wc)**(2*n))
	d=np.sqrt(1+k)
	H[i]=1/d
print(H)
plt.subplot(121)
plt.plot(H)
plt.show()
