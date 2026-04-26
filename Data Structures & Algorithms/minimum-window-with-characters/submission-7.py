class Solution:
    def minWindow(self, s: str, t: str) -> str:
        find = {}
        start = 0
        
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        
        # build frequency map of t
        for t1 in t:
            if t1 in find:
                find[t1] += 1
            else:
                find[t1] = 1
        
        window = {}
        have, need = 0, len(find)
        res, res_len = [-1, -1], float("inf")
        
        for end in range(len(s)):
            c = s[end]
            window[c] = window.get(c, 0) + 1
            
            if c in find and window[c] == find[c]:
                have += 1
            
            # shrink the window from left while it's valid
            while have == need:
                if (end - start + 1) < res_len:
                    res = [start, end]
                    res_len = end - start + 1
                
                window[s[start]] -= 1
                if s[start] in find and window[s[start]] < find[s[start]]:
                    have -= 1
                start += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
