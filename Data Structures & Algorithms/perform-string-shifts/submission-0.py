class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_s = 0
        for d, a in shift:
            amount = a
            if d == 1:
                amount = -a
            left_s += amount
        left_s  %= len(s)
        s = s[left_s:] + s[:left_s]
        return s
