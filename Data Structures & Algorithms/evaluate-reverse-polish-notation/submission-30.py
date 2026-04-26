class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stuff = ["*", "-", "+", "/"]
        stack = []
        for tok in tokens:
            if tok not in stuff:
                stack.append(int(tok))
            else:
                r = stack.pop()
                l = stack.pop()
                if tok == '+':
                    stack.append(l+r)
                elif tok == '-':
                    stack.append(l-r)
                elif tok == '*':
                    stack.append(l * r)
                else:
                    ans = int(l/r)
                    stack.append(ans)
        return stack[0]