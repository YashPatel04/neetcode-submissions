class Solution:
    def calcDist(self, x, y):
        return math.sqrt((x**2) + (y**2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for i in points:
            min_heap.append([self.calcDist(i[0], i[1]), i[0], i[1]])
        heapq.heapify(min_heap)
        res = []
        for j in range(k):
           temp = heapq.heappop(min_heap)
           res.append([temp[1], temp[2]])
        return res 
