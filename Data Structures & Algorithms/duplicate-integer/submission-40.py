class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we will use hash_map
        hash_map = {}
        for i, n in enumerate(nums):
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        for key, val in hash_map.items():
            if val > 1:
                return True
                break
        return False