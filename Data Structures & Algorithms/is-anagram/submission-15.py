from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s1= defaultdict(int)
        s2 = defaultdict(int)

        for str1 in s:
            s1[str1] += 1
            
        for str2 in t:
            s2[str2] += 1
        
        return s1 == s2

