
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            boats+=1
            total = people[left] + people[right]
            if total <= limit:
                left+=1

            right-=1
        return boats
                

