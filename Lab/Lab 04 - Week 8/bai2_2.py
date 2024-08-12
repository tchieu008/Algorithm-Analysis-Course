import numpy as np
k=5

def selectionSort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx]>arr[j]:
				min_idx=j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
	return arr

for i in range(10, 101, 10):
	S = []
	for m in range(0, i):
		count_N=m
		check_scanned=False
		while(check_scanned == False):
			check_scanned=True
			j = np.random.randint(1, 1001)
			for t in range(0, count_N):
				if (S[t] == j): 
					check_scanned = False
					break
		S.append(j)
	print("- Tap S co",i,"phan tu.")
	print("+ Mang S ban dau:\n",S)
	print("+ Sau khi sort S:\n",selectionSort(S))
	print("+ Phan tu thu",k,"cua tap S la:",S[k-1],"\n")

