#!/usr/bin/env python

# Task 02
# Найдите сумму цифр трехзначного числа.

def sumOfDigits(number):
    res = 0
    for digit in number:
        res += int(digit)

    return res


def main():
    number = input('Enter a number:\n')

    print(f'Sum of digits in number = {sumOfDigits(number)}')


if __name__ == '__main__':
    main()

