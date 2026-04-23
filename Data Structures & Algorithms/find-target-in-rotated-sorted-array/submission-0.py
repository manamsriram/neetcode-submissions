class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0,len(nums)-1
        while(l<h):
            m = (l+h)//2
            if (nums[m]>nums[h]):
                l=m+1
            elif (target==nums[m]):
                return m
            else:
                h=m
        p=l
        l,h = 0,len(nums)-1
        if(target>=nums[p] and target<=nums[h]):
            l=p
        else:
            h=p-1
        while(l<=h):
            m = (l+h)//2
            if (target>nums[m]):
                l=m+1
            elif (nums[m]==target):
                return m
            else:
                h=m-1
        return -1