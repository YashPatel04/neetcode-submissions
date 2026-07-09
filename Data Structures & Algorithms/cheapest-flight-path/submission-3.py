class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # form an adjacency list
        # go to source perform dfs also keep track of visited
        # if in visited return 
        # if dest return total
        # backtrack and remove from visited
        # perform dfs for neibour of src
        adj = {}
        for s, d, p in flights:
            adj.setdefault(s, []).append((d, p))

        best = float("inf")
        def dfs(node, cost, stops):
            nonlocal best
            if node==dst:
                best = min(cost, best)
                return
            if stops>k or cost >= best: return
            for nei, price in adj.get(node, []):
                dfs(nei, cost+price, stops+1)

        dfs(src, 0, 0)
        return best if best!=float("inf") else -1
