class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
            

        for count in num_count.values():
            if count > 1:
                return True
        return False
                    