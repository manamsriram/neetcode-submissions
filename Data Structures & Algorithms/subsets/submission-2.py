class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        for i in range(1 << n):
            # check set bits for numbers from 0 to (2 ** n) - 1
            # i.e empty to full set ex. 000 to 111 for n = 3
            # check every range and compute subset with index where 1 bit is set
            subset = [nums[j] for j in range(n) if i & (1 << j)]
            ans.append(subset)
        return ans