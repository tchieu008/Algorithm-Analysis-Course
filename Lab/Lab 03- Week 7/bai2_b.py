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
    return n,sep_up(stepdata_a,n,maxi_a),sep_down(stepdata_a,n,maxi_a),sep_up(stepdata_b,n,maxi_b),sep_down(stepdata_b,n,maxi_b)

def dequy(a,b):
    n,x1,y1,x2,y2=multidata(a,b)
    # print(n)
    print("step : search "+str(a)+"*"+str(b)+"??")
    print("C = "+x1+"*"+x2)
    print("D = "+y1+"*"+y2)
    print("E = ("+x1+"+"+y1+")*("+x2+"+"+y2+")="+str(int(x1)+int(y1))+"*"+str(int(x2)+int(y2))+"-C1-D1")
    print("\n")
    search=0
    if (max(int(x1),int(x2))>=10):
        dequy(int(x1),int(x2))
    if (max(int(y1),int(y2))>=10):
        dequy(int(y1),int(y2))
    if max(int(x1)+int(y1),int(x2)+int(y2))>=10:
        dequy(int(x1)+int(y1),int(x2)+int(y2))
    else:

        C=int(x1)*int(x2)
        D=int(y1)*int(y2)
        E=(int(x1)+int(y1))*(int(x2)+int(y2))-int(x1)*int(x2)-int(y1)*int(y2)
        search=C*10**(n*2)+E*10**n+D

a = int(input("Nhap a: "))
b = int(input("Nhap b:"))
#a=12345
#b=926182
dequy(a,b)
