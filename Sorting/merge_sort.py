from typing import List


def merge_sort(a: List) -> List:
    if len(a) > 1:
        print('Splitting', a)
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    print('merging', a)
    return a


print(merge_sort([1, 3, 5, 6, 2, 1, 5, 7, 3, 6]))
