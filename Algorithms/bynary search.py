def binary_search(list, item):
    low = 0
    high = len(list) - 1 #low and high - limits for searching
    while low <= high: #while list is more than 1
        mid = (low + high) // 2 #check middle element
        guess = list[mid]
        if guess == item: #value found
            return mid
        elif guess > item:#guess>value=>change high limit
            high = mid - 1
        else:             #guess<value=>change low limit
            low = mid + 1
    return None


mylist = [1, 3, 5, 7, 9]

print(binary_search(mylist, 5))
print(binary_search(mylist, 9))
print(binary_search(mylist, 1))
print(binary_search(mylist, 23))
