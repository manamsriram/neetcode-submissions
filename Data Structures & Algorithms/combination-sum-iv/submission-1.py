class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = [-1] * (target + 1)
        memo[0] = 1
        def dfs(a):
            if a == 0:
                return 1
            if memo[a] != -1:
                return memo[a]
            res = 0
            # we can choose any number as ordering matters.
            # so [2, 1] and [1, 2] are both valid
            # that is the only difference between this and coin change 2
            for i in range(len(nums)):
                if a < nums[i]:
                    break
                res += dfs(a - nums[i])
            memo[a] = res
            return memo[a]

        return dfs(target)