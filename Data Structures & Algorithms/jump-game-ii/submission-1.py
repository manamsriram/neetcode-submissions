class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}
        def dfs(i):
            if i >= n - 1:
                return 0
            if i in mem:
                return mem[i]
            res = 1e9
            for j in range(nums[i]):
                res = min(res, 1 + dfs(i + j + 1))
            mem[i] = res
            return res
        return dfs(0)