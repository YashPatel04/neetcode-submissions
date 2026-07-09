class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ourset = set()
        for i in nums:
            if i in ourset:
                return True
            ourset.add(i)
        return False