from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_map = defaultdict(int)
        for n in nums:
            my_map[n] += 1
        for key, value in my_map.items():
            if value > 1:
                return True
        return False


