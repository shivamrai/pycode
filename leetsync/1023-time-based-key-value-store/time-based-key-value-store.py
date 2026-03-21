from collections import defaultdict
from typing import List
class TimeMap:

    def __init__(self):
        self.time_map: defaultdict[str, list[tuple[int, str]]] = defaultdict(list)

    def _find_timestamp_index(self, currtimestamp: int, timestamps: list[tuple[int, str]]) -> str:
        # binary search
        low = 0
        high = len(timestamps) - 1
        result: str = ""
        while low <= high:
            mid = (low + high) // 2
            if timestamps[mid][0] <= currtimestamp:
                result = timestamps[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return result

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            values: List[tuple[int, str]] = self.time_map[key]  # Get the [(ts, val), ...] list
            return self._find_timestamp_index(timestamp, values)
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
