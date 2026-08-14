class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(nums, perm, mask):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            # check from the beginning every backtrack/loop if each index is considered
            for i in range(len(nums)):
                if not mask & 1 << i:
                    recursion(nums, perm + [nums[i]], mask | 1 << i)

        recursion(nums, [], 0)
        return res