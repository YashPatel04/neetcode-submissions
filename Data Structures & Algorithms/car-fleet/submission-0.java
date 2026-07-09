class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int count = 0;
        for(int i = 0; i<speed.length; i++){
           map.put(position[i],speed[i]);
        }
        Stack<Double> stack = new Stack<>();
        Arrays.sort(position);
        for(int i = speed.length-1;i>=0; i-- ){
            double t = (target - position[i])/(double) map.get(position[i]);
            if(stack.isEmpty()){stack.push(t);continue;}
            if(t<stack.peek()){
                continue;
            }else if(t==stack.peek()){
                continue;
            }else{
                stack.push(t);
            }
        }
        return stack.size();
    }
}