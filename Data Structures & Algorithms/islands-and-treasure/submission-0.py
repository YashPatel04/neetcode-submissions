class Solution:
    # Breadth-First-Search Approach
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def addCell(r,c):
            if r>=ROWS or c>=COLS or r<0 or c<0 or (r,c) in visited or grid[r][c]==-1:
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    visited.add((r,c))
                    q.append([r,c])

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c]=dist
                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            dist+=1