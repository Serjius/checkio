def array_left_shift(arr, shift):
    if shift < 1:
        return

    shift = shift % len(arr)

    right_border = len(arr) - shift
    tmp = list()
    for i in range(shift):
        tmp.append(arr[i])

    for i in range(0, right_border):
        arr[i] = arr[i + shift]

    for i in range(len(tmp)):
        arr[right_border + i] = tmp[i]


a = [1, 2, 3, 4, 5, 6]
array_left_shift(a, 4)
print("test #1", "ok" if a == [5, 6, 1, 2, 3, 4] else "failed")

a = [1, 2, 3, 4, 5, 6]
array_left_shift(a, 0)
print("test #2", "ok" if a == [1, 2, 3, 4, 5, 6] else "failed")

a = [1, 2, 3, 4, 5, 6]
array_left_shift(a, 1)
print("test #3", "ok" if a == [2, 3, 4, 5, 6, 1] else "failed")

a = [1, 2, 3, 4, 5, 6]
array_left_shift(a, 12)
print("test #4", "ok" if a == [1, 2, 3, 4, 5, 6] else "failed")

a = [1, 2, 3, 4, 5, 6]
array_left_shift(a, 16)
print("test #5", "ok" if a == [5, 6, 1, 2, 3, 4] else "failed")