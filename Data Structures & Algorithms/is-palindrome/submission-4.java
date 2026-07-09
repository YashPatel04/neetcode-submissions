class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        s = s.toLowerCase();

        while (i <= j) {
            char a = s.charAt(i);
            char b = s.charAt(j);

            // Skip non-alphanumeric characters for 'a'
            if (!((a >= 'a' && a <= 'z') || (a >= '0' && a <= '9'))) {
                i++;
                continue;
            }

            // Skip non-alphanumeric characters for 'b'
            if (!((b >= 'a' && b <= 'z') || (b >= '0' && b <= '9'))) {
                j--;
                continue;
            }

            // Check if characters are equal
            if (a == b) {
                i++;
                j--;
            } else {
                return false;
            }
        }
        return true;
    }
}
