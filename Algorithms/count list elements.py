def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1:])


a = [1, 2, 3]
print(length(a))
