class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=len(nums)
        ans=[[] for i in range(l+1)]
        d={}
        res=[]
        for i in nums:
            d[i]=1+d.get(i,0)
        for i,e in d.items():
            ans[e].append(i)
        for i in range(l,0,-1):
            if ans[i]:
                for j in ans[i]:
                    res.append(j)
                    k-=1
                    if(k==0):
                        return res
        return res