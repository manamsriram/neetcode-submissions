class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def checkset(a, i): 
            nonlocal ans, n
            if i == n:
                ans.append(a)
                return
            checkset(a + [nums[i]], i + 1)
            checkset(a, i + 1)
        
        checkset([], 0)
        return ans