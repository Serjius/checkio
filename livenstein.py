import pprint

pp = pprint.PrettyPrinter(indent=4)


def livenstein2(a, b):
    f = [[i + j if i * j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    pp.pprint(f)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][i - 1]
            else:
                f[i][j] = min(f[i - 1][j - 1], f[i][j - 1], f[i - 1][j]) + 1
    pp.pprint(f)


livenstein2('horse', 'ros')
