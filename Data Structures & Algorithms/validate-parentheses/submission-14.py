class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pair = {'(' : ')', '{': '}', '[':']' }

        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if not stack:
                    return False
                top_elem = stack.pop()
                if pair[top_elem] != c:
                    return False
        return len(stack) == 0
      

   

 
        