class Solution {
    public boolean canEat(int speed, int[] piles, int h){
    int hours = 0;
    for (int pile : piles) {
        hours += (pile + speed - 1) / speed;  // ceiling division
        if (hours > h) {
            return false;  // early stop if hours exceed limit
        }
    }
    return true;

    }
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = 0;
        for(int i: piles){
            if(i>high){
                high=i;
            }
        }
        int minHour = high;
        while(low<high){
            int mid = (low+((high-low)/2));
            boolean canEat = canEat(mid, piles, h);
            if(canEat){
                minHour = Math.min(mid, minHour);
                high=mid;
            }else{
                low=mid+1;
            }
        }
        return minHour;
    }
}