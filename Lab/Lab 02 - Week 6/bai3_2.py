import math
import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
sum = np.double(0)
for i in range(10, 1001, 10):
    temp = (3*i*math.log2(i) + 5)/math.pow(10,8)
    x.append(i)
    sum = sum + temp
    y.append(sum)

print("Tong thoi gian chay la:",sum)

x = np.array(x)
y = np.array(y)

plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Tong thoi gian chay chuong trinh ung voi N")
plt.show()