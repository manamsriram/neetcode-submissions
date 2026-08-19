class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]
        ans = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                # we keep the interval that ends first, so we do not risk overlapping with more of the next intervals.
                prevEnd = min(prevEnd, end)
                ans += 1
            else:
                prevEnd = end
        return ans