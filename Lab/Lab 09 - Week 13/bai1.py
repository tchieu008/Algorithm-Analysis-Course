N = int(input("Nhap N:"))

def process(N):
	sum_n = 0
	while(N!=0):
		temp = N % 10
		N = N // 10
		sum_n += temp*temp
	return sum_n

list_check = []

while True:
	list_check.append(N)
	N = process(N)
	if(N in list_check):
		break	


for i in range(len(list_check)-1):
	print(list_check[i],end='->')
print(list_check[len(list_check)-1])
