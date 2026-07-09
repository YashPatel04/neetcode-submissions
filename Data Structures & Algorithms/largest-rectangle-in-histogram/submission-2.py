class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0
        for i, h in enumerate(heights):
            start=i
            while stack and h<stack[-1][1]:
                index, height = stack.pop()
                area = (i-index)*height
                maxArea = max(area, maxArea)
                start=index
            stack.append((start, h))
        index=len(heights)
        print(stack)
        while stack:
            i, j = stack.pop()
            area = j*(index-i)
            maxArea = max(area, maxArea)
        return maxArea