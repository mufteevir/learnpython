"""
 it is based on a divide and conquer strategy.
 In the first phase, called splitting,
 the algorithm keeps on dividing the data into two parts recursively,
 until the size of the data is less than the defined threshold.
 In the second phase, called merging,
 the algorithm keeps on merging and processing until we get the final result.
"""


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2  # split list in half
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)  # repeats until lenght of each list is 1
        merge_sort(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    return list


print(merge_sort([25, 21, 22, 24, 23, 27, 26]))
