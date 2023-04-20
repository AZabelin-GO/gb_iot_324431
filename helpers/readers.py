def readWord():
    return input(f'Enter a word:\t')


def readIntArray():
    res = list()

    array_length = int(input('Enter a number of items in array:\t'))

    for i in range(array_length):
        res.append(int(input(f'Enter arr[{i}]:\t')))

    return res
