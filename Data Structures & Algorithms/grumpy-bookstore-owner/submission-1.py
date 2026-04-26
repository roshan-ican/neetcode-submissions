class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        c = 0
        g = 0
        while c < len(customers) and g < len(grumpy):
            if grumpy[g] == 0:
                base+=customers[c]
                g+=1
                c+=1
            else:
                g+=1
                c+=1

        maxSaved = 0
        for i in range(len(customers) - minutes + 1):
            currentSaved = 0
            for j in range(i, i + minutes):
                if grumpy[j] == 1:
                    currentSaved+=customers[j]
            maxSaved = max(maxSaved, currentSaved)
        return base + maxSaved