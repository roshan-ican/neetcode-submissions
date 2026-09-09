class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        groups = {}
        for i in range(len(strs)):
            count = Counter(strs[i])
            key = tuple(sorted(count.items()))

            if key in groups:
                groups[key].append(strs[i])
            else:
                groups[key] = [strs[i]]
        return list(groups.values())