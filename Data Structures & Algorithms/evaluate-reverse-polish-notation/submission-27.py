# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:

#         stuff = ["*", "-", "+", "/"]
#         stack = []
#         for tok in tokens:
#             if tok not in stuff:
#                 stack.append(int(tok))
#             else:
#                 l = stack.pop()
#                 r = stack.pop()
#                 if tok == '+':
#                     stack.append(l+r)
#                 elif tok == '-':
#                     stack.append(l-r)
#                 elif tok == '*':
#                     stack.append(l * r)
#                 elif tok == '/':
#                     ans = int(r/l)
#                     stack.append(ans)
#         return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opx = ['+', '-', '*', '/']
        stack = []
        for i, n in enumerate(tokens):
            if n not in opx:
                stack.append(int(n))
            else:
                right = stack.pop()
                left = stack.pop()
                if n == '+':
                    res = right + left
                    stack.append(res)
                elif n == '-':
                    res = left - right
                    stack.append(res)
                elif n == '*':
                    res = right * left
                    stack.append(res)
                else:
                    res = int(left / right)
                    stack.append(res)
                    
        return stack[0]

                

                

                