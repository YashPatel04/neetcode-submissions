class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0: return False
        target = sum(nums) // 2
        targets = set()
        targets.add(0)
        for i in nums:
            temp = []
            for j in targets:
                temp.append(i)
                temp.append(i+j)
            for m in temp:
                targets.add(m)
            if target in targets:
                return True
        return False