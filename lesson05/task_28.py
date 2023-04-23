#!/usr/bin/env python

# Task 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def recursivePositiveSum(a, b):
    if a == 0:
        return b

    return recursivePositiveSum(a - 1, b + 1)


def main():
    a, b = tuple(map(int, input(f'Enter TWO numbers separated by space:\n').split()))

    print(f'Result of {a} + {b} is {recursivePositiveSum(a, b)}')


if __name__ == '__main__':
    main()
