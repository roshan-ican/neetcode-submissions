from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

     
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            needed = 0
            for i in range(len(piles)):
                cal = ceil(piles[i]/ mid)
                needed += cal
            if needed <= h:
                high = mid
            else:
                low = mid + 1
        return low








        