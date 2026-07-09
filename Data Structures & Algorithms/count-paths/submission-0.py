class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if(i-1>=0 and j-1>=0):
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
                else:
                    grid[i][j]=1
        return grid[m - 1][n - 1]