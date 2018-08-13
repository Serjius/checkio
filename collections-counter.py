shoes_num = int(input())
shoes_sizes_lst = list(map(int, input().split(' ')))
customers_num = int(input())

arr = []
for i in range(customers_num):
    arr.append(list(map(int, input().split())))
s = 0
for i in range(len(arr)):
    if arr[i][0] in shoes_sizes_lst:
        shoes_sizes_lst.remove(arr[i][0])
        s += arr[i][1]
print(s)
