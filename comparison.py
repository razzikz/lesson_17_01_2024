import timeit
from itertools import permutations
from math import *

print(f'Number of lesson options: {5 ** 5}')
print(f'Number of nums options (not repetitions): {len(set(permutations("137")))}')
comb = set(permutations("3476"))
count_odd, count_even = 0, 0
for i in comb:
    if int("".join(i)) % 2 != 0:
        count_odd += 1
    elif int("".join(i)) % 2 == 0:
        count_even += 1
print(f"Number of nums options (not repetitions, odd nums): {count_odd}\n"
      f"Number of nums options (not repetitions, even nums): {count_even}")


def factorial_rec(n):
    if n < 1:
        return 1
    else:
        num = n * factorial_rec(n - 1)
        return num


def fact(n):
    teth = 1
    for i in range(1, n + 1):
        teth *= i
    return teth


def fact_math(n):
    return sqrt(2*pi*n) * (n / e)**n * (1 + 1 / sqrt(52*e*n))


num = int(input("Number: "))
print(f"{20*'-'}\n"
      f"Factorial recursion: {factorial_rec(num)}\n"
      f"Time factorial recursion: {timeit.timeit(lambda: factorial_rec(num))}\n"
      f"loss factorial recursion: {100 - (factorial_rec(num) * 100 / factorial(num))}\n"
      f"{20*'-'}\n"
      f"Factorial normal: {fact(num)}\n"
      f"Time factorial normal: {timeit.timeit(lambda: fact(num))}\n"
      f"loss factorial normal: {100 - (fact(num) * 100 / factorial(num))}\n"
      f"{20*'-'}\n"
      f"Factorial Stirling: {fact_math(num)}\n"
      f"Time Stirling: {timeit.timeit(lambda: fact_math(num))}\n"
      f"loss factorial Stirling: {100 - (fact_math(num) * 100 / factorial(num))}\n"
      f"{20*'-'}\n"
      f"Factorial library math: {factorial(num)}\n"
      f"Time factorial library math: {timeit.timeit(lambda: factorial(num))}\n"
      f"{20*'-'}")
