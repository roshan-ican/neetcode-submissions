class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for i in range(len(strs)):
            e += str(len(strs[i])) + "#" + strs[i]
        return e

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j]) # grabs the length
            word = s[j + 1: j + 1 + length] # grabs the word
            r.append(word)
            i = j + 1 + length
        return r
