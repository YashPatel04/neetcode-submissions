class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        maxSum=nums[0]
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(nums[i], nums[i]+dp[i-1])
            maxSum=max(maxSum, dp[i])
        return maxSum
