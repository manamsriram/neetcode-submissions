class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp holds the longest subsequence ending at index i
        dp = [1] * n

        # for every number check the left partition for longest subsequence which can include this index i
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)