class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total, rotten = 0,0
        finalMin = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque() 
        visited = set()           
        for r in range(ROWS):
            for c in range(COLS): 
                if grid[r][c]==1 or grid[r][c]==2:
                    total+=1
                if grid[r][c]==2:
                    rotten+=1
                    q.append([r,c])
                    visited.add((r,c))
        def rot(r,c):
            nonlocal rotten
            if r>=ROWS or c>=COLS or r<0 or c<0 or (r,c) in visited or grid[r][c]==0:
                return False
            visited.add((r,c))
            q.append([r,c])
            rotten+=1
            grid[r][c]=2
            return True
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rot(r+1,c)
                rot(r-1,c)
                rot(r,c+1) 
                rot(r,c-1)
            if q: finalMin+=1
        if total==rotten:
            return finalMin
        else:
            return -1