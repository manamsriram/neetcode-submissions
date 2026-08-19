class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # check if newInterval is to the left of current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # check if newInterval is to the right
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # overlapping case
            # here we only update the new Interval and do not append, becuause it can overlap with other intervals
            # if it does not, then it will be to the left of the next interval handled in first case
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # This is if the newInterval is to be at the end of all the others.
        res.append(newInterval)
        return res