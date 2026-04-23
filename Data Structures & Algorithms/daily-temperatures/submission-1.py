class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0 for _ in temperatures]
        stack=deque([0])
        for i in range(1,len(temperatures)):
            if(temperatures[i]>temperatures[stack[-1]]):
                while(stack and temperatures[stack[-1]]<temperatures[i]):
                    j=stack.pop()
                    ans[j]=i-j
            stack.append(i)
        return ans
