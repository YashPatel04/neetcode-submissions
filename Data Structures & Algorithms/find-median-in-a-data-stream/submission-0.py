class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.maxHeap and self.maxHeap[0]<num:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)
        if len(self.minHeap) > len(self.maxHeap)+1:
            heapq.heappush(self.maxHeap, -(heapq.heappop(self.minHeap)))
        if len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, -(heapq.heappop(self.maxHeap)))

    def findMedian(self) -> float:
        length = len(self.minHeap)+len(self.maxHeap)
        if(length%2==0):
            res = -self.minHeap[0] + self.maxHeap[0]
            return res/2
        else:
            if(len(self.minHeap)>len(self.maxHeap)):
                return -self.minHeap[0]
            else:
                return self.maxHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
        