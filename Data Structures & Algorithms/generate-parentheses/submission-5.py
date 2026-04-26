import operator
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def back_track(o, c, s):
            if o == n and c == n:
                result.append(s)
                return
            if o < n:
                back_track(o + 1, c, s + "(")
            if c < o:
                back_track(o, c + 1, s + ")")
        back_track(0, 0, '')
        return result
            

 
