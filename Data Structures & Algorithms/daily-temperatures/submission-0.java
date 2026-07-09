class Solution {
    public int[] dailyTemperatures(int[] t) {
        Stack<List<Integer>> stack = new Stack<>();
        int[] out  = new int[t.length];
        for(int i = t.length-1; i>=0; i--){
            if(stack.isEmpty()){
                List<Integer> list = new ArrayList<>();
                list.add(t[i]);
                list.add(i);
                stack.push(list);
                out[i]=0;
            }else if(t[i]>=stack.peek().get(0)){
                while(!stack.isEmpty()){
                    if(t[i]<stack.peek().get(0)){
                        int temp = stack.peek().get(1);
                        List<Integer> list = new ArrayList<>();
                        list.add(t[i]);
                        list.add(i);
                        out[i]= temp-i;
                        stack.push(list);
                        break;
                    }else{
                        stack.pop();
                    }
                }   
                if(stack.isEmpty()){
                        List<Integer> list = new ArrayList<>();
                        list.add(t[i]);
                        list.add(i);
                        stack.push(list);
                        out[i]=0;
                }
            }else if(t[i]<stack.peek().get(0)){
                int temp = stack.peek().get(1);
                List<Integer> list = new ArrayList<>();
                list.add(t[i]);
                list.add(i);
                stack.push(list);
                out[i]=temp-i;
            }
        }
        return out;
    }
}