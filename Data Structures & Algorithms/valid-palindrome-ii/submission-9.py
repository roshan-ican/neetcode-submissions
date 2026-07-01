class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if len(s) == 2:
        #     if s[0] != s[1]:
        #         return True

        # count = {}


        # for n in range(len(s)):
        #     # if s[n] != s[n+1]:
        #     #     return False
        #     if s[n] in count: 
        #         count[s[n]] += 1
        #     else:
        #         count[s[n]] = 1
        # odd_count = 0
        # for key, val in count.items():
        #     print(val, "__vl")
           

        #     if val % 2 != 0:
        #         odd_count+=1
        # return odd_count <= 1

        if s == s[::-1]:
            return True
    
    # Try deleting each character once
        for i in range(len(s)):
            # Create string without character at index i
            modified = s[:i] + s[i+1:]
            if modified == modified[::-1]:
                return True
        
        return False

   
        