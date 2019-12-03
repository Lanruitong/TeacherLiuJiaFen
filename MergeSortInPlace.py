import time
import random
all_num = 10000
num = 5000
result = random.sample(range(1,all_num),num)
#A = [4, 6, 9, 7, 3, 5, 1, 0, 8, 2]


def swap(X, f, r):
    temp = X[f]
    X[f] = X[r]
    X[r] = temp


def reverse(X, head, tail):
    while head < tail:
        swap(X, head, tail)
        head = head + 1
        tail = tail - 1


def exchange(X, index, head, tail):
    reverse(X, head, index)
    reverse(X, index + 1, tail)
    reverse(X, head, tail)


def merge_in(X, head, tail):
    f = head
    mid = (head + tail) // 2
    r = mid + 1
    temp_r = 0
    while f < r and r <= tail:
        while f < r and X[f] <= X[r]:
            f = f + 1
        temp_r = r
        while r <= tail and X[r] < X[f]:
            r = r + 1
        exchange(X, temp_r - 1, f, r - 1)
        f = f + r - temp_r
    return


def mergesort(X, head, tail):
    if (tail - head) == 0:
        return
    else:
        mid = (tail + head) // 2
        mergesort(X, head, mid)
        mergesort(X, mid + 1, tail)
        return merge_in(X, head, tail)


start = time.clock()
mergesort(result, 0, len(result) - 1)
end = time.clock()
print(result)

print("run time is:%.010f seconds" % (end - start))
