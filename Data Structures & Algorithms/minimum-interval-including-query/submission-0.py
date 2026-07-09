class Solution:
    # Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]
    # Output: [2,2,3,5,1,-1]
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x:x[0])
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q:
                l,r= intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            
            while minHeap and minHeap[0][1]<q:
                heapq.heappop(minHeap)
            res[q] =  minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]