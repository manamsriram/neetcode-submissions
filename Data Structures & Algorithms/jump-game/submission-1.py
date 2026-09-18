class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i in mem:
                return mem[i]
            for j in range(nums[i]):
                if dfs(i + j + 1):
                    mem[i] = True
                    return True
            mem[i] = False
            return False
        return dfs(0)