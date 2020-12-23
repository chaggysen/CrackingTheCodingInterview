def moveElementToEnd(array, toMove):
    if len(array) == 0:
        return array
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] == toMove and array[end] != toMove:
            swap(array, start, end)
        if array[end] == toMove:
            end -= 1
        if array[start] != toMove:
            start += 1
    return array


def swap(array, x, y):
    array[x], array[y] = array[y], array[x]
