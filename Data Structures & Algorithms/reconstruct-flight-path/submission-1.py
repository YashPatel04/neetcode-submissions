class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort()
        for dp, ar in tickets:
            adj[dp].append(ar)
        res = ["JFK"]
        def dfs(node):
            if len(res)==len(tickets)+1:
                return True
            if node not in adj:
                return False
            temp = list(adj[node])
            for i, location in enumerate(temp):
                res.append(location)
                adj[node].pop(i)
                if dfs(location): return True
                res.pop()
                adj[node].insert(i, location)
            return False
        dfs("JFK")
        return res