from collections import defaultdict
from typing import List


class Solution:

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     word_ctr = defaultdict(list)
    #     res = []
    #     for word in strs:
    #         key = tuple(sorted(Counter(word).items()))
    #         word_ctr[key].append(word)

    #     for v in word_ctr.values():
    #         res.append(v)

    #     return res
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_ctr = defaultdict(list)
        for word in strs:
            # Create a count array for 26 lowercase letters
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            # Use tuple of counts as key (immutable and hashable)
            key = tuple(count)
            word_ctr[key].append(word)
        # Return all groups directly
        return list(word_ctr.values())
