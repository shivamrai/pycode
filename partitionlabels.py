import unittest
class Solution():
    def partitionLabels(self, S: str) -> list:
        #keep track of end Index
        
        end_idx = [0]*26
        for i in range(0,len(S)):
            end_idx[ord(S[i])-ord('a')] = i
        
        res = []
        start, end = 0,0
        
        for i in range(len(S)):
            end = max(end, end_idx[ord(S[i])-ord('a')])
            if i == end:
                res.append(i-start+1)
                start = i+1
        
        return res  

class TestSolution(unittest.TestCase):
    def testpartitionlabels(self):
        x = Solution()
        res = x.partitionLabels("ababcbacadefegdehijhklij")
        self.assertEqual(res,[9,7,8])

if __name__ == "__main__":
    unittest.main()
