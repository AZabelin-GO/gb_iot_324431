#!/usr/bin/env python

# Task 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from helpers import readers as h_readers
from helpers import arrays as h_arrays


def main():
    array = h_readers.readIntArray()

    number = int(input('Enter a number to find occurrences:\t'))

    number_occurrences = h_arrays.countNumberOccurrences(array, number)

    print(f'Number "{number}" found "{number_occurrences}" times in array')


if __name__ == '__main__':
    main()
