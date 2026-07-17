class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for num in operations:
            if num == "C":
                res.pop()

            elif num == "D":
                res.append(res[-1] * 2)

            elif num == "+":
                res.append(res[-1] + res[-2])
                
            else:
                res.append(int(num))
        return sum(res)