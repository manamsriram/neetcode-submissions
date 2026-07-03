class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def check(a, s, i):
            if s == target:
                ans.append(a.copy())
                return
            if i >= len(nums) or s > target:
                return
            a.append(nums[i])
            # check sub array where this element is considered
            check(a, s + nums[i], i)
            # remove the element and check sub array with element not considered
            a.pop()
            check(a, s , i + 1)
        check([], 0, 0)
        return ans