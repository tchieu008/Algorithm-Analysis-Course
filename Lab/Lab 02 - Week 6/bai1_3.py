import numpy as np
import time
def Check(N):
  start = time.time()
  A = sorted(np.random.choice(np.arange(1, 10001), size=N, replace=False))
  #print(A)

  x = int(50)
  count = 0

  for i in range(N):
    target = A[i]
    #temp = i
    while (i <= N):
      mid = int(i + (N-i)/2)
      if ((target == x - A[mid]) and (i != mid) ):
        #print("- Cap (i,j):",temp,mid)
        #print("  Voi gia tri la:",target, A[mid])
        #count+=1
        break
      elif (x-A[mid] < target):
        N = mid-1
      else:
        i = mid+1
  #if count == 0: print("Khong ton tai (i,j) thoa yeu cau bai toan")
  return float(time.time() - start)
total_time = 0.0

x=[]
y=[]
total = 0.0
for i in range(10, 1001, 10):
  #print("Với N = ",i)
  total += Check(i)
  x.append(i)
  y.append(total)

import matplotlib.pyplot as plt


x = np.array(x)
y = np.array(y)

plt.plot(x,y)

plt.xlabel('X')
plt.ylabel('Y')

plt.title("Thoi gian chay chuong trinh ung voi N")

plt.show()

