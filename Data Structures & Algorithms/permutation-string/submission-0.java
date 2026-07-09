class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length()<s1.length()) return false;
        int[] target = new int[26];
        int[] str = new int[26];
        for(int i = 0; i<s1.length(); i++){
            target[s1.charAt(i)-'a']++;
            str[s2.charAt(i)-'a']++;
        }
        int left = 0;
        int right = s1.length()-1;
        while(right<=s2.length()-1){
            int i=left;
            boolean match = true;
            while(i<=right){
                if(target[s2.charAt(i)-'a']!=str[s2.charAt(i)-'a']){
                    match = false;
                }
                i++;
            }
            if(match) return true;
            str[s2.charAt(left)-'a']--;
            left++;
            right++;
            if(right<s2.length()) str[s2.charAt(right)-'a']++;
        }
        return false;
    }
}