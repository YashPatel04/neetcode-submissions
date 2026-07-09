class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        left = 0
        right = 1
        bucket = set()
        maxLen=0
        currLen=2
        bucket.add(s[left])
        while(right<len(s)):
            while s[right] in bucket:
                bucket.remove(s[left])
                left+=1
                currLen-=1
            maxLen = max(currLen, maxLen)
            bucket.add(s[right])
            right+=1
            currLen+=1
        return maxLen
            