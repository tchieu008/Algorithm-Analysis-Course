import numpy as np
k=5
for i in range(10, 101, 10):
	S = sorted(np.random.choice(np.arange(1,1001), size=i, replace=False))
	print("- Tap S co",i,"phan tu.")
	print(S)
	print("Phan tu thu",k,"cua tap S la:",S[k-1])


