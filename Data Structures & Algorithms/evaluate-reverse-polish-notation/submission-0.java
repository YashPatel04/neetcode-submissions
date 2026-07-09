class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        for(String i : tokens){
            //System.out.println(stack);
            if(i.equals("+")){
                if(stack.size()>=2){
                    int a = Integer.parseInt((String)stack.pop());
                    int b = Integer.parseInt((String)stack.pop());
                    stack.push(String.valueOf(a + b));
                }
            } else if(i.equals("-")){
                if(stack.size()>=2){
                    int a = Integer.parseInt((String)stack.pop());
                    int b = Integer.parseInt((String)stack.pop());
                    stack.push(String.valueOf(b-a));
                }
            } else if(i.equals("/")){
                if(stack.size()>=2){
                    int a = Integer.parseInt((String)stack.pop());
                    int b = Integer.parseInt((String)stack.pop());
                    if(a==0){return 0;}
                    stack.push(String.valueOf(b/a));
                }
            } else if(i.equals("*")){
                if(stack.size()>=2){
                    int a = Integer.parseInt((String)stack.pop());
                    int b = Integer.parseInt((String)stack.pop());
                    stack.push(String.valueOf(a * b));
                }
            } else {
                stack.push(i);
            }
    }
    return Integer.parseInt((String)stack.pop());
    }
}