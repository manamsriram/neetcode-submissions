from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0 for _ in temperatures]
        stack=deque()
        stack.append(0)
        print(stack)
        for i in range(1,len(temperatures)):
            if(temperatures[i]<=temperatures[stack[-1]]):
                stack.append(i)
                print(stack)
            else:
                while(stack and temperatures[stack[-1]]<temperatures[i]):
                    j=stack.pop()
                    ans[j]=i-j
                    print(stack,ans)
                stack.append(i)
        return ans
