import numpy as np
n = 10
#n = int(input("Nhap n: "))

A = sorted(np.random.randint(0, 100, size=n))
B = sorted(np.random.randint(0, 100, size=n))

C = [0] * (2 * n)
i = j = k = 0

while i < n and j < n:
    if A[i] <= B[j]:
        C[k] = A[i]
        i += 1
    else:
        C[k] = B[j]
        j += 1
    k += 1

while i < n:
    C[k] = A[i]
    i += 1
    k += 1

while j < n:
    C[k] = B[j]
    j += 1
    k += 1

print("- Ma tran A:\n",A)
print("- Ma tran B:\n",B)
print("- Ma tran merge A va B:\n",C)
