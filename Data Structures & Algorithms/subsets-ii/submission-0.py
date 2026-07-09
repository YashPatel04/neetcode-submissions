class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        nums = sorted(nums)
        def dfs(i, subset):
            if(len(nums)<=i):
                return
            # add the curr char to the result
            subset.append(nums[i])
            res.append(subset.copy())
            dfs(i+1, subset)
            # reset subset and if it is empty then only dfs with the next element
            subset.pop()
            while(i<len(nums)-1 and nums[i]==nums[i+1]): i+=1
            dfs(i+1, subset)
        dfs(0,[])
        return res
