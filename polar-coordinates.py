import cmath
i = input().replace(' ', '')
for j in cmath.polar(complex(i)):
    print(j)


# nice solution
import cmath
print(*cmath.polar(complex(input())), sep='\n')
