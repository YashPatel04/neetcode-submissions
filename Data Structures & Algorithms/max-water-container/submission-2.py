class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxArea=0
        while(left!=right):
            # print(right)
            area=(right-left)*min(heights[right], heights[left])
            maxArea=max(area, maxArea)
            if(heights[left]>heights[right]):
                right-=1;
            else:
                left+=1
        return maxArea