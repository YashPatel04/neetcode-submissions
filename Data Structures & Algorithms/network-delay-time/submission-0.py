class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, t, w in times:
            adj[u].append((w, t))
        minheap = [(0,k)]
        res = 0
        visited = set()
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            res = max(dist, res)
            visited.add(node)
            for value in adj[node]:
                if value[1] not in visited:
                    heapq.heappush(minheap, (value[0]+res,value[1]))
        return res if len(visited)==n else -1