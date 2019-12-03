def fab(n):
    a=0
    b=1
    if(n==1):
        return a
    elif(n==2):
        return 1
    else:
        for i in range(n-2):
            temp = a+b
            a=b
            b=temp
    return b
num = eval(input("第几个数"))

for i in range(1,num+1):
    print(fab(i))
