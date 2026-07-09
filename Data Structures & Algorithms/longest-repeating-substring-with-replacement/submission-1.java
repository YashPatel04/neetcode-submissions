class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int windowCount = 0;
        int maxLength = 0;
        int left = 0;
        for(int r=0; r<s.length(); r++){
            count[s.charAt(r)-'A']++;
            windowCount = Math.max(windowCount, count[s.charAt(r)-'A']);
            if((((r-left)+1)-windowCount)>k){
                count[s.charAt(left)-'A']--;
                left++;
            }
            maxLength=Math.max(maxLength, (r-left)+1);
        }
        return maxLength;
    }
}
