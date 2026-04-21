from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build a tuple list with frequency forward x -1
        freq_counter = Counter(nums)
        freq_list = [[-count, value] for value, count in freq_counter.items()]
        heapify(freq_list)
        res = []
        while k > 0:
            res.append(heapq.heappop(freq_list)[1])
            k-=1
        return res