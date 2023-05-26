#!/usr/bin/env python

# Task 36
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.

def printOperationTable(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        row = list()
        for j in range(1, num_columns + 1):
            row.append(str(operation(i, j)))
        print('\t\t'.join(row))


def main():
    print('Enter a binary function as lambda expression.')
    binary_function = input(f'Example: lambda x, y: x * y\n')

    printOperationTable(eval(binary_function))


if __name__ == '__main__':
    main()
