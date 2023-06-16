import numpy as np
A=[3,4,5]

for a in A:

    print(a)

print(np.dot(np.array([1,-1]),np.array([1,1])))

print(np.array([[1,2],[3,4],[5,6],[7,8]]))

a=np.array([0,1,0,1,0])

b=np.array([1,0,1,0,1])

print(a*b)

a=np.array([0,1])

b=np.array([1,0])

print(np.dot(a,b))

A = ((11, 12), [21, 22])

print(A[0][1])

print('1,2,3,4'.split(','))

V={'A','B'}
V.add('C')
print(V)
