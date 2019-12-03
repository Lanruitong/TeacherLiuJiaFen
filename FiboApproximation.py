from FiboIterative import fab

fi = (1+5**0.5)/2
def fibo(n):
    return fi**n/(5**0.5)
num = eval(input("第几个数"))
for i in range(num):
    print(fibo(i)-fab(i+1))
#Answer1:
#递归算法大约需要跑12000s也就是三个多小时
#迭代算法仅需要跑0.001s

#Answer2:
#前面40项的偏差都较小并逐渐减小，直到40项左右误差最小大为E-8数量级
#后面的项误差将会越来越大一直增到到E+27数量级
#在第200项的误差已经达到了1.160568786830044e+27