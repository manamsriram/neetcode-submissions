class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jumps = nums[0]
        for i in range(n - 1):
            jumps = max(jumps, nums[i])
            if jumps == 0:
                return False
            jumps -= 1
        return True