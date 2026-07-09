class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def rec(i, a):
            if i == len(nums):
                ans.append(a.copy())
                return
            # when including we consider all cases including the nums[i]
            rec(i + 1, a + [nums[i]])
            # if nums[i] is not considered we ignore all other occurunces of nums[i] as 
            # it is handled by the inclusion call above
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            rec(i + 1, a)

        rec(0, [])
        return ans