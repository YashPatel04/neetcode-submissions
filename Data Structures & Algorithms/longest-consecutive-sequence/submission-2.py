class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen=0
        hashmap={}
        visited=set()
        for n in nums:
            hashmap[n]=hashmap.get(n, 0)+1
        for i in nums:
            if i in visited or i-1 in hashmap:
                continue
            start=i
            currLen=0
            while start in hashmap:
                currLen+=1
                maxLen=max(currLen, maxLen)
                visited.add(start)
                start+=1
        return maxLen