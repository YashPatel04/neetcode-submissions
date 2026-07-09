class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0, 0
        for i in s:
            if i == '(':
                openMin, openMax = openMin+1, openMax+1
            elif i == ')':
                openMin, openMax = openMin-1, openMax-1
            else:
                openMin, openMax = openMin-1, openMax+1
            if openMax<0:
                return False
            if openMin<0:
                openMin = 0
        return openMin==0