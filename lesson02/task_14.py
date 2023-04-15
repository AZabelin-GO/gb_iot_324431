#!/usr/bin/env python

# Task 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def main():
    number = int(input('Enter a number:\n'))

    i = 0
    while 2 ** i <= number:
        print(f'2 ^ {i} = {2 ** i}')
        i += 1


if __name__ == '__main__':
    main()
