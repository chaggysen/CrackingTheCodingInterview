def firstDuplicateValue(array):
    memo = {}
    for num in array:
        if num not in memo:
            memo[num] = True
        else:
            return num
    return -1


def firstDuplicateValueTwo(array):
    for value in array:
        if array[abs(value) - 1] < 0:
            return - 1
        array[abs(value) - 1] *= -1
    return - 1
