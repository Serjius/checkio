a = 357
print("10:", a, "2:", bin(a))
print("Last bit:", bin(a % 2), "Rest part:", bin(a // 2))

for i in bin(a):
    print(i)
