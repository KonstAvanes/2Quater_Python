import os

# Очистка терминала для удобства восприятия.
os.system('cls')

# Наишите программу, которая принимает на вход 2 числа. Задайте спислок заполненных в промежутке [-N, N
# Найдите произведение элементов на указанных позициях (не индексах)

n = int(input('Введите число N = '))
pos1 = int(input('Введите позицию №1: '))
pos2 = int(input('Введите позицию №2: '))

array = []
for i in range(-n, n+1):
    array.append(i)
print(f'Список в пределах [-{n}, {n}]: {array}')

if (pos1 and pos2):
    print(
        f'Произведение чисел на позициях списка ({pos1})={array[pos1-1]} и ({pos2})={array[pos2-1]}: {array[pos1-1] * array[pos2-1]}')
else:
    print('Нулевой позиции не существует в данном списке =)')
