class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = 1000000;
        int maxProfit = 0;
        for(int i=0; i<prices.length; i++){
            minPrice = Math.min(prices[i], minPrice);
            maxProfit = Math.max(prices[i]-minPrice, maxProfit);
        }
        return maxProfit;   
    }
}
