class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def check(a, s, i):
            if s == target:
                ans.append(a.copy())
                return
            if i >= len(candidates) or s > target:
                return
            # a.append(candidates[i])
            # include all combinations with multiple occurunces of the same element
            check(a + [candidates[i]], s + candidates[i], i + 1)
            # ignore the element and all the other occurunces of that element to avoid duplicate sets
            # a.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            check(a, s , i + 1)
        check([], 0, 0)
        return ans