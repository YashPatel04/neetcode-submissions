class Solution:
    def isPali(self, s):
        left = 0
        right = len(s)-1
        while(left<right):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset=[]
        def dfs(p):
            if p>=len(s): 
                res.append(subset.copy())
                return
            for j in range(p, len(s)):
                if(self.isPali(s[p:j+1])):
                    subset.append(s[p:j+1])
                    dfs(j+1)
                    subset.pop()
        dfs(0)
        return res