class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        ans = 0
        left = 0

        for right, char in enumerate(s):
            while char in window:
                # TODO: remove arr[left] from window
                window.remove(s[left])
                left += 1

            # TODO: update ans
            window.add(char)
            ans = max(ans, right - left + 1)

        return ans
