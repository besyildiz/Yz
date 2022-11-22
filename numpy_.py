import numpy as np

x=np.array([1,2,3])
y=np.array([4,5,6])
t=np.concatenate([x,y])
print(t)
"""z=np.array([7,8,9])
t=np.concatenate([[4,5,6],z])
"""

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
c=np.concatenate([a,b])



print(c)
d=np.concatenate([a,b],axis=0)
print(d)


x=np.array([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
#np.split(x,3)
#print(np.split(x,3))

print(np.split(x,[2,6]))
 
a,b,c=np.split(x,[2,6])

y=np.arange(16).reshape(4,4)
print(y) 

f,g=np.hsplit(y,2)
print(f,g) 

f,g=np.vsplit(y,2)
print(f,g) 

import numpy as np
x=np.arange(0,11)
print(x) 

print(x+5)
print(x-10)
print(x/2)
print(x*3)
print(x**2)

a=np.array([10,20,30])
b=np.array([1,2,3])

np.add(a,5)
np.add(a,b)

np.subtract(a,5)
np.subtract(a,b)

np.multiply(a,5)
np.multiply(a,b)

np.power(a,2)
np.power(a,b)









