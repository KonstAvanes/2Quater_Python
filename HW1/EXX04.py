import os

# Очистка терминала для удобства восприятия.
os.system('cls')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quater_of_axes = int(input('Введите номер координатной четверти = '))

if quater_of_axes in range(1, 5):
    if quater_of_axes == 1:
        print(f'В {quater_of_axes} координатной четверти диапозон значений = (X > 0, Y > 0)')
    elif quater_of_axes == 2:
        print(f'В {quater_of_axes} координатной четверти диапозон значений = (X < 0, Y > 0)')
    elif quater_of_axes == 3:
        print(f'В {quater_of_axes} координатной четверти диапозон значений = (X < 0, Y < 0)')
    elif quater_of_axes == 4:
        print(f'В {quater_of_axes} координатной четверти диапозон значений = (X > 0, Y < 0)')
else:
    print(f'Значение = {quater_of_axes}, четверти не существует в двухмерной системе координат')
