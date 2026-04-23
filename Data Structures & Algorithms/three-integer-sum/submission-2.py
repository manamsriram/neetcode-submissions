class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            t=0-nums[i]
            l=i+1
            h=len(nums)-1
            while(l<h):
                if(nums[l]+nums[h]==t):
                    ans.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1
                    while(l<h and nums[l]==nums[l-1]):
                        l+=1
                elif(nums[l]+nums[h]<t):
                    l+=1
                else:
                    h-=1
        return ans