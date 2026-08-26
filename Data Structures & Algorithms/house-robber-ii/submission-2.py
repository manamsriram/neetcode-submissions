class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mem = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i, flag):
            # if we go out of bounds or if we took first element, and we are at last element
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if mem[i][flag] != -1:
                return mem[i][flag]
            mem[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
            return mem[i][flag]

        # True indicates we consider first element
        return max(dfs(0, True), dfs(1, False))