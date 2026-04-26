class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        right = 0
        max_len = 0
        uniq = set()

        while left < len(s) and right < len(s):
            if s[right] not in uniq:
                uniq.add(s[right])
                right+=1
                max_len = max(max_len, len(uniq))
            else:
                uniq.remove(s[left])
                left +=1
        
        return max_len