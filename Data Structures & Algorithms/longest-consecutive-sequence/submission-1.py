class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        m=0
        for i in nums:
            length=1
            if(i-1 not in nums):
                while(i+length in nums):
                    length+=1
                m=max(m,length)
        return m