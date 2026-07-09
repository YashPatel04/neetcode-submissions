class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [(-n) for n in stones]
        heapq.heapify(min_heap)
        while len(min_heap)>=2:
            y = -heapq.heappop(min_heap)
            x = -heapq.heappop(min_heap)
            if(y==x):
                if len(min_heap)==0:
                    return 0
                continue
            else:
                heapq.heappush(min_heap, -(y-x))
        return -min_heap[0]