source = [4, 4, 1, 5, 5, 4, 4, 4, 2, 1, 2, 34, 1, 2, 4]
res, cnt = 0, 0
for i in source:
    if cnt == 0:
        res = i
    if res == i:
        cnt += 1
    else:
        cnt -= 1
print(res)
