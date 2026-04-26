
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # get the count of each str
        # map them 
        anagram_map = {}
        for i, n in enumerate(strs):
            s = tuple(sorted(Counter(n).items()))
            if s in anagram_map:
                anagram_map[s].append(n)
            else:
                anagram_map[s] = [n]
        res = list(anagram_map.values())
        return res