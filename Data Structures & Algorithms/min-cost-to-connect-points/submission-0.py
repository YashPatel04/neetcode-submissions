class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i, val in enumerate(points):
            for j, val2 in enumerate(points):
                if(i==j): continue
                temp = abs(val[0]-val2[0]) + abs(val[1]-val2[1])
                adj[i].append([temp, j])
                adj[j].append([temp, i])
        cost = 0
        minheap =[[0,0]]
        visited = set()
        while minheap:
            if(len(visited)==len(points)):
                return cost
            dist, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            cost += dist
            print(node)
            for val in adj[node]:
                if val[1] not in visited:
                    heapq.heappush(minheap, val)
        return cost