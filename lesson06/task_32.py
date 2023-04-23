#!/usr/bin/env python

# Task 32
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума)

from helpers import arrays as h_arrays


def main():
    arr = h_arrays.generateIntArray()
    print(f'Generated array:\n{arr}')
    start, end = tuple(map(int, input(f'Enter TWO numbers separated by space:\t').split()))

    for i in range(len(arr)):
        if start <= arr[i] <= end:
            print(f'arr[{i}] = {arr[i]} is between {start} and {end}')


if __name__ == '__main__':
    main()
