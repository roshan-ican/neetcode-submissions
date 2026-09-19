class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ans = []
        n = len(tokens)
        for i in range(n):
            if tokens[i] not in "+-/*":
                ans.append(int(tokens[i]))
            else:
                num1 = ans.pop()
                num2 = ans.pop()
                if tokens[i] == "+":
                    ans.append(num2 + num1)
                elif tokens[i] == "-":
                    ans.append(num2 - num1)
                elif tokens[i] == "*":
                    ans.append(num2 * num1)
                else:
                    ans.append(int(num2/num1))

        return ans[0]

        