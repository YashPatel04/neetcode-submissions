class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."]*n for i in range(n)] # each ["."] for a cell in a board, we are creating a board

        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            
        backtrack(0)
        return res

