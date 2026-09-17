class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        t_counter = Counter(t)

        left = 0
        have = 0
        need = len(t_counter)

        best_length = float("inf")
        best_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_counter and window[char] == t_counter[char]:
                have+=1
            
            while have == need:
                if right - left + 1 < best_length:
                    best_length = right - left + 1
                    best_start = left
                left_char = s[left]
                window[left_char] -= 1

                if(
                    left_char in t_counter
                    and window[left_char] < t_counter[left_char]
                ):
                    have -= 1
            
                left += 1
        if best_length == float("inf"):
            return ""
        return s[best_start: best_start + best_length]

            
        


        
        