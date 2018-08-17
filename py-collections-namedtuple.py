students_num, marks_idx = int(input()), input().split().index("MARKS")
lst = [int(input().split()[marks_idx]) for _ in range(students_num)]
print(sum(lst) / students_num)
