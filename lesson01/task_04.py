#!/usr/bin/env python

# Task 04
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def calcStat(total):
    if total % 6 != 0:
        raise ValueError('Wrong total! Somebody is lying...')

    tmp = int(total / 6)

    return tmp, tmp * 4, tmp


def main():
    total = int(input('Enter a number:\n'))

    try:
        peter, kate, sergey = calcStat(total)
        print(f'Peter = {peter}\nKate = {kate}\nSergey = {sergey}')
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
