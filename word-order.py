from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    name = input()
    d[name] = d.get(name, 0) + 1
print(len(d))
print(' '.join([str(v) for k, v in d.items()]))
