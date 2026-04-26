class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get the count of each
        # and if the count
        res=""
        for j in range(len(strs[0])):
            char = strs[0][j]

            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != char:
                    return res
            res+= char
        return res
                    