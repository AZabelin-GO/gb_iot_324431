#!/usr/bin/env python

# Task 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


def main():
    numbersSum = int(input('Enter a sum of numbers:\n'))
    numbersProduct = int(input('Enter a product of numbers:\n'))

    isFound = False

    for i in range(1000):
        for j in range(1000):
            if (i + j) == numbersSum and (i * j) == numbersProduct:
                isFound = True
                print(f'Found numbers: {i} and {j}')

    if not isFound:
        print(f'Numbers not found. Somebody is lying...')


if __name__ == '__main__':
    main()
