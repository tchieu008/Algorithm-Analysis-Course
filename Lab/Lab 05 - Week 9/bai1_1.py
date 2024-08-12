import numpy as np

n = int(input("Input n: "))

A = np.random.randint(1, 1001, size=(n,n))
B = np.random.randint(1, 1001, size=(n,n))
C = np.zeros((n,n), dtype=int)

print("- Matrix A is:\n",A)
print("- Matrix B is:\n",B)
print("- Matrix C is:\n",C)

for i in range(0,n):
	for j in range(0,n):
		for k in range(0,n):
			C[i][j] += A[i][k]*B[k][j]
print("- Matrix C=A*B is:\n",C)

