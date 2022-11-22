def sumList(x, i=0):
    if i >= len(x):
        return 0
    return x[i] + sumList(x, i + 1)


print(sumList([1, 2, 3, 4]))
