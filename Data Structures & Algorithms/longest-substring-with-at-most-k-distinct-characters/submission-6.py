class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        l = 0

        seen = {}
        maxi = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1

            while len(seen) > k:
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l += 1

            maxi = max(maxi, r - l + 1)

        return maxi
