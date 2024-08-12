import numpy as np
def Check(n):
  A = sorted(np.random.choice(np.arange(1, 10001), size=n, replace=False))
  #print(A)

  x = int(50)
  count = 0
  for i in range(n):
    target = A[i]
    temp = i
    while (i <= n):
      mid = int(i + (n-i)/2)
      if ((target == x - A[mid]) and (temp != mid) ):
        print("- Cap (i,j):",temp,mid)
        print("  Voi gia tri la:",target, A[mid])
        count+=1
        break
      elif (x-A[mid] < target):
        n = mid-1
      else:
        i = mid+1
  if count == 0: print("Khong ton tai (i,j) thoa yeu cau bai toan")

for i in range(10, 1001, 10):
  print("Với N = ",i)
  Check(i)