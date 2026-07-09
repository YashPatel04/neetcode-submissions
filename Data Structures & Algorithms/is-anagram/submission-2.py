class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        first={}
        sec={}
        for i in range(max(len(s), len(t))):
            if len(s)>i:
                first[s[i]] = first.get(s[i], 0) + 1
            if len(t)>i:
                sec[t[i]]=sec.get(t[i], 0)+1
        print(first)
        print(sec)
        for k in first.keys():
            if k not in sec.keys() or sec[k]!=first[k]:
                return False
        return True