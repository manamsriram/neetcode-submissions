class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(nums[0], self.dfs(nums[1:]), self.dfs(nums[:-1]))
    
    def dfs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(dp1, nums[i] + dp0)
            dp0 = dp1
            dp1 = temp
        return dp1