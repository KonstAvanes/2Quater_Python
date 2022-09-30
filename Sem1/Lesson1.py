from cmath import sqrt
import os
import random


# Clear console for all exercises.
def clear(): return os.system('cls')


clear()

# # EXX_001
# a = int(input('Введите число a = '))
# b = int(input('Введите число b = '))

# if sqrt(a) == b or sqrt(b) == a:
#     print('Correct')
# else:
#     print('UnCorrect')

# # EXX_002
# a = []
# for i in range(10):
#     a.append(random.randint(0, 100))

# print(f'Maximum from {a} = {max(a)}')

# # EXX_003

# n = int(input('Введите число N = '))

# for i in range(-n, n + 1):
#     print(i, end=" ")

# # EXX_004
# num = float(input('Введите число num = '))
# if (num % 1) == 0:
#     print('Error', int(num % 1))
# else:
#     print(int(num*10 % 10))


# EXX_005

num = int (input('Введите num = '))

if (not (num % 5 and num % 10) or not num %15) and num % 30 != 0:
    print(f'Число {num} кратно')
else: 
    print(f'Число {num} некратно')
