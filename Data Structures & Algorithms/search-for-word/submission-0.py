class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r,c,w):
            if w==word:
                return True
            if r==ROWS or c==COLS or r<0 or c<0 or (r,c) in visited or board[r][c]!=word[len(w)]:
                return
            visited.add((r,c))
            w+=board[r][c]
            res = dfs(r+1,c,w) or dfs(r-1,c,w) or dfs(r,c+1,w) or dfs(r,c-1,w)
            visited.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,""): return True
        return False
            