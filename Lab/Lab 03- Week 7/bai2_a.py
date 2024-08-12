def multidata(a,b):
    def maxidx(data):
        maxi=0
        assert data>=0, "a has to be more than zero!!\n"
        stepdata = []
        while(data>=10**maxi):
            stepdata.append(data%(10**(maxi+1))//10**(maxi))
            maxi+=1

        return stepdata, maxi
    def sep(a,b):
        stepdata_a, maxi_a = maxidx(a)
        stepdata_b, maxi_b = maxidx(b)
        n_a=maxi_a//2

        if n_a*2<maxi_a:
            n_a+=1
            maxi_a+=1
            stepdata_a.append(0)

        n_b=maxi_b//2

        if n_b*2<maxi_b:
            n_b+=1
            maxi_b+=1
            stepdata_b.append(0)

        if maxi_a>=maxi_b:
            n=n_a

            for i in range(maxi_a-maxi_b):
              stepdata_b.append(0)
            maxi_b=maxi_a
        else:
            n=n_b

            for i in range(maxi_b-maxi_a):
                stepdata_a.append(0)
            maxi_a=maxi_b
        return maxi_a, maxi_b, n_a, n_b, stepdata_a, stepdata_b, n

    def sep_up(stepdata,n,maxi):
        up=""
        for i in range(0,n):
            up+=str(stepdata[maxi-i-1])
        return up


    def sep_down(stepdata,n,maxi):
        down=""
        for i in range(n,maxi):
            down+=str(stepdata[maxi-i-1])
        return down
    maxi_a, maxi_b, n_a, n_b, stepdata_a, stepdata_b, n = sep(a,b)
    s=0
    for i in range(maxi_a):
        m=0
        print("step "+str(i+1))
        for j in range(maxi_a):
            print(int(stepdata_a[i])*int(stepdata_b[j])*10**(i+j))
            m+=int(stepdata_a[i])*int(stepdata_b[j])*10**(i+j)
        print("="+str(m))
        print()
        s+=m
    print("ket qua phuong phap 1 voi "+str(a)+"*"+str(b)+"="+str(s))
    # return n,sep_up(stepdata_a,n,maxi_a),sep_down(stepdata_a,n,maxi_a),sep_up(stepdata_b,n,maxi_b),sep_down(stepdata_b,n,maxi_b)

#a=123456
#b=926182
import random

def random_number_with_n_digits(n):
    lower_bound = 10 ** (n - 1)  # Lower bound inclusive
    upper_bound = 10 ** n - 1  # Upper bound inclusive
    return random.randint(lower_bound, upper_bound)
for i in range(10,33):
    a = random_number_with_n_digits(i)
    b = random_number_with_n_digits(i)
    multidata(a,b)
multidata(a,b)
