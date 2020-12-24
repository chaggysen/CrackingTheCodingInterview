def spiralTraverse(array):
    output = []
    left = 0
    right = len(array[0]) - 1
    top = 0
    bot = len(array) - 1
    while left <= right and top <= bot:
        for i in range(left, right + 1):
            output.append(array[top][i])

        for i in range(top + 1, bot + 1):
            output.append(array[i][right])

        for i in reversed(range(left, right)):
            if top == bot:
                break
            output.append(array[bot][i])

        for i in reversed(range(top + 1, bot)):
            if left == right:
                break
            output.append(array[i][left])

        left += 1
        right -= 1
        top += 1
        bot -= 1
    return output
