class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            # here we deliberately choose to add the element to subset
            subset.append(nums[i])
            dfs(i+1)

            # here we remove the element and choose to not add that element
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res