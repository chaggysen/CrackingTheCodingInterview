def twoNumberSum(array, targetSum):
    memo = {}
    for num in array:
        diff = targetSum - num
        if diff in memo:
            return [num, diff]
        else:
            memo[num] = True
    return []
