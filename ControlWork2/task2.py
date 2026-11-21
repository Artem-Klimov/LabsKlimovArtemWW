# 2.Задан кортеж, состоящий из чисел, введите с клавиатуры число и сформируйте кортеж, не содержащий этого числа

from random import randint

orgnl = tuple(randint(1, 99) for _ in range(10))
print(orgnl)

deleted = int(input())

ans = tuple(i for i in orgnl if i != deleted)
print(ans)