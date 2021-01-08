def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    output = [0 for i in range(len(array))]
    for i in range(len(array)):
        if i == 0:
            maxSum = array[i]
            output[i] = maxSum
        elif i == 1:
            output[i] = max(array[0], array[1])
        else:
            output[i] = max(output[i - 2] + array[i], output[i - 1])
    return output[-1]
