
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimized sol
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())







        # get the count of each str
        # map them 
        # anagram_map = {}
        # for i, n in enumerate(strs):
        #     s = tuple(sorted(Counter(n).items()))
        #     print(s, "_cou")
        #     if s in anagram_map:
        #         anagram_map[s].append(n)
        #     else:
        #         anagram_map[s] = [n]
        # res = list(anagram_map.values())
        # return res