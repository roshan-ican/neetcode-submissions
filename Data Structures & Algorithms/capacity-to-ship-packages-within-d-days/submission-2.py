class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            currDays = 1
            capacity = 0
            m = l + (r - l) // 2
            for weight in weights:
                if capacity + weight <= m:
                    capacity += weight
                else:
                    currDays += 1
                    capacity = weight
            if currDays > days: 
                l = m + 1
            else:
                r = m

        return l
            
            
            