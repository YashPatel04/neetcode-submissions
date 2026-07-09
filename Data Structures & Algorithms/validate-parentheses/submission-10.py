class Solution:
    def isValid(self, s: str) -> bool:
        open=[]
        close=deque()
        for i in s:
            if (i in {'(', '{', '['}):
                open.append(i)
            else:
                if not open:
                    return False
                if i=='}':
                    if open[-1]!='{':
                        return False
                elif i==']':
                    if open[-1]!='[':
                        return False
                elif i==')':
                    if open[-1]!='(':
                        return False
                open.pop()
        return True if not open else False