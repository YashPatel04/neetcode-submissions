class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge cases in case the len of str is 0 or 1
        if(len(s)<=1):
            return len(s)
        right=1
        left=0
        maxLen=1
        visited={i:0 for i in s}
        visited[s[left]]=1
        while(right<len(s)):
            # print("right", s[right], right)
            # print('left', s[left], left)
            if visited[s[right]]!=0:
                while visited[s[right]]!=0 and right<len(s):
                    if(right==left):
                        right+=1
                        visited[s[right]]+=1
                        continue
                    if(right>=len(s)):
                        break
                    visited[s[left]]-=1
                    left+=1
            else:
                visited[s[right]]+=1
                maxLen=max(maxLen, right-left+1)
                # print("max:", maxLen)
                right+=1
            # print("\n")
        return maxLen
