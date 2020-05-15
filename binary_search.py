def binary_search(arr, target):
    """ simple binary search. If an element find return position
    return -1 if not find
    return THE LAST element if more than one target presend
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


def binary_search_first_element(arr, target):
    """ simple binary search. If an element find return position
    return -1 if not find
    return THE FIRST element if more than one target presend
    We need move left border for that
    """
    if len(arr) == 0:
        return -1

    l = -1
    r = len(arr) - 1

    while l + 1 < r:
        m = l + (r - l) // 2
        if arr[m] < target:
            l = m
        else:
            r = m

    return r if arr[r] == target else -1


def test_binary_search():
    A = []
    t = 1
    print('Test #0 ', 'ok' if binary_search(A, t) == -1 else 'failed')
    print('Test #1 ', 'ok' if binary_search_first_element(A, t) == -1 else 'failed')

    A = [-10, 1, 2, 3, 4, 4, 5, 6, 7]
    t = 2
    print('Test #2 ', 'ok' if binary_search(A, t) == 2 else 'failed')
    print('Test #3 ', 'ok' if binary_search_first_element(A, t) == 2 else 'failed')

    t = -10
    print('Test #4 ', 'ok' if binary_search(A, t) == 0 else 'failed')
    print('Test #5 ', 'ok' if binary_search_first_element(A, t) == 0 else 'failed')

    t = 7
    print('Test #6 ', 'ok' if binary_search(A, t) == 8 else 'failed')
    print('Test #7 ', 'ok' if binary_search_first_element(A, t) == 8 else 'failed')

    t = 4
    print('Test #8', 'ok' if binary_search(A, t) == 5 else 'failed')
    print('Test #9', 'ok' if binary_search_first_element(A, t) == 4 else 'failed')


test_binary_search()
