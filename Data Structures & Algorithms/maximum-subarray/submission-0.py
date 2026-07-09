class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = 0
        max_sum = float("-inf")
        for i in nums:
            currMax = max(i, i+prev)
            prev = currMax
            max_sum = max(max_sum, currMax)
        return max_sum
