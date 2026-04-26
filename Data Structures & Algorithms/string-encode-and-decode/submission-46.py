class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for n in strs:
            res += str(len(n)) + "#" + n
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find the position of #
            j = i
            while s[j] != "#":
                j += 1
            # Extract the length (between i and j)
            length = int(s[i:j])

            # extract string after # for len(chars)
            start = j + 1
            end = start + length
            string = s[start:end]

            res.append(string)

            #move to next encoded
            i = end
        return res




