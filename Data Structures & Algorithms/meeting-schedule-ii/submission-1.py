"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        
        time.sort(key = lambda x: (x[0], x[1]))
        # active is holding positive count of overlapping meetings
        active, res = 0, 0
        for t in time:
            active += t[1]
            res = max(res, active)

        return res