#!/usr/bin/env python

# Task 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from helpers import readers as h_readers
from helpers import arrays as h_arrays


def main():
    array = h_readers.readIntArray()

    number = int(input('Enter a number to find minimal distance:\t'))

    idx, distance = h_arrays.findNumberClosestElement(array, number)

    print(f'The closest to "{number}" element is "arr[{idx}]" with difference "{distance}"')


if __name__ == '__main__':
    main()
