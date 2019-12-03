import random
import time
all_num = 10000
num = 5000
result = random.sample(range(1,all_num),num)

def partition(A, p, q):
    x = A[p]  # pivot
    i = p
    for j in range(p + 1, q+1):
        if (A[j] <= x):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i


def quick_sort(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        quick_sort(arr, l, q - 1)
        quick_sort(arr, q + 1, r)


#a = [4, 6, 9, 3, 5, 1, 7, 0, 2, 8]
start = time.clock()
quick_sort(result, 0, len(result) - 1)
end = time.clock()
print(result)
print("run time is:%.010f seconds" % (end - start))
