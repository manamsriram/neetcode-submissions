class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0] )
        output = [intervals[0]]

        for start, end in intervals[1:]:
            # latest added output value
            lastEnd = output[-1][1]
            if start <= lastEnd:
                # [1,5], [2,4] is an edge case which calls for 
                output[-1][1] = max(lastEnd, end)
            # simply append non-overlapping points
            else:
                output.append([start, end])
            
        return output