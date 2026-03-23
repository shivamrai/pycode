class Solution:

    def _merge_overlap(self, intervals: List[int]) -> List[int]:
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

    def _split_into_intervals(self, s: str, words: List[str]) -> List[int]:
        intervals = []
        for word in words:
            start = s.find(word)
            while start != -1:
                end = start + len(word)
                intervals.append([start, end])
                start = s.find(word, start + 1)  # Find next occurrence
        return intervals

    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not s or not words:
            return s

        intervals = self._split_into_intervals(s, words)
        if not intervals:
            return s

        merged_intervals = self._merge_overlap(intervals)

        result = []
        prev_end = 0
        for start, end in merged_intervals:
            result.append(s[prev_end:start])  # Add non-bold part
            result.append("<b>" + s[start:end] + "</b>")  # Add bold part
            prev_end = end
        result.append(s[prev_end:])  # Add remaining non-bold part

        return "".join(result)