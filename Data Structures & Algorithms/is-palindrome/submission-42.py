class Solution:
    def isPalindrome(self, s: str) -> bool:
        sConv = ""
        for c in s:
            if c.isalnum():
                sConv += c.lower()
        
        l = 0
        r = len(sConv) - 1
        while l < r:
            if sConv[l] != sConv[r]:
                return False
            l+=1
            r-=1
        return True
