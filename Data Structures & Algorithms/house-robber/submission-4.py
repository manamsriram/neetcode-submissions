class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents house i - 2, rob2: i - 1
        rob1, rob2 = 0, 0

        for num in nums:
            # rob1 moves one position to rob2, as we compute a new rob2
            # it will be considering to rob the current house after robbing rob1 or just ignore it
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2