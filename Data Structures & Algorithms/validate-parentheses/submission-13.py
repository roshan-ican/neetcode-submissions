class Solution:
    def isValid(self, s: str) -> bool:

        n = len(s)
        if n % 2 != 0:
            return False
        pairs = {")" : "(", "]" : "[", "}" : "{"}

        stack = []
        for b in s:
            if b in pairs.values():
                stack.append(b)
            else:
                if not stack or stack.pop() != pairs[b]:
                    return False
        return not stack

        