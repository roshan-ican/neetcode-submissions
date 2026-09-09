class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for word in strs:
            pattern = self.wordCounter(word)

            if pattern in groups:
                groups[pattern].append(word)
            else:
                groups[pattern] = [word]
        return list(groups.values())


    

    def wordCounter(self, word):
        counts = Counter(word)
        return tuple(sorted(counts.items()))
        