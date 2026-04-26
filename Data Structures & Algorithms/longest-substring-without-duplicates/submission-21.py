class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 1
        window = 0
        for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            window = max(window, r - l + 1)
        return window
