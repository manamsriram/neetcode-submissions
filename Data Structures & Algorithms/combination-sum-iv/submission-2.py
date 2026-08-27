class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for a in range(1, target + 1):
            # we mark there is currently 0 ways to get this target i
            dp[a] = 0
            # we can choose any number as ordering matters.
            # so [2, 1] and [1, 2] are both valid
            # that is the only difference between this and coin change 2
            for num in nums:
                dp[a] += dp.get(a - num, 0)

        return dp[target]