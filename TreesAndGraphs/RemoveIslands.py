def removeIslands(matrix):
    onesConnectedToBorder = [[False for col in matrix[0]] for row in matrix]
       # top
       for i in range(len(matrix[0])):
            if matrix[0][i] == 1 and not onesConnectedToBorder[0][i]:
                performDFS(0, i, matrix, onesConnectedToBorder)
        # left
        for i in range(len(matrix)):
            if matrix[i][0] == 1 and not onesConnectedToBorder[i][0]:
                performDFS(i, 0, matrix, onesConnectedToBorder)
        # right
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0]) - 1] == 1 and not onesConnectedToBorder[i][len(matrix[0]) - 1]:
                performDFS(i, len(matrix[0]) - 1, matrix, onesConnectedToBorder)
        # bottom
        for i in range(len(matrix[0])):
            if matrix[len(matrix) - 1][i] == 1 and not onesConnectedToBorder[len(matrix) - 1][i]:
                performDFS(len(matrix) - 1, i, matrix, onesConnectedToBorder)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not onesConnectedToBorder[i][j]:
                    matrix[i][j] = 0
        return matrix


def performDFS(i, j, matrix, onesConnectedToBorder):
    nodesToExplore = [[i, j]]
    while len(nodesToExplore) != 0:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if matrix[i][j] == 0:
            continue
        onesConnectedToBorder[i][j] = True
        unvisitedNeighbors = getUnvisitedNeighbors(
            i, j, matrix, onesConnectedToBorder)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors
