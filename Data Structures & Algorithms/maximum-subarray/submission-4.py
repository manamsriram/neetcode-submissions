class Solution:
    def maxSubArray(self, nums):
        # dp already has all the elements for the case of starting sub array at that index
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)