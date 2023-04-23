import random


def countNumberOccurrences(array, number):
    res = 0

    for x in array:
        if x == number:
            res += 1

    return res


def findNumberClosestElement(array, number):
    if len(array) == 0:
        return -1, None

    res_idx = 0
    res_distance = abs(number - array[res_idx])

    for idx, x in enumerate(array):
        if abs(number - x) < res_distance:
            res_idx = idx
            res_distance = abs(number - x)

    return res_idx, res_distance


def generateIntArray(length=10, arr_min=0, arr_max=10):
    return [random.randint(arr_min, arr_max) for _ in range(length)]
