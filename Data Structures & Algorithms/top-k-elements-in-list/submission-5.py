class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
           map[i]=map.get(i,0)+1
        heap=[]
        for ele in map.keys():
            heapq.heappush(heap, (-map[ele], ele))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res