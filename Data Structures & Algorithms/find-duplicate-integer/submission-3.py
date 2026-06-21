class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for b in range(32): # check every bit
            mask = 1 << b 
            c1 = c2 = 0
            for i in nums: # check how many numbers have that bit set in nums
                if i & mask:
                    c1 += 1
            for i in range(1,n): # check how many should have had that bit set if all numbers are unique
                if i & mask:
                    c2 += 1
            if c1 > c2: # if extra then it is because of the duplicate
                ans |= mask 
        return ans