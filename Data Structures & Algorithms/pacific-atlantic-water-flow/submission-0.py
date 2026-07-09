
class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if len(grid)==0: return []
        ROWS, COLS = len(grid), len(grid[0])
        res = []
        pcfc = set()
        atl = set()
        def dfs(s,prev,r,c):
            # check from which cells does water flow to [r][c]
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]<prev or (r,c) in s:
                return 
            prev = grid[r][c]
            s.add((r,c))
            dfs(s,prev,r+1,c)
            dfs(s,prev,r-1,c)
            dfs(s,prev,r,c+1)
            dfs(s,prev,r,c-1)
            return

        # checking the pacific edge
        for c in range(COLS):
            dfs(pcfc,float("-inf"),0,c)
        for r in range(ROWS):
            dfs(pcfc,float("-inf"),r,0)
        # checking the atlantic edge
        for c in range(COLS):
            dfs(atl,float("-inf"),ROWS-1,c)
        for r in range(ROWS):
            dfs(atl,float("-inf"),r,COLS-1)
        return list(pcfc.intersection(atl))    
