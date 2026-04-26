class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        res = []
        for w in words:

            joined = " ".join(words)
            if joined.count(w) > 1:
                res.append(w)
        return res


        