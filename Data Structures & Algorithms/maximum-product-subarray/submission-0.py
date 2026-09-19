class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        ans = nums[0]
        for n in nums:
            temp = curMax
            curMax = max(n * curMin, n * curMax, n)
            curMin = min(n * curMin, n * temp, n)
            ans = max(ans, curMax)
        return ans