class Solution {
    public boolean isValid(String s) {
        if(s.length()<=1) return false;
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(c=='[' || c=='{' || c=='(' ){
                stack.push(c);
            }else{
                if(stack.size()==0) return false;
                if((c==']' && stack.pop()!='[') || (c=='}' && stack.pop()!='{') || (c==')' && stack.pop()!='(')){
                    return false;
                }
            }
        }
        if(stack.size()>0) return false;
        return true;
    }
}
