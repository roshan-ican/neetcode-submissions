class Solution:
    def confusingNumber(self, n: int) -> bool:
        # storing a orginal
        res = 0
        original = n
        while n > 0:
            digit = n % 10 # getting the last digit
            # the last digit
            if digit in [2, 3, 4, 5, 7]:
                return False
            # rotate the roatedable value
            if digit == 9:
                r_digit = 6
            elif digit == 6:
                r_digit = 9
            else:
                r_digit = digit
            
            res = res * 10 + r_digit

            n = n // 10
            
        if original == 0:
            return False
        return res != original


        