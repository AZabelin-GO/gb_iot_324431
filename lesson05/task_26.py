#!/usr/bin/env python

# Task 26
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии

def recursivePositivePower(number, power):
    if power == 0:
        return 1
    elif power == 1:
        return number

    return number * recursivePositivePower(number, power - 1)


def main():
    number, power = tuple(map(int, input(f'Enter TWO numbers separated by space:\n').split()))

    print(f'Result of {number} ^ {power} is {recursivePositivePower(number, power)}')


if __name__ == '__main__':
    main()
