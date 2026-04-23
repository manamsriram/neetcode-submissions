class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[nums[0]]
        post=[nums[n-1]]
        for i in range(1,n):
            pre.append(pre[i-1]*nums[i])
            post.insert(0,post[0]*nums[n-i-1])
        ans=[post[1]]
        for i in range(1,n-1):
            ans.append(pre[i-1]*post[i+1])
        ans.append(pre[n-2])
        return ans