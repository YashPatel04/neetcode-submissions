class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in nums:
            val = hashmap.get(i, 0)
            if val>0:
                return True
            hashmap[i]=val+1
        return False