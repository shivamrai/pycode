class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # i = 1
        # intervals.sort(key = lambda x: x[0])
        # while i < len(intervals):
        #     if intervals[i-1][1] >= intervals[i][0]:
        #         start = intervals[i-1][0]
        #         end = max(intervals[i-1][1], intervals[i][1])
        #         del intervals[i-1]
        #         del intervals[i-1]
        #         intervals.insert(i-1, [start, end])
        #     else:
        #         i+=1
        # return intervals
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]  # Initialize result with first interval
        for i in range(1, len(intervals)):
            # Check if current interval overlaps with last merged interval
            if res[-1][1] >= intervals[i][0]:
                # Merge by updating end to maximum of both ends
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                # No overlap, append current interval to result
                res.append(intervals[i])
        return res