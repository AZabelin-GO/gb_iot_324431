#!/usr/bin/env python

# Task 40
# Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю
# стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd


def main():
    df = pd.read_csv('california_housing_train.csv')
    df_subset = df.loc[(df['population'] >= 0) & (df['population'] <= 500)]

    print(f'Mean house price: {df_subset["median_house_value"].mean()}')


if __name__ == '__main__':
    main()
