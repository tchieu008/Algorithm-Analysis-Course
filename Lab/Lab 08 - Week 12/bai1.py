f_0 = 'abc'
f_1 = 'def'
k = -1
while(k<=0):
	k = int(input("Nhap k (k>=1): "))

def fibonacci(n):
	if(n==0):
		return 'abc'
	if(n==1):
		return 'def'
	else:
		return fibonacci(n-1) + fibonacci(n-2)

temp = 0
a = 0
b = 3
n = 0
while(k>temp):
	temp = a + b
	a = b
	b = temp
	n += 1
if(k<=3):
	n-=1

print("- k la:",k)
print("- n la:",n)
print("- Chuoi:",fibonacci(n))
print("- Ky tu thu",k,"la:",fibonacci(n)[k-1])
