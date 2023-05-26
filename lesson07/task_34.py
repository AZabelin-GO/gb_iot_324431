#!/usr/bin/env python

# Task 34
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

from helpers.consts import RU_LOWER_VOWELS as ruVowelsSet


def calcSyllablesInWord(word: str):
    return sum([word.count(char) for char in ruVowelsSet])


def calcSyllablesInPhrase(phrase: str):
    return map(calcSyllablesInWord, phrase.split('-'))


def main():
    phrases = input(f'Enter TEXT:\n').lower().split()

    syllables_per_phrase = [
        sum(
            calcSyllablesInPhrase(phrase)
        ) for phrase in phrases
    ]

    if len(set(syllables_per_phrase)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


if __name__ == '__main__':
    main()
