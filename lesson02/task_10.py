#!/usr/bin/env python

# Task 10
# На столе лежат N монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


def genCoinsArr(length):
    return [random.randint(0, 1) for x in range(length)]


def main():
    coinsNumber = int(input('Enter a number of coins:\n'))

    coinsArr = genCoinsArr(coinsNumber)
    print(f'Generated array: {coinsArr}')

    headsCount = len([x for x in coinsArr if x == 0])
    tailsCount = len([x for x in coinsArr if x == 1])

    print(f'{min(headsCount, tailsCount)} coins should be flipped')


if __name__ == '__main__':
    main()
