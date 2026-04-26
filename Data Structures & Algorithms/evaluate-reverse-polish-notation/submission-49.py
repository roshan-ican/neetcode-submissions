class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for token in tokens:
            op = token
            if token not in ops:
                stack.append(int(token))
                print(stack)
            else:# its an operation, apply op on stack
                top = stack.pop()
                second = stack.pop()
                if op == "*":
                    stack.append(second*top)
                elif op =="/":
                    stack.append(int(second/top))
                elif op == "+":
                    stack.append(second+top)
                else:
                    stack.append(second-top)
        return stack[0]
                    