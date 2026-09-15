class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        left = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(char)
            longest = max(longest, right - left + 1)
        return longest
        