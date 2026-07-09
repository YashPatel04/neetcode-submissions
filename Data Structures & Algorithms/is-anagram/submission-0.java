class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sOne = String.valueOf(s).toCharArray();
        char[] tOne = String.valueOf(t).toCharArray();
        if(sOne.length != tOne.length) return false;
        Arrays.sort(sOne);
        Arrays.sort(tOne);
        for(int i = 0; i<tOne.length; i++){
            if(sOne[i]!=tOne[i]) return false;
        }
        return true;
    }
}
