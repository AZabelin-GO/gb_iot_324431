#!/usr/bin/env python

# Task 30
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def calcArithmeticProgression(a, delta, length):
    res = [a]

    for i in range(2, length + 1):
        res.append(res[0] + (i - 1) * delta)

    return res


def main():
    a, delta, length = tuple(map(int, input(f'Enter THREE numbers separated by space:\n').split()))

    print('Arithmetic progression items:')

    for x in calcArithmeticProgression(a, delta, length):
        print(x)


if __name__ == '__main__':
    main()
