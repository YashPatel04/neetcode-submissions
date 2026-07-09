class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {}
        for u, v in edges:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        
        visited = set()

        def dfs(val, parent):
            if val in visited:
                return False
            temp = adj.get(val,[])
            visited.add(val)
            if temp==[]: return True
            for i in temp:
                if i == parent: continue
                if not dfs(i,val): return False
            return True
        res = dfs(0, -1)
        if not res or len(visited)!=(n): return False
        return True