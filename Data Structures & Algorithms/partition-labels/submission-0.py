class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        arr = [0]*26
        for alphabet in s:
            arr[ord(alphabet)-ord("a")]+=1
        targets = set()
        res = []
        currSize = 1
        for i in s:
            loc = arr[ord(i)-ord("a")]-1
            arr[ord(i)-ord("a")]-=1
            if loc>0:
                targets.add(i)
            else:
                if i in targets:
                    targets.remove(i)
            if len(targets)==0:
                res.append(currSize)
                currSize = 1
            else:
                currSize+=1
        return res