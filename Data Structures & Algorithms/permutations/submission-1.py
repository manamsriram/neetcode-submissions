class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recursion(nums, perm, visited):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            # check from the beginning every backtrack/loop if each index is considered
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    recursion(nums, perm + [nums[i]], visited)
                    visited[i] = False

        recursion(nums, [], [False] * len(nums))
        return res