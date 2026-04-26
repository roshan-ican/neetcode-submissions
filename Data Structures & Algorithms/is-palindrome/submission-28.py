class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(cleaned) - 1
        
        while start < end:
            if cleaned[start] == cleaned[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
        