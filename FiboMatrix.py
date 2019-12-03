import numpy as np
def fiboMatrix(n):
    a = np.array([[1, 1], [1, 0]])
    b = np.array([[1, 0], [0, 1]])
    for i in range(1,n+1):
        b=b.dot(a.T)
    return b[0][1]
num = eval(input("第几个数"))
print(fiboMatrix(num-1))