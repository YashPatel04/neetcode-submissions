class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        visiting = set()
        adj = {}
        lines=0
        for i, j in edges:
            adj.setdefault(i,[]).append(j)
            adj.setdefault(j,[]).append(i)
        def dfs(val, prev):
            nonlocal lines
            if val in visiting: return
            if val in visited: return
            if prev==-1 and val not in visited:
                lines+=1
            visited.add(val)
            for i in adj.get(val,[]):
                dfs(i, val)
            return
        for i in range(n):
            dfs(i,-1)
        return lines
            