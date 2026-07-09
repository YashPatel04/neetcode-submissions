class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops={"+","-","/","*"}
        for i in tokens:
            if i in ops:
                # ops
                num2=stack.pop()
                num1=stack.pop()
                if i=="-":
                    stack.append(num1-num2)
                elif i=="*":
                    stack.append(num1*num2)
                elif i=="/":
                    stack.append(int(num1 / num2))
                else:
                    stack.append(num1+num2)
            else:
                stack.append(int(i))
        return stack[-1]