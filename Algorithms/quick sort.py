def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]#Recursive Case
        less = [i for i in array[1:] if i <= pivot] #Subarray of all elements,smaller reference
        greater = [i for i in array[1:] if i > pivot]  #Subarray of all elements,bigger reference
        return quicksort(less) + [pivot] + quicksort(greater)#recursiion


print(quicksort([3, 5, 1, 10, 2]))
