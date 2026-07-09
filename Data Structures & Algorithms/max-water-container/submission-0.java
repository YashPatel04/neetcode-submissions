class Solution {
    public int maxArea(int[] height) {
        int finalArea = 0;
        int lOne = 0;
        int lTwo = height.length-1;
        while(lOne<lTwo){
            int area = Math.min(height[lOne],height[lTwo])*(lTwo-lOne);
            if(area>finalArea){
                finalArea = area;
            }
            if(height[lOne]<height[lTwo]){
                lOne++;
            }else if(height[lTwo]<height[lOne]){
                lTwo--;
            }else{
                if((lOne+1)==(lTwo)&&(lTwo-1)==lOne){
                    if(Math.min(height[lOne],height[lTwo])>finalArea) finalArea=Math.min(height[lOne],height[lTwo]);
                    break;
                }
                if((lOne+1)==(lTwo-1)){
                    if(Math.min(height[lOne],height[lTwo-1])>finalArea) finalArea=Math.min(height[lOne],height[lTwo-1]);
                    break;
                }
                else if(height[lOne+1]<height[lTwo-1]) lOne++;
                else if(height[lOne+1]>height[lTwo-1]) lTwo--;

            }
        }
        return finalArea;
    }
}