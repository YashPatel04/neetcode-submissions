class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
            curr.word = True
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        res = set()
        def dfs(r, c, word, node):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit or board[r][c] not in node.children):
                return 
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+=board[r][c]
            if node.word:
                res.add(word)
            
            dfs(r-1, c, word, node)
            dfs(r+1, c, word, node)
            dfs(r, c+1, word, node)
            dfs(r, c-1, word, node)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        return list(res)