class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        res = 0
        for i in range(n):
            res = res ^ i
            if i < n - 1:
                res = res ^ nums[i]
        return res