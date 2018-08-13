shoes_num = int(input())
shoes_sizes_lst = list(map(int, input().split(' ')))
customers_num = int(input())

arr = []
s = 0
for i in range(customers_num):
    size, price = map(int, input().split())
    if size in shoes_sizes_lst:
        shoes_sizes_lst.remove(size)
        s += price
print(s)
"""
With collections for shoes
"""
import collections

numShoes = int(raw_input())
shoes = collections.Counter(map(int, raw_input().split()))
numCust = int(raw_input())

income = 0

for i in range(numCust):
    size, price = map(int, raw_input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1

print income
