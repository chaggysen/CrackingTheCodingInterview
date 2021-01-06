class Solution(object):
    def uniquePaths(self, m, n):
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in range(len(grid)):
            grid[i][0] = 1
        for i in range(len(grid[0])):
            grid[0][i] = 1
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
