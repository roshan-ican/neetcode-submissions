class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                # Check if skipping s[i] OR skipping s[j] results in a palindrome
                opt1 = s[i+1:j+1]
                opt2 = s[i:j]
                return opt1 == opt1[::-1] or opt2 == opt2[::-1]
        return True