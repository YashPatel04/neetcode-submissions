class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for src, dst in tickets[::-1]:
            adj[src].append(dst)
        res = []
        def dfs(n):
            while adj[n]:
                dst = adj[n].pop()
                dfs(dst)
            res.append(n)
        dfs('JFK')
        return res[::-1]