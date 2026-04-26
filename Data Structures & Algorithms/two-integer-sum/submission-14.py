
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}  # value -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_map:
                return [my_map[diff], i]
            my_map[num] = i
        return []

