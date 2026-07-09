class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        maxArea = heights[0];
        stack.push(0);
        for(int i=1; i<heights.length; i++){
            if(heights[i]>=heights[stack.peek()]){
                stack.push(i);
            }else{
                while(!stack.isEmpty() && heights[i]<heights[stack.peek()]){
                    int height = heights[stack.pop()];
                    int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                    int area = height * width;
                    maxArea = Math.max(maxArea, area);        
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty()) {
            int height = heights[stack.pop()];
            int width = stack.isEmpty() ? heights.length : heights.length - stack.peek() - 1;
            int area = height * width;
            maxArea = Math.max(maxArea, area);
        }

        return maxArea;
    }
}