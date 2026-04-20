from collections import defaultdict, Counter

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_ctr = defaultdict(list)
        res = []
        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            word_ctr[key].append(word)
                
        for v in word_ctr.values():
            res.append(v)
        
        return res