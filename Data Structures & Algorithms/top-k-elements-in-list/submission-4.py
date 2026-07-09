class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        heap=[]
        for i in freq.keys():
            heapq.heappush(heap, (-(freq.get(i, 0)), i))
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

