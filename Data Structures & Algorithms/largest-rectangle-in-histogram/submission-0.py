class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans,stack=0,[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                ind,height=stack.pop()
                ans=max(ans,height*(i-ind))
                start=ind
            stack.append((start,h))
        for i,h in stack:
            ans=max(ans,h*(len(heights)-i))
        return ans