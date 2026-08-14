class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents house i - 2, rob2: i - 1
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2