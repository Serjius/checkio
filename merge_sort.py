def merge(a, b):
    c = [0] * (len(a) + len(b))
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1
    return c


def merge_sort(a):
    if len(a) <= 1:
        return
    m = len(a) // 2
    l = a[:m]
    r = a[m:]
    merge_sort(l)
    merge_sort(r)

    c = merge(l, r)
    for i in range(len(a)):
        a[i] = c[i]


a = [1, 4, 6, 8, 9]
b = [2, 2, 3, 4, 5]

c = merge(a, b)
print('test #1', 'ok' if c == [1, 2, 2, 3, 4, 4, 5, 6, 8, 9] else 'failed')

a = [1, 2, 5, 2, 3, 9, 9, 0, 1]
merge_sort(a)
print('test #2', 'ok' if a == [0, 1, 1, 2, 2, 3, 5, 9, 9] else 'failed')
