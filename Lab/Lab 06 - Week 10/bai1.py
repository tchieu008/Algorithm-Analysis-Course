import numpy as np
n = 50
S = 200
V = np.zeros((n+1, S+1))


def print_matrix(matrix):
	n = matrix.shape[0]
	m = matrix.shape[1]
	for i in range(0, n):
		for j in range(0, m):
			print(int(matrix[i][j]),end=" ")
		print()

w = np.random.choice(range(501), size=n+1, replace=False)
w[0] = 0
print("-w:\n",w)
v = np.random.randint(0, 501, size=n+1)
v[0] = 0
print("-v:\n",v)

for i in range(1, n+1):
	for j in range(1, S+1):
		if(j < w[i]):
			V[i][j] = V[i-1][j]
		else:
			V[i][j] = max(V[i-1][j], V[i-1][j-w[i]] + v[i])
#print("- Bang kcapsack:")
#print_matrix(V)
print("- Max = ",int(V[n][S]))

i = n 
j = S 
solution_items = []

print("- Loi giai toi uu cua bai toan Knapsack chua {",end="")
while ((i>0) and (j>0)):
	if(V[i][j]!=V[i-1][j]):
		solution_items.append(i)
		i = i-1 
		j=j-w[i]
	else:
		i=i-1
solution_items.reverse()
print(", ".join(map(str, solution_items)), end="")
print("}")