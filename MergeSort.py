import time

import random
all_num = 10000
num = 5000
result = random.sample(range(1,all_num),num)
def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

def sorts(data):
    length = len(data)
    if length <= 1:
        return data

    mid = int(length / 2)
    a = sorts(data[:mid])
    b = sorts(data[mid:])

    return merge(a, b)

#a = [4, 6, 9, 3, 5, 1, 7, 0, 2, 8]
start = time.clock()
print(sorts(result))
end = time.clock()
print("run time is:%.010f seconds" % (end - start))
