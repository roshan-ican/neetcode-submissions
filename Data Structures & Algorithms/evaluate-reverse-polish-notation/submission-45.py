class Solution:
    def evalStr(self,a,op,b):
        if op == '/':
            return math.trunc(b/a)
        elif op == '*':
            return a*b
        elif op == '-':
            return b-a
        else:
            return a+b
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ["+", "-", "/", "*"]
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in opr:
                f = stack.pop()
                s = stack.pop()
                res = self.evalStr(f,tokens[i],s)
                print("output ",res,f,s)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[0]


        