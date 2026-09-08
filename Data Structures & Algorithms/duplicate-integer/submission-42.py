class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we will use hash_map
        # with set it is better
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False