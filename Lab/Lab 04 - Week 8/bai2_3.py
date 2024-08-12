import numpy as np
k=5
S = []
end = 101

count_sosanh = 0
count_gan = 1


def selectionSort(arr, count_sosanh, count_gan):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx]>arr[j]:
				min_idx=j
				count_gan+=1
			count_sosanh+=1
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		count_gan+=3
	return arr

for m in range(0, end):
	count_N=m
	check_scanned=False

	count_gan+=2

	while(check_scanned==False):
		count_sosanh+=1

		check_scanned=True
		j = np.random.randint(1, 1001)

		count_gan+=2
		for t in range(0, count_N):
			if (S[t] == j): 
				check_scanned = False
				count_gan += 1
			count_sosanh += 1
			break

	count_sosanh+=1
	S.append(j)
print("- Tap S co",end-1,"phan tu.")
print("+ Mang S ban dau:\n",S)
print("+ Sau khi sort S:\n",selectionSort(S, count_sosanh, count_gan))
print("+ Phan tu thu",k,"cua tap S la:",S[k-1])
print("+ So phep gan la:",count_gan)
print("+ So phep so sanh la:",count_sosanh)

