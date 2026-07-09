public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int end = 0;
        int max = 0;
        List<Character> list = new ArrayList<>();

        while(end<s.length()){
            if(!list.contains(s.charAt(end))){
                list.add(s.charAt(end));
                max = Math.max(max,list.size());
                end++;
            }
            else{
                list.remove(0);
            }
        }
        return max;
    }
}