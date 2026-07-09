class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i, c in enumerate(s):
            hashmap[c]=i
        end = 0
        last = 0
        res = []
        for i, c in enumerate(s):
            end = max(end, hashmap[c])
            if i == end:
                res.append(i-last+1)
                last = i+1
        return res


