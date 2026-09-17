class Solution:
    def isValid(self, s: str) -> bool:
        openings = {"{", "[", "("}
        matches = {")": "(", "]": "[", "}": "{"}
        
        stack = []
        n = len(s)
        if n == 1:
            return False

        for i in range(n):
            if s[i] in openings:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != matches[s[i]]:
                    return False
                stack.pop()
        return len(stack) == 0
