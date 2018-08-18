from collections import OrderedDict
n = int(input())
d = OrderedDict()
for i in range(n):
    name, s, qty = input().rpartition(' ')
    d[name] = d.get(name, 0) + int(qty)
for name, qty in d.items():
    print(name, qty)
