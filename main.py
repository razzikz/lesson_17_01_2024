from math import *
from itertools import permutations

all_comb = set(permutations("ATBTATBZA"))
for comb in all_comb:
    print(''.join(comb))

man, woman = 10, 12
print(f'variants: {int(factorial(22) / (factorial(5) * factorial(22-5)))}')

ticket, count = [int(i) for i in range(100000, 1000000)], 0
for i in ticket:
    num_1, num_2, num_3, num_4, num_5, num_6 = i % 10, i // 10 % 10, \
        i // 100 % 10, i // 1000 % 10, i // 10000 % 10, i // 100000 % 10
    if num_1+num_2+num_3 == num_4+num_5+num_6:
        if num_1+num_2+num_3+num_4+num_5+num_6 == 30:
            count += 1

print(count)