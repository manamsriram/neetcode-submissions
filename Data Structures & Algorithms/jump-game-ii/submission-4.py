class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        farthest = 0
        ans = 0
        # sort of like bfs level but next level size is max range we can reach from elements in the current level
        while r < n - 1:
            # go through elements in this level and mark the farthest which becomes the right edge of the next range
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            # Number of jumps or number of levels
            ans += 1
        return ans