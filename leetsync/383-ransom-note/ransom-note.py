class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        mag_dict = {}
        for x in magazine:
            if x in mag_dict:
                mag_dict[x] += 1
            else:
                mag_dict[x] = 1
        for x in ransomNote:
            if x in mag_dict and mag_dict[x] > 0:
                mag_dict[x] -= 1
            else:
                return False
        return True