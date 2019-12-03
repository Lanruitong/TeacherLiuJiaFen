
def f(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
num = eval(input("输入元素序号"))

for i in range(1,num+1):
    print(f(abs(i)))


