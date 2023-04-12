#!/usr/bin/env python

# Task 06
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.


def sumOfDigits(number):
    res = 0
    for digit in number:
        res += int(digit)

    return res


def isWinner(serial_number):
    if len(serial_number) % 2 != 0:
        raise ValueError('Wrong serial! Somebody is lying...')

    return sumOfDigits(serial_number[:int(len(serial_number) / 2)]) == sumOfDigits(
        serial_number[-1 * int(len(serial_number) / 2):])


def main():
    serial_number = input('Enter a serial number:\n')

    try:
        print(f'Result = {isWinner(serial_number)}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
