import random
import numpy as np
def functionNk(N, k):
    arr=[]
    for i in range(N):
        arr.append(random.randint(1,k))
    # print(np.array(arr))
    return np.array(arr)

def cmpfuncN(a,b,k):
    for i in range(10,10010,10):
        print("index ",i)
        arr = functionNk(i, k)
        print("so sanh ", i)
        print("gan ",len(arr[(arr>=a)&(arr<=b)]))


def cmpfunck(a,b,N):
    for i in range(10,1000,10):
        print("index ",i)
        arr = functionNk(N, i)
        # if i==10:
        #     print(arr)
        print("so sanh ", N)
        print("gan ",len(arr[(arr>=a)&(arr<=b)]))


#case 1
a=40
b=70
k=100
cmpfuncN(a,b,k)

#case 2
a=40
b=70
N=20000
cmpfunck(a,b,N)