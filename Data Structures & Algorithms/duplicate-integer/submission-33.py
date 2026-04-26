class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        for k, v in hash_map.items():
            if v > 1:
                return True
        return False