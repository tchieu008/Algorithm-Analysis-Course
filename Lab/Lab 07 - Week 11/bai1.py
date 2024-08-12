import numpy as np
n=1236
#n = int(input("Nhap n: "))
level = n//10
x=0
#x = int(input("Nhap x: "))
A = np.random.randint(0, 10, size=n)
count=0

#print(A)
#print(sorted(A))

for i in A:
	if(i==x):
		count+=1
print("-Count: ",count)
print("-Level: ",level)
if(count>=level):
	print("=>",x,"la phan tu lan chiem cap do 10.")
else:
	print("=>",x,"khong la phan tu lan chiem cap do 10.")

