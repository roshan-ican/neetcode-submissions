class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window = {}
        left = 0
        ans = 0

        for right in range(n):
            # TODO: add arr[right] to window
            window[s[right]] = window.get(s[right], 0) + 1

            while (right - left + 1) - max(window.values()) > k: 
                # TODO: remove arr[left] from window
                window[s[left]] -= 1
                left += 1

            # TODO: update ans
            ans = max(ans, right - left + 1)

        return ans