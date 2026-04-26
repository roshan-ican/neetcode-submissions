class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_set = set()
    
        start = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in count_set:
                count_set.remove(s[start])
                start+=1
            count_set.add(s[right])
            max_len = max(max_len, right - start + 1)
        return  max_len