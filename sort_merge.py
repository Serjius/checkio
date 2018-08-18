def merge(lst):
    if len(lst) <= 1:
        return lst
    n = len(lst) // 2
    l_lst = merge(lst[:n])
    r_lst = merge(lst[n:])

    rslt_lst = []
    r_idx, l_idx = 0, 0
    while r_idx < len(r_lst) and l_idx < len(l_lst):
        if r_lst[r_idx] < l_lst[l_idx]:
            rslt_lst.append(r_lst[r_idx])
            r_idx += 1
        else:
            rslt_lst.append(l_lst[l_idx])
            l_idx += 1
    rslt_lst += r_lst[r_idx:]
    rslt_lst += l_lst[l_idx:]

    return rslt_lst

source = [1, 2, 3, 4, 1, 1, 2, 2, 1, 2, 3, 1, 2, 2, 3, 4]
assert merge(source) == sorted(source)

source = [1, ]
assert merge(source) == sorted(source)

source = []
assert merge(source) == sorted(source)

source = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
assert merge(source) == sorted(source)

print('OK')
