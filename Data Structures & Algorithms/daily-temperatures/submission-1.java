class Solution {
    public int[] dailyTemperatures(int[] t) {
        int n = t.length;
        int[] arr = new int[n];
        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<t.length; i++){
            while(!stack.isEmpty() && t[i]>t[stack.peek()]){
                int prev = stack.pop();
                arr[prev] = i-prev;
            }
            stack.push(i);
        }
        return arr;
    }
}