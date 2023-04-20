#!/usr/bin/env python

# Task 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from helpers import readers as h_readers


def main():
    blueberry_bed = h_readers.readIntArray()

    blueberry_gathered_per_iteration = list()

    if len(blueberry_bed) < 4:
        blueberry_gathered_per_iteration.append(sum(blueberry_bed))
    else:
        for i in range(len(blueberry_bed) - 1):
            blueberry_gathered_per_iteration.append(blueberry_bed[i - 1] + blueberry_bed[i] + blueberry_bed[i + 1])
        # last position in a bed
        blueberry_gathered_per_iteration.append(blueberry_bed[-2] + blueberry_bed[-1] + blueberry_bed[0])

    print(f'Autobot can collect maximum {max(blueberry_gathered_per_iteration)} blueberries per move '
          f'if it chooses bush with index {blueberry_gathered_per_iteration.index(max(blueberry_gathered_per_iteration))}')


if __name__ == '__main__':
    main()
