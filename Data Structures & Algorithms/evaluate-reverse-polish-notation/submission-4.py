class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for tok in tokens:                              
            if tok not in operators:
                stack.append(int(tok))
            else:
                right = stack.pop()
                left = stack.pop()
                if tok == "+":
                    stack.append(left + right)
                elif tok == "-":
                    stack.append(left - right)
                elif tok == "*":
                    stack.append(left * right)
                elif tok == "/":
                    stack.append(math.trunc(left / right))

        return stack[0]