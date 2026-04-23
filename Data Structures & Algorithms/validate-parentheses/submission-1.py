class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','{':'}','[':']'}
        stack=[]
        for i in s:
            if i in d:
                stack.append(i)
            elif(stack):
                x=stack.pop()
                if(i!=d[x]):
                    return False
            else:
                return False
        if(len(stack)>0):
            return False
        return True