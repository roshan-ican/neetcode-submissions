class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for n in s:
            if n in freq:
                freq[n]+=1   # a: 5, b=2, c
            else:
                freq[n]=1
      
        largest_odd = -1
        smallest_even = float("inf")
                #s="abbbcccccddddddddeeeeeeeeffffffff"
        
        for val in freq.values(): # a:1, b:3, c:5, d: 8, e: 8, f: 8
            if val % 2 == 0:
                if val <= smallest_even:
                    smallest_even = val
            elif val % 2 != 0:
                odd = val
                if odd >= largest_odd:
                    largest_odd = odd

        print(largest_odd ,"-", smallest_even,largest_odd - smallest_even)
        result = largest_odd - smallest_even 
        print(result)
        return result