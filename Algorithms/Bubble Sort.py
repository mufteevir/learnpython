"""
Bubble sort is the simplest and slowest algorithm used for sorting.
It is designed in a way that the highest value in its list bubbles
its way to the top as the algorithm loops through iterations.
As its worst-case performance is O(N2)
"""
def bubble_sort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1] = list[idx+1],list[idx]
    return list

print(bubble_sort([25,21,22,24,23,27,26]))
