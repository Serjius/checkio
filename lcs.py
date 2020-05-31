def lcs(a, b):
    t = [[""] * len(b) for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    t[i][j] = a[i]
                else:
                    t[i][j] = t[i - 1][j - 1] + a[i]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1], key=len)

    return t[-1][-1]


a = ['a', 'b', 'c', 'd', 'a', 'f']
b = ['a', 'c', 'b', 'c', 'f']
print('Test #1', lcs(a, b) == 'abcf')

a = ['a', 'b', 'c', 'd', 'g', 'h']
b = ['a', 'e', 'd', 'f', 'h', 'r']
print('Test #2', lcs(a, b) == 'adh')

a = ['a', 'g', 'g', 't', 'a', 'b']
b = ['g', 'x', 't', 'x', 'a', 'y', 'b']
print('Test #3', lcs(a, b) == 'gtab')
