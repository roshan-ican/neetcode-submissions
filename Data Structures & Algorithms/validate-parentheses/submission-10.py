class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in mapping:  # It's a closing bracket
                top_element = stack.pop() if stack else '#' # Pop from stack, or use a dummy if empty
                
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack # True if stack is empty, False otherwise