import matplotlib.pyplot as plt
import numpy as np
import math as mt


x=np.arange(1,10000,1)


y1=[1]*len(x)
y2=x
y3=[pow(x1,2) for x1 in x]
y4=[mt.log(x1,2) for x1 in x]
y5=[x1*mt.log(x1,2) for x1 in x]
y6=[pow(x1,2)*mt.log(x1,2) for x1 in x]
y7=[x1*pow(mt.log(x1,2),2) for x1 in x]
y8=[pow(x1,3) for x1 in x]
y9=[pow(1.01,x1) for x1 in x]

y10=[2]*len(x)
y11=[2*x1 for x1 in x]
y12=[2*pow(x1,2) for x1 in x]
y13=[2*mt.log(x1,2) for x1 in x]
y14=[2*x1*mt.log(x1,2) for x1 in x]
y15=[2*pow(x1,2)*mt.log(x1,2) for x1 in x]
y16=[2*x1*pow(mt.log(x1,2),2) for x1 in x]
y17=[2*pow(x1,3) for x1 in x]
y18=[pow(2,x1) for x1 in x]

y19=[1000]*len(x)
y20=[1000*x1 for x1 in x]
y21=[1000*pow(x1,2) for x1 in x]
y22=[1000*mt.log(x1,2) for x1 in x]
y23=[1000*x1*mt.log(x1,2) for x1 in x]
y24=[1000*pow(x1,2)*mt.log(x1,2) for x1 in x]
y25=[1000*x1*pow(mt.log(x1,2),2) for x1 in x]
y26=[1000*pow(x1,3) for x1 in x]
y27=[pow(10,x1) for x1 in x]

plt.plot(x,y1,label="1")
plt.plot(x,y2,label="n")
plt.plot(x,y3,label="n^2")
plt.plot(x,y4,label="log(n)")
plt.plot(x,y5,label="nlog(n)")
plt.plot(x,y6,label="(n^2)log(n)")
plt.plot(x,y7,label="n(log(n)^2)")
plt.plot(x,y8,label="n^3")
#plt.plot(x,y9,label="1.01^n")
plt.plot(x,y10,label="2")
plt.plot(x,y11,label="2n")
plt.plot(x,y12,label="2n^2")
plt.plot(x,y13,label="2log(n)")
plt.plot(x,y14,label="2nlog(n)")
plt.plot(x,y15,label="2(n^2)log(n)")
plt.plot(x,y16,label="2n(log(n)^2)")
plt.plot(x,y17,label="2n^3")
#plt.plot(x,y18,label="2^n")
plt.plot(x,y19,label="1000")
plt.plot(x,y20,label="1000n")
plt.plot(x,y21,label="1000n^2")
plt.plot(x,y22,label="1000log(n)")
plt.plot(x,y23,label="1000nlog(n)")
plt.plot(x,y24,label="1000(n^2)log(n)")
plt.plot(x,y25,label="1000n(log(n)^2)")
plt.plot(x,y26,label="1000n^3")
#plt.plot(x,y27,label="1000^n")
plt.legend()
plt.show()


# In[ ]:



