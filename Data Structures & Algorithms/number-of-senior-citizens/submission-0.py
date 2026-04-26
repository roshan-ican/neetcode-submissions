class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_citizen = 0
        for i, n in enumerate(details):
            sliced = slice(11, -2)
            age = n[sliced]
            if int(age) > 60:
                senior_citizen += 1
        return senior_citizen

