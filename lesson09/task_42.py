#!/usr/bin/env python

# Task 42
# Узнать какая максимальная households в зоне минимального значения population

import pandas as pd


def main():
    df = pd.read_csv('california_housing_train.csv')
    df_subset = df.loc[df['population'] == df["population"].min()]

    print(f'Maximum households value of houses where population is minimal ({df["population"].min()}):\n'
          f'{df_subset["households"].max()}')


if __name__ == '__main__':
    main()
