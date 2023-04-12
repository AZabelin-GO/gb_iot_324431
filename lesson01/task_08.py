#!/usr/bin/env python

# Task 08
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


def canSplitUp(m, n, k):
    return 0 < k <= m * n and (k % m == 0 or k % n == 0)


def main():
    numbers = [int(x) for x in input('Enter THREE numbers (m, n, k) separated by space:\n').split()]

    print(f'Result = {canSplitUp(numbers[0], numbers[1], numbers[2])}')


if __name__ == '__main__':
    main()
