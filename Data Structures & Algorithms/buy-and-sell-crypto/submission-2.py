class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0    
        maxProfit=0
        lowestVal=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<lowestVal):
                lowestVal=prices[i]
            else:
                maxProfit=max(maxProfit, prices[i]-lowestVal)
        return maxProfit
            
        