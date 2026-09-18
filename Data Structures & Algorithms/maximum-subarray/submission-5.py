class Solution:
    def maxSubArray(self, nums):
        # dp already has all the elements for the case of starting sub array at that index
        # dp = nums.copy()
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # return max(dp)
        ans = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            if s < 0 or s + nums[i] < 0:
                s = 0
            s += nums[i]
            ans = max(ans, s)
        return ans