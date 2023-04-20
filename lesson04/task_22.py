#!/usr/bin/env python

# Task 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from helpers import readers as h_readers


def main():
    first_array = h_readers.readIntSet()
    second_array = h_readers.readIntSet()

    res = sorted(list(first_array.intersection(second_array)))

    print()
    print(f'Result: "{res}"')


if __name__ == '__main__':
    main()
