class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for b in range(32):
            mask = 1 << b
            c1 = c2 = 0
            for i in nums:
                if i & mask:
                    c1 += 1
            for i in range(1,n):
                if i & mask:
                    c2 += 1
            if c1 > c2:
                ans |= mask
        return ans