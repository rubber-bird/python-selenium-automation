# from random import randint
#
# n = randint(100, 999)

digits = int(input('Введіть розряд'))
n = (10000000,99999999)
print(f'ми отримали число {n}')
one = n%10
ten = n // 10 % 10
hundred = n // 100

print(one + ten + hundred)