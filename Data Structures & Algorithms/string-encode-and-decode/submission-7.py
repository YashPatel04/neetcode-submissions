class Solution:

    def encode(self, strs: List[str]) -> str:
        final=[]
        for i in strs:
            l = len(i)
            temp = str(l)+"^#^"+i
            final.append(temp)
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        res=[]
        n=len(s)
        t=0
        while(t<n):
            temp=[]
            while s[t].isdigit():
                temp.append(s[t])
                t+=1
            print("".join(temp))
            num=int("".join(temp))    
            t+=3
            word=s[t:t+num]
            res.append(word)
            t+=num
        return res