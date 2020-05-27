def quick_sort_memory(arr):
    """Sort the array by using quicksort.
       With extra memory. One loop
    """
    if len(arr) <= 1:
        return

    privot = arr[0]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < privot:
            less.append(x)
        elif x > privot:
            greater.append(x)
        else:  # x == privot
            equal.append(x)
    quick_sort_memory(less)
    quick_sort_memory(greater)
    arr[:] = less[:] + equal[:] + greater[:]


def quick_sort_em_gen(arr):
    """Sort the array by using quicksort.
       With extra memory. Generators more pythonist style
    """
    if len(arr) <= 1:
        return

    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    qreater = [x for x in arr if x > pivot]
    equial = [x for x in arr if x == pivot]
    quick_sort_em_gen(less)
    quick_sort_em_gen(qreater)
    arr[:] = less + equial[:] + qreater


def quick_sort_no_em(arr, lft=0, rgt=None):
    rgt = rgt or len(arr) - 1
    if lft >= rgt:
        return

    i = lft
    j = rgt
    pivot = arr[lft + (rgt - lft) // 2]

    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quick_sort_no_em(arr, lft, j)
    quick_sort_no_em(arr, i, rgt)


a = [1, 2, 5, 2, 3, 9, 9, 0, 1]
quick_sort_memory(a)
print('test #1', 'ok' if a == [0, 1, 1, 2, 2, 3, 5, 9, 9] else 'failed')

a = [1, 2, 5, 2, 3, 9, 9, 0, 1]
quick_sort_em_gen(a)
print('test #2', 'ok' if a == [0, 1, 1, 2, 2, 3, 5, 9, 9] else 'failed')

a = [1, 2, 5, 2, 3, 9, 9, 0, 1]
quick_sort_no_em(a)
print('test #3', 'ok' if a == [0, 1, 1, 2, 2, 3, 5, 9, 9] else 'failed')
