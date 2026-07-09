class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r,c):
            if r>=ROWS or c>=COLS or r<0 or c<0 or (r,c) in visited or board[r][c]!="O":
                return
            visited.add((r,c))
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r+1,c)
            return
        # TOP EDGE  # BOTTOM EDGE
        for c in range(COLS):
            if board[0][c]=="O":
                dfs(0,c)
            if board[ROWS-1][c]=="O":
                dfs(ROWS-1,c)
        # LEFT EDGE # RIGHT EDGE
        for r in range(ROWS):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][COLS-1]=="O":
                dfs(r, COLS-1)
  
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and board[r][c]=="O":
                    board[r][c]="X"
