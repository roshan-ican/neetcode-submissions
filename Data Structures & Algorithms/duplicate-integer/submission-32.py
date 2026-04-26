class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for elem in nums:
            if elem in hash_map:
                hash_map[elem] += 1
            else:
                hash_map[elem] = 1
        for n in hash_map.values():
            if n > 1:
                return True
        return False