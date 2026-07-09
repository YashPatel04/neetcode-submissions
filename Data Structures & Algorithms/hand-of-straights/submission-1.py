class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0: return False
        minheap=[]
        hashmap = {}
        for i in hand:
            if i not in hashmap.keys():
                heapq.heappush(minheap, i)
            hashmap[i] = hashmap.get(i,0)+1
        curr = 0
        while minheap:            
            temp = []
            for _ in range(groupSize):
                if not minheap: return False
                t = heapq.heappop(minheap)
                temp.append(t)
            for i in range(len(temp)):
                j = temp[i]
                if len(temp)>0 and i<len(temp)-1 and j+1!=temp[i+1]: return False
                hashmap[j]-=1
                if hashmap[j]>0:
                    heapq.heappush(minheap, j)
        return True