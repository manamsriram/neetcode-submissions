class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                b,a=stack.pop(),stack.pop()
                stack.append(a+b)
            elif i=='-':
                b,a=stack.pop(),stack.pop()
                stack.append(a-b)
            elif i=='*':
                b,a=stack.pop(),stack.pop()
                stack.append(a*b)
            elif i=='/':
                b,a=stack.pop(),stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack[0]