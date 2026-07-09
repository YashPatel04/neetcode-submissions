class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        if len(nums)==2: return max(nums[0], nums[1])
        def robber(houses):
            if len(houses)==1: return houses[0]
            if len(houses)==2: return max(houses[0], houses[1])
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i]=max(houses[i]+ dp[i-2], dp[i-1])
            return dp[-1]
        return max(robber(nums[1:]), robber(nums[:(len(nums)-1)]))