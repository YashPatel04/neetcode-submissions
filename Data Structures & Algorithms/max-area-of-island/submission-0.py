class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            nonlocal area, maxArea
            if r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]==0:
                maxArea = max(maxArea, area)
                return
            grid[r][c]=0
            area+=1
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    dfs(r,c)
                    area=0
        return maxArea