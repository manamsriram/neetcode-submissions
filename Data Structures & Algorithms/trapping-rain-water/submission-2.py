class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if(n<=2):
            return 0
        maxL,maxR,l,r,ans=height[0],height[n-1],0,n-1,0
        while(l<r):
            if(maxL>maxR):
                r-=1
                if(maxR<height[r]):
                    maxR=height[r]
                ans+=maxR-height[r]
            else:
                l+=1
                if(maxL<height[l]):
                    maxL=height[l]
                ans+=maxL-height[l]
        return ans