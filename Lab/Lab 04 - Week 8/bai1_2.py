import numpy as np
def search_x_in_A(A, x):
	save = []
	for index, value in enumerate(A):
		if(value == x):
			save.append(index)
	if save: return save
	else: return "Khong co gia tri nao"

end_range = 10001
x = np.random.randint(0,end_range)
print("x ngau nhien la:",x)

for i in range(10, end_range, 10):
	A = sorted(np.random.randint(0,end_range,i))
	print("- Mang A co",i,"phan tu.")
	print(search_x_in_A(A,x))

