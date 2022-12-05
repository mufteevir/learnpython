def sumList(x, i=0):
    if i >= len(x):
        return 0
    f =  x[i] + sumList(x, i + 1)
    return f

x = sumList([1, 2, 3, 4])
print(x)
