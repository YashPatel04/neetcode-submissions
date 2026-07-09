class Solution {
    public String minWindow(String s, String t) {
        if(t.length()>s.length()) return "";
        Map<Character, Integer> need = new HashMap<>();
        for(char i: t.toCharArray()){
            need.put(i, need.getOrDefault(i, 0)+1);
        }
        Map<Character, Integer> window = new HashMap<>();
        int right = 0;
        int left = 0;
        int formed = 0;
        int start = 0;
        int minLen = Integer.MAX_VALUE;
        while(right<s.length()){
            char c = s.charAt(right);
            if(need.containsKey(c)){
                window.put(c, window.getOrDefault(c,0)+1);
                if(window.get(c).intValue() == need.get(c).intValue()){
                    formed++;
                }
            }
            while(formed == need.size()){
                if((right - left)<minLen){
                    start = left;
                    minLen = right-left;
                }
                char d = s.charAt(left);
                if(need.containsKey(d)){
                    if(window.get(d).intValue()==need.get(d).intValue()){
                    formed--;
                    }
                    window.put(d, window.get(d)-1);
                }
                left++;
            }
            right++;
        }
        return minLen==Integer.MAX_VALUE ? "" : s.substring(start,start+minLen+1);
    }
}