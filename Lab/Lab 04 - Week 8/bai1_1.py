import numpy as np
def search_x_in_A(A, x):
	save = []
	for index, value in enumerate(A):
		if(value == x):
			save.append(index)
	if save: return save
	else: return "Khong co gia tri nao"

x=10
N = 1000

A = sorted(np.random.randint(0,1001,N))
print("- Mang A co",N,"phan tu.")
print(A)
print(search_x_in_A(A,x))

