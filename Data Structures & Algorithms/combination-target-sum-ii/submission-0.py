class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i>=len(nums) or total>target:
                return
            # CHOICE 1: count the number
            subset.append(nums[i])
            dfs(i+1, subset, total+nums[i])
            # CHOICE 2: do not count the number
            subset.pop()
            while i<len(nums)-1 and nums[i+1] == nums[i]: 
                i+=1
            dfs(i+1, subset, total)

        dfs(0, [], 0)
        return res