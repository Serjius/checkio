def binary_search(arr, target):
    """ simple binary search. If an element find return position
    return -1 if not find
    return right element if more than one target presend
    """
    if len(arr) == 0:
        return -1

    l = 0
    r = len(arr)

    while l + 1 < r:
        m = l + (r - l) // 2
        if arr[m] > target:
            r = m
        else:
            l = m

    return l if arr[l] == target else -1


def test_binary_search():
    A = []
    t = 1
    print('Test #0 ', 'ok' if binary_search(A, t) == -1 else 'failed')

    A = [-10, 1, 2, 3, 4, 4, 5, 6, 7]
    t = 2
    print('Test #2 ', 'ok' if binary_search(A, t) == 2 else 'failed')

    t = -10
    print('Test #3 ', 'ok' if binary_search(A, t) == 0 else 'failed')

    t = 7
    print('Test #4 ', 'ok' if binary_search(A, t) == 8 else 'failed')

    t = 4
    print('Test #5', 'ok' if binary_search(A, t) == 5 else 'failed')


test_binary_search()
