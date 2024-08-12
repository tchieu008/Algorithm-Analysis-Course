N = int(input("Nhap N: "))
sum = 0
count = -1

while(N!=0):
	count += 1
	sum = sum + (N%2)*pow(10, count)
	N = N//2
print(sum)


