class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counters = {}

        for i in range(len(s)):
            if s[i] in counters:
                counters[s[i]] += 1
            else:
                counters[s[i]] = 1
        odd_count = 0
        for num in counters.values():
            if num % 2 != 0:
                odd_count += 1
        return odd_count <= 1