import numpy as np
import time
import matplotlib.pyplot as plt


S = 200

def Kcapsack(n):
	start = time.time()
	V = np.zeros((n+1, S+1))
	w = np.random.choice(range(1001), size=n+1, replace=False)
	w[0] = 0
	v = np.random.randint(0, 501, size=n+1)
	v[0] = 0

	for i in range(1, n+1):
		for j in range(1, S+1):
			if(j < w[i]):
				V[i][j] = V[i-1][j]
			else:
				V[i][j] = max(V[i-1][j], V[i-1][j-w[i]] + v[i])

	i = n - 1
	j = S - 1
	solution_items = []

	#print("- Loi giai toi uu cua bai toan Knapsack chua {",end="")
	while ((i>0) and (j>0)):
		if(V[i][j]!=V[i-1][j]):
			solution_items.append(i)
			i = i-1
			j=j-w[i]
		else:
			i=i-1
	solution_items.reverse()
	#print(", ".join(map(str, solution_items)), end="")
	#print("}")
	return time.time() - start

time_list = np.zeros(20)

list_n = []
for n in range(50, 1050, 50):
	list_n.append(n)
	for i in range(0, 10):
		time_list[i] += Kcapsack(n)
	k = int((n-50)/50)
	time_list[k] /= 10
	print("- Voi n =",n,"thi t = ",time_list[k])

# Vẽ đồ thị
plt.plot(list_n,time_list)

# Thêm tiêu đề và nhãn
plt.title('Trung binh t theo n')
plt.xlabel('n')
plt.ylabel('t')

# Hiển thị đồ thị
plt.show()