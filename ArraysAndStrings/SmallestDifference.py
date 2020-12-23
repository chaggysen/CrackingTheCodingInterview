def smallestDifference(arrayOne, arrayTwo):
    output = []
    arrayOne.sort()
    arrayTwo.sort()
    arrayOne_len = len(arrayOne)
    arrayTwo_len = len(arrayTwo)
    pointer_one = 0
    pointer_two = 0
    minDiff = float("inf")
    while pointer_one < arrayOne_len and pointer_two < arrayTwo_len:
        diff = abs(arrayOne[pointer_one] - arrayTwo[pointer_two])
        if diff < minDiff:
            minDiff = diff
            output = [arrayOne[pointer_one], arrayTwo[pointer_two]]
        if arrayOne[pointer_one] < arrayTwo[pointer_two]:
            pointer_one += 1
        elif arrayOne[pointer_one] > arrayTwo[pointer_two]:
            pointer_two += 1
        else:
            output = [arrayOne[pointer_one], arrayTwo[pointer_two]]
            return output
    return output
