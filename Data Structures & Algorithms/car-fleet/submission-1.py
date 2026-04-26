class Solution:
    def carFleet(self, target: int, p: List[int], s: List[int]) -> int:
        cars = sorted(zip(p, s), reverse=True)
        times = [(target - p) / s for p, s in cars]
        # print(times, "___times__")
        fleets = 0
        current_time = 0
        for t in times:
            if t > current_time:
                fleets += 1
                current_time = t
        return fleets