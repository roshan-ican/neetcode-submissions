class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for _s in s:
            if _s in hash_s:
                hash_s[_s] += 1
            else:
                hash_s[_s] = 1
        for _t in t:
            if _t in hash_t:
                hash_t[_t] += 1
            else:
                hash_t[_t] = 1
        if hash_s == hash_t:
            return True
        return False
        