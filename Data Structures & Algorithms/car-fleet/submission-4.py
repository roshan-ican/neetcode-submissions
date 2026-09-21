class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        fleet_time = 0

        by_pos = sorted(zip(position, speed), reverse=True)
        for p, s in by_pos:
            car_time = (target - p) / s

            if car_time > fleet_time:
                fleet+=1
                fleet_time = car_time
        return fleet