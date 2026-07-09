class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        left=0
        right=left+1
        while(right<len(prices)):
            if(prices[right]<prices[left]):
                left=right
            else:
                maxProfit=max(prices[right]-prices[left], maxProfit)
            right+=1
        return maxProfit
