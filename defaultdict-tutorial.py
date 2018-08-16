from collections import defaultdict


m, n = map(int, input().split())

a = defaultdict(list)
for _ in range(m):
    a[input()].append(str(int(_) + 1))

b = [input() for _ in range(n)]

for _ in b:
    lst = a.get(_, [str(-1)])
    print(' '.join(lst))
