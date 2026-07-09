class Solution {
    public List<String> generateParenthesis(int n) {
       List<String> out = new ArrayList<>();
       int open = 0;
       int close = 0;
       StringBuilder sb = new StringBuilder();
       generate(out, 0, 0, sb, n);
       return out;
    }
    public void generate(List<String> out, int open, int close, StringBuilder sb, int n){
        if ((open==n)&&(close==n)){
            out.add(sb.toString());
            //sb.setLength(0);
            return;
        }
        if(open<n) {
            generate(out,open+1,close, sb.append("("),n);
            sb.deleteCharAt(sb.length() - 1); // Backtrack
        }
        if(close<open){
            generate(out, open, close+1, sb.append(")"), n); 
            sb.deleteCharAt(sb.length() - 1); // Backtrack
        }
    }
}