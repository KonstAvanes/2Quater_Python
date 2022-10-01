import os

# Очистка терминала для удобства восприятия.
os.system('cls')

# Задайте список из n чисел, заполненных по формуле (1 + 1/n)** n и выведите на экран их сумму
n = int(input('Введите число n = '))
array = []
summ = 0

for i in range(1, n+1):
    array.append(int(round(((1 + 1/i)**i))))
    summ += array[i-1]

print('Список для n = {}: {}, сумму элементов данного списка = {}'.format(n, array, summ))
