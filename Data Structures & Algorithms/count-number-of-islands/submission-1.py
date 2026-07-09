class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        cols = len(grid[0])
        rows = len(grid)

        def bfs(r,c):
            if (r<0 or r>=rows) or (c<0 or c>=cols):
                return
            if (r,c) in visited or grid[r][c]=="0":
                return
            visited.add((r,c))
            bfs(r+1, c)
            bfs(r, c+1)
            bfs(r-1, c)
            bfs(r, c-1)
        islands=0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]=="1":
                    islands+=1
                    bfs(i, j)
        return islands
