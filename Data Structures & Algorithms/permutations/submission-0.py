class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        # get the rest of array without the first element
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            # +1 becuase we can add to the end of the combination too
            for i in range(len(p) + 1):
                temp = p.copy()
                # insert the first element we ignored into all the combinations
                temp.insert(i, nums[0])
                res.append(temp)
        return res