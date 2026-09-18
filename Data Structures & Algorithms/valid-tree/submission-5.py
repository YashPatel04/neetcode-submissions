class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=(n-1):
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(val, parent):
            if val in visited:
                return False
            visited.add(val)
            for i in adj[val]:
                if i==parent: continue
                if not dfs(i, val):
                    return False
            return True
        res = dfs(0, -1)
        if len(visited)!=n: return False
        return res
        


