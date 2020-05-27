# Get -1 for False and 1 for True
# 2* int(bool) - 1
print(2 * int(False) - 1, 2 * int(True) - 1)

# ASC and DESC compare in one staitment
asc_array = [1, 2]
desc_array = [2, 1]
i = 0
j = 1

desc_sorted = bool(True)
print((2 * int(desc_sorted) - 1) * asc_array[i] <
      (2 * int(desc_sorted) - 1) * asc_array[j])
desc_sorted = bool(False)
print((2 * int(desc_sorted) - 1) * desc_array[i] <
      (2 * int(desc_sorted) - 1) * desc_array[j])


# Store multidemention array in a list
# Linearisation Aij = A[i*M+j]
array = [1, 2, 3, 4, 5, 6, 7, 8]

row_size = 3  # element per each row
for i in range(len(array) // row_size):
    for j in range(row_size):
        print(array[i * row_size + j], end='')
    print()


# how DON'T creata a list of lists
lst = [[0] * 3] * 2
for l in lst:
    print(id(l))
"""
139682403526664
139682403526664
The same objects!
"""

# how DO create a list of lists
lst = [[0] * 3 for _ in range(2)]
for l in lst:
    print(id(l))
"""
139682403526600
139682403526792
Different objects
"""
