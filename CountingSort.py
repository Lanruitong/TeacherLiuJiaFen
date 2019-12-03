
A = [2, 4, 3, 1, 9, 8, 6, 3, 5, 7, 1, 0, 9, 3]
def count(list):
    C = []
    B = []
    for i in range(len(list)):
        B.append(0)
    for i in range(10):
        C.append(0)
    for j in range(len(list)):
        C[list[j]] = C[list[j]] + 1

    D = C[:]

    for i in range(1, len(C)):
        C[i] = C[i] + C[i - 1]


    for j in range(len(list)):
        B[ C[list[j]] - D[list[j]] ] = list[j]
        D[list[j]] -= 1
    return B
C = count(A)
print(C)

