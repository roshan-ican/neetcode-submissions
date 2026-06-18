class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char = {}
        res = -1

        for i, c in enumerate(s):
            if c in char:
                res = max(res, i - char[c] - 1)
            else:
                char[c] = i
        return res
        